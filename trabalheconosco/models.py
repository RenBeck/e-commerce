from django.db import models

class Vaga(models.Model):
    nome = models.CharField(max_length=120)
    sobre_vaga = models.TextField()
    responsabilidades = models.TextField()
    requisitos = models.TextField()
    beneficios = models.TextField()

    def __str__(self):
        return self.nome

class Curriculo(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    vaga = models.CharField(
        max_length=2,
        default='VL',
        choices=(
            ('VL', 'Vendedor de Loja'),
            ('GL', 'Gerente de Loja'),
        )
    )
    arquivo = models.FileField(upload_to='pdfs', null=True)


    def __str__(self):
        return self.nome
    
