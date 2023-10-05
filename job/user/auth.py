from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import *


# jwt自定义
# class MyAuth(BaseJSONWebTokenAuthentication):
#     # 获取jwt的token值
#     def authenticate(self, request):
#         jwt_value = request.META.get('HTTP_AUTHORIZATION')
#         if not jwt_value:
#             raise exceptions.AuthenticationFailed('Authorization字段是必须的')
#         try:
#             # 认证
#             payload = jwt_decode_handler(jwt_value)
#         except jwt.ExpiredSignature:
#             raise exceptions.AuthenticationFailed('token过期')
#         except jwt.DecodeError:
#             raise exceptions.AuthenticationFailed('解码错误')
#         except jwt.InvalidTokenError:
#             raise exceptions.AuthenticationFailed('token无效')
#         # 获取用户对象
#         user = self.authenticate_credentials(payload)
#
#         return user, jwt_value


# drf自定义
class JobAuth(BaseAuthentication):
    def authenticate(self, request):
        if request.data.get('token'):
            token = request.data.get('token')
        else:
            token = request.GET.get('token')

        if token:
            user_token = UserToken.objects.filter(token=token).first()
            if user_token:
                # print(request.user)
                return user_token.uid, token
            else:
                raise AuthenticationFailed('认证失败')
        else:
            raise AuthenticationFailed('请重新登录，获取token')

