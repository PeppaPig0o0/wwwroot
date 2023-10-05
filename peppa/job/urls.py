from django.urls import path, re_path
from .views import *
from job import views
app_name = 'job'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('joblist', views.JobView.as_view(), name='job'),
    path('getcompany', views.GetCompanyView.as_view({'get': 'list'}), name='getcompany'),
    path('getjob', views.GetJobView.as_view({'get': 'list'}), name='getjob'),
    path('getclazz', views.GetClazzView.as_view({'get': 'list'}), name='getclazz'),
    path('record', views.RecordView.as_view({'get': 'list', 'post': 'create'}), name='record'),
    path('record/<int:pk>', views.RecordView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name='record_delete'),
    path('records', views.record, name='records'),
    # re_path(r'^image/?$', views.image, name='image'),
    # re_path(r'^upload_image/?$', views.upload_image, name='upload_image'),
    # # path('/delete_image/<str:image_path>/', views.delete_image, name='delete_image'),
    # re_path(r'^delete_image/(?P<image_path>.+)/$', views.delete_image, name='delete_image'),
]


