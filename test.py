# import functools
# import requests
# from common.readConfig import WRConfigFile
# from logs.logsfile import logger
# from common.base_api import SQL
# from retrying import retry
#
#
# def catch_exception(func):
#     functools.wraps(func)
#
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print('[%s]: %s' % (func.__name__, e))
#     return wrapper
#
# def wraper(args):
#     return isinstance(args,BaseException)
#
#
# @retry(stop_max_attempt_number=3, retry_on_exception=wraper)
# def testdemo():
#     print('正在执行函数......')
#     try:
#         print(123 + c)
#     except BaseException as e:
#         print(e)
#     print(123 + "测试")
#
#
# testdemo()
#