# 导包
import unittest

from parameterized import parameterized

from api.api_article import ApiArticle


# 新进测试类
from tools.read_json import read_json


class TestArticle(unittest.TestCase):
    # 新建收藏文章方法
    @parameterized.expand(read_json('article_collect.json'))
    def test_collect(self, url, headers, data, status_code, expect_result):
        # 临时数据
        # url = 'http://ttapi.research.itcast.cn/app/v1_0/article/collections'
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTg5NjkyMzYsInVzZXJfaWQiOjEzMDA3MTI4MDY4MDIyNTk5NjgsInJlZnJlc2giOmZhbHNlfQ.j7WyrRVTowbt97HWN3KzoCKOsVVrNvU4JH-cExhj4z0"
        # }
        # data = {"target": 2}

        # 调用收藏文章方法
        res = ApiArticle().api_post_collect(url, headers, data)

        # 调试 查看响应数据测试结果
        print('响应结果为:', res.json())

        # 断言 状态码
        self.assertEqual(status_code, res.status_code)

        # 断言 响应信息
        self.assertEqual(expect_result, res.json()['message'])

    # 新建取消收藏文章方法
    @parameterized.expand(read_json('cancel_collect.json'))
    def test_cancel_collect(self, url, headers, status_code):
        # url = 'http://ttapi.research.itcast.cn/app/v1_0/article/collections/2'
        # headers = {
        #     "Content-Type": "application/x-www-form-urlencoded",
        #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTg5NjkyMzYsInVzZXJfaWQiOjEzMDA3MTI4MDY4MDIyNTk5NjgsInJlZnJlc2giOmZhbHNlfQ.j7WyrRVTowbt97HWN3KzoCKOsVVrNvU4JH-cExhj4z0"
        # }

        # 调用取消收藏方法
        res = ApiArticle().api_delete_cancel_collect(url, headers)

        # 调试, 查看响应数据
        print('响应数据为:', res.text)

        # 断言 状态码
        self.assertEqual(status_code, res.status_code)
