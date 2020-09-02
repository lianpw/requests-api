# 导包
import unittest

from parameterized import parameterized

from api.api_channel import ApiChannel


# 新建测试类
from tools.read_json import read_json


class TestChannel(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(read_json('channel.json'))
    def test_channel(self, url, headers, expect_result, status_code):
        # 临时数据
        # url = 'http://ttapi.research.itcast.cn/app/v1_0/user/channels'
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTg5NjAxMTgsInVzZXJfaWQiOjEzMDA3MTI4MDY4MDIyNTk5NjgsInJlZnJlc2giOmZhbHNlfQ.3ijNJfgOvaVt1jxpQiQInNRykothYX7mjKjnGUU3eI0"
        # }

        # 调用获取用户频道列表方法
        res = ApiChannel().api_get_channel(url, headers)

        # 调试信息 打印响应结果
        print('查看响应结果信息为:', res.json())

        # 断言  状态码
        self.assertEqual(status_code, res.status_code)

        # 断言 响应信息
        self.assertEqual(expect_result, res.json()['message'])
