#第四天学习笔记
##内置函数2
    callable() #  是否可以被执行,是否可以被调用
    chr()  # ascii转字符
    ord()  # 字符转ascii
    compile()  # 编译
    eval()  # 执行
    exec()  # 执行
    dict()
    dir()  # 快速查看对象为提供了哪些功能
    help()  #
    divmod()  #输出(商，余数)
    isinstance()  # 判断对象是否是某个类的实例
    filter() # 函数返回True 将元素添加到结果中
    map() # 函数的返回值添加到结果中
    float() #
    format() #
    frozenset() #
    globals() # 所有的全部变量
    localse() #所有的局部变量
    hash() # 生成哈希值
    id() # 查看内存地址
    issubclass() # 查看一个类是不是它的子类（派生类）
    iter() # 
    len() # 查看长度 "李杰"3.x 长度为2（按字符计算）2.7.x中 长度为6 按字节计算
    max()
    min()
    sum()
    memoryview() # 跟内存地址相关的一个类
    iter()
    next()
    object() # 一个类
    pow() # 次方
    property()
    range()
    repr()
    reversed() # 反转
    round() # 四舍五入
    slice() # 
    sorted # 排序
    vars() # 当前模块有哪些可以调用？
    zip() # 
    
    
### 实例 ：随机验证码
    improt random
    random.randrange(1,5)

## 装饰器
1. 定义函数，为调用，函数内部不执行
2. 函数名 > 代指函数

    @ + 函数名
    功能：
    1. 自动执行outer函数并且将其下面的函数f1当做参数传递
    2. 将outer函数的返回值，重复赋值给f1