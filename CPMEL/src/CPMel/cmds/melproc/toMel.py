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
import array

from ...cmds.node import nodedata
from ... import core as cmcore



def toString(val):
    return u"\"%s\"" % unicode(val)



def toInt(val):
    return str(val)



def toFloat(val):
    return str(val)



def toMel(val):
    if isinstance(val, nodedata.CPObject):
        val = val.compile()
    if isinstance(val, nodedata.BaseData):
        val = val.compile()
    for i in object_mel_type:
        if isinstance(val, i):
            return object_mel_type[i](val)
    raise cmcore.CPMelError(u"无法正确转化输入")



def toArray(val):
    return "{%s}" % (",".join([toMel(i) for i in val]))


object_mel_type = {basestring:toString,
                   int:toInt,
                   float:toFloat,
                   tuple:toArray,
                   list:toArray,
                   array.array:toArray
                   }
