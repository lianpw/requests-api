# 导包
import pymysql

# 获取连接对象
conn = pymysql.connect("127.0.0.1", "root", "root", "tpshop2.0", charset='utf8')

# 获取游标对象
cursor = conn.cursor()

# 执行方法 sql
sql = "SELECT cat_id from tp_goods where goods_id = 1"
cursor.execute(sql)

# 获取结果并进行断言
# print(cursor.fetchone())
result = cursor.fetchone()
# 断言
assert 12 == result[0]

# 关闭游标对象
cursor.close()

# 关闭连接对象
conn.close()
