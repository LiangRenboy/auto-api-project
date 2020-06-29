import functools


def catch_exception(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('[%s]: %s' % (func.__name__, e))
    return wrapper


@catch_exception
def testdemo():
    print(123 + "测试")


testdemo()
