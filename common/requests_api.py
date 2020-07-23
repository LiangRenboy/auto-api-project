import requests
from common.readConfig import WRConfigFile
from logs.logsfile import logger


conf = WRConfigFile().read_conf
url_head = conf('requests_setting', 'url_head')


@logger.catch()
def auto_get(url=None, params=None, headers=None, allow_redirects=True, timeout=3):
    all_url = str(url_head) + str(url)
    try:
        get_response = requests.get(url=all_url, headers=headers, params=params, allow_redirects=allow_redirects, timeout=timeout)
        logger.info('正在请求接口:{all_url}', all_url=all_url)
    except requests.exceptions.RequestException as e:
        logger.warning('接口发生异常:{all_url},异常:{e}', all_url=all_url, e=e)
    else:
        logger.success('接口返回数据:{all_url}', all_url=all_url)
        return get_response.text


@logger.catch()
def auto_post(url=None, data=None, headers=None, allow_redirects=True):
    all_url = str(url_head) + str(url)
    try:
        post_response = requests.post(url=all_url, headers=headers, data=data, allow_redirects=allow_redirects)
        logger.info('正在请求接口:{all_url}', all_url=all_url)
    except requests.exceptions.RequestException as e:
        logger.warning('接口发生异常:{all_url},异常:{e}', all_url=all_url, e=e)
    else:
        logger.success('接口返回数据:{all_url}', all_url=all_url)
        return post_response.json()


if __name__ == '__main__':
    a = auto_get(url='/api/user/stu_info', params='stu_name=黑黑', headers='', allow_redirects=False)
    data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
    headers = {'Accept': '*/*'}
    b = auto_post(url='/api/user/login', data=data, headers=headers, allow_redirects=False)


