from django.test import TestCase
from ..models import Perfil

from django.contrib.auth.models import User

class perfil_test_models(TestCase):
   
    def setUp(self):
        user = User.objects.create(username="Beck")

        Perfil.objects.create(
            usuario=user,
            cpf="72543682007",
            ddd="31",
            celular="984987998",
            rua="Rua dos Bobos",
            numero="1233",
            complemento="Apto 303",
            bairro="Centro",
            cep="01234567",
            cidade="São Paulo",
            estado="SP"
        )


    def test_rotorno(self):
        
        user = User.objects.get(username="Beck")

        perfil = Perfil.objects.get(usuario=user)
        self.assertEqual(perfil.usuario, user)
        self.assertEqual(perfil.cpf, "72543682007")
        self.assertEqual(perfil.ddd, "31")
        self.assertEqual(perfil.celular, "984987998")
        self.assertEqual(perfil.rua, "Rua dos Bobos")
        self.assertEqual(perfil.numero, "1233")
        self.assertEqual(perfil.complemento, "Apto 303")
        self.assertEqual(perfil.bairro, "Centro")
        self.assertEqual(perfil.cep, "01234567")
        self.assertEqual(perfil.cidade,"São Paulo") 
        self.assertEqual(perfil.estado, "SP")   

        
        
        
