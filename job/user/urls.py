from django.urls import path, re_path
# from .views import *
from user import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.register(r'your-models', views.RecordView)
router.register('record', views.RecordView, 'record')
router.register('user', views.UserView, 'user')
# router.register(r'changestatus', views.UserStatusViewSet, 'changestatus')
app_name = 'job'

urlpatterns = [
    path('', views.index, name='index'),
    path('statuschange', views.StatusChangeView.as_view(), name='statuschange'),
    # path('change_status/<int:pk>', views.UserStatusViewSet.as_view({'post': 'change_status'}), name='user-change-status'),
    path('users/<str:username>/change_status/', views.UserStatusChange.as_view({'put': 'change_status'}), name='change_status'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('joblist', views.JobView.as_view(), name='job'),
    path('getcompany', views.GetCompanyView.as_view({'get': 'list', 'post': 'create'}), name='getcompany'),
    path('getcompany/<int:pk>', views.GetCompanyView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='retrieve'),
    path('getjob', views.GetJobView.as_view({'get': 'list'}), name='getjob'),
    path('getclazz', views.GetClazzView.as_view({'get': 'list'}), name='getclazz'),

    path('job_record/add', views.RecordCreateView.as_view(), name='record_add'),
    path('job_record/delete/<int:pk>', views.RecordDestroyView.as_view(), name='record_delete'),
    path('records', views.record, name='records'),
    path('users', views.users, name='users'),
    path('usercreate', views.usercreate, name='usercreate'),


    # path('record', views.RecordListView.as_view(), name='record'),
    # path('record/add', views.RecordCreateView.as_view(), name='record_add'),
    # re_path(r'^image/?$', views.image, name='image'),
    # re_path(r'^upload_image/?$', views.upload_image, name='upload_image'),
    # # path('/delete_image/<str:image_path>/', views.delete_image, name='delete_image'),
    # re_path(r'^delete_image/(?P<image_path>.+)/$', views.delete_image, name='delete_image'),
]

urlpatterns += router.urls
