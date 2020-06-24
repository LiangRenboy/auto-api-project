import os
import unittest
from HtmlTestRunner import HTMLTestRunner
import time

dir_path = os.getcwd()
case_path = os.path.abspath('testcase')
report_path = os.path.abspath('report')

test_case = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')


if __name__ == '__main__':

    now_time = time.strftime('%Y-%m-%d_%H.%M.%S')
    file_name = now_time + '_result.html'
    file_path = report_path + '\\' + file_name
    fp = open(file_path, 'a', encoding='utf-8')
    runner = HTMLTestRunner(output='测试报告', stream=fp, report_title='测试报告', descriptions='用例执行情况')
    runner.run(test_case)
    fp.close()
