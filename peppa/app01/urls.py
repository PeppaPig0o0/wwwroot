from django.urls import path,re_path

from app01 import views

urlpatterns = [
    path(r'', views.index),
    re_path(r'list/?', views.StudentList.as_view(), name='student_list')
    # path('api/student/list/', views.StudentList.as_view(), name='student_list'),

]
