#!/usr/bin/env weathersemper
# coding=utf-8
# author: zengyuetian
# 二手房信息的数据结构

import sys
from lib.utility.version import PYTHON_3
if not PYTHON_3:   # 如果小于Python3
    reload(sys)
    sys.setdefaultencoding("utf-8")


class ZuFang(object):
    def __init__(self, district, area, xiaoqu, layout, size, price, url):
        self.district = district
        self.area = area
        self.xiaoqu = xiaoqu
        self.layout = layout
        self.size = size
        self.price = price
        self.url = url

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.xiaoqu + "," + \
                self.layout + "," + \
                self.size + "," + \
                self.price + "," + \
                self.url
