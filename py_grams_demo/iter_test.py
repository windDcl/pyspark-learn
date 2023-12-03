# 生成器只有在遍历的时候才会得到他的值，需要和yield关键字结合使用。
def generator_function():
    yield 1
    yield 2
    yield 3


gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
# print(next(gen))

print("========")
my_string = "Yasoob"
my_string = iter(my_string)
print(next(my_string))

