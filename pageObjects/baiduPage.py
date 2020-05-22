from common.base import BasePage
from config.ReadPageYmal import get_locator
import time


class SearchPage(BasePage):
    yaml_file, page = "baiduPage.yaml", "SearchPage"

    loc1 = get_locator(yaml_file, page, "百度搜索框")
    loc2 = get_locator(yaml_file, page, "百度一下")

    def search_input(self, text):
        self.send_keys(self.loc1, text)

    def click_search_button(self):
        self.click(self.loc2)

    def action(self, text):
        self.search_input(text)
        time.sleep(3)
        self.click_search_button()
        time.sleep(5)
