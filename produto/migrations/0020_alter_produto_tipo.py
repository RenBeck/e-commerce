# Generated by Django 5.0.1 on 2024-01-31 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0019_alter_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('Outro', 'Outro'), ('Camisa', 'Camisa'), ('Cropped', 'Cropped'), ('Short', 'Short'), ('Calca', 'Calça'), ('Vestido', 'Vestido'), ('Camiseta', 'Camiseta'), ('Blazer', 'Blazer'), ('Saia', 'Saia'), ('Moletom', 'Moletom'), ('Jaqueta', 'Jaqueta'), ('Polo', 'Polo'), ('Tenis', 'Tênis'), ('Sandália', 'Sandália'), ('Rasteira', 'Rasteira'), ('Chinelo', 'Chinelo'), ('Oculo', 'Óculo'), ('Mochila', 'Mochila'), ('Bolsa', 'Bolsa'), ('Carteira', 'Carteira'), ('Cinto', 'Cinto'), ('Bone', 'Boné')], default='Outros', max_length=30),
        ),
    ]
