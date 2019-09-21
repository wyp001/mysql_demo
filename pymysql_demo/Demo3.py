import pymysql
'''
    查询数据
'''
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       database="db_crawler_demo",
                       port=3306)
cursor = conn.cursor()

# ##################### fetchone()查询一条数据
# sql = """
# select * from user where id = %s
# """
# id = 1
# cursor.execute(sql,(id))
# result = cursor.fetchone()
# print(result)
# conn.close()

# ##################### fetchall()查询一条数据
# sql = """
# select * from user
# """
# cursor.execute(sql)
# results = cursor.fetchall()
# for x in results:
#     print(x)
# conn.close()

# ##################### ursor.fetchmany(x)查询指定条数的数据
# sql = """
# select * from user
# """
# cursor.execute(sql)
# results = cursor.fetchmany(2) #查询两条数据
# for x in results:
#     print(x)
# conn.close()


