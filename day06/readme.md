# 第6天

## 递归

## 反射
利用字符串的形式去对象（模块）中操作（寻找/检查/删除/设置）成员
实例：伪造web框架的路由系统
反射：基于字符串的形式去对象（模块）中操作其成员

    hasattr()
    getattr()
    delattr()
    setattr()

扩展：导入模块

    import xxxx
    form xxx import ooo

    obj = __import__("xxxxxx")
    obj = __import__("xxxxxx.oo.xx", fromlist = True)

## 模块
    loggeing
    time/datetime
    
    json/pickle
    requests
    
### 模块中特殊的变量
    __doc__
    __package__
    __cached__
    
    __name__
    __file__
    
    
### sys模块


### os模块


### hashlib加密模块
用于加密相关的操作,代替了md5模块和sha模块,主要提供过SHA1, SHA224, SHA384, SHA512, MD5算法
