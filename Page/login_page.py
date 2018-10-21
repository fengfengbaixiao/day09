from Base.Base import Base
import Page


class Login_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def login(self,name, passwd):
        self.send_element(Page.login_account_id,name)
        self.send_element(Page.login_passwd_id, passwd)
        self.click_element(Page.login_btn_id)

    def if_login_btn_exits(self):
        # 判断登录按钮是否存在 存在返回True 不存在返回False
        try:
            self.search_element(Page.login_btn_id)
            return True
        except Exception as e:
            return False
