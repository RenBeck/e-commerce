from django.test import TestCase
from django.urls import reverse

class TrabalheConosco_Wiew_Test(TestCase):
    def test_status_core_200_listavagas(self):
        response = self.client.get(reverse('trabalheconosco:listavagas'))
        self.assertEqual(response.status_code, 200)

    def test_status_core_200_listavagas(self):
        response = self.client.get(reverse('trabalheconosco:curriculo'))
        self.assertEqual(response.status_code, 200)
  