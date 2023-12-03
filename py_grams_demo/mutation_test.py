foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
# 可以看到foo列表竟然改变了！！！
print(foo)
print("============")

foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
print(foo)
# Output: ['hi']

print(bar)