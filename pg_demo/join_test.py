import psycopg2.extras

# 设置数据库连接参数
db_params = {
    "host": "localhost",
    "database": "test",
    "user": "dcl",
    "password": "123456",
    "port": "5432"
}
# 连接到数据库
conn1 = psycopg2.connect(**db_params)
# 创建一个游标对象
cursor1 = conn1.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
cursor1.execute("select * from schema1.tb1")
res = cursor1.fetchall()

# 设置数据库连接参数------------------------
db_params = {
    "host": "localhost",
    "database": "test2",
    "user": "postgres",
    "password": "123456",
    "port": "5432"
}
# 连接到数据库
conn2 = psycopg2.connect(**db_params)
# 创建一个游标对象
cursor2 = conn2.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
cursor2.execute("select * from tb3")
res2 = cursor2.fetchall()

print(res)
print(res2)

# 关闭游标和连接
cursor1.close()
conn1.close()

cursor2.close()
conn2.close()
