import psycopg2

# 设置连接参数
db_params = {
    "host": "linux01",
    "database": "test",
    "user": "dcl",
    "password": "123456",
    "port": "5432"
}

# 连接到 PostgreSQL 数据库
connection = psycopg2.connect(**db_params)

# 创建一个游标对象以执行 SQL 语句
cursor = connection.cursor()

# 执行一个简单的查询
query = "SELECT version();"
cursor.execute(query)

# 获取查询结果
db_version = cursor.fetchone()
print("PostgreSQL Database Version:", db_version)

# 关闭游标和数据库连接
cursor.close()
connection.close()
