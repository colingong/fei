"""这个middleware用于初始化一些模型
    例如，注册用户一开始只有基本的信息：username/first_name/last_name/email等，
    其它 UserExtra， UserAsset等等都没有数据，或者某些模型是后来增加的，也没有专门的初始化
    这个middleware用于判断用户的某些数据是否已初始化，如果没有则进行初始化，增加相应的记录
    例：当用户访问的时候，检测用户是否有UserAsset记录，如果没有，则为该用户初始化，balance=0
"""

from app_models.models_extra_user import UserExtra
from app_models.models_user_asset import UserAsset
from django.core.exceptions import ObjectDoesNotExist
import decimal

def add_initial_data(get_response):
    """检查当前登录用户的UserExtra和UserAsset记录是否存在

        如果不存在，则自动为用户添加一条记录到数据库
        UserExtra增加一条记录，其中weixin_openid/qq/phone/pay_password都为null
        由于weixin_openid/qq/phone均为unique，因此不能设为空字串''，null即可
        在以后某个场景，例如用户认证时，由用户将其中的部分或全部信息补齐

        UserAsset增加一条记录，将balance设为0即可
    """
    def middleware(request):
        # do sth here
        if request.user.is_authenticated:
            #  UserExtra 记录的处理
            try:
                request.user.userextra
            except ObjectDoesNotExist:
                print(f'---> 用户{request.user.username}的 userextra 不存在')
                userextra = UserExtra(user=request.user)
                userextra.save()

            # UserAsset 记录的处理
            try:
                request.user.userasset
            except ObjectDoesNotExist:
                print(f'---> 用户的 资产记录不存在')
                asset = UserAsset(user=request.user)
                asset.balance = 0
                asset.save()

        response = get_response(request)
        return response
    return middleware

