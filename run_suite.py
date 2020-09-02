"""
    目标:
        1. 搜索组装测试套件
        2. 运行测试套件并生成测试报告
"""

# 导包
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner

# 组装测试套件
suite = unittest.TestLoader().discover('./case', pattern='test*.py')

# 指定报告存放路径及文件名称
file_path = './report/{}.html'.format(time.strftime('%Y-%m-%d %H-%M-%S'))

# 运行测试套件并生成测试报告
with open(file_path, 'wb') as f:
    HTMLTestRunner(stream=f).run(suite)
