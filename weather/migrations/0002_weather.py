# Generated by Django 4.0.1 on 2022-02-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='weather',
            fields=[
                ('coordinate', models.IntegerField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('discription', models.CharField(blank=True, max_length=100, null=True)),
                ('tempreature', models.TextField(blank=True, null=True)),
                ('tempmin', models.TextField(blank=True, null=True)),
                ('tempmax', models.TextField(blank=True, null=True)),
                ('pressure', models.TextField(blank=True, null=True)),
                ('humidity', models.TextField(blank=True, null=True)),
            ],
        ),
    ]