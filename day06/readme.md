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

## 正则表达式
元字符

    . 通配符 除换行符以外的
    ^ 以什么开头
    $ 以什么结束
    * + ？ ｛｝ 都是代表重复
    * 匹配前一个0到多次重复
    + 匹配前一个1到多次重复
    ? 匹配前一个0或1次重复
    {} 匹配前一个如意次数或者范围
    
    [] 匹配字符集中的一个 
    [^ ] ^代表非
    [\d] 表示一个数字
    
    \:
    反斜杠后边跟元字符去除特殊功能
    反斜杠后边跟着普通字符实现特殊功能
    引用序号对应的字组所匹配的字符串
    
    \d 匹配任何十进制数; 它相当于类[0-9]
    \D 匹配任何非数字字符；它相当于类[^0-9]
    \s 匹配任何空白字符；它相当于类[ \t\n\f\v]
    \S 匹配任何非空白字符；它相当于类[^ \t\n\f\v]
    \w 匹配任何字母数字字符；它相当于类[a-zA-Z0-9_]
    \w 匹配任何非字母数字字符；它相当于类[^a-zA-Z0-9_]
    \b 匹配一个
    
    
方法
    
    mathch：
        re.match(pattrtn, string, flags=0)
        