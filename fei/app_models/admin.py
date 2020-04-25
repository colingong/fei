from app_drf.urls import app_name
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
    """管理Product模型
    
    """
    list_display = (
        'product_name', 
        'product_description', 
        'product_price', 
        'product_stock', 
        'category',
        'warehouse',
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
    list_display = ('warehouse_name', 'warehouse_code', 'warehouse_address',)
    fields = ('warehouse_name', 'warehouse_code', 'warehouse_address',)

@admin.register(UserOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_number', 'total_price',)
    fields = ('user', 'order_number', 'total_price',)

@admin.register(SubUserOrder)
class SubOrderAdmin(admin.ModelAdmin):
    list_display = ('userorder', 'sub_userorder_number',)
    fields = ('userorder', 'sub_userorder_number',)

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('subuserorder', 'product', 'quntity',)
    fields = ('subuserorder', 'product', 'quntity',)

# @admin.register(Permission)
# class PermissionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'codename')
#     fields = ('name', 'codename')

# @admin.register(UserExtra)
# class UserExtraAdmin(admin.ModelAdmin):
#     """UserExtra不提供add和delete功能

#     禁止add/delete操作
#         每个用户有且仅有一条记录，这条记录在用户登录时自动生成，后期再由用户补充完全。
#         既不允许手动添加，也不允许手动删除；仅可以view/change这两个操作
    
#     """
#     list_display = ('user', 'weixin_openid', 'phone', 'qq', 'pay_password',)
#     fields = ('user', 'weixin_openid', 'phone', 'qq', 'pay_password',)

#     def has_delete_permission(self, request, obj=None):
#         return False
    
#     def has_add_permission(self, request, obj=None):
#         return False

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role_code')
    fields = ('user', 'role_code')

# @admin.register(UserAsset)
# class UserAssetAdmin(admin.ModelAdmin):
#     """UserAsset管理

#     禁止add/delete操作
#         每个用户有且仅有一条asset 记录，在用户第一次登录时自动由middleware创建
#         之后仅可以view/change，不允许add/delete操作
    
#     """
#     list_display = ('user', 'balance')
#     fields = ('user', 'balance')

#     def has_add_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False

# 在app_models里，定制User的管理
from django.contrib.auth.models import User

# class FullUserInfo(User):
#     """这是一个django built-in User的代理模型

#     作用：
#         用这个代理模型，定制一个User管理
#         让这个可以管理到关连的UserExtra和UserAsset

#     为什么需要这个代理模型：
#         实现一个用户自定义的User模型管理
#         由于User已经默认被admin.register注册过，就不能再次注册了
#         所以实现一个代理模型，用这个代理模型再来注册
    
#     """
#     class Meta:
#         proxy = True
    
class UserExtraInline(admin.StackedInline):
    """UserExtra模型作为StackedInline

    模型关系:
        UserExtra和User是One to One
        因此每个User有一条（且仅有一条）UserExtra记录
        作为StackedInline，现在管理每个User的时候，也可一起管理UserExtra
    
    """
    model = UserExtra

    # 每个用户都必须有一条user extra记录，不允许删除
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

class UserAssetInline(admin.StackedInline):
    """UserAsset StackedInline

    模型关系：
        UserAsset和User也是One to One
        同样每个User都会有一条（且仅有一条）UserAsset记录
        作为StackedInline，管理User的时候也可管理UserAsset
    
    """
    model = UserAsset

    # 由于每个用户都必须有一条 user asset记录，因此不允许删除
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

# @admin.register(FullUserInfo)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'email')
#     fields = ('username', 'first_name', 'email')
#     inlines = [UserAssetInline, UserExtraInline]

# 定制的一个 User / UserExtra /UserAsset 的管理
# 将 UserExtra和UserAsset的字段，和User字段一起显示，而不是作为StackedInline
# TODO
class UserInfo(User):
    class Meta:
        proxy = User

@admin.register(UserInfo)
class CustAdmin(admin.ModelAdmin):
    """除了注册的模型之外，增加一些字段，这些增加的字段来自于其它模型
    
    UserExtra:
        'weixin_openid', 'qq'

    UserAsset:
        'balance'

    增加的这些字段，需要定义一个方法，和增加的字段名字一样的方法
    例如字段名为 'weixin_openid'， 则 def weixin_openid(self, instance):
    这个方法的参数是模型的实例，名字可以任取，但是传入的就是模型实例，
    例如这里注册的是模型NewUserInfo，那么传入的实际就是NewUserInfo的一个实例，也就是一个user object

    """
    list_display = (
        'cust_field1',                          # 这是一个自定义字段，需要定义方法获取或赋值
        'username', 'first_name', 'last_name',  # 这是来自于模型的字段，不用定义方法获取
        'weixin_openid', 'qq',                  # 这是来自于UserExtra的字段，两个需要分别定义方法
        'balance')                              # 这是来自于UserAsset的字段，需要定义方法
    fields = ('username', 'first_name', 'last_name', )
    inlines = [UserExtraInline, UserAssetInline]
    
    def cust_field1(self, inst):
        return 'abc'

    def weixin_openid(self, instance):
        return instance.userextra.weixin_openid

    def qq(self, instance):
        return instance.userextra.qq
    
    def balance(self, instance):
        return instance.userasset.balance

# admin.site.register(UserInfo, CustAdmin)
