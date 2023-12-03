# 这种函数被称为工厂函数，根据参数的不同可以返回不同的函数供程序使用，是专门生产函数的函数。
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)
print(a())
