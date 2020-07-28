import functools
import requests
from common.readConfig import WRConfigFile
from logs.logsfile import logger
from common.base_api import SQL


sql = SQL().select_all(table_name='testcase_cjxm')
conf = WRConfigFile().read_conf
url_head = conf('requests_setting', 'url_head')


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


def auto_get(url=None, method='GET', body=None, headers=None, allow_redirects=True, timeout=3):
    all_url = str(url_head) + str(url)
    global get_response
    global post_response
    try:
        logger.info('开始请求接口:{all_url}', all_url=all_url)
        if method == 'GET':
            get_response = requests.get(url=all_url, headers=headers, params=body, allow_redirects=allow_redirects, timeout=timeout)
            logger.success('接口请求成功，等待返回数据。请求URL:{get_response_url}', get_response_url=get_response.url)

        elif method == 'POST':
            post_response = requests.post(url=all_url, headers=headers, data=body, allow_redirects=allow_redirects, timeout=timeout)
            logger.success('接口请求成功，等待返回数据。请求URL:{post_response_url}', post_response_url=post_response.url)
        else:
            logger.warning('接口method方法错误,请检查后重试')
            raise BaseException('接口请求方法错误,暂无'+str(method)+'方法')
    except BaseException as e:
        logger.warning('接口请求时发生异常:{all_url},异常:{e}', all_url=all_url, e=e)

    else:
        if method == 'GET':
            logger.success('接口请求执行成功，返回数据:{get_response}', get_response=get_response.content)
            return get_response.text
        elif method == 'POST':
            logger.success('接口请求执行成功，返回数据:{post_response}', post_response=post_response.json())
            return post_response.json()
    finally:
        logger.info('接口执行完毕')


# testdemo()
# method = "DELETE"
# data = {'username':'abctest','pwd':'Aa123456','cpwd':'Aa123456'}
# r = auto_get(url='/api/user/user_reg', method=method, body=data)
# print(r)
# url = sql[1]['url']
# method = sql[1]['method']
# body = eval(sql[1]['body'])
# assertion = eval(sql[1]['assert'])
# print(url)
# print(method)
# print(body)
# print(assertion['error_code'])
#
# result = auto_get(url=url, method=method, body=body)
# print(result)



