import unittest

from selenium.webdriver import ActionChains

from pageObjects.AlexaLoginPage import AlexaLoginPage
from pageObjects.AlexaHomePage import AlexaHomePage
from pageObjects.AlexaSkillsPage import AlexaSkillsPage
from pageObjects.VesyncLoginPage import VesyncLoginPage
from config import read_cfg
from config.getDriver import get_driver
import time
from common.logger import Log

"""
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
"""
"""
思路：
1、登录alexa，点击skills--yourSkills
2、点击DEV SKILLS
3、点击vesync_testOnline，如果状态是已绑定，先解绑
4、然后再操作绑定的流程

todo:
1、支持多语言；
2、环境配置
"""


class TestAlexaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.log = Log()

        self.driver.get("https://alexa.amazon.com/spa/index.html#appliances")
        self.driver.maximize_window()
        self.AlexaLoginPage = AlexaLoginPage(self.driver)
        self.AlexaHomePage = AlexaHomePage(self.driver)
        self.AlexaSkillsPage = AlexaSkillsPage(self.driver)
        self.VesyncLoginPage = VesyncLoginPage(self.driver)
        self.alexa_username = read_cfg.get_username('alexa_nana')
        self.alexa_password = read_cfg.get_password('alexa_nana')
        self.vesync_username = read_cfg.get_username('vesync_cy')
        self.vesync_password = read_cfg.get_password('vesync_cy')

    def blind_account(self):
        self.AlexaSkillsPage.click_enable_button()
        time.sleep(5)
        # 点击enable按钮后，浏览器会新开一个标签页，此时需要切换句柄
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        # 在vesync页面进行登录授权
        self.VesyncLoginPage.action(self.vesync_username, self.vesync_password)
        time.sleep(2)
        try:
            if "successfully" in self.VesyncLoginPage.authorize_success_text():
                self.log.info("授权成功")
        except Exception as e:
            self.log.error("vesync账号授权异常")
            raise e
        # 授权成功之后，要切换句柄回到alexa页面继续操作
        self.driver.switch_to.window(handles[0])
        time.sleep(2)
        # 关闭弹框
        self.AlexaSkillsPage.click_clone_button()

        # self.AlexaSkillsPage.click_discover_devices_button()
        # time.sleep(50)
        # self.AlexaSkillsPage.discover_button()

        # self.AlexaHomePage.action()
        # self.AlexaSkillsPage.click_vesync_testonline_action()
        time.sleep(2)
        try:
            if self.AlexaSkillsPage.status_text() == 'Disabling this skill will unlink your account':
                self.log.info("当前账号通过UI自动化绑定账号成功")
                time.sleep(2)
        except Exception as e:
            self.log.error("UI自动化绑定账号没有成功")
            raise e

    def test_alexa_bind_vesync(self):
        self.AlexaLoginPage.action(username=self.alexa_username,
                                   password=self.alexa_password)
        time.sleep(5)
        self.AlexaHomePage.action()

        self.AlexaSkillsPage.click_vesync_testonline_action()

        if self.AlexaSkillsPage.status_text() == 'Disabling this skill will unlink your account':
            # 先解绑
            self.log.info("设备已绑定，先解绑，再走绑定流程")
            time.sleep(2)
            self.AlexaSkillsPage.click_disable_button()
            time.sleep(2)
            # 解绑之后，再绑定
            self.blind_account()
        else:
            if self.AlexaSkillsPage.status_text() == 'Account linking required':
                self.log.info("设备未绑定，需要绑定")
            time.sleep(3)
            self.blind_account()


if __name__ == '__main__':
    unittest.main()
