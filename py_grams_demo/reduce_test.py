from functools import reduce
# 计算1*2*3*4得到聚合结果
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
