from django.test import TestCase
from ..forms import PerfilForm, UserForm

class PerfilForm_Test(TestCase):
    def test_perfilForm_valido(self):
        form = PerfilForm(data={
            'first_name': 'Renato', 
            'last_name': 'Beck', 
            'usuario': 'Beck', 
            'password': 'Re123456',
            'password2': 'Re123456', 
            'email': 'beck@gmail.com',
            'cpf': '06090697648',
            'ddd': '11',
            'celular': '999999999',
            'rua': 'Rua dos Bobos',
            'numero': '10',
            'bairro': 'Centro',
            'cep': '12345678',
            'cidade': 'São Paulo',
            'estado': 'SP',
            'complemento': 'casa',
        })
        self.assertTrue(form.is_valid())

class UserForm_Test(TestCase):
    def test_userForm_valido(self):
        form = UserForm(data={
            'first_name': 'Renato', 
            'last_name': 'Beck', 
            'username': 'Beck',  
            'password': 'Re123456',
            'password2': 'Re123456', 
            'email': 'beck@gmail.com',
        })
        self.assertTrue(form.is_valid())