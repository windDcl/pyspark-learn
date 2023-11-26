import psycopg2
from psycopg2 import sql

# 设置数据库连接参数
db_params = {
    "host": "linux01",
    "database": "test",
    "user": "dcl",
    "password": "123456",
    "port": "5432"
}

# 连接到数据库
conn = psycopg2.connect(**db_params)

# 创建一个游标对象
cursor = conn.cursor()

# 定义要创建的表的结构
table_name = 'your_table'
columns = [
    ('id', 'SERIAL PRIMARY KEY'),
    ('name', 'VARCHAR(255)'),
    ('age', 'INTEGER')
]

# 生成SQL语句
create_table_query = sql.SQL("CREATE TABLE {} ({})").format(
    sql.Identifier(table_name),
    sql.SQL(', ').join(sql.SQL("{} {}").format(sql.Identifier(column[0]), sql.SQL(column[1])) for column in columns)
)

# 执行创建表的SQL语句
cursor.execute(create_table_query)

# 提交更改
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()
