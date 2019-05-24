import pymysql
import settings
conn=pymysql.Connect(**settings.set1)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

count=0
while count<3:
    _username = input("请输入用户名:")
    _password = input("请输入密码")
    sql = '''sql = "select username,password from user where username='%s',password='%s';
    ''' % (_username, _password)
    ret = cursor.execute(sql)
    records = cursor.fetchall()
    if _username == records.username and _password == records.password:   #判断用户输入的用户名和密码是否一致
        print(ret)
        break    #一致则跳出循环
    elif count<2:
        print("请重新输入用户和密码")
    count+=1

cursor.close()
conn.close()

# 显示用户信息
sql='''desc user;
'''
ret = cursor.execute(sql)
records = cursor.fetchall()

print()










