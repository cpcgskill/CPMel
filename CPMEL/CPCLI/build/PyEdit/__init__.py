#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/9/29 22:15
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
import re
from .. import config


editFuncs = list()
def addGlobalSet(func):
    editFuncs.append(func)

from .. import comms

# 命令模块
addGlobalSet(comms.main)

deletedoc_reo = re.compile(r'u""".*?"""', flags=re.M | re.S)
deletelinedoc_reo = re.compile(r'#.*')


def deletedoc(string=""):
    u"""
    删除注释全局处理器

    :param string:
    :return:
    """
    if not config.get("deletedoc", False):
        return string
    string = deletedoc_reo.sub("", string)
    string_st = string.split("\r\n")
    head = "\r\n".join(string_st[:2])
    boody = "\r\n".join(string_st[2:])
    return "\r\n".join([head, deletelinedoc_reo.sub("", boody)])

addGlobalSet(deletedoc)


def deletezeroline(string=u""):
    u"""
    删除空行

    :param string:
    :return:
    """
    if not config.get("deletezeroline", False):
        return string
    string = string.replace("\r", "")
    return u"\r\n".join([i for i in string.split("\n") if len(i.replace(" ", "").replace("  ", "")) != 0])

addGlobalSet(deletezeroline)
