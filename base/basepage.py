from selenium.webdriver.common.by import By


# 定义一个类：描述每个页面相同的属性及行为
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def by_id(self, id):
        return self.driver.find_element(By.ID, id)

    def by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def by_class_name(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)




    def click_by_id(self, id):
        element = self.by_id(id)
        element.click()

    def click_by_xpath(self, xpath):
        element = self.by_xpath(xpath)
        element.click()

    # def sleep(self, seconds):
    #     self.sleep(seconds)

# 滑动（上下左右）
    def swipe(self, start_x, start_y, end_x, end_y, duration=0):
        # 获取屏幕尺寸
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        self.driver.swipe(start_x=x*start_x, start_y=y*start_y, end_x=x*end_x, end_y=y*end_y, duration=duration)


