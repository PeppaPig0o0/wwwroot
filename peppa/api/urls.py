from django.urls import path, include, re_path
from api import views
from rest_framework import routers
router = routers.SimpleRouter()

# router.register('student/v5', views.StudentView_V5, 'student_v5')
# router.register('student/v6', views.StudentView_V6, 'student_v6')
# router.register('student/v7', views.StudentView_V7, 'student_v7')
urlpatterns = [
    path('class_06/spot', views.Class06SpotView.as_view({'get': 'list'}), name='class06_spot'),
    path('class_06/spot/<int:pk>', views.Class06SpotView.as_view({'get': 'retrieve'}), name='class06_spot'),

    path('class_05/items', views.Class05ItemsView.as_view({'get':'list'}), name='class05_items'),
    path('class_05/items/<int:pk>', views.Class05ItemsView.as_view({'get':'retrieve'}), name='class05_item'),

    path('class_05/info', views.Class05InfoView.as_view({'get': 'list'}), name='class05_info'),
    path('class_05/info/<int:pk>', views.Class05InfoView.as_view({'get': 'retrieve'}), name='class05_info'),

    path('class_05/province', views.Class05ProvinceView.as_view({'get':'list'}), name='class05_items'),
    path('class_05/province/<int:pk>', views.Class05ProvinceView.as_view({'get':'retrieve'}), name='class05_item'),

    path('class_05/source', views.Class05SourceView.as_view({'get': 'list'}), name='class05_source'),
    path('class_05/source/<int:pk>', views.Class05SourceView.as_view({'get': 'retrieve'}), name='class05_source'),

    path('class_05/temp', views.Class05TempView.as_view({'get': 'list'}), name='class05_temp'),
    path('class_05/temp/<int:pk>', views.Class05TempView.as_view({'get': 'retrieve'}), name='class05_temp'),

    path('class_01/type', views.Class01TypeView.as_view({'get':'list'}), name='class01_types'),
    path('class_01/type/<int:pk>', views.Class01TypeView.as_view({'get':'retrieve'}), name='class01_type'),

    path('class_01/city', views.Class01CityView.as_view({'get':'list'}), name='class01_cities'),
    path('class_01/city/<int:pk>', views.Class01CityView.as_view({'get':'retrieve'}), name='class01_city'),

    path('class_01/sales', views.Class01SalesView.as_view({'get':'list'}), name='class01_sales'),
    path('class_01/sales/<int:pk>', views.Class01SalesView.as_view({'get':'retrieve'}), name='class01_sales'),

    path('class_01/age', views.Class01AgeView.as_view({'get':'list'}), name='class01_ages'),
    path('class_01/age/<int:pk>', views.Class01AgeView.as_view({'get':'retrieve'}), name='class01_age'),

    path('class_01/way', views.Class01WayView.as_view({'get':'list'}), name='class01_ways'),
    path('class_01/way/<int:pk>', views.Class01WayView.as_view({'get':'retrieve'}), name='class01_way'),

    path('class_01/day', views.Class01DayView.as_view({'get':'list'}), name='class01_days'),
    path('class_01/day/<int:pk>', views.Class01DayView.as_view({'get':'retrieve'}), name='class01_days'),

    path('class_08/store', views.Class08StoreView.as_view({'get':'list'}), name='class08_stores'),
    path('class_08/tystorepe/<int:pk>', views.Class08StoreView.as_view({'get':'retrieve'}), name='class08_store'),

    path('class_08/type', views.Class08TypeView.as_view({'get': 'list'}), name='class08_type'),
    path('class_08/type/<int:pk>', views.Class08TypeView.as_view({'get': 'retrieve'}), name='class08_type'),

    path('class_08/month', views.Class08MonthView.as_view({'get': 'list'}), name='class08_month'),
    # path('class_08/type/<int:pk>', views.Class08TypeView.as_view({'get': 'retrieve'}), name='class08_type'),

    path('class_02/player', views.Class02PlayerView.as_view({'get':'list'}), name='class02_player'),
    path('class_02/player/<int:pk>', views.Class02PlayerView.as_view({'get':'retrieve'}), name='class02_player'),
    path('class_02/sales', views.Class02SalesView.as_view({'get': 'list'}), name='class02_sales'),
    path('class_02/sales/<int:pk>', views.Class02SalesView.as_view({'get': 'retrieve'}), name='class02_sales'),
]

urlpatterns += router.urls
