from django.shortcuts import render, redirect
from pedido.models import Pedido, Entrega
import requests, json

from django.core.cache import cache


def getPublicKey():
    url = 'https://sandbox.api.pagseguro.com/public-keys/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization' : '40768D77BE9542BBA6656D0CF9C7B59A'
    }
    body = json.dumps({
        "type": "card"
    })
    reqs = requests.post(url,headers=headers,data=body)
    return reqs.json()['public_key']


def paymentController(request):
    pedido_id = cache.get('pedido_id')
    url = 'https://sandbox.api.pagseguro.com/orders'
    headers = {
        'Content-Type': 'application/json',
        'Authorization' : '40768D77BE9542BBA6656D0CF9C7B59A'
    }
    body = json.dumps({
        "reference_id": "ex-00001",
        "customer": {
            "name": "Jose da Silva",
            "email": "email@test.com",
            "tax_id": "12345678909",
            "phones": [
                {
                    "country": "55",
                    "area": "11",
                    "number": "999999999",
                    "type": "MOBILE"
                }
            ]
        },
        "items": [
            {
                "reference_id": "referencia do item",
                "name": "nome do item",
                "quantity": 1,
                "unit_amount": 500
            }
        ],
        "shipping": {
            "address": {
                "street": "Avenida Brigadeiro Faria Lima",
                "number": "1384",
                "complement": "apto 12",
                "locality": "Pinheiros",
                "city": "São Paulo",
                "region_code": "SP",
                "country": "BRA",
                "postal_code": "01452002"
            }
        },
        "notification_urls": [
            "https://meusite.com/notificacoes"
        ],
        "charges": [
            {
                "reference_id": "referencia da cobranca",
                "description": "descricao da cobranca",
                "amount": {
                    "value": 500,
                    "currency": "BRL"
                },
                "payment_method": {
                    "type": "CREDIT_CARD",
                    "installments": 1,
                    "capture": True,
                    "card": {
                        "encrypted": request.POST['encriptedCard'],
                        "security_code": "123",
                        "holder": {
                            "name": "Jose da Silva"
                        },
                        "store": True
                    }
                }
            }
        ]
    })
    reqs = requests.post(url,headers=headers,data=body)
    response_json = reqs.json()
    usuario =  cache.get('user')
    try:
        payment_response = response_json["charges"][0]["payment_response"]
        result = 'Pagamento com ' + payment_response["message"]
        pedido = Pedido.objects.get(pk=pedido_id)
        
        if result == 'Pagamento com SUCESSO':
            usuario =  cache.get('user')
            pedido.status = 'Pagamento Aprovado'
            pedido.save() 
            entrega = Entrega.objects.filter(pedido=pedido).first()
            if entrega:
                entrega.usuario = usuario
                entrega.pedido = pedido
                entrega.save()
            else:
                entrega = Entrega.objects.create(
                    usuario = usuario,
                    pedido = pedido,
                )
                entrega.save()

        else:  
            pedido.status = 'Pagamento Reprovado'  
            pedido.save() 

        return redirect('pedido:lista')
        
    except KeyError as e:
        
        print("Error processing response:", e)
        cache.set('pedido_id', pedido_id)
        cache.set('user', usuario)
        pedido = Pedido.objects.get(pk=pedido_id)
        pedido.status = 'Pagamento Reprovado' 
        pedido.save() 

        return redirect('pedido:lista')
       

def pagar(request):
    data = {}
    data['publicKey'] = getPublicKey()
    return render(request, 'pagar/pagar.html', data)