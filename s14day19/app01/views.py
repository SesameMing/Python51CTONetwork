from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# USER_DICT = {
#     'k1': 'root1',
#     'k2': 'root2',
#     'k3': 'root3',
#     'k4': 'root4',
#     'k5': 'root5',
# }

USER_DICT = {
    '1': {'name': 'root1', 'email': 'admin@qq.com'},
    '2': {'name': 'root2', 'email': 'admin@qq.com'},
    '3': {'name': 'root3', 'email': 'admin@qq.com'},
    '4': {'name': 'root4', 'email': 'admin@qq.com'},
    '5': {'name': 'root5', 'email': 'admin@qq.com'},
    '6': {'name': 'root6', 'email': 'admin@qq.com'},
    '7': {'name': 'root7', 'email': 'admin@qq.com'}
}


def index(request):
    return render(request, 'index.html', {'user_dict': USER_DICT})


# def detail(request):
#     nid = request.GET.get('nid')
#     user_info = USER_DICT[nid]
#     return render(request, 'detail.html', {'user_info': user_info})


def detail(request, nid, uid):
    # return  HttpResponse(nid)
    print(nid, uid)
    user_info = USER_DICT[nid]
    return render(request, 'detail.html', {'user_info': user_info})


"""
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'admin' and p == '123':
            return redirect('/index/')
        else:
            return render(request, 'login.html')

    else:
        redirect('/index/')
"""


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 在数据库中做select
        return render(request, 'login.html')
    else:
        redirect('/index/')


from app01 import models


def orm(request):
    # 创建
    # models.UserInfo.objects.create(username='root', password='123')

    # dict = {'username':'daming','password':'123'}
    # models.UserInfo.objects.create(**dict)

    #obj = models.UserInfo(username='root', password='123')
    #obj.save()

    # 查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='root',password='123')
    # for row in result:
    #    print(row.id, row.username, row.password)

    # 删除
    # models.UserInfo.objects.filter(id=4).delete()


    # 更新
    models.UserInfo.objects.update(password="6669")
    models.UserInfo.objects.filter(id=1).update(password="99999")




    return HttpResponse('orm')


from django.views import View


class Home(View):

    def dispatch(self, request, *args, **kwargs):
        result = super(Home, self).dispatch(request, *args, **kwargs)
        return result

    def get(self, request):
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        print(request.method)
        return render(request, 'home.html')
