from appium import webdriver
import pytest

from pageobjects.indexpage import indexPage
from pageobjects.loadingpage import loadingPage
from pageobjects.loginpage import LoginPage
from pageobjects.setting import SettingPage


class TestLogin:
    # 设置终端参数，实际项目中用yaml数据格式封装到data中
    desired_caps = {
        "platformName": "Android",  # 平台名称：IOS、Android、Firefoxos
        'deviceName': 'd1c4de5c',  # 或者连接的设备名称
        'appPackage': 'com.cmcc.hebao',  # 移动应用的包名
        'appActivity': 'com.cmcc.wallet.LoadingActivity',  # 移动应用的启动Activity
        'automationName': 'UiAutomator2'  # 或者 'XCUITest'，取决于你的应用和平台
    }

    # 发送指令给到appium service
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_hebao(self):
        login_page = LoginPage(driver=self.driver)
        loading_page = loadingPage(driver=self.driver)
        index_page = indexPage(driver=self.driver)
        setting_page = SettingPage(driver=self.driver)

        loading_page.agree()
        login_page.login()
        index_page.index()
        setting_page.setting()




#自动化测试入口
if __name__ == '__main__':
    pytest.main()
