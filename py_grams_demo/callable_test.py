def callback(x, y, func):
    return func(x, y)


def add(x, y):
    return x + y


print(callback(3, 5, add))
