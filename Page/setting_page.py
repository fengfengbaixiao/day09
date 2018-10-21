from time import sleep

from Base.Base import Base
import Page

class Setting_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_logout(self,tag=1):
        self.swipe(1)
        self.click_element(Page.logout_btn_id)
        if tag == 1:
            self.click_element(Page.logout_acc_btn_id)
        else:
            self.click_element(Page.log_out_miss_btn_id)


