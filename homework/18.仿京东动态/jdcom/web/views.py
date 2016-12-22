from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
# Create your views here.


# 商城首页
def index(request):
    return render(request, 'index.html')


# 登录页面
def login(request):
    return render(request, 'login.html')


def login_ajax(request):
    ret = {"status": "", "message": ""}


    return HttpResponse(json.dumps(ret))


# 注册
def reg(request):
    return render(request, 'reg.html')
