# Generated by Django 3.1.3 on 2023-06-16 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numeros', '0003_auto_20230613_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numero',
            name='lanzamiento',
        ),
    ]
