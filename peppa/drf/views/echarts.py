from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Student

from ..serializers import *
from django.http import Http404
# Create your views here.

class Index(View):
    msg = None
    def get(self,request):
        response = {
            'msg': self.msg,
            'status_code': 200,
            'data': {
                'name':['张三','李四','王五','赵六'],
                'yuwen': [random.randint(10,90) for i in range(4)],
                'shuxue': [random.randint(10,90) for i in range(4)]
            }
        }
        return JsonResponse(response, content_type='application/json', json_dumps_params={'ensure_ascii': False})




class StackLine01(View):
    msg = None

    def get(self, request):

        data = [[140, 232, 101, 264, 90, 340, 250],]
        a = []
        for i in range(5):
            if i == 0:
                a == data[0]
            else:
                # a = [j+random.randint(20,80) for j in data[i-1]]
                a= [random.randint(50,150) for j in range(7)]
                data.append(a)
        response = {
            'msg': self.msg,
            'status_code': 200,
            'data': data
        }
        return JsonResponse(response, content_type='application/json', json_dumps_params={'ensure_ascii': False})
