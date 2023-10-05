from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializers import StudentSerializer
# Create your views here.
def index(request):
    return HttpResponse('成功')

class StudentList(APIView):
    authentication_classes = ()
    # permission_classes = [AllowAny]
    print(123)
    def get(self, request):
        print(456)
        queryset = Student.objects.all()

        res = StudentSerializer(instance=queryset, many=True)
        return Response(res.data, status=status.HTTP_200_OK)


    def post(self,request):
        res = StudentSerializer(data=request.data)
        if res.is_valid():
            res.save()
            return Response(data=res.data, status=status.HTTP_201_CREATED)
        return Response(res.errors, status=status.HTTP_400_BAD_REQUEST)
