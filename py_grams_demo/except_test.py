try:
    file = open('test.txt', 'rb')
    print("本行不会被打印")
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
    raise e
finally:
    print("This would be printed whether or not an exception occurred!")

