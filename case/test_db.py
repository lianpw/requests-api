"""
    目标: 在unittest框架中使用数据库工具类
"""
# 导包
import unittest
from tools.read_db import ReadDb


# 新建测试类
class TestDb(unittest.TestCase):
    # 新建测试方法
    def test_db(self):
        # 定义sql语句
        sql = "SELECT cat_id from tp_goods where goods_id = 1"

        # 调用 get_sql_one方法
        data = ReadDb().get_sql_one(sql)

        # 调试 查看响应数据
        print(data)

        # 断言
        self.assertEqual(12, data[0])
