from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    qtd_total = models.PositiveIntegerField()
    status = models.CharField(
        default="Criado",
        max_length=25,
        choices=(
            ('Pagamento Aprovado', 'Pagamento Aprovado'),
            ('Criado', 'Criado'),
            ('Pagamento Reprovado', 'Pagamento Reprovado'),
            ('Enviando', 'Enviando'),
            ('Entregue', 'Entregue'),
            ('Processando Devolucao','Processando Devolução'),
            ('Finalizado', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)
    devolvido=models.BooleanField(default=False)

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'


class Entrega(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cod_rastreamento = models.CharField(max_length=13, blank=True, null=True)
    status = models.CharField(
    default="Processondo Entrega",
    max_length=25,
    choices=(
            ('Processondo Entrega', 'Processondo Entrega'),
            ('Enviando', 'Enviando'),
            ('Entregue', 'Entregue'),
            ('Processo Arrependimento', 'Processo Arrependimento'),
            ('Pedido Devolvido',' Pedido Devolvido'),
            ('Itens Devolvidos','Item(s) Devolvido'),
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'