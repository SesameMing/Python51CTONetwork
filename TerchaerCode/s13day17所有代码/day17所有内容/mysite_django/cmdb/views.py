from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from cmdb import models
# Create your views here.
# 处理用户请求

def index(request):
    # ...
    # 判断用户是否是POST请求
    # return redirect('http://baidu.com')
    # return redirect('')

    if(request.method == 'POST'):
        u = request.POST.get('user',None)
        e = request.POST.get('email',None)
        models.UserInfo.objects.create(user=u,email=e)

        # request.POST.get('pwd',None)

    # return HttpResponse('123')
    # 模版引擎
    # 获取index.html模版 + {'data': USER_INPUT } ==》 渲染
    # 字符串

    data_list = models.UserInfo.objects.all()
    # [UserInfo对象，UserInfo对象，。。。]
    # for item in data_list:
    #     print(item.user,item.email)
    return render(request, 'index.html', {'data': data_list })