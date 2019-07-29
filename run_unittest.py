import os

from common import HTMLTestRunner
import unittest
import time
RUN_PATH = os.path.dirname(os.path.abspath(__file__))
discover = unittest.defaultTestLoader.discover("./test_open_api", pattern='test_*.py', top_level_dir=None)
now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

filename = "./unittest_report/" + now + "_result.html"
print(filename)

if __name__ == '__main__':
    with open(filename, 'wb') as fp:
        HTMLTestRunner.HTMLTestRunner(stream=fp, title='OPEN API 报告', description='用例执行情况：', verbosity=2).run(discover)
