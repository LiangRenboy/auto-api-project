import os
import time
import unittest
from testcase import test_CJXM, test_NDXS
from HtmlTestRunner import HTMLTestRunner
from HtmlTestRunner_PY3 import HTMLTestRunner_PY3
from HtmlTestRunner_PY3 import HTMLTestRunner_PY2


dir_path = os.getcwd()
case_path = os.path.abspath('testcase')
report_path = os.path.abspath('report')
test_case = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
my_test_case = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
now_time = time.strftime('%Y-%m-%d_%H.%M.%S')
file_name = now_time + '_result.html'
file_path = report_path + '\\' + file_name
pytwo_report = report_path + '\\' + now_time + '_all_result.html'


if __name__ == '__main__':
    """生成两种类型的测试报告"""
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

    with open(pytwo_report, 'wb') as pyreport:
        runn = HTMLTestRunner_PY2.HTMLTestRunner(stream=pyreport, title='My unit test', description='HTMLTestRunner')
        runn.run(my_test_case)



