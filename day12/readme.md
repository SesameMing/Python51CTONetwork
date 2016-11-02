# day12
线程池：http://www.cnblogs.com/wupeiqi/articles/4839959.html
redis：http://www.cnblogs.com/wupeiqi/articles/5132791.html
Mysql：http://www.cnblogs.com/wupeiqi/articles/5699254.html

一、线程池

    上下文管理
    终止线程池操作

二、redis, 发布和订阅
    
    连接池
    自定义列表操作
    事务的操作
        原子性操作
        


三、rabbitMQ


四、MySQL

    基本的表的创建
    基本操作
        增
            insert into 表(字段) values ('值') 一条记录
            insert into 表(字段) values ('值1'), ('值2') 两条记录
            insert into 表(字段) select 字段 from 表
        删
            delete from 表
            delete from where id = 1 and name = 'alex'
        改
            update 表 set 字段 = '值'
            update 表 set 字段 = '值' where id > 3
        查
            select * form 表
            select * form 表 where id > 5
            select 字段 form 表 where id > 5
        其他
            1. 条件
                select * from 表 where id > 1 and 
            2. 通配符
            3. 限制
            4. 排序
            5. 分组
            6. 连表
            7. 组合

五、python pymysql
    python2.x-> MySQLdb
    python3.x-> PyMySQL
    1. 安装
    
        
六、Python ORM框架 SQLAchemy
    

七、Paramiko


八、堡垒机