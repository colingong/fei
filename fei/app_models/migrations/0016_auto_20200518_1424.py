# Generated by Django 2.2.11 on 2020-05-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0015_auto_20200518_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextratest',
            name='_pay_password',
        ),
        migrations.AddField(
            model_name='userextratest',
            name='pay_password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]