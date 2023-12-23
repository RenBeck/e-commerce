# Generated by Django 4.2.7 on 2023-12-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_remove_produto_imagem_variacao_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('I', 'Infantil')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='produto',
            name='sub_categoria',
            field=models.CharField(choices=[('R', 'Roupa'), ('C', 'Calçados'), ('A', 'Acessórios')], default='F', max_length=1),
        ),
    ]