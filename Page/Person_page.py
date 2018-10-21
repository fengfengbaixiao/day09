from Base.Base import Base
import Page


class Person_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_setting(self):
        self.click_element(Page.setting_btn_id)

    def get_coupons_text(self):
        return self.search_element(Page.person_coupons_id).text
