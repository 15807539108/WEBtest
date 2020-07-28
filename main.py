import unittest
import time
import os
from HTMLTestRunnerNew import HTMLTestRunner
from BeautifulReport import BeautifulReport

from Common.handle_path import cases_dir, report_dir


case_suite = unittest.TestLoader().discover(cases_dir)  # 使用TestLoader的discover方法在指定目录下搜索测试用例

now_time = time.strftime("%m%d%H%M")  # 获取当前时间用于后续报告命名

# 生成报告文件 HTMLTestRunner格式# report_file = os.path.join(report_dir, now_time+"report.html")  # 定义报告输出的路径和名称
# with open(report_file, "wb") as fs:
#     runner = HTMLTestRunner(fs)  # 实例化HTMLTestRunner方法
#     runner.run(case_suite)  # 使用HTMLTestRunner的run方法运行TestLoader找到的用例

# 生成报告文件 BeautifulReport格式
runner = BeautifulReport(case_suite)
runner.report("测试报告", now_time+"br_report.html", report_dir)