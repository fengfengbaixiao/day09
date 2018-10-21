from Base.Base import Base
import Page


class Sign_In(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_sign_in(self):
        self.click_element(Page.exits_account_id)