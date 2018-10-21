import sys, os, time
from time import sleep

sys.path.append(os.getcwd())
from Base.get_data import Get_Data
import pytest

from Base.get_driver import get_driver
from Page.page_in import Page_In
from selenium.common.exceptions import TimeoutException


"""
[(用例编号,手机号,密码,tag,tag_message,预期结果)]
"""
def get_login_data():
    login_list=[]
    data = Get_Data().get_yaml_data("aolai.yml")
    for i in data.keys():
        login_list.append((i,data.get(i).get("phone"),data.get(i).get("passwd"),
                           data.get(i).get("tag"), data.get(i).get("tag_message"),
                           data.get(i).get("expect_result")))
    return login_list

class Test_Login():
    def setup_class(self):
        self.page_in_obj = Page_In(get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        self.page_in_obj.driver.quit()

    @pytest.mark.parametrize("test_num,phone,passwd,tag,tag_message,expect_result", get_login_data())
    def test_login(self,test_num,phone,passwd,tag,tag_message,expect_result):
        self.page_in_obj.get_home_page_obj().click_my_btn()
        self.page_in_obj.get_sign_page_obj().click_sign_in()
        self.page_in_obj.get_login_page_obj().login(phone,passwd)
        if tag:
            try:
                coupons = self.page_in_obj.get_person_page_obj().get_coupons_text()
                try:
                    assert coupons == expect_result
                except AssertionError as e:
                    print(e.__str__())
                sleep(4)
                self.page_in_obj.get_person_page_obj().click_setting()
                time.sleep(2)
                self.page_in_obj.get_setting_page_obj().click_logout()
            except TimeoutException as e:
                self.page_in_obj.close_login_page()
                assert False
        else:
            try:
                toast_text=self.page_in_obj.get_login_page_obj().get_toast(tag_message)
                print(toast_text,expect_result)
                assert toast_text == expect_result
                # if_login = self.page_in_obj.get_login_page_obj().if_login_btn_exits()
                # assert if_login and toast_text == expect_result
            except TimeoutException as e:
                assert False
            finally:
                # 关闭登录页面
                self.page_in_obj.get_login_page_obj().close_login_page()

















