#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
>>> 创建时间
    2020/7/27 23:42
>>> 作者
    苍之幻灵
>>> 我的主页
    http://www.cpcgskill.com
>>> QQ
    2921251087
>>> 爱发电
    https://afdian.net/@Phantom_of_the_Cang
>>> aboutcg
    https://www.aboutcg.org/teacher/54335
>>> bilibili
    https://space.bilibili.com/351598127

测试程序性能
"""

import time
import maya.cmds as cm
import pymel.core as pm
from cpweidgets import CPMel as cc

cmds_vs = list()
pymel_vs = list()
cpmel_vs = list()
for _ in range(10):
    grp = cm.group([cm.spaceLocator()[0] for i in range(1000)], n = "locs")
    a = time.clock()
    [cm.getAttr(i + ".visibility") for i in cm.listRelatives(grp, ad = True)]
    b = time.clock()
    cmds_vs.append(b - a)
    a = time.clock()
    [i.visibility.get() for i in pm.listRelatives(grp, ad = True)]
    b = time.clock()
    pymel_vs.append(b - a)
    a = time.clock()
    [i.visibility.get() for i in cc.listRelatives(grp, ad = True)]
    b = time.clock()
    cpmel_vs.append(b - a)
    cm.delete(grp)
v = 0
for i in cmds_vs:
    v += i
print "maya.cmds == ",v / len(cmds_vs)
v = 0
for i in pymel_vs:
    v += i
print "pymel == ", v / len(pymel_vs)

v = 0
for i in cpmel_vs:
    v += i
print "CPMel == ",v / len(cpmel_vs)
