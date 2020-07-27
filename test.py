import functools
import requests


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
# fp = open('thinking.txt', 'r', encoding='utf-8')
# print(fp.read())
# fp.close()

# url = 'http://172.16.24.80:1001/zuul/wisdom-supervised/policeMediaPhoto/add'
# files = {'file': ('thinking.txt', open('thinking.txt', 'rb'))}
# params = {'policeCode': '56460f015aa14af9bd3fa30171789a73',
#           'policeName': '1呃5777万',
#           'pictureType': '04',
#           'pictureRemark': '图片说明'}
# headers = {'Authorization': 'bearer afef58bc-75e4-4602-9ca8-7cb9acbd0cb6',
#            'Referer': 'http://172.16.24.80/'}
# r = requests.post(url=url, params=params, headers=headers, files=files)
# data = {'stu_id':'100002630','gold': 1}
headers = {'Referer': 'http://api.nnzhp.cn/'}
r = requests.get(url='http://api.nnzhp.cn/api/user/all_stu', headers=headers)
print(r.text)











