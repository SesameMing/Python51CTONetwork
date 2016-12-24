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
    ret = {"status": "0", "message": "帐号或密码错误"}

    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == '111':
        ret['status'] = 1
        ret['message'] = "验证成功"
        return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps(ret))


# 注册
def reg(request):
    return render(request, 'reg.html')


def cart(request):
    return render(request, 'cart.html')