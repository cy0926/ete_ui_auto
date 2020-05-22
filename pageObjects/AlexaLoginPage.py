from common.base import BasePage
from config.ReadPageYmal import get_locator
import time


class AlexaLoginPage(BasePage):
    yaml_file, page = "AlexaLoginPage.yaml", "AmazonAlexaLoginPage"

    loc1 = get_locator(yaml_file, page, "用户名输入框")
    loc2 = get_locator(yaml_file, page, "密码输入框")
    loc3 = get_locator(yaml_file, page, "sign-in按钮")

    def username_input(self, username):
        self.send_keys(self.loc1, username)

    def password_input(self, password):
        self.send_keys(self.loc2, password)

    def click_sign_in(self):
        self.click(self.loc3)

    def action(self, username, password):
        self.username_input(username)
        time.sleep(2)
        self.password_input(password)
        time.sleep(2)
        self.click_sign_in()
        time.sleep(10)
