from django.shortcuts import render

# Create your views here.
import random
from collections import defaultdict
import django_filters
from .models import *
from .serializers import *
from django.http.response import JsonResponse
from django.views import View
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class Class06SpotView(ReadOnlyModelViewSet):
    queryset = Class06Spot.objects.all()
    serializer_class = Class06SpotSerializer


class Class05ItemsView(ReadOnlyModelViewSet):
    queryset = Class05Items.objects.all()
    serializer_class = Class05ItemsSerializer


class Class05InfoView(ReadOnlyModelViewSet):
    queryset = Class05Info.objects.all()
    serializer_class = Class05InfoSerializer


class Class05SourceView(ReadOnlyModelViewSet):
    queryset = Class05Source.objects.all()
    serializer_class = Class05SourceSerializer


class Class05TempView(ReadOnlyModelViewSet):
    queryset = Class05Temp.objects.all()
    serializer_class = Class05TempSerializer


class Class05ProvinceView(ReadOnlyModelViewSet):
    queryset = Class05Province.objects.all()
    serializer_class = Class05ProvinceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Class01TypeView(ReadOnlyModelViewSet):
    queryset = Class01Type.objects.all()
    serializer_class = Class01TypeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Class01SalesView(ReadOnlyModelViewSet):
    queryset = Class01Sales.objects.all()
    serializer_class = Class01SalesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.get_serializer(page, many=True)
            result = defaultdict(list)

            for item in serializer.data:
                result[item['year']].append(item['money'])
            result = {year: monthly_data for year, monthly_data in result.items() if any(monthly_data)}
            return self.get_paginated_response(result)


        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Class01CityView(ReadOnlyModelViewSet):
    queryset = Class01City.objects.all().order_by('-money')
    serializer_class = Class01CitySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['city', 'province', 'money']  # 指定过滤的字段
    ordering_fields = ('money', 'city', 'province')

class Class01AgeView(ReadOnlyModelViewSet):
    queryset = Class01Age.objects.all()
    serializer_class = Class01AgeSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # results = defaultdict(list)
            # results['age'] = [item['age'] for item in serializer.data]
            # results['money'] = [item['money'] for item in serializer.data]
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Class01WayView(ReadOnlyModelViewSet):
    queryset = Class01Way.objects.all()
    serializer_class = Class01WaySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            results = defaultdict(list)
            results['way'] = [item['way'] for item in serializer.data]
            results['money'] = [item['money'] for item in serializer.data]
            return self.get_paginated_response(results)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Class01DayView(ReadOnlyModelViewSet):
    queryset = Class01Day.objects.all()
    serializer_class = Class01DaySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            results = defaultdict(list)
            results['day'] = [item['day'] for item in serializer.data]
            results['money'] = [item['money'] for item in serializer.data]
            results['month_total'] = sum(results['money'])
            print(results)

            return self.get_paginated_response(results)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class Class08TypeView(ReadOnlyModelViewSet):
    queryset = Class08Store.objects.all()
    serializer_class = Class08StoreSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = defaultdict(list)

            for item in serializer.data:
                result[item['store']].append(item['sales_today'])

            return self.get_paginated_response(result)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class Class08MonthView(ReadOnlyModelViewSet):
    queryset = Class08Month.objects.all()
    serializer_class = Class08MonthSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = defaultdict(list)

            for item in serializer.data:
                result[item['store']] = item['money'].replace(' ','').split(',')

            return self.get_paginated_response(result)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Class08StoreView(ReadOnlyModelViewSet):
    queryset = Class08Store.objects.all()
    serializer_class = Class08StoreSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            print(123)
            serializer = self.get_serializer(page, many=True)
            print(serializer.data)
            stores = []
            stores_number = []
            drinks = []
            drinks_number = []
            for i in serializer.data:
                if i['store'] not in stores:
                    stores.append(i['store'])
                if i['drink'] not in drinks:
                    drinks.append(i['drink'])
            for i in stores:
                a = 0
                for j in serializer.data:
                    if i == j['store']:
                        a += j['sales_today']
                stores_number.append(a)
            for i in drinks:
                b = 0
                for j in serializer.data:
                    if i == j['drink']:
                        b += j['sales_today']
                drinks_number.append(b)

            res = {
                'stores':stores,
                'stores_number':stores_number,
                'drinks':drinks,
                'drinks_number':drinks_number
            }

            return self.get_paginated_response(res)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class Class02PlayerView(ReadOnlyModelViewSet):
    queryset = Class02Player.objects.all()
    serializer_class = Class02PlayerSerializer

class Class02SalesView(ReadOnlyModelViewSet):
    queryset = Class02Sales.objects.all()
    serializer_class = Class02SalesSerializer