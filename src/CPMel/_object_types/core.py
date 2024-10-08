# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/17 4:11
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import sys

import maya.cmds as mc
try:
    from PySide6.QtWidgets import QWidget
    from shiboken6 import wrapInstance
except ImportError:
    try:
        from PySide2.QtWidgets import QWidget
        from shiboken2 import wrapInstance
    except ImportError:
        from PySide.QtGui import QWidget
        from shiboken import wrapInstance

import cpapi.utils as omtl
import cpapi.OpenMaya as om
import cpapi.OpenMayaUI as omui
import maya.api.OpenMaya as om2

import cpref.object_ref as cr
from cpref.object_ref import Ref
from cpref import make_ref

from cpmel.exc import *

__all__ = [
    'BaseType',
    'Node', 'DagNode', 'Transform', 'Shape', 'Attr', 'Component',
    'UI',
    'other_node_cls', 'new_object',
]

_ptr = long if sys.version_info.major == 2 else int
_any_int = (int, long) if sys.version_info.major == 2 else int


class BaseType(object):
    __slots__ = ('ref',)

    def __init__(self, ref):
        self.ref = ref  # type: Ref

    def __melobject__(self):
        return self.ref.as_string()

    def __melobject_list__(self):
        return self.ref.as_string_list()

    def assert_valid(self):
        if self.ref.is_null():
            raise RefException("引用已丢失")
        return self

    def name(self):
        self.assert_valid()
        return self.ref.unsafe_as_string_list()[0]


class Node(BaseType):
    __slots__ = ('ref',)

    def type(self):
        return self.api2_m_fn_dependency_node().typeName

    def __hash__(self):
        return om2.MObjectHandle(self.api2_node_object()).hashCode()

    def __eq__(self, other):
        if isinstance(other, BaseType):
            return hash(self) == hash(other)
        return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return self.name()

    def __repr__(self):
        return "{}({})".format(mc.objectType(self.name()), repr(self.name()))

    def attr(self, name):
        return new_object("{}.{}".format(self.name(), name))

    def __getitem__(self, item):
        return self.attr(item).get_value()

    def __setitem__(self, item, value):
        return self.attr(item).set_value(value)

    def __getattr__(self, item):
        try:
            return self.attr(item)
        except CPMelException:
            raise AttributeError("{} object has no attribute '{}'".format(self.__class__.__name__, item))

    def api1_node_object(self):
        self.assert_valid()

        sel = om.MSelectionList()
        sel.add(self.ref.as_string())
        obj = om.MObject()
        sel.getDependNode(0, obj)
        return obj

    def api2_node_object(self):
        self.assert_valid()

        return self.ref.unsafe_m_selection_list().getDependNode(0)

    def api1_m_fn_dependency_node(self):
        return om.MFnDependencyNode(self.api1_node_object())

    def api2_m_fn_dependency_node(self):
        return om2.MFnDependencyNode(self.api2_node_object())

    def api1_m_fn(self):
        return self.api1_m_fn_dependency_node()

    def api2_m_fn(self):
        return self.api2_m_fn_dependency_node()

    def rename(self, name):
        self.api2_m_fn_dependency_node().setName(name)
        return self

    def node_name(self):
        return self.api2_m_fn_dependency_node().name()

    def copy(self):
        u"""

        :return:
        :rtype: Node
        """
        return new_object(mc.duplicate(str(self), rc=True)[0])


class DagNode(Node):
    __slots__ = ('ref',)

    def api1_m_dag_path(self):
        self.assert_valid()

        sel = om.MSelectionList()
        sel.add(self.ref.as_string())
        p = om.MDagPath()
        sel.getDagPath(0, p)
        return p

    def api2_m_dag_path(self):
        self.assert_valid()

        return self.ref.unsafe_m_dag_path()

    def get_translation(self, ws=True):
        ws = arg_conv(ws)
        return om.MVector(*mc.xform(self.name(), q=True, t=True, ws=ws))

    def set_translation(self, p, ws=True):
        p = arg_conv(p)
        ws = arg_conv(ws)
        mc.xform(self.name(), t=(p[0], p[1], p[2]), ws=ws)
        return self

    @property
    def local_translation(self):
        return self.get_translation(ws=False)

    @local_translation.setter
    def local_translation(self, value):
        self.set_translation(value, ws=False)

    @property
    def world_translation(self):
        return self.get_translation(ws=True)

    @world_translation.setter
    def world_translation(self, value):
        self.set_translation(value, ws=True)

    @property
    def translation(self):
        return self.get_translation(ws=True)

    @translation.setter
    def translation(self, value):
        self.set_translation(value, ws=True)

    def get_rotation(self, ws=True):
        ws = arg_conv(ws)
        return om.MEulerRotation(*mc.xform(self.name(), q=True, ro=True, ws=ws))

    def set_rotation(self, r, ws=True):
        r = arg_conv(r)
        ws = arg_conv(ws)
        mc.xform(self.name(), ro=(r[0], r[1], r[2]), ws=ws)
        return self

    @property
    def local_rotation(self):
        return self.get_rotation(ws=False)

    @local_rotation.setter
    def local_rotation(self, value):
        self.set_rotation(value, ws=False)

    @property
    def world_rotation(self):
        return self.get_rotation(ws=True)

    @world_rotation.setter
    def world_rotation(self, value):
        self.set_rotation(value, ws=True)

    @property
    def rotation(self):
        return self.get_rotation(ws=True)

    @rotation.setter
    def rotation(self, value):
        self.set_rotation(value, ws=True)

    def get_scale(self, ws=True):
        ws = arg_conv(ws)
        return mc.xform(self.name(), q=True, s=True, ws=ws)

    def set_scale(self, s, ws=True):
        s = arg_conv(s)
        ws = arg_conv(ws)
        mc.xform(self.name(), s=(s[0], s[1], s[2]), ws=ws)
        return self

    @property
    def local_scale(self):
        return self.get_scale(ws=False)

    @local_scale.setter
    def local_scale(self, value):
        self.set_scale(value, ws=False)

    @property
    def world_scale(self):
        return self.get_scale(ws=True)

    @world_scale.setter
    def world_scale(self, value):
        self.set_scale(value, ws=True)

    @property
    def scale(self):
        return self.get_scale(ws=True)

    @scale.setter
    def scale(self, value):
        self.set_scale(value, ws=True)

    def get_matrix(self, ws=True):
        ws = arg_conv(ws)
        return omtl.new_matrix(mc.xform(self.name(), q=True, m=True, ws=ws))

    def set_matrix(self, m, ws=True):
        m = arg_conv(m)
        ws = arg_conv(ws)
        mc.xform(self.name(), m=m, ws=ws)
        return self

    @property
    def local_matrix(self):
        return self.get_matrix(ws=False)

    @local_matrix.setter
    def local_matrix(self, value):
        self.set_matrix(value, ws=False)

    @property
    def world_matrix(self):
        return self.get_matrix(ws=True)

    @world_matrix.setter
    def world_matrix(self, value):
        self.set_matrix(value, ws=True)

    @property
    def matrix(self):
        return self.get_matrix(ws=True)

    @matrix.setter
    def matrix(self, value):
        self.set_matrix(value, ws=True)

    def api1_m_fn(self):
        return om.MFnDagNode(self.api1_m_dag_path())

    def api2_m_fn(self):
        return om2.MFnDagNode(self.api2_m_dag_path())

    def full_path_name(self):
        self.assert_valid()
        return self.ref.unsafe_full_path_name()

    def add_child(self, *c):
        self_ = arg_conv(self)
        for i in c:
            i = arg_conv(i)
            mc.parent(i, self_)
        return self

    def get_childs(self):
        self_ = arg_conv(self)
        childs = mc.listRelatives(self_, c=True, pa=True)
        if childs is None:
            return []
        return [new_object(i) for i in childs]

    @property
    def childs(self):
        return self.get_childs()

    def set_parent(self, p):
        self_ = arg_conv(self)
        p = arg_conv(p)
        mc.parent(self_, p)
        return self

    def get_parent(self):
        u"""
        获得父对象

        :return:
        :rtype: DagNode
        """
        p = mc.listRelatives(self.name(), p=True, pa=True)
        if p is None:
            return p
        return new_object(p[0])

    @property
    def parent(self):
        return self.get_parent()

    @parent.setter
    def parent(self, v):
        self.set_parent(v)

    def show(self):
        self['visibility'] = True
        return self

    def hide(self):
        self['visibility'] = False
        return self


class Transform(DagNode):
    def __init__(self, ref):
        super(Transform, self).__init__(ref)
        p = self.api2_m_dag_path()  # type: om2.MDagPath
        self.shapes = [new_object(p.extendToShape(i).fullPathName()) for i in range(p.numberOfShapesDirectlyBelow())]
        if len(self.shapes):
            self.shape = self.shapes[0]
        else:
            self.shape = None
        if self.shape is not None:
            for n, _ in self.shape.component_configs:
                setattr(self, n, getattr(self.shape, n))


class Shape(DagNode):
    component_configs = []

    def __init__(self, ref):
        super(Shape, self).__init__(ref)
        for c_n, init_str in type(self).component_configs:
            setattr(self, c_n, new_object("{}.{}".format(self.name(), init_str)))


class Attr(BaseType):
    def __hash__(self):
        return om2.MObjectHandle(self.api2_m_plug().attribute()).hashCode()

    def __eq__(self, other):
        if isinstance(other, BaseType):
            return hash(self) == hash(other)
        return False

    def __ne__(self, other):
        return not self == other

    def __lshift__(self, other):
        a = arg_conv(self)
        b = arg_conv(other)
        mc.connectAttr(b, a, f=True)
        return new_object(b)

    def __rshift__(self, other):
        a = arg_conv(self)
        b = arg_conv(other)
        mc.connectAttr(a, b, f=True)
        return new_object(b)

    def __iter__(self):
        attr_plug = self.api1_m_plug()
        if attr_plug.isCompound():
            return (new_object(attr_plug.child(i).name()) for i in range(attr_plug.numChildren()))
        elif attr_plug.isArray():
            return (new_object(attr_plug.child(i).name()) for i in range(attr_plug.numElements()))
        raise CPMelException('This plugin cannot create iterable objects')

    @property
    def childs(self):
        attr_plug = self.api1_m_plug()
        if not attr_plug.isCompound():
            raise CPMelException('This plug is not a compound')
        return list(self)

    @property
    def elements(self):
        attr_plug = self.api1_m_plug()
        if not attr_plug.isArray():
            raise CPMelException('This plug is not a compound')
        return list(self)

    def attr(self, name):
        return new_object("{}.{}".format(self.name(), name))

    def __getattr__(self, item):
        try:
            return self.attr(item)
        except CPMelException:
            raise AttributeError("{} object has no attribute '{}'".format(self.__class__.__name__, item))

    def __getitem__(self, item):
        try:
            if isinstance(item, _any_int):
                return new_object("{}[{}]".format(self.name(), item))
            else:
                raise TypeError('attribute indices must be integers, not {}'.format(item.__class__.__name__))
        except CPMelException:
            raise AttributeError("{} object has no item '{}'".format(self.__class__.__name__, item))

    def api1_m_plug(self):
        self.assert_valid()

        sel = om.MSelectionList()
        sel.add(self.ref.unsafe_as_string_list()[0])
        p = om.MPlug()
        sel.getPlug(0, p)
        return p

    def api2_m_plug(self):
        self.assert_valid()
        return self.ref.unsafe_m_selection_list().getPlug(0)

    def node(self):
        return new_object(self.name().split('.', 1)[0])

    def type(self):
        try:
            return mc.getAttr(self.name(), type=True)
        except RuntimeError:
            return None

    def lock(self):
        mc.setAttr(self.name(), lock=True)
        return self

    def unlock(self):
        mc.setAttr(self.name(), lock=False)
        return self

    def is_lock(self):
        return mc.getAttr(self.name(), lock=True)

    def connect(self, b):
        self_ = arg_conv(self)
        b = arg_conv(b)
        mc.connectAttr(self_, b, f=True)
        return self

    def disconnect(self, b):
        self_ = arg_conv(self)
        b = arg_conv(b)
        mc.disconnectAttr(self_, b)
        return self

    def get_value(self):
        t = self.type()
        v = mc.getAttr(self.name())
        if t in {"double3", "float3"}:
            return om.MVector(*(v[0]))
        elif t in {'reflectanceRGB', 'short3', 'spectrumRGB', 'long3'}:
            return v[0]
        elif t == 'matrix':
            return omtl.new_matrix((
                v[0:4],
                v[4:8],
                v[8:12],
                v[12:16]
            ))
        return v

    def set_value(self, val):
        val = arg_conv(val)
        t = self.type()
        if t in {'float3', 'short3', 'spectrumRGB', 'reflectanceRGB', 'double3', 'long3'}:
            mc.setAttr(self.name(), *val, type=t)
        elif t in {'string', 'Int32Array', 'doubleArray'}:
            mc.setAttr(self.name(), val, type=t)
        elif t in {'vectorArray', 'pointArray', 'stringArray', 'componentList'}:
            mc.setAttr(self.name(), len(val), *val)
        elif t == "matrix":
            mc.setAttr(self.name(), *val, type=t)
        else:
            mc.setAttr(self.name(), val)
        return self

    @property
    def value(self):
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)

    def __str__(self):
        return self.name()

    def __repr__(self):
        return "{}('{}', attr='{}')".format(mc.objectType(self.node().name()), *self.name().split('.', 1))


class Component(BaseType):
    def __hash__(self):
        return om2.MObjectHandle(self.api2_m_component()[1]).hashCode()

    def __eq__(self, other):
        if isinstance(other, BaseType):
            return hash(self) == hash(other)
        return False

    def __ne__(self, other):
        return not self == other

    def api1_m_component(self):
        self.assert_valid()

        sel = om.MSelectionList()
        sel.add(self.ref.unsafe_as_string_list()[0])
        p = om.MDagPath()
        c = om.MObject()
        sel.getDagPath(0, p, c)
        return p, c

    def api2_m_component(self):
        self.assert_valid()
        return self.ref.unsafe_m_selection_list().getComponent(0)

    def node(self):
        return new_object(self.name().split('.', 1)[0])

    def get_point(self, ws=True):
        return om.MVector(*mc.xform(self.name(), q=True, t=True, ws=ws))

    def set_point(self, p, ws=True):
        p = arg_conv(p)
        mc.xform(self.name(), t=(p[0], p[1], p[2]), ws=ws)
        return self

    @property
    def point(self):
        return self.get_point(ws=True)

    @point.setter
    def point(self, value):
        self.set_point(value, ws=True)

    def __str__(self):
        return self.name()

    def __repr__(self):
        obj = self.__melobject_list__()
        return "{}('{}', component={})".format(
            mc.objectType(self.node().name()),
            self.name().split('.', 1)[0],
            repr(list(obj) if len(obj) > 1 else obj[0])
        )

    def __iter__(self):
        return (new_object(i) for i in mc.ls(self.__melobject__(), fl=True))


class UI(object):
    __slots__ = ('ui',)

    def __init__(self, ui):
        self.ui = ui

    def __hash__(self):
        return hash(self.ui)

    def __eq__(self, other):
        if isinstance(other, UI):
            return hash(self) == hash(other)
        return False

    def __ne__(self, other):
        return not self == other

    def get_widget(self):
        u"""
        :return:
        """
        return wrapInstance(_ptr(omui.MQtUtil.findWindow(self.ui)), QWidget)

    def get_control_widget(self):
        u"""
        :return:
        """
        return wrapInstance(_ptr(omui.MQtUtil.findControl(self.ui)), QWidget)

    def get_layout_widget(self):
        u"""
        :return:
        """
        return wrapInstance(_ptr(omui.MQtUtil.findLayout(self.ui)), QWidget)

    def get_item_widget(self):
        u"""
        :return:
        """
        return wrapInstance(_ptr(omui.MQtUtil.findMenuItem(self.ui)), QWidget)

    def __melobject__(self):
        u"""
        获得mel对象

        :return:
        """
        return self.ui

    def __str__(self):
        return "UI({})".format(repr(self.ui))

    def __repr__(self):
        return "UI({})".format(repr(self.ui))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


__other_node_cls_table = dict()


def other_node_cls(api_type_str):
    def _node(cls):
        __other_node_cls_table[api_type_str] = cls
        return cls

    return _node


_u_str_t = type('')
_any_str_t = (bytes, _u_str_t)


def new_object(o):
    if isinstance(o, BaseType):
        return o
    if isinstance(o, _any_str_t):
        try:
            ref = make_ref(o)
        except RuntimeError as ex:
            raise CPMelException("对象 {} 不存在".format(repr(o)))
        # 优先判断组件和属性减少判断次数
        # 优先判断组件因为组件的调用次数可能比较多
        if ref.ref_type == cr.TComponent:
            return Component(ref)
        if ref.ref_type == cr.TPlug:
            return Attr(ref)

        # 创建节点
        o = ref.unsafe_m_selection_list().getDependNode(0)
        other_cls = __other_node_cls_table.get(o.apiTypeStr)
        if other_cls is None:
            if ref.ref_type == cr.TDependencyNode:
                return Node(ref)
            else:
                if o.hasFn(om2.MFn.kShape):
                    return Shape(ref)
                if o.hasFn(om2.MFn.kTransform):
                    return Transform(ref)
                return DagNode(ref)
        return other_cls(ref)
    raise TypeError


from cpmel._args_conv import arg_conv

import cpmel._object_types.other as _

del _
