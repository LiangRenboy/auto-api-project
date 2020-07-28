import unittest
from common.requests_api import auto_request
from common.base_api import SQL
sql = SQL().select_all(table_name='testcase_ndxs')


class TestNDXS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ZCJK(self):
        pass

    def test_DL(self):
        pass

    def test_TJJP(self):
        pass

    def test_CJJK(self):
        pass

    def test_CKZJJL(self):
        pass

    def test_HQSYJPXX(self):
        pass


if __name__ == '__main__':
    unittest.main()
