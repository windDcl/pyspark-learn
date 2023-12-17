import psycopg2.extras

# 设置第一个数据库连接参数
db_params1 = {
    "host": "localhost",
    "database": "test",
    "user": "dcl",
    "password": "123456",
    "port": "5432"
}

# 连接到第一个数据库
conn1 = psycopg2.connect(**db_params1)
cursor1 = conn1.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
cursor1.execute("SELECT name, age FROM schema1.tb1")
res1 = cursor1.fetchall()

# 获取所有名字的集合
names_set = set(row['name'] for row in res1)

# 关闭第一个数据库连接
cursor1.close()
conn1.close()

# 设置第二个数据库连接参数
db_params2 = {
    "host": "localhost",
    "database": "test2",
    "user": "postgres",
    "password": "123456",
    "port": "5432"
}

# 连接到第二个数据库
conn2 = psycopg2.connect(**db_params2)
cursor2 = conn2.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# 使用名字集合在第二个数据库中进行查询
result = []
for name in names_set:
    cursor2.execute(f"SELECT * FROM tb3 WHERE name = '{name}'")
    row = cursor2.fetchone()
    if row:
        result.append(row)

# 打印结果
print(result)

# 关闭第二个数据库连接
cursor2.close()
conn2.close()
