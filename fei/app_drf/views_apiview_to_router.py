"""实现类似api_view的功能，但是要能够注册到router，以便可以在api root能看到
    api_view不能注册到router，那么就换成一个viewset，但是实际上功能还是类似上面的function views那样
"""

from django.contrib.auth.models import User
from app_models.models import UserExtra
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response

class UserAndExtra(viewsets.ViewSet):
    lookup_field = 'username_or_pk'
    def retrieve(self, request, username_or_pk, format=None):
        user = None
        try:
            user = User.objects.get(username=username_or_pk)
        except:
            user = User.objects.get(id=username_or_pk)

        user_and_extra = {'username': user.username,
            'first_name': user.first_name,
            'weixin_openid': user.userextra.weixin_openid,
            'qq': user.userextra.qq}

        return Response(user_and_extra)

    def list(self, request, format=None):
        users = User.objects.all()

        user_and_extra = []

        for u in users:
            u_data = {'username': u.username,
            'first_name': u.first_name,
            'weixin_openid': u.userextra.weixin_openid,
            'qq': u.userextra.qq}
            user_and_extra.append(u_data)

        print(f'---> {user_and_extra}')
        return Response(user_and_extra)