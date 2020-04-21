from django.contrib import admin

# Register your models here.

'''
class EventAdminSite(AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Event heros": 1,
            "Event villains": 2,
            "Epics": 3,
            "Events": 4
        }
        app_dict = self._build_app_dict(request)
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list
'''

from app_models.models import UserExtra, Category, Product
# from app_models.models import UserOrder, SubUserOrder, OrderDetail, Warehouse
# from app_models.models import UserRole
from app_models.models import UserAsset


# 如果把admin.site替换成自定义的，暂时会有点问题
# class FeiAdminSite(admin.AdminSite):
#     def get_app_list(self, request):
#         ordering = {
#             'Proxy user assets': 1,
#             'Proxy userextras': 2,
#         }
#         app_dict = self._build_app_dict(request)
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])
#         return app_list
# 替换admin.site会有问题，先不要替换
# admin.site = FeiAdminSite()

class ProxyUserextra(UserExtra):
    class Meta:
        proxy = True

class ProxyUserAsset(UserAsset):
    class Meta:
        proxy = True

@admin.register(ProxyUserextra)
class UserExtraAdmin(admin.ModelAdmin):
    # list_display = ('user', 'weixin_openid', 'phone', 'qq', 'pay_password',)
    list_display = ('weixin_openid', 'phone', 'qq', 'pay_password',)
    # fields = ('user', 'weixin_openid', 'phone', 'qq', 'pay_password',)
    fields = ('weixin_openid', 'phone', 'qq', 'pay_password',)

@admin.register(ProxyUserAsset)
class UserAssetAdmin(admin.ModelAdmin):
    # list_display = ('user', 'balance')
    # fields = ('user', 'balance')
    list_display = ('balance',)
    fields = ('balance',)