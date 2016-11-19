from django.shortcuts import render,HttpResponse,render_to_response

# Create your views here.
from django import forms
from app01 import models
class IndexForm(forms.Form):
    # c = [
    #     (1,'CEO'),
    #     (2,'COO')
    # ]
    c = models.UserType.objects.all().values_list('id','caption')
    user_type_id = forms.IntegerField(widget=forms.Select(choices=c))

    def __init__(self,*args, **kwargs):
        # 父类构造方法：1、获取所有静态字段   2、fields = []
        super(IndexForm, self).__init__(*args, **kwargs)

        # print(self.fields['user_type_id'].widget.choices)
        self.fields['user_type_id'].widget.choices = models.UserType.objects.all().values_list('id','caption')

def index(request):
    # for i in range(10):
    #     models.UserType.objects.create(caption='CE'+str(i))
    # c = models.UserType.objects.all().count()
    # print(c)
    form = IndexForm()
    from django.db.models import Q
    """
    q1 = Q()
    q1.connector = 'OR'
    q1.children.append(('id', 1))
    q1.children.append(('id', 2))
    q1.children.append(('id', 3))
    # 1 CE0
    # 2 CE1
    # 3 CE2

    obj = models.UserType.objects.filter(q1)
    for item in obj:
        print(item.id,item.caption)
    """
    con = Q()

    q1 = Q()
    q1.connector = 'OR'
    q1.children.append(('id', 1))
    q1.children.append(('id', 2))
    q1.children.append(('id', 3))

    q2 = Q()
    q2.connector = 'OR'
    q2.children.append(('caption', 'CE1'))
    q2.children.append(('caption', 'CE2'))

    con.add(q1, 'AND')
    con.add(q2, 'AND')

    obj = models.UserType.objects.filter(con)
    for item in obj:
        print(item.id,item.caption)

    return render(request, 'index.html', {'form': form})


def add_user_type(request):
    q = request.GET.get('q', None)
    if q:
        models.UserType.objects.create(caption=q)
    return HttpResponse(q)

def add_boy(request):
    boy = request.GET.get('v',None)
    if boy:
        models.Boy.objects.create(username=boy)
    return HttpResponse(boy)

def add_girl(request):
    girl = request.GET.get('v',None)
    if girl:
        models.Girl.objects.create(name=girl)
    return HttpResponse(girl)

def boy_to_girl(request):

    """
    ########### 增加数据 ###########
    # 获取一个女孩对象
    g1 = models.Girl.objects.get(id=1)

    # 获取一个男孩对象
    b1 = models.Boy.objects.get(id=1)

    # 利用对对多字段b将男孩和女孩建立关系
    g1.b.add(models.Boy.objects.get(id=1))
    g1.b.add(1)

    bs = models.Boy.objects.all()
    g1.b.add(*bs)
    g1.b.add(*[1,2,3])

    """

    """
    ########### 查询数据 ###########
    # 获取一个女孩对象
    g1 = models.Girl.objects.get(id=1)

    # 获取和当前女孩有关系的所有男孩
    boy_list = g1.b.all()
    print(boy_list)
    """

    """
    # 删除第三张表中和女孩1关联的所有关联信息
    g1 = models.Girl.objects.get(id=1)
    g1.b.clear()
    # 查询和女孩1关联所有男孩
    g1 = models.Girl.objects.get(id=1)
    boy_list = g1.b.all()
    print(boy_list)
    """

    """
    # 添加和女孩1和 男孩1，2，3，4关联
    # g1 = models.Girl.objects.get(id=1)
    # g1.b.add(*[1,2,3,4])
    # 删除女孩1和男孩1的关联
    g1 = models.Girl.objects.get(id=1)
    g1.b.remove(1)
    # 删除女孩1和男孩2，3的关联
    g1 = models.Girl.objects.get(id=1)
    g1.b.remove(*[2,3])
    # 查询和女孩1关联所有男孩
    g1 = models.Girl.objects.get(id=1)
    boy_list = g1.b.all()
    print(boy_list)
    """

    # r = models.Girl.objects.all().values('id', 'name', 'b__username')
    # print(r)
    # print(r.query)
    # r = models.Boy.objects.exclude(girl__name=None).values('id','username', 'girl__name')
    # print(r)
    # print(r.query)
    g1 = models.Girl.objects.get(id=1)
    r = g1.b.all()
    print(r)
    return HttpResponse('ok')


def md(request):

    print('views.md')
    obj = HttpResponse('ok')
    # 如果obj中有render方法，则执行中间接的procecss_template_response
    # render(request, 'index.html')
    # render_to_response('index')
    return obj

from django.views.decorators.cache import cache_page

# @cache_page(5)
def cache1(request):
    from s13day20_form import pizza_done
    pizza_done.send(sender='seven',toppings=123, size=456)
    import time
    c = time.time()
    return render(request, 'cache.html', {'c': c})

# class Foo:
#
#     def __init__(self, req, a1,a2):
#         self.req = req
#         self.a1 = a1
#         self.a2 = a2
#
#     def render(self):
#
#         return self.req.render()

def page(request):
    # for i in range(100, 500):
    #     models.UserType.objects.create(caption='CO'+str(i))
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    # 每页显示10条数据
    # 第current_page=1页：0,10
    # 第current_page=2页 10,20
    start = (current_page-1) * 10
    end = current_page * 10
    type_list = models.UserType.objects.all()[start:end]
    # select * from tb limit 5 offset 10

    # 将所有的页面显示在页面上
    total_item = models.UserType.objects.all().count()
    a,b = divmod(total_item, 10)
    if b == 0:
        pass
    else:
        a = a+1
    list_page = []
    if current_page <= 1:
        prev = "<a href='javascript:void(0);'>上一页</a>"
    else:
        prev = "<a href='/page?p=%s'>上一页</a>" % (current_page-1, )
    list_page.append(prev)
    for i in range(1,a+1):
        if i == current_page:
            temp = "<a class='active' href='/page?p=%s'>%s</a>" % (i, i,)
        else:
            temp = "<a href='/page?p=%s'>%s</a>" % (i, i,)
        list_page.append(temp)
    str_page = ''.join(list_page)
    from django.utils.safestring import mark_safe
    str_page = mark_safe(str_page)
    return render(request, 'page.html', {'type_list': type_list, 'str_page': str_page})
    # return render_to_response('page.html')
    # return Foo(request, 'page.html',{'type_list': type_list, 'str_page': str_page})