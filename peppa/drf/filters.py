
from django_filters import rest_framework as filters
from .models import Student


class StudentFilter(filters.FilterSet):
    min_age = filters.NumberFilter(field_name="age", lookup_expr='gte')
    max_age = filters.NumberFilter(field_name="age", lookup_expr='lte')
    # sort = filters.OrderingFilter(fields=('age',))
    class Meta:
        model = Student
        fields = ['name', 'gender']
        # fields = {
        #     'name': ['exact', 'icontains'],
        #     'age': ['exact', ],
        #     'gender': ['exact', ],
        # }