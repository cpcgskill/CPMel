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

fileTypes = dict()


def baseFile(build_file, out_file):
    with open(build_file, "rb") as f:
        with open(out_file, "wb") as o_f:
            o_f.write(f.read())


def PYD(build_file, out_file):
    with open(build_file, "rb") as f:
        with open(out_file, "wb") as o_f:
            o_f.write(f.read())


fileTypes["pyd"] = PYD


def PY(build_file, out_file):
    with codecs.open(build_file, "r", encoding="utf-8") as f:
        with codecs.open(out_file, "w", encoding="utf-8") as o_f:
            string = f.read()
            for i in PyEdit.editFuncs:
                string = i(string)
            o_f.write(string)


fileTypes["py"] = PY
