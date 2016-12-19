from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

def f1(request):
    return HttpResponse("OK")


def login(request):
    return HttpResponse("login")


def deteil(request, nid):
    print(nid)
    return HttpResponse(nid)


def deteil1(request, nid, nnid):
    print(nid, nnid)
    return HttpResponse(nid)


def deteil2(request, p1, x2):
    print(p1, x2)
    return HttpResponse("ok")

USER_LIST = []
for item in range(94):
    temp = {'id': item, 'username': 'alax' + str(item), 'email': 'email' + str(item)}
    USER_LIST.append(temp)


def index(request, page):
    print(page)
    page = int(page)
    start = (page -1) * 10
    end = page * 10
    user_list = USER_LIST[start:end]

    # return HttpResponse("OK")
    return render(request, 'index.html', {'user_list': user_list})


def detail(request, nid):
    nid = int(nid)
    current_detail_dict = USER_LIST[nid]

    return render(request, 'detail.html', {'current_detail_dict': current_detail_dict})


def ajax_demo(request):
    if request.method == 'POST':
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        ret = {'status': False, 'message': ''}
        if user == '111' and pwd == '222':
            ret['status'] = True
            return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(ret))

    return render(request, 'ajax_demo.html')