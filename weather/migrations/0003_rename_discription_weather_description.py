# Generated by Django 4.0.1 on 2022-02-08 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_weather'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='discription',
            new_name='description',
        ),
    ]
