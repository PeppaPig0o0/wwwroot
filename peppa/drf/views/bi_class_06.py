import random
import django_filters
from ..models import Student
from ..serializers import *
from django.http.response import JsonResponse
from django.views import View
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

class Class06Gauge(View):
    def get(self, request):
        percent = random.randint(1,100)
        data = {
            'data':percent
        }
        return JsonResponse(data, content_type='application/json', json_dumps_params={'ensure_ascii': False})


