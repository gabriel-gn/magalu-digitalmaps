# Generated by Django 3.0.3 on 2020-03-03 02:06

from django.db import migrations


class Migration(migrations.Migration):
    """
    Removendo usuário que cadastrou
    """

    dependencies = [
        ('locais', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localizacao',
            name='user',
        ),
    ]
