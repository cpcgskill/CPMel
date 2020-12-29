#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/5/18 23:57
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
from .. import MAYAPLUG

import maya.cmds as cmds

PLUG_Path = u"{}\\MeldoIt.py".format(MAYAPLUG)

PLUG_NAME = u"CPMel_" + str(hash(MAYAPLUG)).replace(u"-", u"_")
# DELETE #
from .. import ISDEBUG

if ISDEBUG:
    if cmds.pluginInfo(PLUG_NAME, query=True, loaded=True):
        cmds.unloadPlugin(PLUG_NAME)
# \DELETE #
if not cmds.pluginInfo(PLUG_NAME, query=True, loaded=True):
    cmds.loadPlugin(PLUG_Path, n=PLUG_NAME)

import sys

CPMeldoIt_Name = str(sys.cpmel_data.get(u"CPMeldoIt"))
