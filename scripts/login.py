from selenium.webdriver.common.by import By

from Base.get_driver import get_driver
from Page.page_in import Page_In

Page_In_obj = Page_In(get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity"))
Page_In_obj.get_home_page_obj().click_my_btn()
Page_In_obj.get_sign_page_obj().click_sign_in()
Page_In_obj.get_login_page_obj().login("11111","123456")  # 18758361075
def get_mess(mess):
    mess_xpath = "//*[contains(@text,'{}')]".format(mess)
    return Page_In_obj.get_login_page_obj().search_element((By.XPATH,mess_xpath),timeout=5,poll_frequency=0.5).text
print(get_mess("此用户"))
Page_In_obj.driver.quit()




