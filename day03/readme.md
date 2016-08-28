# 第三天学习笔记

## set集合
集合是无序、不重复序列
可嵌套


### 创建
```
se = {"123", "456"}  # 直接创建一个集合
se = set(list)  # 将列表转化成集合
```

###功能（操作集合）
```
s = set()  # 创建一个集合
s.add(123)  # 添加一个元素
s.clear()  # 清除元素，清空

s1 = {11,22,33}
s2 = {22,33,44}
s3 = s1.difference(s2)  # s1中存在，s2中不存在 赋值给新的变量s3
s3 = s1.symmetric_difference(s2)  # s1存在s2中不存的 和 s2中存在s1中不存的 赋值给新的变量s3
s1.difference_update(s2)  # s1中存在，s2中不存在 更新到s1
s1.symmetric_difference_update(s2)  # s1存在s2中不存的和s2中存在s1中不存的更新到s1
s1.discard(11)  # 移除指定元素，不存在不报错
s1.remove(11)  # 移除指定元素，不存会报错
s1.pop()  # 移除某个元素，并返回这个元素
s1.intersection(s2)  # 取两个的交集 赋值给新的变量s3
s1.intersection_update(s2 )  # 取两个的交集,更新给s1
s1.isdisjoint(s2)  # 判断两个集合有没有交集
s1.issubset(s2)  # 是否是子序列
s1.issuperset(s2)  # 是否是父序列
s3 =  s1.union(s2)  # 并集
s1.update()  # 更新，接受一个可以迭代的对象，可以是list，元组，字符串
```

## 函数
### 创建函数/函数的定义
1. def关键字，创建函数
2. 函数名
3. ()
4. 函数体
5. 返回值

定义函数，函数体不执行，只有调用函数的时候，函数体才执行
在函数中 一旦执行了 return 函数立即终止
默认的函数return值为 None

### 函数的参数
1. 形参
2. 实参
------------
1. 普通参数
2. 默认参数（参数列表的后面）
3. 指定参数
4. 动态参数
    * \*  默认将传入的参数，全部放置在元组中f(\*args)   f1(*[11,22,33,44]) 会将列表所有的元素赋值进去
    * \** 默认将传入的参数，全部放置在字典中f(\*\*args)  f1(**{"k1":"v1", "k2":"v2"}) 会将字典的元素赋值进去
5. 万能参数*ages, **kwarges  f(*ages, **kwarges)
  
    
str.format() #  格式化输出

```
s = "i am {0}, age {1}".format("dm", 18)
s = "i am {0}, age {1}".format(*["dm", 18])
s = "i am {name}, age {age}".format(name="dm", age="18")
dic = {"name":"dm", "age":18}
s = "i am {name}, age {age}".format(**dic)
```

### 函数的要点(补充)

* py是顺序执行的，并且函数可以重复定义函数相同名称的函数。调用时会执行最后一个被定义的函数。
    ```
    def f1(){
        print(1)
    }
    def f1(){
        print(2)
    }
    f1()
    
    #输出
    >>>1
    ```
* 函数的参数在传递的时候，到底是传一份引用，还是值. (传递的是引用)



* 全局变量

    全局变量，所有的作用域都可读，函数外定义的变量　*特殊*字典列表，可以修改，不可以重新赋值
    
    函数里默认定义的变量是私有的
    
    全局变量和私有变量同时存在时，默认优先使用局部私有变量
    
    global 变量，能将局部的私有变量定义/表示为全局变量，在作用域里给全局变量*重新赋值*，需要使用global
    
    默认规则，定义全局变量全部大写
    
    
## 三元运算
    name = "alxe" if 1 == 1 else "sb"
    如果 1 == 1成立 那么 name = "alxe"
    否则 name = 'sb'
    
## lambda表达式
    f2 = lambda a1, a2=9: a1 + a2 + 100

## 内置函数
    # 0, None, "", [], {}, () 是False
    abs()  # 绝对值 s = abs(-1)
    all()  # 所有为真，才为真
    any()  # 任何一个一个为真，就为真
    ascii()  # 自动执行对象的 __repr__方法
    bin()  # 十进制转二进制
    oct()  # 十进制转八进制
    hex()  # 十进制转十六进制
    bool()  # 布尔值
    bytes()  # 字符串转换字节类型
    bytearray()  #
    str()  # 转换成字符串
    open()  # 打开文件。具体可看文件操作





###补充
utf-8编码，一个汉字是三个字节
gbk编码，一个汉字是两个字节
字符串转换字节类型
bytes(只要转换的字符串， 按照什么编码 )
    s = "中国"
    n = bytes(s, encoding="utf-8")
    print(n)
    
字节转换成字符串
str(bytes(s, encoding="utf-8"), enconding="utf-8")

## 文件操作
