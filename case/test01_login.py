"""
    目标: 完成登录业务层实现
"""
# 导包
import unittest
from parameterized import parameterized
from api.api_login import ApiLogin
from tools.read_json import read_json
from tools.read_yaml import read_yaml


# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(read_yaml('login.yaml'))
    def test_login(self, url, mobile, code, expect_result, status_code):
        # 调用登录方法
        res = ApiLogin().api_post_login(url, mobile, code)

        # 调试使用
        print('查看响应结果:', res.json())

        # 断言 响应信息
        self.assertEqual(expect_result, res.json()['message'])

        # 断言响应状态码
        self.assertEqual(status_code, res.status_code)
