#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: yukin
# date: 2020-05-16

import yaml
import os

# 获取当前脚本所在文件夹路径
curPath2 = os.path.dirname(os.path.realpath(__file__))
# print(curPath2)
# 获取yaml文件路径
yamlPath1 = os.path.join(curPath2, "cfg.yaml")
# print(yamlPath1)

# open方法打开直接读出来
f = open(yamlPath1, 'r', encoding='utf-8')
cfg = f.read()
# print(type(cfg))
#  读出来是字符串
# print(cfg)
d = yaml.load(cfg, Loader=yaml.FullLoader)


#  用load方法转字典
# print(type(d))
# print(d)

def get_username(user):
    # print(d['username'][user])
    return d['username'][user]


def get_password(pwd):
    # print(d['password'][pwd])
    return d['password'][pwd]


def get_key_word(key):
    # print(d['keyWord'][key])
    return d['keyWord'][key]


if __name__ == '__main__':
    get_username('cy')
    get_password('cy')
    get_key_word('input')
