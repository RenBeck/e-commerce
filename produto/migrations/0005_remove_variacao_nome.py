# Generated by Django 4.2.7 on 2023-12-16 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_variacao_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variacao',
            name='nome',
        ),
    ]
