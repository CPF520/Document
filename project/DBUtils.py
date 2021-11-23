import pymysql

host="localhost"
user="root"
password ="123456"
database="icbc"

# 增，删，改
def update(sql,param):
    # 连接数据库
    con= pymysql.connect(host=host,user=user,password=password,database=database)
    # 创建控制台
    cursor=con.cursor()
    # 执行sql语句
    cursor.execute(sql,param)
    # 提交操作
    con.commit()
    # 关闭控制台资源
    cursor.close()
    # 关闭数据库连接资源
    con.close()

# 查询
def select(sql,param,mode="many",dize=0):
    # 连接数据库
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    # 创建控制台
    cursor=con.cursor()
    # 执行sql语句
    cursor.execute(sql,param)
    # 提取数据
    if mode =="all":
        return cursor.fetchall()
    elif mode =="one":
        return cursor.fetchall()
    elif mode =="many":
        return cursor.fetchmany(dize)
    # 提交操作
    con.commit()
    # 关闭控制台资源
    cursor.close()
    # 关闭数据库连接资源
    con.close()