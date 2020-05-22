from common.base import BasePage
from config.ReadPageYmal import get_locator
import time


class VesyncLoginPage(BasePage):
    yaml_file, page = "VesyncLoginPage.yaml", "LoginPage"

    loc1 = get_locator(yaml_file, page, "用户名输入框")
    loc2 = get_locator(yaml_file, page, "密码输入框")
    loc3 = get_locator(yaml_file, page, "授权按钮")
    loc4 = get_locator(yaml_file, page, "授权成功的文案")

    def username_input(self, username):
        self.send_keys(self.loc1, username)

    def password_input(self, password):
        self.send_keys(self.loc2, password)

    def click_authorize(self):
        self.click(self.loc3)

    def authorize_success_text(self):
        return self.get_text(self.loc4)

    def action(self, username, password):
        self.username_input(username)
        time.sleep(2)
        self.password_input(password)
        time.sleep(2)
        self.click_authorize()
        time.sleep(3)
