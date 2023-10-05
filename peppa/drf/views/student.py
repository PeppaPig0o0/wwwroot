import random
import uuid

import django_filters

from ..models import *
from ..serializers import *
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from ..filters import StudentFilter
from rest_framework.permissions import BasePermission




# Create your views here.

'''
1.APIView通用类视图
'''


class StudentList(APIView):

    def get(self, request):
        queryset = Student.objects.filter(is_delete=False)
        res = StudentSerializer(instance=queryset, many=True)
        if res:
            return Response(res.data, status=status.HTTP_200_OK)
        return Response(res.data, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):

        res = StudentSerializer(data=request.data)
        if res.is_valid():
            res.save()
            return Response(res.data, status=status.HTTP_201_CREATED)
        return Response(res.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_obj(self, pk):
        try:
            return Student.objects.get(pk=pk, is_delete=False)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_obj(pk)
        serializer = StudentSerializer(instance=queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_obj(pk)
        serializer = StudentSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        queryset = self.get_obj(pk)
        queryset.is_delete = True
        queryset.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)


'''
2.GenericAPIView
继承自APIVIew。
主要增加了操作序列化器和数据库查询的方法，作用是为下面Mixin扩展类的执行提供方法支持。
通常在使用时，可搭配一个或多个Mixin扩展类。
'''


class StudentList_V2(GenericAPIView):
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer

    def get(self, request):
        students = self.get_queryset()
        res = self.get_serializer(instance=students, many=True)
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = self.get_serializer(data=request.data)
        if res.is_valid():
            res.save()
            return Response(res.data, status=status.HTTP_201_CREATED)
        return Response(res.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail_V2(GenericAPIView):
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer

    def get(self, request, pk):
        student = self.get_object()
        res = self.get_serializer(instance=student)
        return Response(res.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = self.get_object()
        res = self.get_serializer(instance=student, data=request.data)
        if res.is_valid():
            res.save()
            return Response(res.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(res.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        student = self.get_object()
        if student:
            student.is_delete = True
            student.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


'''
3.GenericAPIView+5个视图扩展类
*重要* 
'''


class StudentList_V3(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetail_V3(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer

    def get(self, request, pk):

        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    def perform_destroy(self, instance):  # 重写删除方法，逻辑删除
        instance.is_delete = True
        instance.save(update_fields=['is_delete'])


'''
4. GenericAPIView的视图子类 9个
CreateAPIView,ListAPIView,RetrieveAPIView,DestoryAPIView,UpdateAPIView 
ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
'''


class StudentList_V4(ListCreateAPIView):
    # queryset = Student.objects.filter(is_delete=False)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['name', 'age', 'gender']  # 指定过滤的字段
    ordering_fields = ('age','name')
    # filter_class = StudentFilter

class StudentDetail_V4(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save(updata_fields=['is_delete'])

'''
5. modelviewset 
'''
class StudentView_V5(ModelViewSet):

    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['name', 'age', 'gender']  # 指定过滤的字段
    ordering_fields = ('age','name','gender')


'''
6.modelviewset 中的action
'''
from ..auth import MyAuth
class StudentView_V6(ModelViewSet):
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['name', 'age', 'gender']  # 指定过滤的字段
    ordering_fields = ('age','name')

    # methods 请求方式，  detail:True单条查询，带pk
    @action(methods=['GET'], detail=False)
    def get_2(self, request):
        students = self.get_queryset()
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

'''
7.加入了jwt认证的第6个案例
'''
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class StudentView_V7(ModelViewSet):
    authentication_classes = [MyAuth,]
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['name', 'age', 'gender']  # 指定过滤的字段
    ordering_fields = ('age', 'name')

    # methods 请求方式，  detail:True单条查询，带pk
    @action(methods=['GET'], detail=False)
    def get_2(self, request):
        students = self.get_queryset()
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentView_V8(StudentView_V7):
    ...


class LoginView(APIView):
    # authentication_classes = []

    def post(self, request):
        query = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
        }
        user = User1.objects.filter(**query).first()
        if user:
            token = uuid.uuid4()
            User1Token.objects.update_or_create(defaults={'token': token}, user=user)
            return Response({'status': 100, 'msg': '登录成功', 'token': token})
        else:
            return Response({'status': 100, 'msg': '用户名或密码错误'})



