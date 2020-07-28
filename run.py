import os
import unittest
from HtmlTestRunner import HTMLTestRunner
import time
from testcase import test_CJXM, test_NDXS
from HtmlTestRunner_PY3 import HTMLTestRunner_PY3

dir_path = os.getcwd()
case_path = os.path.abspath('testcase')
report_path = os.path.abspath('report')

test_case = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')


if __name__ == '__main__':

    now_time = time.strftime('%Y-%m-%d_%H.%M.%S')
    file_name = now_time + '_result.html'
    file_path = report_path + '\\' + file_name
    fp = open(file_path, 'a', encoding='utf-8')
    runner = HTMLTestRunner(output=report_path, stream=fp, report_title='测试报告', descriptions='用例执行情况')
    runner.run(test_case)
    fp.close()

    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_CJXM.TestCJXM))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_NDXS.TestNDXS))
    with open(file_path, 'wb') as report:
        all_runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=report, title='测试报告', description='用例执行情况')
        all_runner.run(suite)
