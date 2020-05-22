#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: yukin
date: 2020-05-16
notes: 读取yaml中每个模块定位元素的方法
"""

import os
import yaml

# 获取当前路径
path = os.path.dirname(os.path.realpath(__file__))
print(path)


def read_page_ymal(yaml_file):
    """
    这个方法用于读取ymal文件的所有值，并转成字典返回
    :param yaml_path: xxpage.ymal文件
    :return:
    """
    ele_path = os.path.join(path, "PageElementsYaml", yaml_file)
    f = open(ele_path, "r", encoding="utf-8")
    ele = f.read()
    ele_dic = yaml.load(ele, Loader=yaml.FullLoader)  # 将读取到的yaml值，转成字典返回
    return ele_dic


def get_locator(yaml_file, page, name):
    """
    获取某个元素的 locator，用于后续的定位
    eg：{'name': '搜索输入框点击', 'by': 'id', 'value': 'com.epet.android.app:id/search_bar_main_index'}
    :param page_yaml: xxpage.ymal文件
    :param page: xxxpage.yaml文件的第一个page标识字段，eg：MyPage
    :param name: 需要定位的元素自定义名称
    :return:
    """
    pages_dic = read_page_ymal(yaml_file)
    elements = pages_dic[page]["locators"]
    for locator in elements:
        if locator["name"] == name:
            return locator


if __name__ == "__main__":
    loc1 = get_locator("AlexaHomePage.yaml", "AlexaHomePage", "Skills")
    print(loc1)
