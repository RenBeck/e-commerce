from django.test import TestCase
from ..models import Vaga, Curriculo

class trabalhe_conosco_test(TestCase):
    def  setUp(self):
        Vaga.objects.create(
            nome='Desenvolvedor',
            sobre_vaga='Vaga para desenvolvedor full stack',
            responsabilidades='todas',
            requisitos='superior',   
            beneficios='nenhum'         
        )

        Curriculo.objects.create(
            nome= 'Fulano de Tal',
            email = "fulanodetal@email",
            vaga = 'Gerente de Loja',
            arquivo='Fulano de Tal currículo'
        )

    def test_retorno(self):
        vaga = Vaga.objects.get(nome="Desenvolvedor")
        self.assertEqual(vaga.nome, 'Desenvolvedor')
        self.assertEqual(vaga.sobre_vaga, 'Vaga para desenvolvedor full stack')
        self.assertEqual(vaga.responsabilidades, 'todas')
        self.assertEqual(vaga.requisitos, 'superior')
        self.assertEqual(vaga.beneficios, 'nenhum')