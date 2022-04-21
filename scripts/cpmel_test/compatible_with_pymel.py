# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/21 21:52
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import pymel.core as pm
import cpmel.cmds as cc

if __name__ == '__main__':
    n = pm.createNode("joint")
    print("pymel joint >> ", n)
    n = cc.ls(n)[0]
    print("cpmel joint >> ", n)
