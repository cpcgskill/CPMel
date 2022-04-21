# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/15 4:23
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

from cpmel._command.build_new_func import new_func_list_from_module as _new_func_list_from_module
import cpmel._mel as _mel

_new_func_list_from_module(globals())

mel = _mel.Mel()

from cpmel._object_types.core import new_object, Node, DagNode, Transform, Attr, Component, UI
from maya.mel import eval
