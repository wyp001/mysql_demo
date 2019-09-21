import pymysql
'''
    向数据库中插入数据
'''
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       database="db_crawler_demo",
                       port=3306)
cursor = conn.cursor()
sql = '''
insert into user(username,age) values(%s,%s)
'''
username = "ccc"
age = 18

cursor.execute(sql,(username,age))
conn.commit()

conn.close()