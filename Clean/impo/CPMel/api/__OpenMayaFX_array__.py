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
from . import __OpenMayaFX__ as omfx
from .__ALL import MAyyayIt



# MRenderLineArray

class MRenderLineArray(omfx.MRenderLineArray):
    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ", ".join([i.__repr__() for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ", ".join([i.__str__() for i in self]))



__all__ = ["MRenderLineArray"]
