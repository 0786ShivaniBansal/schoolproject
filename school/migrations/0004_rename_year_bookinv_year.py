# Generated by Django 4.0.1 on 2022-02-17 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_bookinv_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinv',
            old_name='Year',
            new_name='year',
        ),
    ]
