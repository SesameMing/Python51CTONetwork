from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def login(request):
    # return  HttpResponse('Login')
    # request 包含用户提交的所有信息
    # 获取用户的提交方式
    # print(request.method)
    error_msg = ''
    if request.method == 'POST':
        # 下面的方式 如果不存在会报错
        # user = request.POST['user']
        # pwd = request.POST['pwd']
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == 'root' and pwd == '123':
            return redirect('http://blog.1024dream.net')
        else:
            # 用户名和密码不匹配
            error_msg = '用户名或密码错误'
            pass

    return render(request, 'login.html',{'error_msg': error_msg})


def home(request):
    return HttpResponse ('<h1>CMDB</h1>')