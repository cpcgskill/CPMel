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
在包裹完成之前导入，之后将会被重新包裹
"""
from maya.cmds import *
import maya.cmds as cmds

# ...
__all__ = ["spaceLocator"]



def spaceLocator(*args, **kwargs):
    out = cmds.spaceLocator(*args, **kwargs)
    if "q" in kwargs or "query" in kwargs:
        return out
    else:
        if isinstance(out, list):
            if len(out) == 1:
                return out[0]
            else:
                return out
        else:
            return out
