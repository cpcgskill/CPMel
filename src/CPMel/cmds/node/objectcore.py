#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
>>> 创建时间
    2020/7/7 12:06
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
"""
import maya.api.OpenMaya as OpenMaya
from ... import api
from ... import core as cmcore



class coreObject(object):
    def __init__(self, obj = OpenMaya.MObject):
        self.select_list = OpenMaya.MSelectionList()
        if isinstance(obj, basestring):
            try:
                self.select_list.add(obj)
            except RuntimeError:
                raise cmcore.CPMelError(u"对象不存在")
        else:
            try:
                if isinstance(obj, OpenMaya.MObject) or \
                        isinstance(obj, OpenMaya.MPlug) or \
                        isinstance(obj, OpenMaya.MDagPath):
                    self.select_list.add(obj)
                else:
                    if isinstance(obj, api.OpenMaya.MObject):
                        self.select_list.add(api.OpenMaya.MObject(obj))
                    elif isinstance(obj, api.OpenMaya.MPlug):
                        self.select_list.add(api.OpenMaya.MPlug(obj))
                    else:
                        self.select_list.add(api.OpenMaya.MDagPath(obj))
            except RuntimeError:
                raise cmcore.CPMelError(u"对象不存在")
        # try:
        #
        #     self.isAttr = not (self.select_list.getPlug(0).isNull)
        # except RuntimeError:
        #     self.isComponent = not (self.select_list.getComponent(0)[1].isNull())
        #     self.isNode = not (self.select_list.getDependNode(0).isNull())
        # else:
        #     self.isComponent = False
        #     self.isNode = False

    def compile(self):
        return self.select_list.getSelectionStrings()

    def __str__(self):
        u"""
        字符串化

        :return:
        """
        return str(self.compile())

    def __repr__(self):
        return repr(str(self))

    def __eq__(self, other):
        u"""
        ==判断

        :param other:
        :return:
        """
        if isinstance(other, coreObject):
            if self is other:
                return True
            return str(self) == str(other)
        return False

    def __ne__(self, other):
        u"""
        !=判断

        :param other:
        :return:
        """
        return not self.__eq__(other)
