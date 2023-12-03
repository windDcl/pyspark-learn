items = [1, 2, 3, 4, 5]
square = list(map(lambda x: x * x, items))
print(square)

print("====================")


# 函数生成器lambda x: x(i)
def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    # 同时处理多个函数的值
    value = map(lambda x: x(i), funcs)
    print(list(value))
