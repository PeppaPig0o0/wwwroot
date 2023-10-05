from django.urls import path,include
from app02 import views

urlpatterns = [
    # path('', views.clazz_name),
    path('', views.index, name='index'),
    path('a', views.a, name='a'),
    path('setcookie', views.set_cookie, name='set_cookie'),
    path('getcookie', views.get_cookie, name='get_cookie'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('news', views.news, name='news'),

]