from time import sleep
from base.basepage import BasePage


class indexPage(BasePage):
    # 属性：每一个操作相应的定位
    # 如果提示手机被root,点击继续

    root_go_on_xpath =  '//android.widget.Button[@resource-id="com.cmcc.hebao:id/positiveTB"]'
    return_index_xpath =  '//android.widget.LinearLayout[@resource-id="com.cmcc.hebao:id/ll_cancel"]'
    mall_xpath ='//android.widget.ImageView[@resource-id="com.cmcc.hebao:id/corner_mall"]'
    money_xpath = '//android.widget.ImageView[@resource-id="com.cmcc.hebao:id/corner_money"]'
    my_module_xpath='//android.widget.ImageView[@resource-id="com.cmcc.hebao:id/corner_mine"]'
    # 行为
    # 登录
    def index(self):
        self.click_by_xpath(self.root_go_on_xpath)
        sleep(2)
        self.click_by_xpath(self.return_index_xpath)
        sleep(2)
        self.click_by_xpath(self.mall_xpath)
        sleep(5)
        self.click_by_xpath(self.money_xpath)
        sleep(5)
        self.click_by_xpath(self.my_module_xpath)

