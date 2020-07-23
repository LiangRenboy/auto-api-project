from logs.logsfile import logger
from common.requests_api import auto_get
# from common.base_api import SQL
# logger.warning('ws')
#
#
# @logger.catch()
# def add(a, b):
#     return a + b
#
#
# print(add(1, 't'))
#
#
# logger.error('error!!!')
# print(SQL().select_one())


url = 'http://api.nnzhp.cn/api/product/choice'
params = {'userid': 'test', 'sign': 'test'}
r = auto_get(url=url, params=params)
print(r)



