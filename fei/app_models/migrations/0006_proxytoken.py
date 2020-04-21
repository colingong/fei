# Generated by Django 2.2.11 on 2020-04-21 02:55

from django.db import migrations
import rest_framework.authtoken.models


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('app_models', '0005_fulluserinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyToken',
            fields=[
            ],
            options={
                'proxy': rest_framework.authtoken.models.Token,
                'indexes': [],
                'constraints': [],
            },
            bases=('authtoken.token',),
        ),
    ]
