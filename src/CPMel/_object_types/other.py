# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/18 19:04
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import array

from cpapi.all import *
import cpapi.all as om
import cpapi.utils as omtl
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as om2aim
from cpmel._object_types.core import Node, Transform, Shape, other_node_cls, new_object, Attr, Component
from cpmel._args_conv import arg_conv
from cpmel.exc import *

__all__ = ['Joint', 'Mesh', 'Curve', 'Surface', 'SkinClusterFilter']


@other_node_cls("kJoint")
class Joint(Transform):
    pass


@other_node_cls("kMesh")
class Mesh(Shape):
    component_configs = [
        ('vtx', 'vtx[*]'),
        ('e', 'e[*]'),
        ('f', 'f[*]'),
        ('vtxFace', 'vtxFace[*][*]'),
        ('map', 'map[*]'),
    ]
    __slots__ = tuple(['ref'] + [i[0] for i in component_configs])

    def api1_m_fn(self):
        return MFnMesh(self.api1_m_dag_path())

    def api2_m_fn(self):
        return om2.MFnMesh(self.api2_m_dag_path())

    def set_point(self, i, p, ws=True):
        i = arg_conv(i)
        p = arg_conv(p)
        ws = arg_conv(ws)
        new_object("{}.vtx[{}]".format(self.name(), i)).set_point(p, ws)
        return self

    def get_point(self, i, ws=True):
        i = arg_conv(i)
        ws = arg_conv(ws)
        return new_object("{}.vtx[{}]".format(self.name(), i)).get_point(ws)

    def set_points(self, points, ws=True):
        """
        设置所有顶点位置

        :param points: 点位置列表
        :param ws: 是否为世界空间
        :return:
        """
        [i.set_point(p, ws) for i, p in zip(new_object("{}.vtx[*]".format(self.name())), points)]
        return self

    def get_points(self, ws=True):
        return [i.get_point(ws) for i in new_object("{}.vtx[*]".format(self.name()))]


@other_node_cls('kNurbsCurve')
class Curve(Shape):
    component_configs = [
        ('cv', 'cv[*]'),
        ('ep', 'ep[*]'),
        ('u', 'u[*]'),
    ]
    __slots__ = tuple(['ref'] + [i[0] for i in component_configs])

    def api1_m_fn(self):
        return om.MFnNurbsCurve(self.api1_m_dag_path())

    def api2_m_fn(self):
        return om2.MFnNurbsCurve(self.api2_m_dag_path())

    def set_point(self, i, p, ws=True):
        i = arg_conv(i)
        p = arg_conv(p)
        ws = arg_conv(ws)
        new_object("{}.cv[{}]".format(self.name(), i)).set_point(p, ws)
        return self

    def get_point(self, i, ws=True):
        i = arg_conv(i)
        ws = arg_conv(ws)
        return new_object("{}.cv[{}]".format(self.name(), i)).get_point(ws)

    def set_points(self, points, ws=True):
        """
        设置所有顶点位置

        :param points: 点位置列表
        :param ws: 是否为世界空间
        :return:
        """
        [i.set_point(p, ws) for i, p in zip(new_object("{}.cv[*]".format(self.name())), points)]
        return self

    def get_points(self, ws=True):
        return [i.get_point(ws) for i in new_object("{}.cv[*]".format(self.name()))]

    def num_cvs(self):
        u"""
        返回此曲线的CV数

        :return:
        """
        return self.api1_m_fn().numCVs()

    def num_spans(self):
        u"""
        返回此曲线的跨度数

        :return:
        """
        return self.api1_m_fn().numSpans()

    def num_knots(self):
        u"""
        返回此曲线的结数

        :return:
        """
        return self.api1_m_fn().numKnots()

    def degree(self):
        u"""
        返回此曲线的度数

        :return:
        """
        return self.api1_m_fn().degree()


@other_node_cls('kNurbsSurface')
class Surface(Shape):
    component_configs = [
        ('cv', 'cv[*]'),
        ('u', 'u[*]'),
        ('v', 'v[*]'),
        ('uv', 'uv[*][*]'),
        ('sf', 'sf[*][*]'),
    ]
    __slots__ = tuple(['ref'] + [i[0] for i in component_configs])

    def api1_m_fn(self):
        return om.MFnNurbsSurface(self.api1_m_dag_path())

    def api2_m_fn(self):
        return om2.MFnNurbsSurface(self.api2_m_dag_path())

    def set_point(self, ia, ib, p, ws=True):
        ia = arg_conv(ia)
        ib = arg_conv(ib)
        p = arg_conv(p)
        ws = arg_conv(ws)
        new_object("{}.cv[{}][{}]".format(self.name(), ia, ib)).set_point(p, ws)
        return self

    def get_point(self, ia, ib, ws=True):
        ia = arg_conv(ia)
        ib = arg_conv(ib)
        ws = arg_conv(ws)
        return new_object("{}.cv[{}][{}]".format(self.name(), ia, ib)).get_point(ws)

    def set_points(self, points, ws=True):
        """
        设置所有顶点位置

        :param points: 点位置列表
        :param ws: 是否为世界空间
        :return:
        """
        [i.set_point(p, ws) for i, p in zip(new_object("{}.cv[*]".format(self.name())), points)]
        return self

    def get_points(self, ws=True):
        return [i.get_point(ws) for i in new_object("{}.cv[*]".format(self.name()))]


@other_node_cls("kSkinClusterFilter")
class SkinClusterFilter(Node):
    def api1_m_fn(self):
        return om.MFnSkinCluster(self.api1_node_object())

    def api2_m_fn(self):
        return om2aim.MFnSkinCluster(self.api2_node_object())

    def get_weights(self, geo, inf):
        """
        获得骨骼蒙皮权重

        :param geo: 组件 例:xxx.vtx
        :param inf: 关节索引
        :return:
        :rtype:list
        """

        geo = new_object(arg_conv(geo))
        if not isinstance(geo, Component):
            raise CPMelException("需要组件")
        p, c = geo.api1_m_component()

        try:
            inf = array.array('i', inf)
        except TypeError:
            raise CPMelException(u"inf 不是整形数组")

        m_inf = MIntArray()
        ScriptUtil = om.MScriptUtil()
        ScriptUtil.createIntArrayFromList(inf, m_inf)
        m_weigth = MDoubleArray()
        self.api1_m_fn().getWeights(p, c, m_inf, m_weigth)
        return array.array('f', m_weigth)

    def unsafe_set_weights(self, geo, inf, weights):
        """
        获得骨骼蒙皮权重

        :param geo: 组件 例:xxx.vtx
        :param inf: 关节索引
        :param weights: 权重数组
        :return:
        """
        geo = new_object(arg_conv(geo))
        if not isinstance(geo, Component):
            raise CPMelException("需要组件")
        p, c = geo.api1_m_component()

        try:
            inf = array.array('i', inf)
        except TypeError:
            raise CPMelException("inf 不是整形数组")

        try:
            weights = array.array('f', weights)
        except TypeError:
            raise CPMelException("weight 不是浮点数组")

        m_inf = MIntArray()
        ScriptUtil = om.MScriptUtil()
        ScriptUtil.createIntArrayFromList(inf, m_inf)
        m_weights = MDoubleArray()
        for i in weights:
            m_weights.append(i)
        # 撤销的权重
        un_weights = MDoubleArray()

        self.api1_m_fn().setWeights(p, c, m_inf, m_weights, True, un_weights)
        return self

    def get_blend_weights(self, geo):
        """
        获得权重已混合权重

        :param geo: 组件
        :return:
        :rtype:list
        """
        geo = new_object(arg_conv(geo))
        if not isinstance(geo, Component):
            raise CPMelException("需要组件")
        p, c = geo.api1_m_component()

        weights = MDoubleArray()
        self.api1_m_fn().getBlendWeights(p, c, weights)
        return array.array('f', weights)

    def unsafe_set_blend_weights(self, geo, weights):
        """
        设置权重已混合权重

        :param geo: 组件
        :param weights: 权重数组
        :return:
        """
        geo = new_object(arg_conv(geo))
        if not isinstance(geo, Component):
            raise CPMelException("需要组件")
        p, c = geo.api1_m_component()

        try:
            weights = array.array('f', weights)
        except TypeError:
            raise CPMelException("weight 不是浮点数组")

        m_weights = MDoubleArray()
        for i in weights:
            m_weights.append(i)

        self.api1_m_fn().setBlendWeights(p, c, m_weights)

        return self
