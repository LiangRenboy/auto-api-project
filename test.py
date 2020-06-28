import functools


def catch_exception(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(func.__name__, e)
    return wrapper


@catch_exception
def testdemo():
    open(filename, 'a')
    print(123 + "测试")


testdemo()


def add():
    open(filename,'a')


print(callable(add))
