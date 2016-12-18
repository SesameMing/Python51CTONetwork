from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from cmdb import models


def index(request):
    # 判断用户是否是POST请求

    # return redirect('http://wwww.baidu.com')
    if request.method == 'POST':
        u = request.POST.get('user', None)
        e = request.POST.get('email', None)
        models.UserInfo.objects.create(user=u, email=e)

    data_list = models.UserInfo.objects.all()
    # [UserInfo对象, UserInfo对象, UserInfo对象]

    return render(request, 'index.html', {'data': data_list})
