"""peppa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import ObtainJSONWebToken


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("admin/", admin.site.urls),
    path('', include('app02.urls')),
    # path('api/student/list/', views.StudentList.as_view(), name='student_list'),
    re_path(r'^api/student/?', include('app01.urls')),
    path('drf/', include('drf.urls', namespace='drf')),

    re_path(r'^api/?', include('api.urls')),
    re_path(r'^job/?', include('job.urls', namespace='job')),
    re_path(r'^login/?', ObtainJSONWebToken.as_view(), name='login')
]
