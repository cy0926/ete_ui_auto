# coding=utf-8

import logging
import time
import inspect
import os

current_path = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(current_path, "logs")
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log(object):
    def __init__(self, filename=time.strftime('%Y-%m-%d')):
        """配置日志规则（命名，输出格式）"""
        self.logname = os.path.join(log_path, '%s.log' % filename)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s:%(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    @staticmethod
    def sclog(r="", interface="", api_data="", *args):
        currentname = inspect.stack()[1][3]
        Log(currentname).info("----------------------------------------------------------------------")
        Log(currentname).info(r)
        Log(currentname).info("[" + interface + "：" + api_data + "]响应耗时%ss,响应码%s" % args)

    @staticmethod
    def log(interface, r):
        currentname = inspect.stack()[1][3]
        Log(currentname).info(interface + "：" + r)


if __name__ == '__main__':
    log = Log()
    log.info('info msg1000013333')
    log.debug('debug msg')
    log.warning('warning msg')
    log.error('error msg')
