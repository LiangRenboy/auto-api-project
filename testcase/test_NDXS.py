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
        unittest.TestCase().fail('test-fail')

    def test_DL(self):
        unittest.TestCase().fail()

    def test_TJJP(self):
        unittest.TestCase().fail()

    def test_CJJK(self):
        unittest.TestCase().fail()

    def test_CKZJJL(self):
        unittest.TestCase().fail()

    def test_HQSYJPXX(self):
        unittest.TestCase().fail()


if __name__ == '__main__':
    unittest.main()
