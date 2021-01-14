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
CPMel。cmds的数据类型定义
"""
import array
from array import array
from ... import ISDEBUG

import maya.cmds as cmds
from ...api import OpenMaya
from ... import core as cmcore
from ...cppplug import Double3, Matrix, NewMatrixs, NewDouble3s, BaseData



class Space:
    u"""
    对象空间 object
    世界空间 world
    变换矩阵（相对）空间 transform
    预转换矩阵（几何）preTransform
    转换后的矩阵（世界）空间 postTransform
    """
    object = OpenMaya.MSpace.kObject
    world = OpenMaya.MSpace.kWorld
    transform = OpenMaya.MSpace.kTransform
    preTransform = OpenMaya.MSpace.kPreTransform
    postTransform = OpenMaya.MSpace.kPostTransform



class ValueArray(array):
    def __str__(self):
        return "%s[%s]" % (self.__class__.__name__, ", ".join([str(i) for i in self]))

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return unicode(self.__str__())



class IntArray(ValueArray):
    def __new__(cls, value):
        return array.__new__(cls, "i", value)



class DoubleArray(ValueArray):
    def __new__(cls, value):
        return array.__new__(cls, "d", value)



class FloatArray(ValueArray):
    def __new__(cls, value):
        return array.__new__(cls, "f", value)
