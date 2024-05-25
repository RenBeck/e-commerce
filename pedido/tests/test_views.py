from django.test import TestCase
from django.urls import reverse

class Pedido_Wiew_Test(TestCase):
    def test_status_core_200_pagar(self):
        response = self.client.get(reverse('pedido:pagar', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    def test_status_core_200_detalhe(self):
        response = self.client.get(reverse('pedido:detalhe', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    def test_status_core_200_salvarpedido(self):
        response = self.client.get(reverse('pedido:salvarpedido'))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    def test_status_core_200_lista(self):
        response = self.client.get(reverse('pedido:lista'))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

   
    