# 导包
import requests


# 创建对象类
class ApiChannel:
    # 获取用户频道列表方法
    def api_get_channel(self, url, headers):
        return requests.get(url, headers=headers)
