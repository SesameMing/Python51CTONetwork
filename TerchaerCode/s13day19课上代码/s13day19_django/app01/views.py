from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django import forms
from django.core.exceptions import ValidationError
import re
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class LoginForm(forms.Form):
    user = forms.CharField(required=True, error_messages={'required': '用户名不能为空.'})
    pwd = forms.CharField(required=True,
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})

    num = forms.IntegerField(error_messages={'required': '数字不能空.','invalid': '必须输入数字'})

    phone = forms.CharField(validators=[mobile_validate, ],)

    #test = forms.CharField(widget=forms.Textarea(attrs={'class': 'c1'}))
    test_choices = (
        (0, '上海'),
        (1, '背景'),
    )
    test = forms.IntegerField(widget=forms.Select(choices=test_choices))

def login(request):
    if request.POST:
        objPost = LoginForm(request.POST)
        ret = objPost.is_valid()
        if ret:
            print(objPost.clean())
        else:
            from django.forms.utils import ErrorDict
            #print(type(obj.errors),obj.errors.as_json())
            # obj1.errors
            pass
        return render(request, 'login.html',{'obj1': objPost})
    else:
        objGet = LoginForm()
        return render(request, 'login.html',{'obj1': objGet})
from django.views.decorators.csrf import csrf_exempt,csrf_protect
@csrf_exempt
def csrf(request):

    return render(request,'csrf.html')

def cookie(request):
    print(request.COOKIES)
    obj = render(request, 'cookie.html')
    obj.set_cookie('k3','v3',path='/cookie/')
    return obj

def cookie1(request):
    print(request.COOKIES)
    obj = render(request, 'cookie.html')
    return obj

def log(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'alex' and p == '123':
            print(u)
            red = redirect('/index/')
            red.set_cookie('username', u)
            return red
        else:
            return render(request, 'log.html')
    else:
        return render(request, 'log.html')

def index(request):
    user = request.COOKIES.get('username')
    if user:
        return render(request, 'index.html', {'user':user})
    else:
        return redirect('/log/')

USER_LIST = ['alex','eric','wangminglong', 'hu']

def session_login(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if p == '123' and u in USER_LIST:
            request.session['user'] = u
            return redirect('/session_index/')
    return render(request,'session_login.html')

"""
def session_index(request):
    user = request.session.get('user',None)
    if not user:
        return redirect('/session_login/')
    else:
        return render(request,'session_index.html',{'user': user})
"""
def auth(func):
    def inner(request, *args,**kwargs):
        # print(request,args,kwargs)
        user = request.session.get('user', None)
        if not user:
            return redirect('/session_login/')
        return func(request, *args,**kwargs)
    return inner

@auth
def session_index(request):

    user = request.session.get('user', None)
    return render(request,'session_index.html',{'user': user})

@auth
def session_logout(request):
    del request.session['user']
    return redirect('/session_login/')



