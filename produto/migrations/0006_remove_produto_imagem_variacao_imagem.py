# Generated by Django 4.2.7 on 2023-12-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_remove_variacao_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='imagem',
        ),
        migrations.AddField(
            model_name='variacao',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens'),
        ),
    ]
