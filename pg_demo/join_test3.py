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

# 逐批次处理数据
batch_size = 1000  # 每批次处理的行数
offset = 0

while True:
    # 获取一批次的名字
    cursor1.execute(f"SELECT name FROM schema1.tb1 LIMIT {batch_size} OFFSET {offset}")
    batch_names = set(row['name'] for row in cursor1.fetchall())

    # 如果没有数据了，退出循环
    if not batch_names:
        break

    # 在第二个数据库中执行查询
    if batch_names:
        # 处理单一元素情况
        if len(batch_names) == 1:
            query = f"""
                SELECT * FROM tb3
                WHERE name = '{next(iter(batch_names))}'
            """
        else:
            query = f"""
                SELECT * FROM tb3
                WHERE name IN {tuple(batch_names)}
            """
        cursor2.execute(query)
        result = cursor2.fetchall()

        # 处理结果，可以根据需要进行其他操作
        print(result)

    # 更新偏移量
    offset += batch_size

# 关闭数据库连接
cursor1.close()
conn1.close()

cursor2.close()
conn2.close()
