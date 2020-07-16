import unittest,time
from common.requests_api import auto_get, auto_post
from common.base_api import SQL


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_001(self):
        select_one = SQL().select_one()
        url = select_one[0]['url']

        params = {'stu_name': '黑黑'}
        response = auto_get(url=url, params=params)
        print(response)

        print(type(url))
        print(select_one)
        # time.sleep(5)

    def test_002(self):
        url = '/api/user/login'
        data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
        t = auto_post(url=url, data=data)
        print(t)
        # time.sleep(5)

    def test_003(self):
        unittest.TestCase.fail()


if __name__ == '__main__':
    unittest.main()
