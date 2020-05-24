# Generated by Django 2.2.11 on 2020-05-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0018_auto_20200518_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(null=True)),
                ('userid', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(max_length=250)),
                ('method', models.CharField(max_length=15)),
                ('payload', models.CharField(max_length=1024)),
            ],
        ),
    ]