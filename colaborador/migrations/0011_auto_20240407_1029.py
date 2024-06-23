# Generated by Django 3.2.25 on 2024-04-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0010_rename_estado_civil_perfil_colaborador_estado_civil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalhe_cargo',
            name='data_inicio',
            field=models.DateField(verbose_name='Data de início do emprego'),
        ),
        migrations.AlterField(
            model_name='perfil_colaborador',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
    ]