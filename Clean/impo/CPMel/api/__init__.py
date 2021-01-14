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

* 本模块提供了对Maya Api数组的封装让其可以顺利的融入Python循环机制中
    >>> from cpweidgets import CPMel as api
    >>> api.OpenMaya.MFloatArray(10, 0)
    <class 'CPMel.api.__OpenMaya_array__.MFloatArray'>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> arr = api.OpenMaya.MFloatArray(10, 0)
    >>> [i for i in arr]
    [<CPMel.api.__OpenMaya_it__.MItDag; proxy of <Swig Object of type 'MItDag *' at 0x0000000016A16E10> >,...]

* 不仅如此还提供了迭代器的封装
    >>> from cpweidgets.CPMel import MItDag
    >>> itdg = MItDag()
    >>> [i for i in itdg] # 注意迭代器循环的 “i”是迭代器本身


"""
# 初始化MayaApi
import maya.OpenMaya
import maya.OpenMayaAnim
import maya.OpenMayaUI
import maya.OpenMayaFX
import maya.OpenMayaRender
import maya.OpenMayaMPx
del maya

import __OpenMaya__
import __OpenMayaAnim__
import __OpenMayaRender__
import __OpenMayaFX__
import __OpenMayaUI__
import __OpenMayaMPx__
import __OpenMaya_it__
import __OpenMayaAnim_it__
import __OpenMaya_array__
import __OpenMayaAnim_array__
import OpenMaya
import OpenMayaAnim
import OpenMayaFX
import OpenMayaRender
import OpenMayaUI
import OpenMayaMPx
# DELETE #
from .. import ISDEBUG
if ISDEBUG:
    reload(__OpenMaya__)
    reload(__OpenMayaAnim__)
    reload(__OpenMayaFX__)
    reload(__OpenMayaRender__)
    reload(__OpenMayaUI__)
    reload(__OpenMayaMPx__)
    reload(__OpenMaya_it__)
    reload(__OpenMayaAnim_it__)
    reload(__OpenMaya_array__)
    reload(__OpenMayaAnim_array__)
    reload(OpenMaya)
    reload(OpenMayaAnim)
    reload(OpenMayaFX)
    reload(OpenMayaRender)
    reload(OpenMayaUI)
    reload(OpenMayaMPx)
# \DELETE #