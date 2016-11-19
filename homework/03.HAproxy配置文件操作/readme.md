[day03博客笔记](http://blog.v-api.cn/code/982.html)


## HAproxy配置文件操作（作业要求）
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6. 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作


## 已经实现的功能
- [x] 获取backend 和sever信息
- [x] 添加backend 和sever信息
- [x] 修改backend 和sever信息
- [x] 删除backend 和sever信息
- [x] 备份
- [x] 回滚
- [X] 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作


## 操作流程
1. 执行.py文件
2. 检查用户配置文件是否存在
3. 存在->输出操作菜单
4. 不存在->系统退出


## 问题
1. 感觉中间重复的代码很多，但是又不是完全一样的重复，觉的还是可以优化,还没想好。
2. 如果是使用字符Q退出，是不是可以重新定一个输入的input的方法，把退出字符设置在里面，这样就不需要每次在输入之后判断，但是如果是跳出循环continue,好像就不合适？







