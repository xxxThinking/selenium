'''
@File:runner.py
@DateTime:2021/12/15 21:27
@Author:sweet
@Desc:
'''


import unittest
from BeautifulReport import BeautifulReport

# 增加套件的写法
suite = unittest.TestSuite()
case = unittest.defaultTestLoader.discover(start_dir="G:\selenium\OfficeUpdate.exe\python+selenium\selenium_day05\script",pattern="test*.py")
suite.addTests(case)
test_runner = unittest.TextTestRunner()
test_runner.run(suite)

# # 输出测试报告
# case = unittest.defaultTestLoader.discover(start_dir="G:\selenium\OfficeUpdate.exe\python+selenium\selenium_day05\script",pattern="test*.py")
# result = BeautifulReport(case)
# result.report(description="系统测试报告",filename="sit文件",report_dir=r"G:\selenium\OfficeUpdate.exe\python+selenium\selenium_day05\report")


# 调高效率
# case = unittest.defaultTestLoader.discover(start_dir="G:\selenium\OfficeUpdate.exe\python+selenium\selenium_day05\script",pattern="test*.py")
# test_runner = unittest.TextTestRunner()
# test_runner.run(case)