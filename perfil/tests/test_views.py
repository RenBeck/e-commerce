from django.test import TestCase
from django.urls import reverse

class Perfil_Wiew_Test(TestCase):
    def test_status_core_200_criar(self):
        response = self.client.get(reverse('perfil:criar'))
        self.assertEqual(response.status_code, 200)

    def test_status_core_200_atualizar(self):
        response = self.client.get(reverse('perfil:atualizar'))
        self.assertEqual(response.status_code, 200)

    def test_status_core_200_login(self):
        response = self.client.post(reverse('perfil:login'))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    def test_status_core_200_logout(self):
        response = self.client.get(reverse('perfil:logout'))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    
