import requests
from common.readConfig import WRConfigFile


conf = WRConfigFile().read_conf
url_head = conf('requests_setting', 'url_head')


def auto_get(url=None, params=None, headers=None, allow_redirects=True):
    all_url = str(url_head) + str(url)
    get_response = requests.get(url=all_url, headers=headers, params=params, allow_redirects=allow_redirects)
    return get_response.text


def auto_post(url=None, data=None, headers=None, allow_redirects=True):
    all_url = str(url_head) + str(url)
    post_response = requests.post(url=all_url, headers=headers, data=data, allow_redirects=allow_redirects)
    return post_response.json()


if __name__ == '__main__':
    a = auto_get(url='/api/user/stu_info', params='stu_name=黑黑', headers='', allow_redirects=False)
    print(a)
    print(type(eval(a)))
    data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
    headers = {'Accept': '*/*'}
    b = auto_post(url='/api/user/login',data=data,headers=headers,allow_redirects=False)
    print(b)
    print(type(b))


