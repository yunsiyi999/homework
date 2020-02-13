from selenium.webdriver.common.by import By
from test_homework2.page.main_page import Main


class Test_Main:
    def setup(self):
        self.main = Main(reuse=True)

    def test_upload_material(self):

        self.main.upload_material()

    def test_add_member(self):
        self.main.add_member(name="测试",account="333",mobile="15100000002")

    def test_edit_menber(self):
        self.main.edit_member(membername="测试")
















