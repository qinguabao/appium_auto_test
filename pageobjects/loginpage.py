# from basepage import BasePage
from time import sleep
from base.basepage import BasePage


class LoginPage(BasePage):
    # 属性：每一个操作相应的定位
    # 本机号码一键登录
    local_mobile_id = 'com.cmcc.hebao:id/btn_auto_login'
    #阅读同意
    confirm_xpath ='//android.widget.Button[@resource-id="com.cmcc.hebao:id/positiveTB"]'

    # 行为
    # 登录
    def login(self):
        sleep(3)
        self.click_by_id(self.local_mobile_id)
        sleep(3)
        self.click_by_xpath(self.confirm_xpath)
        sleep(3)

