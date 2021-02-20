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
from functools import partial
import maya.mel
import maya.cmds as mc

from toMel import toMel, toArray, toFloat, toInt, toString

eval = maya.mel.eval


def melProc(item, *args, **kwargs):
    args_s = u" ".join(
        [
            toArray(i) if isinstance(i, Iterable) and (not isinstance(i, basestring)) else toMel(i)
            for i in args
        ]
    )
    kwargs_s = u" ".join(
        [
            u"-%s %s" % (
                k,
                toArray(v) if isinstance(v, Iterable) and (
                    not isinstance(v, basestring)) else toMel(v)
            )
            for k, v in kwargs.items()
        ]
    )
    command_s = u"{0} {2} {1};".format(item, args_s, kwargs_s)
    return eval(command_s)


class melbase(object):
    def __getattribute__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            return partial(melProc, item)
