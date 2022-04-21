#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/9/29 14:55
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
import codecs
from .. import PyEdit
from ...utils import *

fileTypes = dict()


def baseFile(file):
    pass


def PYD(out_file):
    pass


fileTypes["pyd"] = PYD


def PY(file):
    string = decode(readFile(file))
    for i in PyEdit.editFuncs:
        string = i(string)
    writeFile(file, string)


fileTypes["py"] = PY
