# Generated by Django 5.0.1 on 2024-01-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('Outros', 'Outros'), ('Camisas', 'Camisas'), ('Croppeds', 'Croppeds'), ('Shorts', 'Shorts'), ('Calças', 'Calças'), ('Vestidos', 'Vestidos'), ('Camisetas', 'Camisetas'), ('Blazer', 'Blazer'), ('Saias', 'Saias'), ('Casacos', 'Casacos'), ('Jaquetas', 'Jaquetas'), ('Polos', 'Polos'), ('Regatas', 'Regatas'), ('Bermudas', 'Bermudas'), ('Tênis', 'Tênis'), ('Sapatos', 'Sapatos'), ('Sandálias', 'Sandálias'), ('Rasteiras', 'Rasteiras'), ('Chinelos', 'Chinelos'), ('Óculos', 'Óculos'), ('Mochilas', 'Mochilas'), ('Bolsas', 'Bolsas'), ('Necessaire', 'Necessaire'), ('Carteiras', 'Carteiras'), ('Cintos', 'Cintos'), ('Bonés', 'Bonés')], default='Outros', max_length=30),
        ),
    ]
