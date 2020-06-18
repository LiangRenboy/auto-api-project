import requests
import configparser
import os
import json
import ast

config_path = os.getcwd()
file_path = os.path.dirname(config_path)
config_file = file_path + '\\configfile.ini'
conf = configparser.ConfigParser()
conf.read(config_file)


url_head = conf.get('requests_setting','url_head')
User_Agent = conf.get('requests_setting','User-agent')


class request_method():
    def __init__(self):
        pass

    def auto_get(self,url=None,headers=None,params=None):
        all_url = str(url_head) + str(url)
        get_response = requests.get(url=all_url,headers=headers,params=params)
        return get_response.url,get_response.text




    def auto_post(self,headers,url=None,data=None):
        all_url = str(url_head) + str(url)
        all_headers = "{'User-Agent':'%s',%s}" %(User_Agent,str(headers).replace('{','').replace('}',''))

        post_response = requests.post(url=all_url, headers=eval(all_headers), data=data)
        return post_response.status_code, post_response.text




if __name__ == '__main__':
    a = request_method().auto_get(url='/api/user/stu_info',params='stu_name=黑黑',headers='')
    # print(a[0])
    # print(a[1])
    data = {'username':'niuhanyang','passwd':'aA123456'}
    headers = {'Accept':'*/*'}
    b = request_method().auto_post(url='/api/user/login',data=data,headers=headers)
    print(b[0])
    print(b[1])


