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
CPMel.cmds 脚本模块
"""
from collections import Iterable

from collections import Iterable
import maya.cmds as mc

from ...api import OpenMaya
from ... import core as cmcore
from . import basedata
from . import nodedata
from . import nodetypes
from ...tool import decode
# DELETE #
from ... import ISDEBUG

if ISDEBUG:
    reload(basedata)
    reload(nodedata)
    reload(nodetypes)
# \DELETE #
from .basedata import *
from .nodedata import *
from .nodetypes import *
from .nodedata import newObject

__all__ = ["CPMelToCmds", "cmdsToCPMel", "commandWrap"]

# __ToTuple__ = {OpenMaya.MVector, OpenMaya.MFloatVector, OpenMaya.MPoint, OpenMaya.MFloatPoint, OpenMaya.MFloatArray,
#                OpenMaya.MDoubleArray, OpenMaya.MIntArray, OpenMaya.MInt64Array}

__ToTuple__ = (list, tuple)


# __RecursiveToList__ = {list, tuple, OpenMaya.MPointArray, OpenMaya.MFloatPointArray, OpenMaya.MVectorArray,
#                        OpenMaya.MFloatVector}

# CreateObjectType = nodedata.CreateObjectType()


def CPMelToCmds(val):
    u"""
    用于将CPMel的对象转化为cmds可以理解的值的函数

    :param val:	Cmds模块输入参数列表中的元素
    :return: 转化完成的对象
    """
    if isinstance(val, BaseData):
        return val.compile()
    if isinstance(val, CPObject):
        return val.compile()
    # 检查参数是否为需要递归转化为列表的值
    for i in __ToTuple__:
        if isinstance(val, i):
            return tuple((CPMelToCmds(t) for t in val))
    return val


def cmdsToCPMel(val):
    u"""
    将cmds的返回值转化为CPMel使用的对象的函数

    :param val: Cmds模块返回参数列表中的元素
    :return: 转化完成的对象
    """
    if isinstance(val, tuple):
        if len(val) == 3:
            try:
                return basedata.Double3(val)
            except Exception:
                return val
        return val
    if isinstance(val, basestring):
        try:
            return newObject(val)
        except Exception:
            return val
        # return val
    if isinstance(val, list):
        return [cmdsToCPMel(i) for i in val]
    return val


def inCommandWrap(fn):
    u"""
    命令包裹函数

    :param fn:
    :return:
    """

    def test(*args, **kwargs):
        args = tuple((CPMelToCmds(i) for i in args))
        kwargs = {i: CPMelToCmds(kwargs[i]) for i in kwargs}
        try:
            return fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError(u"Command error >> " + u"\n".join([decode(i) for i in ex.args]))

    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test


def runCommandWrap(fn):
    u"""
    命令返回包裹函数

    :param fn:
    :return:
    """

    def test(*args, **kwargs):
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError(u"Command error >> " + u"\n".join([decode(i) for i in ex.args]))
        if isinstance(out_args, Iterable) and (not isinstance(out_args, basestring)):
            return type(out_args)((cmdsToCPMel(i) for i in out_args))
        return cmdsToCPMel(out_args)

    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test


def runUiCommandWrap(fn):
    u"""
    gui命令返回值包裹函数
    :param fn:
    :return: fn
    """

    def test(*args, **kwargs):
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError(u"Command error >> " + u"\n".join([decode(i) for i in ex.args]))
        if (not 'q' in kwargs) and (not 'query' in kwargs) and isinstance(out_args, basestring):
            return nodedata.UIObject(out_args)
        else:
            return out_args

    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test


def commandWrap(fn):
    u"""
    命令包裹函数

    :param fn:
    :return:
    """

    def test(*args, **kwargs):
        args = tuple((CPMelToCmds(i) for i in args))
        kwargs = {i: CPMelToCmds(kwargs[i]) for i in kwargs}
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError(u"Command error >> " + u"\n".join([decode(i) for i in ex.args]))

        if isinstance(out_args, Iterable) and (not isinstance(out_args, basestring)):
            return type(out_args)((cmdsToCPMel(i) for i in out_args))
        return cmdsToCPMel(out_args)

    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test


def uiCommandWrap(fn):
    u"""
    gui命令包裹函数
    :param fn:
    :return: fn
    """

    def test(*args, **kwargs):
        args = tuple((CPMelToCmds(i) for i in args))
        kwargs = {i: CPMelToCmds(kwargs[i]) for i in kwargs}
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError(u"Command error >> " + u"\n".join([decode(i) for i in ex.args]))
        if (not 'q' in kwargs) and (not 'query' in kwargs) and isinstance(out_args, basestring):
            return nodedata.UIObject(out_args)
        else:
            return out_args

    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test

# def getCmdInfoBasic(command):
#     typemap = {
#         'string': unicode,
#         'length': float,
#         'float': float,
#         'angle': float,
#         'int': int,
#         'unsignedint': int,
#         'on|off': bool,
#         'script': callable,
#         'name': 'PyNode'
#     }
#     flags = {}
#     shortFlags = {}
#     removedFlags = {}
#     try:
#         lines = cmds.help(command).split('\n')
#     except RuntimeError:
#         pass
#     else:
#         synopsis = lines.pop(0)
#         # certain commands on certain platforms have an empty first line
#         if not synopsis:
#             synopsis = lines.pop(0)
#         #_logger.debug(synopsis)
#         if lines:
#             lines.pop(0)  # 'Flags'
#             #_logger.debug(lines)
#
#             for line in lines:
#                 line = line.replace('(Query Arg Mandatory)', '')
#                 line = line.replace('(Query Arg Optional)', '')
#                 tokens = line.split()
#
#                 try:
#                     tokens.remove('(multi-use)')
#                     multiuse = True
#                 except ValueError:
#                     multiuse = False
#                 #_logger.debug(tokens)
#                 if len(tokens) > 1 and tokens[0].startswith('-'):
#
#                     args = [typemap.get(x.lower(), util.uncapitalize(x)) for x in tokens[2:]]
#                     numArgs = len(args)
#
#                     # lags with no args in mel require a boolean val in python
#                     if numArgs == 0:
#                         args = bool
#                         # numArgs will stay at 0, which is the number of mel arguments.
#                         # this flag should be renamed to numMelArgs
#                         #numArgs = 1
#                     elif numArgs == 1:
#                         args = args[0]
#
#                     longname = str(tokens[1][1:])
#                     shortname = str(tokens[0][1:])
#
#                     if longname in keyword.kwlist:
#                         removedFlags[longname] = shortname
#                         longname = shortname
#                     elif shortname in keyword.kwlist:
#                         removedFlags[shortname] = longname
#                         shortname = longname
#                     # sometimes the longname is empty, so we'll use the shortname for both
#                     elif longname == '':
#                         longname = shortname
#
#                     flags[longname] = {'longname': longname, 'shortname': shortname, 'args': args, 'numArgs': numArgs, 'docstring': ''}
#                     if multiuse:
#                         flags[longname].setdefault('modes', []).append('multiuse')
#                     shortFlags[shortname] = longname
#
#     # except:
#     #    pass
#         #_logger.debug("could not retrieve command info for", command)
#     res = {'flags': flags, 'shortFlags': shortFlags, 'description': '', 'example': '', 'type': 'other'}
#     if removedFlags:
#         res['removedFlags'] = removedFlags
#     return res
