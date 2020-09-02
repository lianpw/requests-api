# 导包
import requests


# 新建测试类
class ApiArticle:
    # 新建收藏文章方法
    def api_post_collect(self, url, headders, data):
        # 调用post方法, 并返回响应对象
        return requests.post(url, json=data, headers=headders)

    # 新建取消收藏文章方法
    def api_delete_cancel_collect(self, url, headers):
        # 调用delete方法, 并返回响应对象
        return requests.delete(url, headers=headers)
