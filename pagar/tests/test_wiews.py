from django.test import TestCase
from django.urls import reverse

class Pagar_Wiew_Tesrt(TestCase):
    def test_status_core_200_pagar(self):
        response = self.client.get('/pagar/')
        self.assertEqual(response.status_code, 200)