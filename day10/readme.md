# 第10天
## 小知识
### 作用域
* python中无块级作用域
* python中以函数为作用域
* 函数体在没有执行之前，内部代码不执行

##
li = [x+100 for x in range(10)]
li = [x+100 for x in range(10) if x > 6 ]
li = [lambda:x for x in range(10)]
li[0]()输出的多少 （9）
