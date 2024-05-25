from django.db import models
from utils import utils


class Perfil_colaborador(models.Model):
    status = models.BooleanField()
    nome = models.CharField(max_length=50)
    salario = models.FloatField(default=0, verbose_name='Salário')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    email = models.EmailField(help_text='bs@email.com')
    data_nascimento =  models.DateField(auto_now=False, auto_now_add=False, verbose_name='Data de nascimento') 
    ddd = models.CharField(max_length=2, help_text=31, verbose_name='DDD')
    celular = models.CharField(max_length=9, help_text=999999999)
    genero = models.CharField(
    max_length=1,
    default='F',
    choices=(
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ))
    estado_civil = models.CharField(
    verbose_name='Estado Civil',    
    max_length=1,
    default='S',
    choices=(
        ('C', 'Casado(a)'),
        ('S', 'Solteiro(a)'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viuvo(a)'),
    ))
    nacionalidade = models.CharField(max_length=100)

    def get_salario_formatado(self):
        return utils.formata_salario(self.salario)
    get_salario_formatado.short_description = 'Salário'


    def __str__(self):
        return f'{self.nome}'


    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
   
        
class Detalhe_cargo(models.Model):
    perfil = models.ForeignKey(Perfil_colaborador, on_delete=models.CASCADE)   
    cargo = models.CharField(max_length=100) 
    departamento = models.CharField(max_length=100) 
    data_inicio =  models.DateField(auto_now=False, auto_now_add=False, verbose_name='Data de início do emprego') 
    horario_trabalho = models.CharField(
    max_length=1,
    default='2',
    verbose_name='Horário de trabalho',
    choices=(
        ('1', '7h às 17h'),
        ('2', '8h às 18h'),
        ('3', '9h às 19h'),
        ('4', '10h às 20h'),
        ('5', 'enter às 7h e 20h'),
        ('6', 'flexível'),
    ))
    tipo_contrato = models.CharField(
    max_length=1,
    default='2',
    verbose_name='Tipo de Contrato',
    choices=(
        ('1', 'Integral'),
        ('2', 'Meio Período'),
        ('3', 'Temporário'),
        ('4', 'Estagio'),
        ('5', 'Pessoa Jurídica'),     
    ))


    def __str__(self):
        return f'{self.cargo}'
    
    class Meta:
        verbose_name = 'Detalhe do cargo'
        verbose_name_plural = 'Detalhes dos cargos'


class Inf_bancarias(models.Model):
    perfil = models.ForeignKey(Perfil_colaborador, on_delete=models.CASCADE)
    banco = models.CharField(max_length=100)  
    numero_agencia = models.CharField(max_length=4, verbose_name='Número da agência',) 
    numero_conta = models.CharField(max_length=20, verbose_name='Número da conta',)  
    tipo_conta = models.CharField(
    max_length=1,
    default='2',
    verbose_name='Tipo de conta',
    choices=(
        ('1', 'Corrente'),
        ('2', 'Poupança'),
        ('3', 'Conjunta'),
        ('4', 'Salário'),
        ('5', 'Empresarial'),  
    ))
    
    def __str__(self):
        return f'{self.banco}'
    
    class Meta:
        verbose_name = 'Informação Bancária'
        verbose_name_plural = 'Informações Bancárias'


class Beneficios(models.Model):
    perfil = models.ForeignKey(Perfil_colaborador, on_delete=models.CASCADE)
    beneficio = models.CharField(
    max_length=1,
    default='1',
    verbose_name='Benefício',
    choices=(
        ('1', 'Plano de saúde'),
        ('2', 'Plano Odontológico'),
        ('3', 'Seguro de Vida'),
        ('4', 'Previdência Privada'),
        ('5', 'Vale-Alimentação'),  
        ('6', 'Vale-Refeição'), 
        ('7', 'Auxílio-Educação'),
        ('8', 'Auxílio-Creche'), 
        ('9', 'Vale-Transporte'),
    )) 


    def __str__(self):
        return self.beneficio


    class Meta:
        verbose_name = 'Benefício'
        verbose_name_plural = 'Benefícios'


class Endereco(models.Model):
    perfil = models.ForeignKey(Perfil_colaborador, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )


    def __str__(self):
        return f'{self.rua}'


    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Enderoços'
   
         