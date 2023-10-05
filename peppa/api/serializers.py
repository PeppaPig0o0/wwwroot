from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError

# def check_age(age):
#     if age > 200 or age < 0:
#         raise ValidationError('...')
#     return age

# class StudentSerializer(serializers.ModelSerializer):
#     gender_name = serializers.ReadOnlyField(source='get_gender_display')
#     name = serializers.CharField(max_length=8,min_length=2,trim_whitespace=True)
#     age = serializers.IntegerField(max_value=200, min_value=0, validators=[check_age,])
#     gender = serializers.ChoiceField(choices=(1,2))
#     class Meta:
#         model = Student
#         fields = '__all__'
#         extra_kwargs = {
#             'age':{'read_only': True}
#         }



class Class05ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class05Items
        fields = '__all__'

class Class05TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class05Temp
        fields = '__all__'

class Class05ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class05Province
        fields = '__all__'



class Class05SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class05Source
        fields = '__all__'


class Class05InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class05Info
        fields = '__all__'


class Class01TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class01Type
        fields = '__all__'

class Class01SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class01Sales
        exclude = ['id']

class Class01AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class01Age
        exclude = ['id']
class Class01CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Class01City
        exclude = ['id']

class Class01WaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Class01Way
        exclude = ['id']
class Class01DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Class01Day
        exclude = ['id']


class Class08StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class08Store
        fields = '__all__'

class Class08MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class08Month
        fields = '__all__'


class Class02PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class02Player
        fields = '__all__'

class Class02SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class02Sales
        fields = '__all__'


class Class06SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class06Spot
        fields = '__all__'