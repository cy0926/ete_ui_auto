from common.base import BasePage
from config.ReadPageYmal import get_locator
import time


class AlexaHomePage(BasePage):
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
        time.sleep(3)
        self.click_skills()
        time.sleep(3)
        self.click_you_skills()
        time.sleep(2)
