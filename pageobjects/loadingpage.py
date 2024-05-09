from base.basepage import BasePage


class loadingPage(BasePage):
    agree_id = 'com.cmcc.hebao:id/positiveTB'
    # 行为
    # 进入欢迎界面，同意
    def agree(self):

        self.click_by_id(self.agree_id)
        print('come here agree')


