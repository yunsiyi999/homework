from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):  # 给driver注释一个类型,后续driver会联想出很多自带方法
        if driver == None:  # index页面使用
            if reuse:
                options = Options()
                # 使用已经存在的Chrome进程
                # 终端启动浏览器： / Applications / Google\ Chrome.app / Contents / MacOS / Google\ Chrome - -remote - debugging - port = 9222
                options.debugger_address = '127.0.0.1:9222'
                self._driver = webdriver.Chrome(options=options)

            else:
                self._driver = webdriver.Chrome()

            self._driver.implicitly_wait(1)
            self._driver.get(self._base_url)
        else:
            # login和register会使用
            self._driver = driver

    def find(self, By, locator=""):
        if isinstance(By, tuple):
            return self._driver.find_element(*By)
        else:
            return self._driver.find_element(By, locator)

        # return self._driver.find_element(*locator) #locator指位置定位，作为参数使用，类型为元组

    def close(self):  # 创建一个关闭方法
        sleep(20)
        self._driver.quit()
