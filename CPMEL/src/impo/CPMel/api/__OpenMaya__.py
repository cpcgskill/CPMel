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
from collections import Iterable
import maya.OpenMaya as OpenMaya
from maya.OpenMaya import *

__all__ = ["MMatrix", "MPoint", "MFloatPoint", "MVector", "MFloatVector"]

ScriptUtil = OpenMaya.MScriptUtil()



class MDagPath(OpenMaya.MDagPath):
    def __repr__(self):
        return 'MDagPath("{}")'.format(self.fullPathName())

    def __str__(self):
        return 'MDagPath("{}")'.format(self.fullPathName())



def newMatrix(matrix = (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1), cls = OpenMaya.MMatrix):
    u"""
    创建MMatrix类的方法
    :param matrix: None 或 MMatrix 或 （[[...], [...]...] 4*4）
    :return: MMatrix
    """
    if isinstance(matrix, cls):
        return cls(matrix)
    if matrix is None:
        new_obj = cls()
        return new_obj
    if len(matrix) == 4:
        matrix = [t for i in matrix for t in i]
    if len(matrix) == 16:
        new_obj = cls()
        ScriptUtil.createMatrixFromList(matrix, new_obj)
        return new_obj
    else:
        raise RuntimeError(u"构建矩阵需要16个值")



def newFloatMatrix(matrix = (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1), cls = OpenMaya.MMatrix):
    return newMatrix(matrix, OpenMaya.MFloatMatrix)



class MMatrix(OpenMaya.MMatrix):
    @classmethod
    def newMatrix(cls, matrix = None):
        u"""
        创建MMatrix类的方法
        :param matrix: None 或 MMatrix 或 （[[...], [...]...] 4*4 或 4*3）
        :return: MMatrix
        """
        if isinstance(matrix, cls):
            return cls(matrix)
        if matrix is None:
            new_obj = cls()
            return new_obj
        if len(matrix) == 4:
            matrix = [t for i in matrix for t in i]
        if len(matrix) == 16:
            new_obj = cls()
            ScriptUtil.createMatrixFromList(matrix, new_obj)
            return new_obj
        else:
            raise RuntimeError(u"构建矩阵需要16个值")

    def __str__(self):
        return "Matrix%s" % str(tuple(self))

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        if isinstance(item, int):
            return (self(item, 0), self(item, 1), self(item, 2), self(item, 3))
        else:
            return self(*item)



class MPoint(OpenMaya.MPoint):
    def __str__(self):
        return "MPoint%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, OpenMaya.MPoint):
            other = OpenMaya.MVector(other)
        return OpenMaya.MPoint.__add__(self, other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z



class MFloatPoint(OpenMaya.MFloatPoint):
    def __str__(self):
        return "MFloatPoint%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, OpenMaya.MFloatPoint):
            other = OpenMaya.MFloatVector(other)
        return OpenMaya.MFloatPoint.__add__(self, other)



class MVector(OpenMaya.MVector):
    def __str__(self):
        return "MVector%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()



class MFloatVector(OpenMaya.MFloatVector):
    def __str__(self):
        return "MFloatVector%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()
