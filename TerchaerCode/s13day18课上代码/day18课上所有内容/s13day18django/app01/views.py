from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
"""
def f1(request):
    return HttpResponse('OK')

def login(request):
    return HttpResponse('OK')

def detail(request, nid):
    print(nid)
    return HttpResponse('OK')
# detail2(1,2)
def detail2(request, xid, nnid):
    print(xid,nnid)
    return HttpResponse('OK')

# detail3(x2=234,p1=123)
def detail3(request, p1, x2):
    print(p1,x2)
    return HttpResponse('OK')
"""
##############################################################
from django.shortcuts import render
USER_LIST = []
for item in range(94):
    temp = {"id": item, 'username':'alex'+str(item), 'email': 'email' + str(item)}
    USER_LIST.append(temp)

def index(request, page):
    print(page)
    # 1,0-9
    # 2,10-19
    # 3,20-29
    page = int(page)
    start = (page - 1) * 10
    end = page * 10
    user_list = USER_LIST[start:end]
    # return HttpResponse('OK')
    return render(request, 'index.html', {'user_list': user_list})

def detail(request, nid):
    nid = int(nid)
    current_detail_dict = USER_LIST[nid]
    # current_detail_dict?
    return render(request, 'detail.html', {'current_detail_dict': current_detail_dict})


def template(request):

    return render(request,
                  'template.html',
                  {'k1':'VVVV','k2':[11,22,33],'k3': {'nid':12,'name': 'alex'}})

def assets(request):
    assets_list = []
    for i in range(10):
        temp = {'hostname': 'h1'+str(i), 'port': 80}
        assets_list.append(temp)
    return render(request, 'assets.html', {'assets_list': assets_list})

def userinfo(request):
    user_list = []
    for i in range(10):
        temp = {'username': 'h1'+str(i), 'salary': 80}
        user_list.append(temp)
    return render(request, 'userinfo.html', {"user_list": user_list})
import json
def ajax_demo(request):
    if request.method == 'POST':
        ret = {'status': False, 'message': ''}

        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)

        if user == '111' and pwd == '222':
            ret['status'] = True
            return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = "用户名或密码错误"
            return HttpResponse(json.dumps(ret))
    return render(request, 'ajax_demo.html')












