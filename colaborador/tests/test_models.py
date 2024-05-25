from django.test import TestCase
from ..models import Perfil_colaborador, Detalhe_cargo, Inf_bancarias, Beneficios, Endereco

class Perfil_colaborador_test(TestCase):

    def setUp(self):
        perfil = Perfil_colaborador.objects.create(
            status=True,
            nome="Renato Beck",
            salario=5001.78,
            cpf="72543682007",
            email="bs@email.com", 
            data_nascimento="1983-03-01",
            ddd="31",
            celular="984987998",
            genero="Masculino",
            estado_civil="Solteiro(a)",
            nacionalidade="Brasileiro"
        )

        Detalhe_cargo.objects.create(
            perfil=perfil,
            cargo="Gerente",
            departamento="Vendas",
            data_inicio="2024-01-02",
            horario_trabalho="7h às 17h",
            tipo_contrato="Integral"
        )

        Inf_bancarias.objects.create(
            perfil=perfil,
            banco= "Itau",
            numero_agencia= "1234", 
            numero_conta= "46526-2",
            tipo_conta= 'Corrente'
        )

        Beneficios.objects.create(
            perfil=perfil,
            beneficio='Plano de saúde'
        )

        Endereco.objects.create(
            perfil=perfil,
            rua="Rua dos Bobos",
            numero="1233",
            complemento="Apto 303",
            bairro="Centro",
            cep="01234567",
            cidade="São Paulo",
            estado="SP"
        )

    def test_retorno_colaborador(self):
        perfil = Perfil_colaborador.objects.get(nome='Renato Beck')
        self.assertEqual(perfil.status, True)
        self.assertEqual(perfil.nome, 'Renato Beck')
        self.assertEqual(perfil.salario, 5001.78)
        self.assertEqual(perfil.cpf, '72543682007')
        self.assertEqual(perfil.email, 'bs@email.com')
        self.assertEqual(str(perfil.data_nascimento), '1983-03-01')
        self.assertEqual(perfil.ddd, '31')
        self.assertEqual(perfil.celular, '984987998')
        self.assertEqual(perfil.genero, 'Masculino')
        self.assertEqual(perfil.estado_civil, 'Solteiro(a)')
        self.assertEqual(perfil.nacionalidade, 'Brasileiro')

        detalhe_cargo = Detalhe_cargo.objects.get(cargo='Gerente')
        self.assertEqual(detalhe_cargo.cargo, "Gerente")
        self.assertEqual(detalhe_cargo.departamento, "Vendas")
        self.assertEqual(str(detalhe_cargo.data_inicio),  '2024-01-02')
        self.assertEqual(detalhe_cargo.horario_trabalho, "7h às 17h")
        self.assertTrue(detalhe_cargo.tipo_contrato, 'Integral')

        inf_bancarias = Inf_bancarias.objects.get(banco='Itau')
        self.assertEqual(inf_bancarias.banco, 'Itau')
        self.assertEqual(inf_bancarias.numero_agencia, '1234')
        self.assertEqual(inf_bancarias.numero_conta, '46526-2')
        self.assertEqual(inf_bancarias.tipo_conta, 'Corrente')

        beneficios = Beneficios.objects.get(beneficio='Plano de saúde')
        self.assertEqual(beneficios.beneficio, 'Plano de saúde')

        endereco = Endereco.objects.get(rua='Rua dos Bobos')
        self.assertEqual(endereco.rua, 'Rua dos Bobos')
        self.assertEqual(endereco.numero, '1233')
        self.assertEqual(endereco.complemento, 'Apto 303')
        self.assertEqual(endereco.bairro, 'Centro')
        self.assertEqual(endereco.cep, '01234567')
        self.assertEqual(endereco.cidade, 'São Paulo')
        self.assertEqual(endereco.estado,  'SP')

