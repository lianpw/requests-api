"""
    目标: 完成数据库相关工具类封装
    分析:
        1. 主要方法
            假设: def get_sql_one(sql)
        2. 辅助方法
            1. 获取连接对象
            2. 获取游标对象
            3. 关闭游标对象方法
            4. 关闭连接对象方法
"""
# 导包
import pymysql


# 新建工具类 数据库
class ReadDb:
    # 定义连接对象 类方法
    conn = None

    # 获取连接对象方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect('127.0.0.1', 'root', 'root', 'tpshop2.0', charset='utf8')
        return self.conn

    # 获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标对象方法封装
    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭连接对象方法封装
    def close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    # 主要 执行方法 --> 在外界调用此方法就可以完成数据相应的操作
    def get_sql_one(self, sql):
        # 定义游标对象及数据变量
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()

            # 调用执行方法
            cursor.execute(sql)

            # 获取结果
            data = cursor.fetchone()
        except Exception as e:
            print('get_sql_one error:', e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)

            # 关闭连接对象
            self.close_conn()

            # 返回执行结果
            return data
    
    # 获取 所有数据库结果集
    def get_sql_all(self, sql):
        # 定义游标对象及数据变量
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()

            # 调用执行方法
            cursor.execute(sql)

            # 获取所有结果
            data = cursor.fetchall()
        except Exception as e:
            print('get_sql_one error:', e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)

            # 关闭连接对象
            self.close_conn()

            # 返回执行结果
            return data

    # 修改, 删除, 新增
    def update_sql(self, sql):
        # 定义游标对象及数据变量
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()

            # 调用执行方法
            cursor.execute(sql)

            # 提交事务
            self.conn.commit()

        except Exception as e:
            # 事务回滚
            self.conn.rollback()
            print('get_sql_one error:', e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)

            # 关闭连接对象
            self.close_conn()
