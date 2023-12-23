from django.conf import settings
import os
from PIL import Image
from django.db import models
from utils import utils

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(
        upload_to='produto_imagens', blank=True, null=True)
    descricao = models.TextField()
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
    marca = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco = models.FloatField(verbose_name='Preço')
    preco_minimo = models.FloatField(
        default=preco, verbose_name='Preço Minimo.')
    
    def get_preco_formatado(self):
        return utils.formata_preco(self.preco)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_minimo_formatado(self):
        return utils.formata_preco(self.preco_minimo)
    get_preco_minimo_formatado.short_description = 'Preço Minimo.'

    @staticmethod
    def resize_image(img):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        new_img = img_pil.resize((original_width, original_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=80
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
            
        self.resize_image(self.imagem)


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cor = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=3)
    estoque = models.PositiveIntegerField(default=1)
    imagem = models.ImageField(
        upload_to='produto_imagens', blank=True, null=True)
    
    @staticmethod
    def resize_image(img):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        new_img = img_pil.resize((original_width, original_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=80
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
            
        self.resize_image(self.imagem)

    def __str__(self):
        return self.nome
    

    def __str__(self):
        return self.cor or self.produto.cor

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'