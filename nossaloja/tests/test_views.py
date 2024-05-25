from django.test import TestCase
from django.urls import reverse

class NossasLojas_Wiew_Test(TestCase):
    def test_status_core_200_listalojas(self):
        response = self.client.get(reverse('nossaloja:listalojas'))
        self.assertEqual(response.status_code, 200)
  