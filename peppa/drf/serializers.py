from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError

def check_age(age):
    if age > 200 or age < 0:
        raise ValidationError('...')
    return age

class User1Serializer(serializers.ModelSerializer):
    type_name = serializers.ReadOnlyField(source='get_user_type_display')
    # name = serializers.CharField(max_length=8, min_length=2, trim_whitespace=True)
    # age = serializers.IntegerField(max_value=200, min_value=0, validators=[check_age, ])
    # gender = serializers.ChoiceField(choices=(1, 2))

    class Meta:
        model = User1
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    gender_name = serializers.ReadOnlyField(source='get_gender_display')
    name = serializers.CharField(max_length=8,min_length=2,trim_whitespace=True)
    age = serializers.IntegerField(max_value=200, min_value=0, validators=[check_age,])
    gender = serializers.ChoiceField(choices=(1,2))
    class Meta:
        model = Student
        fields = '__all__'
        # extra_kwargs = {
        #     'age':{'read_only': True}
        # }
        # read_only_fields = ('name',)

    # def validate_age(self,data):
    #     print(data)
    #     if data<150:
    #         return data
    #     raise ValidationError('年龄不能超过300')
    #
    # def validate(self, validate_data):
    #     name = validate_data.get('name')
    #     age = validate_data.get('age')
    #     if age>200 or age<0:
    #         raise ValidationError('...')
    #     return validate_data