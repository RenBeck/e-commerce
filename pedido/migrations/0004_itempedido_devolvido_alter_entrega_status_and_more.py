# Generated by Django 5.0.1 on 2024-05-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_alter_pedido_status_entrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='devolvido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='status',
            field=models.CharField(choices=[('Processondo Entrega', 'Processondo Entrega'), ('Enviando', 'Enviando'), ('Entregue', 'Entregue'), ('Processo Arrependimento', 'Processo Arrependimento'), ('Pedido Devolvido', ' Pedido Devolvido'), ('Itens Devolvidos', 'Item(s) Devolvido')], default='Processondo Entrega', max_length=25),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Pagamento Aprovado', 'Pagamento Aprovado'), ('Criado', 'Criado'), ('Pagamento Reprovado', 'Pagamento Reprovado'), ('Enviando', 'Enviando'), ('Entregue', 'Entregue'), ('Processando Devolucao', 'Processando Devolução'), ('Finalizado', 'Finalizado')], default='Criado', max_length=25),
        ),
    ]
