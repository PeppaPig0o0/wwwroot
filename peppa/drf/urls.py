from django.urls import path, re_path
from rest_framework import routers
from rest_framework_jwt.views import ObtainJSONWebToken

from drf import views

router = routers.SimpleRouter()
router.register('student/v5', views.StudentView_V5, 'student_v5')
router.register('student/v6', views.StudentView_V6, 'student_v6')
# router.register('student/v8', views.StudentView_V8, 'student_v8')
# router.register('student/v7', views.StudentView_V7, 'student_v7')

app_name = 'drf'

urlpatterns = [
    re_path(r'^image/?$', views.image, name='image'),
    re_path(r'^upload_image/?$', views.upload_image, name='upload_image'),
    # path('/delete_image/<str:image_path>/', views.delete_image, name='delete_image'),
    re_path(r'^delete_image/(?P<image_path>.+)/$', views.delete_image, name='delete_image'),

    path('index', views.Index.as_view(msg='请求成功'), name='index'),
    # re_path(r'^login/?', ObtainJSONWebToken.as_view(), name='login'),
    # re_path(r'^refresh/?', RefreshJSONWebToken.as_view(), name='refresh'),
    re_path(r'^login/?', views.LoginView.as_view(), name='login'),
    path('bi_class05/pie1', views.Class05Pie1.as_view(), name='class05_pie1'),
    path('bi_class06/gauge', views.Class06Gauge.as_view(), name='class06_gauge'),
    path('stackline01', views.StackLine01.as_view(msg='请求成功'), name='stackline01'),

    path('student', views.StudentList.as_view(), name='student'),
    path('student/<int:pk>', views.StudentDetail.as_view(), name='student'),

    path('student/v2', views.StudentList_V2.as_view(), name='student_v2'),
    path('student/v2/<int:pk>', views.StudentDetail_V2.as_view(), name='student_v2'),

    path('student/v3', views.StudentList_V3.as_view(), name='student_v3'),
    path('student/v3/<int:pk>', views.StudentDetail_V3.as_view(), name='student_v3'),

    path('student/v4', views.StudentList_V4.as_view(), name='student_v4'),
    path('student/v4/<int:pk>', views.StudentDetail_V4.as_view(), name='student_v4'),

    path('student/v7', views.StudentView_V7.as_view({'get': 'list', 'post': 'create'}), name='student_v7'),
    path('student/v7/<int:pk>', views.StudentView_V7.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name='student_v7'),

    path('student/v8', views.StudentView_V8.as_view({'get': 'list', 'post': 'create'}), name='student_v8'),
    path('student/v8/<int:pk>', views.StudentView_V8.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name='student_v8'),
]

urlpatterns += router.urls
