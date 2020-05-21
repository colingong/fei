# Generated by Django 2.2.11 on 2020-05-18 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_models', '0012_auto_20200516_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtraTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weixin_openid', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('qq', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('_pay_password', models.CharField(blank=True, db_column='pay_password', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]