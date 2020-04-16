from app_models.models_product import Warehouse
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import UserExtra, Category, Product
from .models import UserOrder, SubUserOrder, OrderDetail, Warehouse
from .models import UserRole
from .models import UserAsset

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_type_name', 'category_type_code')
    fields = ('category_type_name', 'category_type_code')
    # def has_change_permission(self, request, obj=None):
    #     if request.user.username == 'user':
    #         return False
    #     return True

    # def has_delete_permission(self, request, obj=None):
    #     if request.user.username == 'user':
    #         return False
    #     return True

    # # to disable view and add you can do this 
    # def has_view_permission(self, request, obj=None):
    #     return True

    # def has_add_permission(self, request):
    #     if request.user.username == 'user':
    #         return False
    #     return True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'warehouse',
        'product_name', 
        'product_description', 
        'product_price', 
        'product_stock', 
        'for_sale')
    fields = (
        'category',
        'warehouse',
        'product_name', 
        'product_description', 
        'product_price', 
        'product_stock', 
        'for_sale')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_type_name', 'warehouse_code', 'warehouse_address',)
    fields = ('warehouse_type_name', 'warehouse_code', 'warehouse_address',)

@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_number', 'total_price',)
    fields = ('user', 'order_number', 'total_price',)

@admin.register(SubUserOrder)
class SubUserOrderAdmin(admin.ModelAdmin):
    list_display = ('userorder', 'sub_userorder_number',)
    fields = ('userorder', 'sub_userorder_number',)

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('subuserorder', 'product', 'quntity',)
    fields = ('subuserorder', 'product', 'quntity',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')
    fields = ('name', 'codename')

@admin.register(UserExtra)
class UserExtraAdmin(admin.ModelAdmin):
    list_display = ('user', 'weixin_openid', 'phone', 'qq', 'pay_password',)
    fields = ('user', 'weixin_openid', 'phone', 'qq', 'pay_password',)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role_code')
    fields = ('user', 'role_code')

@admin.register(UserAsset)
class UserAssetAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    fields = ('user', 'balance')


# 在app_models里，定制User的管理
from django.contrib.auth.models import User

class FullUserInfo(User):
    class Meta:
        proxy = True
    
class UserExtraInline(admin.StackedInline):
    model = UserExtra

class UserAssetInline(admin.StackedInline):
    model = UserAsset

@admin.register(FullUserInfo)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email')
    fields = ('username', 'first_name', 'email')
    inlines = [UserAssetInline, UserExtraInline]