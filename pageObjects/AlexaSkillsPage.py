from common.base import BasePage
from config.ReadPageYmal import get_locator
import time


class AlexaSkillsPage(BasePage):
    yaml_file, page = "AlexaSkillsPage.yaml", "AlexaSkillsPage"

    loc1 = get_locator(yaml_file, page, "DEV_SKILLS")
    loc2 = get_locator(yaml_file, page, "vesync_testOnline")
    loc2_1 = get_locator(yaml_file, page, "")
    loc3 = get_locator(yaml_file, page, "vesync_pre_deploy_english_en")
    loc4 = get_locator(yaml_file, page, "是否绑定的文案提示")
    loc5 = get_locator(yaml_file, page, "enable按钮")
    loc6 = get_locator(yaml_file, page, "disable按钮")
    loc7 = get_locator(yaml_file, page, "discover_devices_button")
    loc8 = get_locator(yaml_file, page, "discover_button")
    loc9 = get_locator(yaml_file, page, "关闭弹框")

    def click_dev_skills(self):
        self.click(self.loc1)

    def click_vesync_test_online(self):
        self.click(self.loc2)

    def click_vesync_pre_deploy_english_en(self):
        self.click(self.loc3)

    def status_text(self):
        text = self.get_text(self.loc4)
        return text

    def click_enable_button(self):
        self.click(self.loc5)

    def click_disable_button(self):
        # 点击 Disable Skill按钮，解绑
        self.click(self.loc6)

    def click_discover_devices_button(self):
        self.click(self.loc7)

    def discover_button(self):
        self.find_element(self.loc8)

    def discover_text(self):
        return self.get_text(self.loc7)

    def click_clone_button(self):
        self.click(self.loc9)

    def click_vesync_testonline_action(self):
        self.click_dev_skills()
        self.click_vesync_test_online()

    def click_vesync_pred_action(self):
        self.click_dev_skills()
        self.click_vesync_pre_deploy_english_en()
