#!/usr/bin/python
# -*-coding:utf-8 -*-
# :创建时间: 2020/5/18 23:57
# :作者: 苍之幻灵
# :我的主页: https://cpcgskill.com
# :QQ: 2921251087
# :爱发电: https://afdian.net/@Phantom_of_the_Cang
# :aboutcg: https://www.aboutcg.org/teacher/54335
# :bilibili: https://space.bilibili.com/351598127
from .. import ISDEBUG
from ..cmds.node import nodedata
from ..api import OpenMaya
from . import base
if ISDEBUG:
    reload(base)



class Dg(base.EventBase):
    def __init__(self):
        super(Dg, self).__init__()
        self.message_ids.append(OpenMaya.MDGMessage.addNodeAddedCallback(self.__createNode))
        self.message_ids.append(OpenMaya.MDGMessage.addNodeRemovedCallback(self.__removeNode))
        self.message_ids.append(OpenMaya.MDGMessage.addPreConnectionCallback(self.__connectMessage))
        self.message_ids.append(OpenMaya.MDGMessage.addConnectionCallback(self.__connectedMessage))

    def __createNode(self, node = OpenMaya.MObject, data = None):
        self.createNode(nodedata.Global.objToNode(node))

    def __removeNode(self, node = OpenMaya.MObject, data = None):
        self.removeNode(nodedata.Global.objToNode(node))

    def __connectedMessage(self, in_attr = OpenMaya.MPlug, out_attr = OpenMaya.MPlug, is_connect = bool, data = None):
        in_attr = nodedata.Global.plugToAttr(in_attr)
        out_attr = nodedata.Global.plugToAttr(out_attr)
        if is_connect:
            self.connected(in_attr, out_attr)
        else:
            self.disconnected(in_attr, out_attr)

    def __connectMessage(self, in_attr = OpenMaya.MPlug, out_attr = OpenMaya.MPlug, is_connect = bool, data = None):
        in_attr = nodedata.Global.plugToAttr(in_attr)
        out_attr = nodedata.Global.plugToAttr(out_attr)
        if is_connect:
            self.connect(in_attr, out_attr)
        else:
            self.disconnect(in_attr, out_attr)

    def createNode(self, node = nodedata.DgNode):
        u"""
        节点创建事件

        :param node:
        :return:
        """
        pass

    def removeNode(self, node = nodedata.DgNode):
        u"""
        节点移除事件

        :param node:
        :return:
        """
        pass

    def connect(self, in_attr = nodedata.AttrObject, out_attr = nodedata.AttrObject):
        u"""
        属性连接事件

        :param in_attr:
        :param out_attr:
        :return:
        """
        pass

    def disconnect(self, in_attr = nodedata.AttrObject, out_attr = nodedata.AttrObject):
        u"""
        属性断开连接事件

        :param in_attr:
        :param out_attr:
        :return:
        """
        pass

    def connected(self, in_attr = nodedata.AttrObject, out_attr = nodedata.AttrObject):
        u"""
        属性连接结束事件

        :param in_attr:
        :param out_attr:
        :return:
        """
        pass

    def disconnected(self, in_attr = nodedata.AttrObject, out_attr = nodedata.AttrObject):
        u"""
        属性断开连接结束事件

        :param in_attr:
        :param out_attr:
        :return:
        """
        pass



class Dag(Dg):
    def __init__(self):
        super(Dag, self).__init__()
        self.message_ids.append(OpenMaya.MDagMessage.addParentAddedCallback(self.__moveLevel))

    def __moveLevel(self, child = OpenMaya.MDagPath, parent = OpenMaya.MDagPath, data = None):
        self.moveLevel(nodedata.newObject(child.fullPathName()), nodedata.newObject(parent.fullPathName()))

    def moveLevel(self, child = nodedata.DagNode, parent = nodedata.DagNode):
        u"""
        层级移动

        :param child:
        :param parent:
        :return:
        """
        pass



class Select(base.EventBase):
    def __init__(self):
        super(Select, self).__init__()
        self.message_ids.append(
                OpenMaya.MEventMessage.addEventCallback(u"SelectionChanged", self.__selected)
                )

    def __selected(self, data = None):
        self.selected()

    def selected(self):
        u"""
        选择事件

        :return:
        """
        pass
