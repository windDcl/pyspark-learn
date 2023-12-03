# 这里做了两件事：
# 1.创建函数对象： Python 解释器会创建一个函数对象，该对象包含了函数的代码和相关信息。
# 2.变量赋值： 解释器将函数对象赋值给一个变量，这个变量的名称就是你用于定义函数的名称。
def hello(name):
    return name + "tree"


print(hello("zhang"))

green = hello

del hello

print(green("liming"))

print("====================")


# 函数内部可以继续定义函数。
def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()


