import unittest
from common.requests_api import auto_get, auto_post


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_001(self):
        url = '/api/user/stu_info'
        params = {'stu_name': '黑黑'}
        response = auto_get(url=url, params=params)
        print(response[1])

    def test_002(self):
        url = '/api/user/login'
        data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
        t = auto_post(url=url, data=data)
        print(t[1])

    @unittest.skip
    def test_003(self):
        unittest.TestCase.fail()


if __name__ == '__main__':
    unittest.main()
