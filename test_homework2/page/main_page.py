from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_homework2.page.base import BasePage
from test_homework2.page.login import Login
from test_homework2.page.register import Register


class Main(BasePage):
    # def _init_(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly.wait(3)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/")
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def upload_material(self):
        manager_locator = (By.CSS_SELECTOR, "#menu_manageTools")
        material_locator = (By.PARTIAL_LINK_TEXT, "素材库")
        material_pic = (By.CSS_SELECTOR, ".material_tabNav li:nth-child(3) .ww_tabNav_itemLink")
        add_pic_button = (By.CSS_SELECTOR, ".js_upload_file_selector")
        upload_pic = (By.ID, "js_upload_input")
        done = (By.LINK_TEXT, "完成")

        self.find(manager_locator).click()
        WebDriverWait(self._driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.PARTIAL_LINK_TEXT, "素材库")))  # element_to_be_clickable的参数是元祖类型，需要两层括号
        # 显示等待中元素定位的方式要与下一步目标元素定位方式相同，不然会报错，找不到元素
        self.find(material_locator).click()
        self.find(material_pic).click()
        self.find(add_pic_button).click()
        self.find(upload_pic).send_keys("/Users/liuna/PycharmProjects/Hgwz11/pic.jpg")
        self.find(done).click()
        return self

    def add_member(self, name="", account="", mobile=""):
        self.find(By.ID, "menu_contacts").click()
        sleep(3)  #  强制等待会能解决找到添加成员元素问题，这里主要推荐使用显示等待解决此问题
        # 下面的显示等待是为了处理按钮点击没反应加的显示等待（条件是直到元素可点击）
        # WebDriverWait()中指定driver，指定等多久
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(By.CSS_SELECTOR,'.js_has_member div:nth-child(1) .js_add_member'))
        # WebDriverWait(self._driver, 2000).until((self.wait_element))  # until方法定义中显示调用的函数method有参数，所以次数调用的wait_element也要传参，否则会报传参错误
        self.find(By.CSS_SELECTOR, ".js_has_member div:nth-child(1) .js_add_member").click()
        self.find(By.ID, "username").send_keys(name)
        self.find(By.CSS_SELECTOR, ".member_edit_item_Account div:nth-child(2) #memberAdd_acctid").send_keys(account)
        self.find(By.CSS_SELECTOR, ".ww_telInput_mainNumber").send_keys(mobile)
        self.find(By.CSS_SELECTOR, ".js_member_editor_form div:nth-child(3) .js_btn_save").click()
        return self

    # def wait_element(self,x):
    #     size=len(self.find(By.ID,"username"))#查找 所有 username元素
    #     if size<1:
    #         self.find(By.CSS_SELECTOR,".js_has_member div:nth-child(1) .js_add_member").click()#循环查找元素，并点击添加成员按钮
    #     return size>=1



    def edit_member(self,membername=""):
        self.find(By.ID, "menu_contacts").click()
        sleep(2)
        self.find(By.CSS_SELECTOR,".ww_searchInput_text").send_keys(membername)
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".ww_searchResult_title_peopleName")))
        self.find(By.LINK_TEXT,"编辑").click()
        #WebDriverWait(self._driver,10).until(expected_conditions._element_if_visible(By.ID,"#username"))
        self.find(By.ID,"username").send_keys("测试666")
        self.find(By.CSS_SELECTOR,'.ww_radio[value="2"]').click()
        self.find(By.LINK_TEXT,'保存').click()

    def get_message(self):
        messagelist=[]
        for e in self.find(By.CSS_SELECTOR,'.ww_tip error'):
            messagelist.append(e.text)

        return messagelist


    def goto_register(self):
        # self._driver = wbdriver.Chrome()
        # self._driver.implicitly_wait(3)
        # self._driver.get("https://work.weixin.qq.com/wework_admin/")
        self.find(By.LINK_TEXT, "立即注册").click()
        return Register(self._driver)  # 返回到注册页（返回的是类的实例化对象，实现类的跳转）

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()

        return Login(self._driver)  # 返回到登录页
