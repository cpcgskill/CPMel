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
CPMel.cmds的基本类型定义
"""
import re
import itertools

import maya.cmds as cmds
import functools

try:
    from PySide2.QtWidgets import QWidget
    from shiboken2 import wrapInstance
except ImportError:
    from PySide.QtGui import QWidget
    from shiboken import wrapInstance

from ...api import OpenMaya
from ...api import OpenMayaUI
from ...api.OpenMaya import *
from ...api.OpenMayaUI import *
from ... import core as cmcore
from . import basedata
from .basedata import *

from ... import MAYAINDEX

__all__ = ["newObject", "CPObject", "DgNode", "DagNode", "AttrObject", "ArrayAttrObject", "UIObject",
           "Components1Base", "Components2Base", "Components3Base", "Global", "ObjectMetadef", "componentsTypesMetadef"]


class Global(object):
    u"""
    全局静态方法类

    """
    DependencyNode_o = MFnDependencyNode()
    NewNodes = dict()
    new_object = None
    # objects = dict()
    DependencyNodeTypes = dict()
    DgTypes = list()
    # # 同级类型树
    # SiblingTypeTree = tuple()
    ComponentsTypes = list()
    re_object = re.compile(r"\[([\d:\*]*?)\]")

    @staticmethod
    def nameToApiObject(obj_name):
        u"""
        获得对应的api对象

        :param obj_name: 对象名称字符串
        :return: MObject or (MObject, MPlug) or (MObject, MObject)
        """
        sel = MSelectionList()
        try:
            sel.add(obj_name)
        except Exception:
            if "." in obj_name:
                try:
                    buf = obj_name.split('.')
                    obj = Global.nameToApiObject(buf[0])
                    mfn = MFnDependencyNode(obj)
                    plug = mfn.findPlug(buf[-1], False)

                    return (obj, plug)
                except (RuntimeError, ValueError):
                    pass
            return None
        else:
            if sel.length() != 1:
                return None
            if "." in obj_name:
                try:
                    plug = MPlug()
                    sel.getPlug(0, plug)
                    return (plug.node(), plug)
                except RuntimeError:
                    # Components
                    dag = MDagPath()
                    comp = MObject()
                    try:
                        sel.getDagPath(0, dag, comp)
                    except RuntimeError:
                        pass
                    if not comp.isNull():
                        return (dag.node(), comp)
                    splitName = obj_name.split('.')
                    if len(splitName) == 2:
                        obj = MObject()
                        try:
                            sel.add(splitName[0])
                            sel.getDependNode(1, obj)
                        except RuntimeError:
                            pass
                        else:
                            mfn = MFnDependencyNode(obj)
                            aliases = []
                            if mfn.getAliasList(aliases):
                                this_iter = iter(aliases)
                                for aliasName, trueName in itertools.izip(this_iter, this_iter):
                                    if aliasName == splitName[1]:
                                        return Global.nameToApiObject('.'.join((splitName[0], trueName)))
            else:
                obj = MObject()
                sel.getDependNode(0, obj)
                return obj

    @staticmethod
    def nameToMObject(obj_name):
        sel = MSelectionList()
        sel.add(obj_name)
        obj = MObject()
        sel.getDependNode(0, obj)
        return obj

    @staticmethod
    def nameToMDagPath(obj_name):
        sel = MSelectionList()
        sel.add(obj_name)
        path = MDagPath()
        obj = MObject()
        sel.getDagPath(0, path, obj)
        return (path, obj)

    @staticmethod
    def nameToComponentsMObject(obj_name):
        sel = MSelectionList()
        sel.add(obj_name)
        obj = MObject()
        sel.getDagPath(0, MDagPath(), obj)
        return obj

    @staticmethod
    def objToNode(obj):
        u"""
        将Maya对象转化为Node

        :type obj: MObject
        :param obj: MObject对象
        :return:
        """
        Global.DependencyNode_o.setObject(obj)
        uuid = Global.DependencyNode_o.uuid()
        uuid_s = uuid.asString()
        try:
            cp_obj = Global.NewNodes[uuid_s]
            if not cp_obj.isNull():
                return cp_obj
        except KeyError:
            pass
        api_type = obj.apiType()
        try:
            o = Global.DependencyNodeTypes[api_type](obj, uuid, uuid_s)
            Global.NewNodes[uuid_s] = o
            return o
        except KeyError:
            for i in Global.DgTypes:
                if obj.hasFn(i):
                    cla = Global.DependencyNodeTypes[i]
                    Global.DependencyNodeTypes[api_type] = cla
                    o = cla(obj, uuid, uuid_s)
                    Global.NewNodes[uuid_s] = o
                    return o
            raise cmcore.CPMelError(u"找不到对应的节点类型")

    @staticmethod
    def nameToObject(name):
        return newObject(name)

    @staticmethod
    def nameToNode(name):
        u"""
        创建一个节点对象根据不同的节点创建不同的对象的方法

        :param name: Str 或 Unicode 输入的节点名称
        :return:
        """

        try:
            obj = Global.nameToMObject(name)
        except RuntimeError:
            raise cmcore.CPMelError(u"节点不存在")
        return Global.objToNode(obj)

    @staticmethod
    def nameToAttr(attr_name):
        u"""
        创建AttrObject对象

        :param name: Str 或 Unicode 输入的属性名称
        :return:
        :rtype:AttrObject|ArrayAttrObject
        """
        names = attr_name.split(".")
        node = Global.nameToNode(names[0])
        current_obj = node
        for i in names[1:]:
            current_obj = current_obj.attr(i)
        return current_obj

    @staticmethod
    def nameToComponents(name, components_val):
        u"""
        创建组件对象

        :param name: Str 或 Unicode 输入的节点名称
        :param components_val: Str 或 Unicode 输入的组件名称
        :return:
        :rtype:Components1Base|Components2Base|Components3Base
        """
        find = components_val.find("[")
        if find > 0:
            try:
                components_type = components_val[0:find]
                no_compile = components_val[find:]
                compile = Global.re_object.findall(no_compile)
                node = Global.nameToNode(name)
                if compile[0] == "*":
                    return getattr(node, components_type)
                split_s = tuple((tuple((int(t) for t in i.split(":"))) for i in compile))
                cur_o = getattr(node, components_type)
            except Exception:
                raise cmcore.CPMelError(u"对象不存在")
            for i in split_s:
                if len(i) > 1:
                    cur_o = cur_o[i[0]:i[1]]
                else:
                    cur_o = cur_o[i[0]]
            return cur_o
        else:
            raise cmcore.CPMelError(u"无法创建组件")

    @staticmethod
    def plugToAttr(plug=MPlug):
        u"""
        MPlug转化为Attr

        :param plug: MPlug
        :return:
        :rtype:AttrObject|ArrayAttrObject
        """
        if plug.isNull():
            raise cmcore.CPMelError(u"无法创建CPMel属性")
        if plug.isArray():
            return ArrayAttrObject(plug)
        return AttrObject(plug)

    NoWrapHead = ("__", "cp__")

    @staticmethod
    def objectMetadef(api_type=MFn.kBase):
        def metadef(name, bases, attrs):
            def _(k):
                for t in Global.NoWrapHead:
                    if k.find(t) == 0:
                        return True

            for k, v in attrs.items():
                if k == "isNull":
                    continue
                elif _(k):
                    continue
                elif callable(v):
                    try:
                        NullType = v.NullType
                    except AttributeError:
                        NullType = Global.NullErr
                    if NullType == Global.NullErr:
                        attrs[k] = Global._NullErrFunc(v)
                    elif NullType == Global.NullUp:
                        attrs[k] = Global._NullGetUpFunc(v)
                    else:
                        attrs[k] = Global._NullDoItFunc(v)
                else:
                    attrs[k] = v
            cls = type(name, bases, attrs)
            Global.DependencyNodeTypes[api_type] = cls
            Global.DgTypes.insert(0, api_type)

            # if issubclass(cls, DagNode):
            #     Global.DagTypes.insert(0, api_type)
            # else:
            #     Global.DgTypes.insert(0, api_type)
            return cls

        return metadef

    @staticmethod
    def componentsTypesMetadef(name, bases, attrs):
        cls = type(name, bases, attrs)
        Global.ComponentsTypes.append(cls.components_type_str)
        # print CreateObjectType.ComponentsTypes
        return cls

    NullErr, NullUp, NullDo = range(3)

    # @staticmethod
    # def doesItExistError(fn):
    #     return Global.NullErrFunc(fn)
    #
    # @staticmethod
    # def NullGetUpFunc(fn):
    #     return Global.NullGetUpFunc(fn)

    @staticmethod
    def NullErrFunc(fn):
        u"""
        检查对象是否存在的节点对象类所操作的对象是否存在的装饰器
        如果不存在就报错

        :param fn:
        :return:
        """
        fn.NullType = Global.NullErr
        return fn

    @staticmethod
    def NullGetUpFunc(fn):
        u"""
        检查对象是否存在的节点对象类所操作的对象是否存在的装饰器
        如果不存在就使用上一个数据

        :param fn:
        :return:
        """

        fn.NullType = Global.NullUp
        return fn

    @staticmethod
    def NullDoItFunc(fn):
        u"""
        检查对象是否存在的节点对象类所操作的对象是否存在的装饰器
        如果不存在仍然执行

        :param fn:
        :return:
        """
        fn.NullType = Global.NullDo
        return fn

    @staticmethod
    def _NullErrFunc(fn):
        u"""
        检查对象是否存在的节点对象类所操作的对象是否存在的装饰器
        如果不存在就报错

        :param fn:
        :return:
        """

        def _(self, *args, **kwargs):
            if self.isNull():
                cmcore.CPMelError(u"节点对象自身已不存在无法操作")
            else:
                return fn(self, *args, **kwargs)

        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    @staticmethod
    def _NullGetUpFunc(fn):
        u"""
        检查对象是否存在的节点对象类所操作的对象是否存在的装饰器
        如果不存在就使用上一个数据

        :param fn:
        :return:
        """

        def _(self, *args, **kwargs):
            if self.isNull():
                try:
                    return _.data
                except AttributeError:
                    return None
            else:
                _.data = fn(self, *args, **kwargs)
                return _.data

        _.data = None
        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    @staticmethod
    def _NullDoItFunc(fn):
        u"""
        检查对象是否存在的节点对象类所操作的对象是否存在的装饰器
        如果不存在就使用上一个数据

        :param fn:
        :return:
        """
        return fn


class CPObject(object):
    u"""
    所有CPObject的基类
    """
    Globalfunction = Global
    Object_List = None

    def __add__(self, other):
        u"""
        this + oyher

        :param other:
        :return:
        """
        if isinstance(other, basestring):
            return u"%s%s" % (str(self), other)
        if isinstance(other, DgNode):
            return u"%s%s" % (str(self), str(other))

    def __radd__(self, other):
        u"""
        other + this

        :param other:
        :return:
        """
        if isinstance(other, basestring):
            return u"%s%s" % (other, str(self))
        if isinstance(other, DgNode):
            return u"%s%s" % (str(other), str(self))

    def __repr__(self):
        return repr(self.__str__())

    def isNull(self):
        u"""
        检查对象是否可以使用
        所有方法默认都会检查是否可以调用（这个除外）
        :return:
        :rtype:bool
        """
        return True

    def compile(self):
        return unicode(self)


class DgNode(CPObject):
    u"""
    节点对象基类
    """
    __metaclass__ = Global.objectMetadef(MFn.kDependencyNode)

    def __init__(self, obj=MObject, uuid=MUuid, uuid_s=u""):
        if obj.isNull():
            return
        self.obj = obj
        self.uuid = uuid
        self.uuid_s = uuid_s
        self.objecthandle = MObjectHandle(obj)
        self.fn = self.cp__getFnClass()
        self.type = self.fn.typeName()

    def cp__getFnClass(self):
        u"""
        获得当前函数集

        :return: MFn
        :rtype:MFnDependencyNode
        """
        return MFnDependencyNode(self.obj)

    def isNull(self):
        u"""
        检查对象是否可以使用

        :return:
        :rtype:bool
        """
        return not self.objecthandle.isValid() and self.uuid.valid()

    def __unicode__(self):
        u"""
        __unicode__输出

        :return:
        """
        return self.name()

    def __str__(self):
        u"""
        str输出

        :return:
        """
        return self.name()

    def __repr__(self):
        u"""
        repr输出

        :return:
        """

        return "%s(%s)" % (self.type, repr(self.name()))

    def __eq__(self, other):
        u"""
        ==判断

        :param other:
        :return:
        """
        if isinstance(other, DgNode):
            return self.uuid_s == other.uuid_s
        return False

    def __ne__(self, other):
        u"""
        !=判断

        :param other:
        :return:
        """
        return not self.__eq__(other)

    def __getitem__(self, item):
        u"""
        []访问操作

        :param item:
        :return:
        :rtype:int|float|bool|tuple|list
        """
        if isinstance(item, basestring):
            return self.attr(item).get()
        else:
            raise cmcore.CPMelError(u"仅支持字符串访问")

    def __setitem__(self, key, value):
        if isinstance(key, basestring):
            return self.attr(key).set(value)
        else:
            raise cmcore.CPMelError(u"仅支持字符串访问")

    def __getattribute__(self, item):
        u"""
        .访问操作

        :param item:
        :return:
        """
        try:
            # if item == "__class__":
            #     return type(self)
            return object.__getattribute__(self, item)
        except AttributeError:
            return object.__getattribute__(self, "attr")(item)

    @staticmethod
    def isCurrentNodeType(obj=MObject):
        u"""
        返回节点这个类是否支持这个节点

        :param obj: api1.0 MObject 指向一个节点的MObject
        :return: bool
        """
        return True

    def _attr(self, attr):
        find = attr.find("[")
        if find < 0:
            try:
                plug = self.fn.findPlug(attr)
                attr_obj = self.Globalfunction.plugToAttr(plug)
            except RuntimeError:
                raise cmcore.CPMelError(u"属性不存在")
            return attr_obj
        else:
            find = attr.find("[")
            if find < 0:
                raise cmcore.CPMelError(u"属性不存在")
            else:
                try:
                    arr_attr_obj = self.Globalfunction.plugToAttr(self.fn.findPlug(attr[:find]))
                    if not isinstance(arr_attr_obj, ArrayAttrObject):
                        raise cmcore.CPMelError(u"要获得的属性不是数组属性")
                    finde = attr.find("]")
                    if finde < 0:
                        raise cmcore.CPMelError(u"字符串结构错误 attr 或 attr[?]")
                    index = int(attr[find + 1: finde])
                    return arr_attr_obj[index]

                except RuntimeError:
                    raise cmcore.CPMelError(u"属性不存在")

    def attr(self, attr):
        u"""
        获得maya属性的CPMel对象

        :param attr:
        :return:
        :rtype: AttrObject|ArrayAttrObject
        """
        try:
            sel = MSelectionList()
            sel.add(u"%s.%s" % (str(self), attr))
            plug = MPlug()
            sel.getPlug(0, plug)
            attr_obj = self.Globalfunction.plugToAttr(plug)
        except RuntimeError:
            attr_obj = self
            for i in attr.split("."):
                if attr_obj is self:
                    attr_obj = attr_obj._attr(i)
                else:
                    attr_obj.attr(i)
        setattr(self, attr, attr_obj)
        return attr_obj

    def functionSet(self):
        u"""
        获得节点函数集

        :return:
        """
        sel_l = MSelectionList()
        sel_l.add(self.uuid)
        self.obj = MObject()
        sel_l.getDependNode(0, self.obj)
        self.objecthandle = MObjectHandle(self.obj)
        self.cp__fn = self.cp__getFnClass()
        return self.cp__fn

    @Global.NullGetUpFunc
    def name(self):
        u"""
        获得节点最短名称

        :return: Unicode 节点最短名称
        :rtype: unicode
        """
        return self.fn.name()

    def rename(self, p_str):
        u"""
        重命名

        :return: Unicode 新名称
        """
        cmds.rename(str(self), p_str)

    def listAttr(self, *args, **kwargs):
        u"""
        获得所有属性对象

        :return:
        :rtype: list
        """
        attrs = cmds.listAttr(str(self), *args, **kwargs)
        if attrs is None:
            return []
        else:
            return [self.attr(i) for i in attrs]

    def copy(self):
        u"""

        :return:
        :rtype: DgNode:DagNode
        """
        return self.Globalfunction.nameToNode(cmds.duplicate(str(self), rc=True)[0])

    def isFromReferencedFile(self):
        u"""
        此节点是否来自引用的文件

        :return:
        :rtype: bool
        """
        return self.fn.isFromReferencedFile()

    def isDefaultNode(self):
        u"""
        如果该节点是默认节点返回true

        :return:
        :rtype:bool
        """
        return self.fn.isDefaultNode()

    def getNamespace(self):
        u"""
        返回此节点所在的名称空间的名称

        :return:
        :rtype:unicode
        """
        return self.fn.parentNamespace()

    def setLocked(self, bool):
        u"""
        设置节点锁定状态

        :param bool:
        :return:
        """

        def doIt():
            self.functionSet().setLocked(bool)

        def undoIt():
            self.functionSet().setLocked(not bool)

        return cmcore.addCommand(doIt, undoIt)

    def getLocked(self):
        u"""
        获得节点锁定状态

        :return:
        :rtype:bool
        """
        return self.fn.isLocked()


class DagNode(DgNode):
    __metaclass__ = Global.objectMetadef(MFn.kDagNode)

    def __init__(self, obj=MObject, uuid=MUuid, uuid_s=u""):
        super(DagNode, self).__init__(obj, uuid, uuid_s)

    def cp__getFnClass(self):
        u"""
        获得当前函数集

        :return: MFn
        :rtype:MFnDagNode
        """
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnDagNode(path)

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u"""
        返回节点这个类是否支持这个节点

        :param path: api1.0 MObject 指向一个节点的MObject
        :return: bool
        :rtype:bool
        """
        return True

    @Global.NullGetUpFunc
    def nodeName(self):
        u"""
        获得节点名称

        :return: Unicode 节点名称
        :rtype:unicode
        """
        return self.fn.name()

    @Global.NullGetUpFunc
    def name(self):
        u"""
        获得节点最短名称

        :return: Unicode 节点最短名称
        :rtype:unicode
        """
        return self.fn.partialPathName()

    @Global.NullGetUpFunc
    def fullPathName(self):
        u"""
        获得节点绝对路径

        :return: Unicode 节点绝对路径
        :rtype:unicode
        """
        return self.fn.fullPathName()

    def childCount(self):
        u"""
        获得子对象的数量

        :return:
        :rtype:int
        """
        return self.fn.childCount()

    def addChild(self, obj):
        u"""
        添加子对象

        :param obj:
        :return:
        """
        if isinstance(obj, DagNode):
            obj = str(obj)
        if isinstance(obj, basestring):
            cmds.parent(str(obj), str(self))
        else:
            raise cmcore.CPMelError(u"不是Dag节点")

    def getChilds(self):
        u"""

        :return:
        :rtype:list
        """
        return [self.Globalfunction.objToNode(self.fn.child(i)) for i in xrange(self.childCount())]

    def getParent(self):
        u"""
        获得父对象

        :return:
        :rtype: DagNode
        """
        parents = self.fullPathName().split("|")
        if len(parents) > 2:
            return self.Globalfunction.nameToNode("|".join(parents[0:-1]))
        else:
            return

    def setParent(self, obj):
        u"""
        设置父对象

        :param obj:
        :return:
        """
        if isinstance(obj, DagNode):
            obj = str(obj)
        if isinstance(obj, basestring):
            cmds.parent(str(self), str(obj))
            # self.fn.addChild(obj.cp__obj)
        else:
            raise cmcore.CPMelError(u"不是Dag节点")

    parent = property(getParent, setParent)

    def getParents(self):
        u"""
        获得所有父对象

        :return:
        :rtype:list
        """
        parents = self.fullPathName().split("|")
        return [self.Globalfunction.nameToNode("|".join(parents[0:i])) for i in range(2, len(parents))]

    parents = property(getParents)

    def toRoot(self):
        u"""
        转到根路径

        :return:
        """
        cmds.parent(str(self), w=True)

    def setTranslate(self, point=basedata.Double3, is_word=True):
        u"""
        设置位置

        :param point: 位置参数
        :param is_word: 是否在世界空间下
        :return:
        """
        cmds.xform(str(self), t=(point[0], point[1], point[2]), ws=is_word)
        return

    def getTranslate(self, is_word=True):
        u"""
        获得位置

        :param is_word: 是否在世界空间下
        :return:
        :rtype:Double3
        """
        return basedata.Double3(cmds.xform(str(self), q=True, t=True, ws=is_word))

    def setRotate(self, vector=basedata.Double3, is_word=True):
        u"""
        设置旋转

        :param vector: 旋转值
        :param is_word: 是否在世界空间下
        :return:
        """
        cmds.xform(str(self), ro=(vector[0], vector[1], vector[2]), ws=is_word)
        return

    def getRotate(self, is_word=True):
        u"""
        获得旋转

        :param is_word: 是否在世界空间下
        :return:
        :rtype:Double3
        """
        return basedata.Double3(cmds.xform(str(self), q=True, ro=True, ws=is_word))

    def setScale(self, vector=basedata.Double3, is_word=True):
        u"""
        设置缩放

        :param vector: 缩放值
        :param is_word: 是否在世界空间下
        :return:
        """
        cmds.xform(str(self), s=(vector[0], vector[1], vector[2]), ws=is_word)
        return

    def getScale(self, is_word=True):
        u"""
        获得缩放

        :param is_word: 是否在世界空间下
        :return:
        :rtype:Double3
        """
        return basedata.Double3(cmds.xform(str(self), q=True, s=True, ws=is_word))


# class Test(DagNode):
#     def __init__(self, obj):
#         super(Test, self).__init__(obj)


# class Shape(DagNode):
#     components = dict()
#     # def getComponents


class AttrObject(CPObject):
    u"""
    属性对象
    """

    def __init__(self, plug=MPlug):
        self.cp__node = self.Globalfunction.objToNode(plug.node())
        self.plug = plug
        self.obj = plug.attribute()
        self.objecthandle = MObjectHandle(self.obj)
        try:
            self.type = cmds.getAttr(str(self), type=True)
        except RuntimeError as ex:
            def test_set(val, **kwargs):
                cmds.setAttr(str(self), val, **kwargs)

            def test_get(**kwargs):
                raise cmcore.CPMelError(u"不可获得属性的值")

            self.type = u""
        else:
            def test_set(val, **kwargs):
                cmds.setAttr(str(self), val, **kwargs)

            def test_get(**kwargs):
                return cmds.getAttr(str(self), **kwargs)

            type_type = (u"Int32Array", u"doubleArray", u"string")
            size_array_type = (u"pointArray", u"vectorArray", u"stringArray", u"componentList")
            val3_type = (u"double3", u"float3", u"short3", u"long3", u"reflectanceRGB", u"spectrumRGB")
            if self.type in val3_type:
                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), *val, type=self.type, **kwargs)

                def test_get(**kwargs):
                    return cmds.getAttr(str(self), **kwargs)[0]
            elif self.type in type_type:
                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), val, type=self.type, **kwargs)
            elif self.type in size_array_type:
                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), len(val), *val, type=self.type, **kwargs)
            elif self.type == u"matrix":
                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), *[t for i in val for t in i], type=self.type, **kwargs)

                def test_get(**kwargs):
                    lis = cmds.getAttr(str(self), **kwargs)
                    return (
                        lis[0:4],
                        lis[4:8],
                        lis[8:12],
                        lis[12:16]
                    )
        self.__set = test_set
        self.__get = test_get

    def cp__attrPartialName(self):
        u"""
        获得属性名称

        :return:
        :rtype:unicode
        """
        return self.plug.partialName(False,
                                     True,
                                     True,
                                     False,
                                     False,
                                     True).replace('[-1]', '')

    @property
    def attrname(self):
        u"""

        :return:
        :rtype:unicode
        """
        return self.cp__attrPartialName()

    def cp__attrname(self):
        u"""
        获得CPMel属性对象名称

        :return:
        :rtype:unicode
        """
        return u"%s.%s" % (self.cp__node.name(), self.cp__attrPartialName())

    def set(self, val, **kwargs):
        u"""
        设置值

        :param val:
        :param kwargs:
        :return:
        """
        try:
            return self.__set(val, **kwargs)
        except RuntimeError as ex:
            raise cmcore.CPMelError(*ex.args)

    def get(self, **kwargs):
        u"""
        获得值

        :param kwargs:
        :return:
        :rtype: int|float|tuple|Double3|list
        """
        try:
            return self.__get(**kwargs)
        except RuntimeError as ex:
            raise cmcore.CPMelError(*ex.args)

    v = property(get, set)

    def __str__(self):
        return self.cp__attrname()

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.cp__attrname()))

    def __eq__(self, other):
        u"""
        ==判断

        :param other:
        :return:
        """
        if isinstance(other, AttrObject):
            return self.cp__attrname() == other.cp__attrname()
        return False

    def __ne__(self, other):
        u"""
        !=判断

        :param other:
        :return:
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        u"""
        this>xxx 操作

        :param other:
        :return:
        """
        other.set(self.get())
        return

    def __lshift__(self, other):
        u"""
        this << xxx

        :param other:
        :return:
        """
        return other.connect(self)

    def __rshift__(self, other):
        u"""
        this >> xxx

        :param other:
        :return:
        """
        return self.connect(other)

    def attr(self, attr):
        u"""

        :param attr:
        :return:
        :rtype: AttrObject|ArrayAttrObject
        :raise: CPMelError
        """
        if attr in self.__dict__:
            return self.__dict__[attr]
        # try:
        #     self.Globalfunction.nameToAttr(u"%s.%s"%(str(self), attr))
        find = attr.find("[")
        if find < 0:
            for i in xrange(self.plug.numChildren()):
                test_plug = self.plug.child(i)
                test_attr_name = test_plug.partialName().split(".")[-1]
                if attr == test_attr_name:
                    attr_obj = self.Globalfunction.plugToAttr(test_plug)
                    self.__dict__[attr] = attr_obj
                    return attr_obj
                test_attr_name = test_plug.partialName(False, False, False, False, False, True).split(".")[-1]
                if attr == test_attr_name:
                    attr_obj = self.Globalfunction.plugToAttr(test_plug)
                    self.__dict__[attr] = attr_obj
                    return attr_obj
            raise cmcore.CPMelError(u"属性不存在")
        else:
            try:
                arr_attr_obj = self.attr(attr[:find])
                if not isinstance(arr_attr_obj, ArrayAttrObject):
                    raise cmcore.CPMelError(u"要获得的属性不是数组属性")
                finde = attr.find("]")
                if finde < 0:
                    raise cmcore.CPMelError(u"字符串结构错误 attr 或 attr[?]")
                index = int(attr[find + 1: finde])
                return arr_attr_obj[index]

            except RuntimeError:
                raise cmcore.CPMelError(u"属性不存在")

    def __getattribute__(self, item):
        u"""
        .访问操作

        :param item:
        :return:
        """
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            if isinstance(item, basestring):
                return object.__getattribute__(self, "attr")(item)
            else:
                raise cmcore.CPMelError(u"对象没有属性")

    def node(self):
        u"""
        获得节点对象

        :return:
        :rtype:DgNode|DagNode
        """
        return self.cp__node

    def connect(self, attr):
        u"""
        连接

        :param attr:
        :return:
        """
        cmds.connectAttr(self.cp__attrname(), attr.cp__attrname(), f=True)

    def disConnect(self, attr):
        u"""
        断开连接

        :param attr:
        :return:
        """
        cmds.disconnectAttr(self.cp__attrname(), attr.cp__attrname())

    def isConnect(self):
        u"""
        插点是否连接

        :return:
        :rtype:bool
        """
        return self.plug.isConnected()

    if MAYAINDEX > 2016:
        def getInConnect(self):
            u"""
            获得输入连接2016+版本

            :return:
            :rtype:AttrObject|ArrayAttrObject
            """
            plug = self.plug.source()
            if plug.isNull():
                return None
            return self.Globalfunction.plugToAttr(plug)

        def getOutConnects(self):
            u"""
            获得输出连接2016+版本

            :return:
            :rtype:tuple
            """
            plugs = MPlugArray()
            self.plug.destinations(plugs)
            return tuple((self.Globalfunction.plugToAttr(i) for i in plugs if not i.isNull()))
    else:
        def getInConnect(self):
            u"""
            获得输入连接2017-版本

            :return:
            :rtype:AttrObject|ArrayAttrObject
            """
            o = cmds.listConnections(str(self), s=True, d=False, scn=True, p=True)
            if o is None:
                return None
            return self.Globalfunction.nameToAttr(o[0])

        def getOutConnects(self):
            u"""
            获得输出连接2017-版本

            :return:
            :rtype:tuple
            """
            o = cmds.listConnections(str(self), s=False, d=True, scn=True, p=True)
            if o is None:
                return tuple()

            return tuple((self.Globalfunction.nameToAttr(i) for i in o))


class ArrayAttrObject(AttrObject):
    def itemids(self):
        ids = MIntArray()

        self.plug.getExistingArrayAttributeIndices(ids)
        return ids

    def items(self):
        u"""

        :return:
        :rtype:list
        """
        return [self.cp__node.attr("%s[%d]" % (self.cp__attrPartialName(), i)) for i in self.itemids()]

    def __getitem__(self, item):
        plug = self.plug.elementByLogicalIndex(item)
        return self.Globalfunction.plugToAttr(plug)

    def __iter__(self):
        return (self[i] for i in self.itemids())


class UIObject(BaseData):
    u"""
    UI对象基类
    """

    def __init__(self, ui):
        self.ui = ui

    def getWeidget(self):
        u"""
        :return:
        """
        return wrapInstance(long(OpenMayaUI.MQtUtil.findWindow(self.ui)), QWidget)

    def getControlWeidget(self):
        u"""
        :return:
        """
        return wrapInstance(long(OpenMayaUI.MQtUtil.findControl(self.ui)), QWidget)

    def getLayoutWeidget(self):
        u"""
        :return:
        """
        return wrapInstance(long(OpenMayaUI.MQtUtil.findLayout(self.ui)), QWidget)

    def getItemWeidget(self):
        u"""
        :return:
        """
        return wrapInstance(long(OpenMayaUI.MQtUtil.findMenuItem(self.ui)), QWidget)

    def compile(self):
        u"""
        编译为mel对象

        :return:
        """
        return self.ui

    def __str__(self):
        return str(self.ui)

    def __unicode__(self):
        return self.ui

    def __repr__(self):
        return repr(self.ui)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def newObject(name=str):
    u"""
    根据不同的输入返回不同的CPMel对象
    :param name:
    :return: DgNode或AttrObject本身或其子类
    :rtype:CPObject|DgNode|DagNode|AttrObject|ArrayAttrObject|Components1Base|Components2Base|Components3Base
    """
    if isinstance(name, DgNode):
        return name
    if not isinstance(name, basestring):
        name = str(name)
    find = name.find(".")
    if find > 0:
        node_name = name[0:find]
        attr_or_comp = name[find + 1:]
        comp_find = attr_or_comp.find("[")
        if comp_find < 0:
            comp_find = len(attr_or_comp)
        if attr_or_comp[0:comp_find] in Global.ComponentsTypes:
            return Global.nameToComponents(node_name, attr_or_comp)
        else:
            return Global.nameToAttr(name)
    return Global.nameToNode(name)


ObjectMetadef = Global.objectMetadef

componentsTypesMetadef = Global.componentsTypesMetadef


class Components1Base(CPObject):
    components_type_str = ""
    index = None

    def __init__(self, node=DgNode):
        self.node = node

    def cp__init_componenrs(self):
        pass

    @staticmethod
    def IsSingleComponent(fn):
        def _(self, *args, **kwargs):
            if type(self.index) == int:
                return fn(self, *args, **kwargs)
            else:
                raise cmcore.CPMelError(fn.__name__ + u" 方法只能在单组件模式下运行")

        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    def __str__(self):
        if self.index is None:
            return "%s.%s[*]" % (self.node.compile(), self.components_type_str)
        else:
            if type(self.index) == int:
                return "%s.%s[%d]" % (self.node.compile(), self.components_type_str, self.index)
            else:
                return "%s.%s[%d:%d]" % (self.node.compile(), self.components_type_str, self.index[0], self.index[1])

    def cp__newIndexObject(self, index):
        u"""

        :param index:
        :return:
        :rtype:Components1Base
        """
        obj = self.__class__(self.node)
        obj.index = index
        obj.cp__init_componenrs()
        return obj

    def __getitem__(self, item):
        u"""

        :param item:
        :return:
        :rtype:Components1Base
        """
        obj = self.__class__(self.node)
        if self.index is None:
            if type(item) == int:
                obj.index = item
            else:
                obj.index = (item.start, item.stop)
        else:
            raise cmcore.CPMelError(u"没有更深索引的组件")
        obj.cp__init_componenrs()
        return obj

    def __len__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnSingleIndexedComponent(obj)
        indexs = MIntArray()
        self.indexed_component.getElements(indexs)
        return indexs.length()

    def __iter__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnSingleIndexedComponent(obj)
        indexs = MIntArray()
        self.indexed_component.getElements(indexs)
        return (self.cp__newIndexObject(i) for i in indexs)


class Components2Base(CPObject):
    components_type_str = ""
    indexu = None
    indexv = None

    def __init__(self, node=DgNode):
        self.node = node

    def cp__init_componenrs(self):
        pass

    @staticmethod
    def IsSingleComponent(fn):
        def _(self, *args, **kwargs):
            if type(self.indexu) == int and type(self.indexv) == int:
                return fn(self, *args, **kwargs)
            else:
                raise cmcore.CPMelError(fn.__name__ + u" 方法只能在单组件模式下运行")

        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    def __str__(self):
        if self.indexu is None:
            return "%s.%s[*][*]" % (self.node.compile(), self.components_type_str)
        elif self.indexv is None:
            if type(self.indexu) == int:
                return "%s.%s[%d][*]" % (self.node.compile(), self.components_type_str, self.indexu)
            else:
                return "%s.%s[%d:%d][*]" % (
                    self.node.compile(), self.components_type_str, self.indexu[0], self.indexu[1])
        else:
            if type(self.indexu) == int:
                if type(self.indexv) == int:
                    return "%s.%s[%d][%d]" % (self.node.compile(), self.components_type_str, self.indexu, self.indexv)
                else:
                    return "%s.%s[%d][%d:%d]" % (
                        self.node.compile(), self.components_type_str, self.indexu, self.indexv[0], self.indexv[1])
            else:
                if type(self.indexv) == int:
                    return "%s.%s[%d:%d][%d]" % (
                        self.node.compile(), self.components_type_str, self.indexu[0], self.indexu[1], self.indexv)
                else:
                    return "%s.%s[%d:%d][%d:%d]" % (
                        self.node.compile(), self.components_type_str, self.indexu[0], self.indexu[1], self.indexv[0],
                        self.indexv[1])

    def cp__newIndexObject(self, indexu, indexv):
        u"""

        :param indexu:
        :param indexv:
        :return:
        :rtype:Components2Base
        """
        obj = self.__class__(self.node)
        obj.indexu = indexu
        obj.indexv = indexv
        obj.cp__init_componenrs()
        return obj

    def __getitem__(self, item):
        u"""

        :param item:
        :return:
        :rtype:Components2Base
        """
        obj = self.__class__(self.node)
        if self.indexu is None:
            if type(item) == int:
                obj.indexu = item
            else:
                obj.indexu = (item.start, item.stop)
        elif self.indexv is None:
            if type(item) == int:
                obj.indexv = item
            else:
                obj.indexv = (item.start, item.stop)
        else:
            raise cmcore.CPMelError(u"没有更深索引的组件")
        obj.cp__init_componenrs()
        return obj

    def __len__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnDoubleIndexedComponent(obj)
        indexus = MIntArray()
        indexvs = MIntArray()
        self.indexed_component.getElements(indexus, indexvs)
        return indexus.length()

    def __iter__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnDoubleIndexedComponent(obj)
        indexus = MIntArray()
        indexvs = MIntArray()
        self.indexed_component.getElements(indexus, indexvs)
        return (self.cp__newIndexObject(indexus[i], indexvs[i]) for i in xrange(indexus.length()))


class Components3Base(CPObject):
    components_type_str = ""
    indexs = None
    indext = None
    indexu = None

    def __init__(self, node=DgNode):
        self.node = node

    def cp__init_componenrs(self):
        pass

    def __str__(self):
        if self.indexs is None:
            return "%s.%s[*][*][*]" % (self.node.compile(), self.components_type_str)
        elif self.indext is None:
            if type(self.indext) == int:
                return "%s.%s[%d][*][*]" % (self.node.compile(), self.components_type_str, self.indexs)
            else:
                return "%s.%s[%d:%d][*][*]" % (
                    self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1])
        elif self.indexu is None:
            if type(self.indexs) == int:
                if type(self.indext) == int:
                    return "%s.%s[%d][%d][*]" % (
                        self.node.compile(), self.components_type_str, self.indexs, self.indext)
                else:
                    return "%s.%s[%d][%d:%d][*]" % (
                        self.node.compile(), self.components_type_str, self.indexs, self.indext[0], self.indext[1])
            else:
                if type(self.indext) == int:
                    return "%s.%s[%d:%d][%d][*]" % (
                        self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext)
                else:
                    return "%s.%s[%d:%d][%d:%d][*]" % (
                        self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext[0],
                        self.indext[1])
        else:
            if type(self.indexs) == int:
                if type(self.indext) == int:
                    if type(self.indexu) == int:
                        return "%s.%s[%d][%d][%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs, self.indext, self.indexu)
                    else:
                        return "%s.%s[%d][%d][%d:%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs, self.indext, self.indexu[0],
                            self.indexu[1])
                else:
                    if type(self.indexu) == int:
                        return "%s.%s[%d][%d:%d][%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs, self.indext[0], self.indext[1],
                            self.indexu)
                    else:
                        return "%s.%s[%d][%d:%d][%d:%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs, self.indext[0], self.indext[1],
                            self.indexu[0], self.indexu[1])
            else:
                if type(self.indext) == int:
                    if type(self.indexu) == int:
                        return "%s.%s[%d:%d][%d][%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext,
                            self.indexu)
                    else:
                        return "%s.%s[%d:%d][%d][%d:%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext,
                            self.indexu[0], self.indexu[1])
                else:
                    if type(self.indexu) == int:
                        return "%s.%s[%d:%d][%d:%d][%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1],
                            self.indext[0], self.indext[1], self.indexu)
                    else:
                        return "%s.%s[%d:%d][%d:%d][%d:%d]" % (
                            self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1],
                            self.indext[0], self.indext[1], self.indexu[0], self.indexu[1])

    def cp__newIndexObject(self, indexs, indext, indexu):
        u"""

        :param indexs:
        :param indext:
        :param indexu:
        :return:
        :rtype:Components3Base
        """
        obj = self.__class__(self.node)
        obj.indexs = indexs
        obj.indext = indext
        obj.indexu = indexu
        obj.cp__init_componenrs()
        return obj

    def __getitem__(self, item):
        u"""

        :param item:
        :return:
        :rtype:Components3Base
        """
        obj = self.__class__(self.node)
        if self.indexs is None:
            if type(item) == int:
                obj.indexs = item
            else:
                obj.indexs = (item.start, item.stop)
        elif self.indext is None:
            if type(item) == int:
                obj.indext = item
            else:
                obj.indext = (item.start, item.stop)
        elif self.indexu is None:
            if type(item) == int:
                obj.indexu = item
            else:
                obj.indexu = (item.start, item.stop)
        else:
            raise cmcore.CPMelError(u"没有更深索引的组件")
        obj.cp__init_componenrs()
        return obj

    def __len__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnTripleIndexedComponent(obj)
        indexss = MIntArray()
        indexts = MIntArray()
        indexus = MIntArray()
        self.indexed_component.getElements(indexss, indexts, indexus)
        return indexus.length()

    def __iter__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnTripleIndexedComponent(obj)
        indexss = MIntArray()
        indexts = MIntArray()
        indexus = MIntArray()
        self.indexed_component.getElements(indexss, indexts, indexus)
        return (self.cp__newIndexObject(indexss[i], indexts[i], indexus[i]) for i in xrange(indexss.length()))
