from django.conf import settings
import os
from django.db import models
from django.utils.text import slugify
from utils import utils

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    imagem = models.ImageField(
        upload_to='produto_imagens', blank=True, null=True)
    descricao = models.TextField()
    cor = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=1,
        default='F',
        choices=(
            ('F', 'Feminino'),
            ('M', 'Masculino'),
            ('I', 'Infantil'),
        )
    )
    sub_categoria = models.CharField(
        max_length=1,
        default='F',
        choices=(
            ('R', 'Roupa'),
            ('C', 'Calçados'),
            ('A', 'Acessórios'),
        )
    )
    tipo =  models.CharField(
        max_length=30,
        default='Outros',
        choices=(
            ('Outro','Outro'),
            ('Camisa', 'Camisa'),
            ('Cropped', 'Cropped'),
            ('Short', 'Short'),
            ('Calca','Calça'),
            ('Vestido','Vestido'),
            ('Camiseta','Camiseta'),
            ('Blazer','Blazer'),
            ('Saia','Saia'),
            ('Moletom','Moletom'),
            ('Jaqueta','Jaqueta'),
            ('Polo','Polo'),
            ('Tenis','Tênis'),
            ('Sandalia','Sandália'),
            ('Rasteira','Rasteira'),
            ('Chinelo','Chinelo'),
            ('Oculos','Óculos'),
            ('Mochila','Mochila'),
            ('Bolca','Bolça'),
            ('Carteira','Carteira'),
            ('Cinto','Cinto'),
            ('Bone','Boné'),       
        )
    )
    marca = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(
        default=preco, verbose_name='Preço Promocional')
    
    def get_preco_formatado(self):
        return utils.formata_preco(self.preco)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return utils.formata_preco(self.preco_promocional)
    get_preco_promocional_formatado.short_description = 'Preço Promo.'
    

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nome

class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)   
    nome = models.CharField(max_length=10, default='U')
    estoque = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

class Imagem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='imagens_produtos/', blank=True, null=True, verbose_name='Imagem do Produto')

    def __str__(self):
        return self.imagem.url if self.imagem else "No Image"

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

