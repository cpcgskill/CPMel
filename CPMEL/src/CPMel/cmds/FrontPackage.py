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
from .node.nodedata import DagNode, AttrObject, ArrayAttrObject, UIObject
__all__ = ["spaceLocator", "listHistory"]

def spaceLocator(*args, **kwargs):
    u"""

    :param args:
    :param kwargs:
    :return:
    :rtype: list|str|basestring|DagNode|AttrObject
    """
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


def listHistory(*args, **kwargs):
    u"""
    修改内容：
        -当结果为None时返回一个空列表
        -当arg为空列表，元组，集合或空时，引发RuntimeError
         Frozenset，使其行为与未传递时一致，或者
         无参数且未选择任何内容（以前会引发TypeError）
        -添加了类型过滤器
    :return: `CPObject` list
    :rtype: list|str|basestring|DagNode|AttrObject
    """
    type = None
    if 'type' in kwargs:
        type = kwargs.pop('type')
    results = cmds.listHistory(*args, **kwargs)
    if results is None:
        return []
    if type:
        results = [i for i in results if type in cmds.nodeType(i, inherited=True)]
    return results
