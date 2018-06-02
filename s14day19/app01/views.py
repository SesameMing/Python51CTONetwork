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
        # gender = request.POST.get('gender')
        #         # print(gender)
        # favor = request.POST.getlist('favor')
        # print(favor)
        obj = request.FILES.get('fafafa')
        import os
        file_path = os.path.join('upload', obj.name)
        f = open(file_path, 'wb')
        for i in obj.chunks():
            f.write(i)
        f.close()
        return render(request, 'login.html')
    else:
        redirect('/index/')


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
