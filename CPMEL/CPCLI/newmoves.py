#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/4 14:46
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import os
import re
from .utils import *


def newmoves(root,
             moves_file=u"moves.txt",
             re_s=r".*\.(py|pyd|pyo|pyw)$"):
    re_o = re.compile(re_s)
    root = root.replace(u"\\", u"/")
    outs = list()
    root_size = len(root)
    for _root, dirs, files in os.walk(root):
        for file in files:
            if not re_o.match(file) is None:
                print file
                file = _root + u"\\" + file
                file = file.replace(u"\\", u"/")
                file = file[root_size:]
                tab = u"    " * (len(file.split(u"/")) - 1)
                file = tab + file
                outs.append(file)
    writeFile(moves_file, u"\n".join(outs))
