# Generated by Django 5.0.1 on 2024-01-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0016_alter_variacao_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variacao',
            name='nome',
            field=models.CharField(default='U', max_length=10),
        ),
    ]