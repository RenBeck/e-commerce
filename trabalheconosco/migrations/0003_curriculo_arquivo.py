# Generated by Django 5.0.1 on 2024-01-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalheconosco', '0002_curriculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculo',
            name='arquivo',
            field=models.FileField(null=True, upload_to='pdfs'),
        ),
    ]
