# from basepage import BasePage
from time import sleep
from base.basepage import BasePage


class SettingPage(BasePage):
    # 属性：每一个操作相应的定位
    # 如果提示手机被root,点击继续

    # root_go_on = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.cmcc.hebao:id/positiveTB"]')
    # 弹出签到框
    sign_xpath= '//android.widget.LinearLayout[@resource-id="com.cmcc.hebao:id/vip_yunying"]/android.view.ViewGroup[2]'
    return_back_xpath = '//android.widget.RelativeLayout[@resource-id="com.cmcc.hebao:id/webview_return_layout"]'
    #进入设置模块
    setting_xpath = '//android.widget.ImageView[@resource-id="com.cmcc.hebao:id/iv_setting"]'
    sim_button_xpath ='//android.widget.TextView[@text="超级SIM卡"]'
    # 行为
    def setting(self):

        self.click_by_xpath(self.sign_xpath)
        sleep(2)
        try:
          self.click_by_xpath(self.return_back_xpath)
          sleep(2)
        except Exception as e:
            print('点击返回异常',e)

        sleep(2)
        self.click_by_xpath(self.setting_xpath)
        sleep(5)
        self.click_by_xpath(self.sim_button_xpath)
        sleep(5)


