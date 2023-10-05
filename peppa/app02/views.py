
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from .models import *
from django.core.cache import cache
from rest_framework.views import APIView
# from .serializers import StudentSerializer
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    # uname = request.session.get('uname')
    # if uname=='111':
    #     return render(request, 'index.html', {'uname':uname})
    return render(request, 'index.html')
def a(request):
    # uname = request.session.get('uname')
    # if uname=='111':
    #     return render(request, 'index.html', {'uname':uname})
    return render(request, 'a.html')

# def index(request):
#     uname = request.session.get('uname')
#     if uname=='111':
#         return render(request, 'index.html', {'uname':uname})
#     return redirect('login')


def clazz_name(request):
    student = Student.objects.get(pk=1)

    clazz = student.clazz
    # url = reverse('index')

    #return HttpResponse(clazz.name)
    # return HttpResponseRedirect('app02/index')
    return redirect('app02/index')

def set_cookie(request):
    data = {
        'username': '123',
        'password': '456'
    }
    response = HttpResponse('设置cookie')
    response.set_cookie('username', '123')
    response.set_cookie('password', '456')
    return response

def get_cookie(request):
    username = request.COOKIES.get('username')
    csrf = request.COOKIES.get('csrftoken')
    return HttpResponse([csrf,username])


def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    if request.POST.get('uname')=='111' and request.POST.get('pwd')=='456':
        # response.set_cookie('uname', '111', max_age=30)
        request.session['uname'] = '111'
        return redirect('index')
    return HttpResponse('登录失败')


def logout(request):
    response = redirect('login')
    request.session.flush()
    return response


# @cache_page(timeout=30,cache=None, key_prefix=None)
def news(request):
    result = cache.get('news',)
    if result:
        return render(request, 'news.html', {'news_list': result})
    news_list = []
    for a in Student.objects.all():
        news_list.append(a.name)
    cache.set('news', news_list, timeout=30)
    return render(request, 'news.html', {'news_list': news_list})




