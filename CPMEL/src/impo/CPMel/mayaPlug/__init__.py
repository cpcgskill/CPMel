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

plugs = cmds.pluginInfo(q = True, ls = True)
# DELETE #
from .. import ISDEBUG
if ISDEBUG:
    if "import_api_1" in plugs:
        cmds.unloadPlugin(u"import_api_1.py", f = True)
    if "import_api_2" in plugs:
        cmds.unloadPlugin(u"import_api_2.py", f = True)
# \DELETE #
if not "import_api_1" in plugs:
    cmds.loadPlugin(u"{}\\import_api_1.py".format(MAYAPLUG))
if not "import_api_2" in plugs:
    cmds.loadPlugin(u"{}\\import_api_2.py".format(MAYAPLUG))
# def release_load():
#     mc.loadPlugin("%s\\import_api_1.py"%MAYAPLUG)
#     mc.loadPlugin("%s\\import_api_2.py"%MAYAPLUG)
#
# def debug_load():
#     mc.loadPlugin("%s\\import_api_1.py"%MAYAPLUG)
#     mc.loadPlugin("%s\\import_api_2.py"%MAYAPLUG)
