from selenium import webdriver


class GetDriver:
    driver = None

    # 获取driver
    # @classmethod
    # def get_driver(cls):
    #     if cls.driver is None:
    #         cls.driver = webdriver.Chrome()
    #         cls.driver.maximize_window()
    #         cls.driver.get('http://www.baidu.com')
    #     return cls.driver

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get('http://www.baidu.com')
        return self.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            print('关闭之前', cls.driver)
            cls.driver.quit()
            print('关闭之后', cls.driver)
            # 注意: 此处需要将driver重置为None
            cls.driver = None
            print('置空之后', cls.driver)


if __name__ == '__main__':
    # 第一次获取浏览器驱动对象
    print(GetDriver().get_driver())
    # 第二次获取浏览器驱动对象(与第一次一样)
    print(GetDriver().get_driver())
    GetDriver.quit_driver()
