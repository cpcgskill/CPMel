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
在包裹完成之后替换之前的包裹
这部分手动重写以避免自动包裹带来的问题
"""
import maya.cmds as cmds
from ..api import OpenMaya

from .. import ISDEBUG
from . import node
from .node import nodedata
from ..core import metaclass
from . import node
from .node import DgNode, DagNode, AttrObject
from . import create_node

if ISDEBUG:
    reload(create_node)


@node.commandWrap
def selected(**kwargs):
    u"""

    :param kwargs:
    :return:
    :rtype: list
    """
    return cmds.ls(sl=True, **kwargs)


def isDg(obj):
    u"""
    检查是否为Dg节点

    :param obj:
    :return:
    :rtype: bool
    """
    if isinstance(obj, basestring):
        obj = node.nodedata.newObject(obj)
    return isinstance(obj, node.nodedata.DgNode)


def isDag(obj):
    u"""
    检查是否为Dag节点

    :param obj:
    :return:
    :rtype: bool
    """
    if isinstance(obj, basestring):
        obj = node.nodedata.newObject(obj)
    return isinstance(obj, node.nodedata.DagNode)


def isShape(obj):
    u"""
    检查是否为形状节点

    :param obj:
    :return:
    :rtype: bool
    """
    if isinstance(obj, basestring):
        obj = node.nodedata.newObject(obj)
    if isDag(obj):
        return obj.obj.hasFn(OpenMaya.MFn.kShape)
    else:
        return False


def curveToCv(curve, min_dis=0.001):
    u"""
    将曲线附加到它的Cv点上

    :param curve:曲线
    :param min_dis:最小距离 = 0.001
    :return:
    """
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(curve)
    size = curve.numCvs()
    cv_ids = range(size)
    max_u = curve.numSpans()
    max_size = size - 1
    cv_pts = tuple((curve.getPoint(i) for i in cv_ids))
    while len(cv_ids):
        for i in cv_ids:
            end_pt = cv_pts[i]
            curr_pt = (curve.getPointAtParam(float(i) / max_size * max_u))
            if curr_pt.dis(end_pt) < min_dis:
                cv_ids.remove(i)
            curve.setPoint(i, cv_pts[i] - curr_pt + curve.getPoint(i))


def smoothCurve(curve):
    u"""
    平滑曲线

    :param curve:曲线
    :return:None
    """
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(str(curve))
    pts = tuple((curve.getPoint(i) for i in range(curve.numCvs())))
    if len(pts) < 3:
        return
    [curve.setPoint(i, (pts[i - 1] + pts[i] + pts[i + 1]) / 3) for i in range(1, curve.numCvs() - 1)]


def reconstructionCurve(curve, size=10, d=1):
    u"""
    根据路径重建曲线

    :param curve: 曲线
    :param size: cv点数量 = 10
    :param d: 曲线次方数 = 1
    :return: None
    """
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(curve)
    max_u = curve.numSpans()
    max_size = size - 1
    cmds.curve(str(curve), r=True, p=[tuple(curve.getPointAtParam(float(i) / max_size * max_u)) for i in range(size)],
               d=d)


def attachToModel(mesh=node.Mesh, curve=node.Curve):
    u"""
    附加到模型

    :param mesh: 模型
    :param curve: 曲线
    :return:
    """
    if not isinstance(mesh, node.DgNode):
        mesh = node.newObject(mesh)
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(curve)
    [curve.setPoint(i,
                    mesh.getClosestPointAndFace(
                        curve.getPoint(i, node.Space.world), node.Space.world
                    )[0],
                    node.Space.world
                    ) for i in range(curve.numCvs())]


@node.commandWrap
def duplicate(*args, **kwargs):
    u"""

    :param args:
    :param kwargs:
    :return:
    :rtype: list|str|basestring|DagNode|AttrObject
    """
    kwargs[u"rc"] = True
    return cmds.duplicate(*args, **kwargs)


@node.inCommandWrap
def listAttr(*args, **kwargs):
    u"""

    :param args:
    :param kwargs:
    :return:
    :rtype: list|str|basestring|DagNode|AttrObject
    """
    return cmds.listAttr(*args, **kwargs)


from .create_node import createNode
