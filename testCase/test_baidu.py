import unittest

from common.logger import Log
from config.getDriver import get_driver
from pageObjects.baiduPage import SearchPage


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.log = Log()

        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.SearchPage = SearchPage(self.driver)

    def test_search(self):
        self.SearchPage.action("pageObject设计模式")
        self.log.info("百度搜索成功")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.log.info("切换句柄成功")
