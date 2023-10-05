from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views import View
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from collections import defaultdict
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from .auth import JobAuth
from .permission import *
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
        return Response({'jwttoken': token})


# class UserProfileView(APIView):
#     def get(self, request):
#         user = request.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data)



        # permission_classes = [IsAuthenticated, IsTeacher]


def index(request):
    return render(request, 'job.html')


def record(request):
    return render(request, 'record.html')


class JobView(ListAPIView):
    # authentication_classes = [JobAuth,]
    permission_classes = [IsTeacher]
    # queryset = Student.objects.filter(is_delete=False)
    queryset = Job.objects.all()
    serializer_class = JobSerializer

 # 获得公司
# def getProvince(request):
#      provinces = AreaInfo.objects.filter(aParent__isnull = True)
#       res = []
#       for i in provinces:
#          res.append( [i.id , i.atitle] )
#      return JsonResponse({'provinces':res})
#
#  # 获得城市
# def getCity(request):
#      city_id = request.GET.get('city_id')
#      cities = AreaInfo.objects.filter(aParent_id=city_id)
#      res = []
#      for i in cities:
#          res.append([i.id, i.atitle])
#      return JsonResponse({'cities':res})

class GetCompanyView(ReadOnlyModelViewSet):
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

class GetJobView(ReadOnlyModelViewSet):
    queryset = Job.objects.filter(still_number__gt=0)
    # queryset = Job.objects.all()

    serializer_class = JobSerializer
    filter_backends = (SearchFilter, OrderingFilter,)  # 指定过滤器

    filterset_fields = ['company__id',]
    search_fields = ['company__id', ]  # 指定可搜索的字段
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.get_serializer(page, many=True)
            res = []
            for i in serializer.data:
                res.append([i['id'], i['jname']])
            return self.get_paginated_response(res)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GetClazzView(ReadOnlyModelViewSet):
    queryset = Clazz.objects.all()
    serializer_class = ClazzSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.get_serializer(page, many=True)
            res = []
            for i in serializer.data:
                res.append([i['id'], i['clazz']])

            return self.get_paginated_response(res)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from django.db.models import F
class RecordView(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    # filter_backends = (SearchFilter, OrderingFilter,)  # 指定过滤器
    #
    # filterset_fields = ['company__cname','job__jname']
    # search_fields = ['company__name','job__jname', 'sid', 'sname']  # 指定可搜索的字段

    def create(self, request, *args, **kwargs):
        # print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)


        obj = Job.objects.get(pk=request.data['job'])
        obj.still_number = F("still_number") - 1
        obj.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        obj = Job.objects.get(pk=instance.job_id)
        obj.still_number = F("still_number") + 1
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)






