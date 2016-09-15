## 字符串格式化

### 百分号

### format

## 生成器

## 迭代器

## 递归

## 模块
* py：模块
* 其他：类库

1. 内置模块
2. 自定义模块
3. 第三方模块    
   安装：
    * pip3
    * 源码

* 先导入
* 再使用

可以是文件
可以是文件夹

### 序列化相关
    import json
    import pickle
#### json
* 将python基本数据类型转换成字符串形式
`json.dumps()`
* 将python字符串形式转换成基本数据类型
`json.loads()`
* 将python基本数据类型转换成字符串形式,并写入文件
 `json.dump()`
* 读取文件字符串，字符串形式转换成基本数据类型
 `json.load()`

通过loads()反序列化时，一定要使用“”

#### pickle
*只能python自己用*

    import pickle
    li = [11, 22, 33]
    r = pickle.dumps(li)
    print(r)
    restult = pickle.loads(r)
    print(restult)
    
    pickle.dumps()
    pickle.loads()
    pickle.dump()
    pickle.load()
    
*json更适合跨语言，字符串，基本类型做操作*

*pickle,python所有类型做操作*


### time模块

### datetime模块

### logging模块
|   级别  |什么时候时候使用|
| ------- |:-------------:|
|  DEBUG  |Detailed |
|   INFO  |XXXX|
| WARNING |AXXXX|
| ERROR   |XXXXX|
| CRITICAL|XXXXX|


