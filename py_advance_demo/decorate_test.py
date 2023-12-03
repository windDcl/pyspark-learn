from functools import wraps


def decorate(func):
    def wrapper():
        print("before func execute")
        func()
        print("after func execute")

    return wrapper


@decorate
def hello():
    print("hello!")


hello()

print("================")
# 其实@这种加注解的方式等价下面这种方式
# hello2 = decorate(hello)
# hello2()

# 但是这样的函数名就改变了
print(hello.__name__)

print("================最终版=")


def decorate2(func):
    """
    这是个装饰器
    :param func: 任意函数
    :return: 装饰后的函数
    """

    # 加这个的目的在于方便调试和文档生成
    @wraps(func)
    def wrapper():
        """
        装饰器
        :return:
        """
        print("before func")
        func()
        print("after func")

    return wrapper


@decorate2
def hello2():
    """
    hell o
    :return:
    """
    print("hello2")


hello2()
print(hello2.__name__)
print(decorate2.__doc__)
print(hello2.__doc__)
