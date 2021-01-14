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
import maya.OpenMaya as om
import API_1



def initializePlugin(mobject = om.MObject):
    for i in API_1.__modes__:
        i.initializePlugin(mobject)



def uninitializePlugin(mobject = om.MObject):
    for i in API_1.__modes__[::-1]:
        i.uninitializePlugin(mobject)
