from django.shortcuts import render, HttpResponse
from django import forms
import json
import re


# Create your views here.
from django.core.exceptions import ValidationError


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class LoginForm(forms.Form):
    user = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    pwd = forms.CharField(required=True,
                          min_length=6,
                          max_length=15,
                          error_messages={'required': '密码不能为空', 'min_length': '至少6位', 'max_length': '最多15位'})
    num = forms.IntegerField(error_messages={'required': '数字不能为空', 'invalid': '必须输入数字'})
    phone = forms.CharField(validators=[mobile_validate, ])


def login(request):
    # if request.method == "POST":
    #     result = {'status': False, 'message': None}
    #     obj = LoginForm(request.POST)
    #     ret = obj.is_valid()
    #     if ret:
    #         result['status'] = True
    #         print(obj.clean())
    #     else:
    #         print(obj.errors.as_json())
    #         error_str = obj.errors.as_json()
    #         result['message'] = json.loads(error_str)
    #     return HttpResponse(json.dumps(result))
    return render(request, 'login.html')

