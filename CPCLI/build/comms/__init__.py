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
import re
from .. import config

comms = dict()

re_o = re.compile(r"# *?(\w*) *?#(.*?)(?(1)# *?\\\1 *?#)", flags=re.M | re.S)


def main(string):
    if not config.get("comms", False):
        return string
    def _(m):
        comm_name = m.string[m.regs[1][0]:m.regs[1][1]]
        m_string = m.string[m.regs[2][0]:m.regs[2][1]]
        m_string = main(m_string)
        if comm_name.upper() in comms:
            return comms[comm_name](m_string)
        return u"# %s #\r\n%s\r\n# \ #" % (comm_name, m_string)

    return re_o.sub(_, string)


def comm(comm_name=u""):
    def addComm(func):
        comms[comm_name.upper()] = func

    return addComm

from . import baseComm
