# Generated by Django 4.0.1 on 2022-03-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailaddress', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.TextField()),
            ],
        ),
    ]
