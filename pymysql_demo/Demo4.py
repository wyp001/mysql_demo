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

# #删除id=1的这条数据
# sql = """
# delete from user where id = %s
# """
# id = 1
# cursor.execute(sql,(id))
# # 插入、删除、更新操作都需要执行commit操作
# conn.commit()

# 更新数据
# 此处更新的sql如果不加id限制，会将user表中的所有的username都改为ddd
sql = """
update user set username = %s  where id = %s
"""
username = "ddd"
id = 2
cursor.execute(sql,(username,id))
conn.commit()

conn.close()
