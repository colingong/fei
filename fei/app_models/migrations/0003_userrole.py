# Generated by Django 2.2.11 on 2020-04-15 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_models', '0002_category_orderdetail_product_subuserorder_supplier_userorder_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_code', models.CharField(choices=[('VIP_CUSTOMER', 'VIP客户'), ('SYSTEM_ADMIN', '系统管理员'), ('BUSINESS_ADMIN', '商城管理员'), ('VEIRFIED_CUSTOMER', '已认证客户'), ('UNVERIFIED_CUSTOMER', '未认证客户')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
