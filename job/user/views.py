import random
import threading
from queue import Queue
import time

from django.shortcuts import render
from .models import *
from .serializers import *
from django.views.generic import ListView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, DestroyAPIView

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from collections import defaultdict
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from .auth import JobAuth
from .permission import *
from django.db.models import F, Q
from rest_framework.generics import CreateAPIView
from django.db import transaction
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from django.views.decorators.cache import cache_page
# Create your views here.


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserLoginView(APIView):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        uid = request.data.get('uid')
        name = request.data.get('name')

        try:
            user = User.objects.get(username=uid, name=name)
        except User.DoesNotExist:
            return Response({'错误': '用户身份信息出错'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        UserToken.objects.update_or_create(defaults={'token': token}, uid=user)

        serializer = UserSerializer(user)
        return Response({'jwttoken': token, 'user': serializer.data})


class StatusChangeView(APIView):
    authentication_classes = [JobAuth, ]
    permission_classes = [IsTeacher, ]

    @transaction.atomic
    def post(self, request):
        uid = request.data.get('uid')
        new_status = int(request.data.get('status'))
        old_status = int(request.data.get('old_status'))
        # return Response({'msg': uid, 'code': new_status})
        if (old_status >= 3) and (new_status < 3):
            return Response({'msg': '未择岗状态不能修改为择岗状态！', 'code': 1})

        elif (old_status >= 3) and (new_status >= 3):
            user = User.objects.get(username=uid)
            user.status_id = new_status
            user.save()
            return Response({'msg': '修改成功', 'code': 2})

        elif (old_status < 3) and (new_status < 3):
            user = User.objects.get(username=uid)
            user.status_id = new_status
            user.save()
            return Response({'msg': '修改成功', 'code': 2})

        elif (old_status < 3) and (new_status >= 3):
            try:
                with transaction.atomic():
                    user = User.objects.get(username=uid)
                    user.status_id = new_status
                    user.save()

                    record = Record.objects.get(sid=uid)

                    job = Job.objects.get(pk=record.job_id)
                    job.still_number = F("still_number") + 1
                    job.save()

                    record.delete()
            except Exception as e:
                # Handle the exception and return an error response
                return Response({'msg': '修改失败', 'code': 3})

            return Response({'msg': '修改成功', 'code': 2})





# 首页
@cache_page(30)
def index(request):
    return render(request, 'job.html')


# 学生选岗信息列表管理页面
@cache_page(30)
def record(request):
    return render(request, 'record.html')


# 学生信息新增或修改页面
# @cache_page(30)
def usercreate(request):
    return render(request, 'usercreate.html')


# 用户管理页面
# @cache_page(30)
def users(request):
    return render(request, 'user.html')


# 用户管理模块
class UserView(ModelViewSet):
    authentication_classes = [JobAuth, ]

    permission_classes = [IsTeacher, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (SearchFilter, OrderingFilter,)  # 指定过滤器
    filterset_fields = ['clazz__id', ]
    search_fields = ['clazz__id', ]  # 指定可搜索的字段

    def list(self, request, *args, **kwargs):
        clazz_value = request.query_params.get('clazz')
        queryset = self.filter_queryset(self.get_queryset())

        if clazz_value:
            # 根据传入的 search 参数进行精确查找
            queryset = queryset.filter(Q(clazz__id=clazz_value))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        # user = User.objects.get(username=uid)
        # user.status_id = new_status
        # user.save()
        try:
            record = Record.objects.get(sid=instance.username)
            job = Job.objects.get(pk=record.job_id)
            job.still_number = F("still_number") + 1
            job.save()
            record.delete()

        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({'msg':'删除成功'},status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserStatusChange(ModelViewSet):
    authentication_classes = [JobAuth, ]

    permission_classes = [IsTeacher, ]
    queryset = User.objects.all()
    serializer_class = UserstatusSerializer

    filter_backends = (SearchFilter, OrderingFilter,)  # 指定过滤器
    filterset_fields = ['clazz__id', ]
    search_fields = ['clazz__id', ]  # 指定可搜索的字段

    @transaction.atomic
    def change_status(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        username = kwargs.get('username')

        try:
            instance = self.get_queryset().get(username=username)
        except User.DoesNotExist:
            return Response({'msg': '用户不存在', 'code': 404}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        new_status = int(data.get('status'))
        old_status = int(data.get('old_status'))

        if old_status >= 3 and new_status < 3:
            return Response({'msg': '未择岗状态不能修改为择岗状态！', 'code': 1}, status=status.HTTP_400_BAD_REQUEST)
        # Update user status
        instance.status_id = new_status
        instance.save()

        if old_status < 3 and new_status >= 3:
            try:
                with transaction.atomic():
                    record = Record.objects.get(sid=username)
                    job = record.job
                    job.still_number = F("still_number") + 1
                    job.save()

                    record.delete()


            except Record.DoesNotExist:
                return Response({'msg': '修改失败，未找到相关记录', 'code': 3}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'msg': '修改失败', 'code': 3}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # return Response({'msg': '22222', 'code': 404}, status=status.HTTP_200_OK)
        self.perform_update(serializer)

        return Response({'msg': '修改成功', 'code': 2})


# 岗位信息列表
class JobView(ListAPIView):
    authentication_classes = [JobAuth, ]
    # queryset = Student.objects.filter(is_delete=False)
    queryset = Job.objects.filter(is_end=0)
    serializer_class = JobSerializer


# 获取所有公司列表
class GetCompanyView(CacheResponseMixin,ModelViewSet):
    cache_response_timeout = 120
    authentication_classes = [JobAuth, ]

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.get_serializer(page, many=True)
            res = []
            for i in serializer.data:
                res.append([i['id'], i['cname']])

            return self.get_paginated_response(res)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 根据公司名，获取对应公司名下所有岗位的ID和名字
class GetJobView(CacheResponseMixin,ReadOnlyModelViewSet):
    cache_response_timeout = 120
    authentication_classes = [JobAuth, ]

    queryset = Job.objects.filter(still_number__gt=0, is_end=0)

    serializer_class = JobSerializer
    filter_backends = (SearchFilter, OrderingFilter,)  # 指定过滤器

    filterset_fields = ['company__id',]
    search_fields = ['company__id', ]  # 指定可搜索的字段

    def list(self, request, *args, **kwargs):
        search_value = request.query_params.get('search')
        queryset = self.filter_queryset(self.get_queryset())

        if search_value:
            # 根据传入的 search 参数进行精确查找
            queryset = queryset.filter(Q(company__id=search_value))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            res = [[item['id'], item['jname']] for item in serializer.data]
            return self.get_paginated_response(res)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 获取所有班级列表
class GetClazzView(CacheResponseMixin,ReadOnlyModelViewSet):
    cache_response_timeout = 120
    authentication_classes = [JobAuth, ]
    queryset = Clazz.objects.all()
    serializer_class = ClazzSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.get_serializer(page, many=True)
            res = []
            for i in serializer.data:
                res.append([i['id'], i['clazz_name']])

            return self.get_paginated_response(res)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 查看岗位报名列表
class RecordView(ReadOnlyModelViewSet):
    authentication_classes = [JobAuth, ]
    permission_classes = [IsTeacher,]

    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    filter_backends = (SearchFilter, OrderingFilter,)  # 指定过滤器
    # filterset_fields = ['clazz__id',]
    # search_fields = ['clazz__id', ]  # 指定可搜索的字段

    def list(self, request, *args, **kwargs):
        search_value = request.query_params.get('search')
        clazz_id = request.query_params.get('clazz')
        company_id = request.query_params.get('company')

        queryset = self.filter_queryset(self.get_queryset())

        if search_value:
            # 根据传入的 search 参数进行精确查找
            queryset = queryset.filter(Q(clazz__id=search_value) | Q(company__id=search_value))

        if clazz_id:
            # 根据传入的 clazz 参数进行精确查找
            queryset = queryset.filter(clazz__id=clazz_id)

        if company_id:
            # 根据传入的 company 参数进行精确查找
            queryset = queryset.filter(company__id=company_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 删除一条学生选岗信息
class RecordDestroyView(DestroyAPIView):
    authentication_classes = [JobAuth, ]
    permission_classes = [IsTeacher,]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        obj = Job.objects.get(pk=instance.job_id)
        obj.still_number = F("still_number") + 1
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 学生提交岗位信息
class RecordCreateView(CreateAPIView):
    authentication_classes = [JobAuth, ]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                obj = Job.objects.select_for_update().get(pk=request.data['job'], still_number__gt=0)
                obj.still_number -= 1
                obj.save()
                time.sleep(0.7)
                self.perform_create(serializer)
                user = User.objects.get(username=request.data.get('sid'))
                user.status_id = 1
                user.save()
        except Exception as e:
            # Handle the exception and return an error response
            return Response({'error': '岗位已被选完，请选择其他岗位'}, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



