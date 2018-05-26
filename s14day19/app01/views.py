from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse('Index')

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
        favor = request.POST.getlist('favor')
        print(favor)
        return render(request, 'login.html')
    else:
        redirect('/index/')