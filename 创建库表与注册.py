import pymysql
import datetime
import settings

conn=pymysql.Connect(**settings.set1)

cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 创建数据库
# sql="create database bbs default charset=utf8;"
# 创建表
# sql='''create table  if not exists user(uid int auto_increment,username varchar(2),usertype enum('普通用户','管理员') default '普通用户',password varchar(30) not null,regtime varchar(10) not null,email varchar(20) not null,primary key(uid,username));
# '''
# num=cursor.execute(sql)

# 注册用户信息
count=0
while count>1:
    username=input("请输入用户名")
    if not username and len(username)>2 :
        print("输入成功")
        break

    else:
        print("请重新输入")
    count+=1
usetype=input("请输入用户类型")
password=input("请输入密码")
regtime=datetime.datetime.now()
email=input("请输入邮箱")

sql='''insert into user(username,usetype,password,email,regtime) values('%s','%s',sha1('%s'),'%s','%s')
'''%(username,usetype,password,email,regtime)
print(sql)
try:
    res = cursor.execute(sql)
    if res:
        conn.commit()
        print(cursor._lastrowid)
    else:
        conn.rollback()
except Exception as e:
    conn.rollback()
finally:
    cursor.close()
    conn.close()












