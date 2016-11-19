# day13
## ORM
###连表
#### 一对多
1. 创建表,主动指定外键约束
2. 操作
   - 类：repr
   - 单表
   - 连表
       + session.query(表1)。join(表2)。all()
       
#### 多对多
1. 创建表，额外的关系表
2. filter()
    - ==
    - int_(都可以是另一个查询)
3. relationship
    A
    AB ==> fk, 关系
    B
4.  A 关系（B，AB）
    AB
    B
    