class Test:
    # 可以限制不能填写其他属性变量，并且可以节省内存
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Test("fef", 12)
print(obj.name)

obj.address = "232"
print(obj.address)
