from common.base import BasePage
from common.logger import Log
from config.ReadPageYmal import get_locator
import time


class AlexaHomePage(BasePage):
    log = Log()
    yaml_file, page = "AlexaHomePage.yaml", "AlexaHomePage"

    loc1 = get_locator(yaml_file, page, "Skills")
    loc2 = get_locator(yaml_file, page, "YourSkills")

    def skill_text(self):
        return self.get_text(self.loc1)

    def click_skills(self):
        self.click(self.loc1)

    def click_you_skills(self):
        self.click(self.loc2)

    def action(self):
        self.log.info("登录成功，进入首页")
        self.click_skills()
        self.log.info("点击了skill")
        self.click_you_skills()
        self.log.info("点击了your skill")
