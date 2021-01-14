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
import maya.cmds as cmds
from .. import core as cmcore
from . import OpenMaya

class MeshVertex(object):
    u"""

    Meshapi包装
    """
    def __init__(self, obj_name):
        sel = OpenMaya.MSelectionList()
        sel.add(obj_name)
        path = OpenMaya.MDagPath()
        obj = OpenMaya.MObject()
        sel.getDagPath(path, obj)
        self.it = OpenMaya.MItMeshVertex(path, obj)
        self.fn = OpenMaya.MFnMesh(path)
        self.init_points = OpenMaya.MPointArray()
        self.fn.getPoints(self.init_points)
        self.init_us = OpenMaya.MFloatArray()
        self.init_vs = OpenMaya.MFloatArray()
        self.fn.getUVs(self.init_us, self.init_vs)

    def end(self):
        u"""
        结束方法

        :return:
        """
        self.end_points = OpenMaya.MPointArray()
        self.fn.getPoints(self.end_points)
        self.end_us = OpenMaya.MFloatArray()
        self.end_vs = OpenMaya.MFloatArray()
        self.fn.getUVs(self.end_us, self.end_vs)

    def redoIt(self):
        u"""
        执行

        :return:
        """
        self.fn.setPoints(self.end_points)
        self.fn.setUVs(self.end_us, self.end_vs)

    def undoIt(self):
        u"""
        撤销

        :return:
        """
        self.fn.setPoints(self.init_points)
        self.fn.setUVs(self.init_us, self.init_vs)

    def __enter__(self):
        return self.it

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
        cmcore.defAddCommandList(self.redoIt, self.undoIt)
