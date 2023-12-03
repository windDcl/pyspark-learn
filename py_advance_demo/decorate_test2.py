from functools import wraps


# 装饰器模板
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func(*args, **kwargs):
    return "Function is running"


# 这个变量是个全局变量，可以被后面的程序访问到
can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run

can_run = True
print(func("hell"))
