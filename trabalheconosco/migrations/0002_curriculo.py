# Generated by Django 5.0.1 on 2024-01-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalheconosco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('vaga', models.CharField(choices=[('VL', 'Vendedor de Loja'), ('GL', 'Gerente de Loja')], default='VL', max_length=2)),
            ],
        ),
    ]