# Generated by Django 3.2.25 on 2024-04-08 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0012_alter_endereco_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficios',
            name='beneficio',
            field=models.CharField(choices=[('1', 'Plano de saúde'), ('2', 'Plano Odontológico'), ('3', 'Seguro de Vida'), ('4', 'Previdência Privada'), ('5', 'Vale-Alimentação'), ('6', 'Vale-Refeição'), ('7', 'Auxílio-Educação'), ('8', 'Auxílio-Creche'), ('9', 'Vale-Transporte')], default='1', max_length=1, verbose_name='Benefício'),
        ),
    ]
