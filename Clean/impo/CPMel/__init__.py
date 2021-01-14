#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/5/18 23:57
:作者: 苍之幻灵
:我的主页: https://www.cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

* 获得路径模块
    * PATH : CPMel所在路径
    * MAYAPLUG : CPMel的Maya插件所在路径
    * ISDEBUG : 是否处在Debug模式

* 快速入门:

    * 导入:
        >>> from cpweidgets import CPMel as OpenMaya, CPMel as OpenMayaMPx, CPMel as cc, CPMel as cmcore, CPMel as cevent, CPMel as ctl
        >>> ...
        >>> from cpweidgets.CPMel import *
    * 命令:

        * maya.cmds:
            >>> import maya.cmds as cmds
            >>> cmds.joint()
            u"xxx"

        * CPMel.cmds

            >>> cc.joint()
            joint(u"xxx")

    * 命令参数转化规则:

        * CPObject = str ，Double3 = （x,y,z）， Matrix = (x,x,x,..*16)

    * 更加方便的创建节点的方法:
        >>> cc.createNode.transform()
        transform(u"transform")

    * mel方法访问:
        >>> cc.mel.SmoothSkinWeights()
        None
    * 事件引擎:
        >>> class printDg(cevent.Dg):
        ...     def createNode(self, node):
        ...         print(node)
        ...     def removeNode(self, node):
        ...         print(node)

        >>> obj = printDg()

        >>> cc.createNode.transform()
        transform1 << 打印
        transform(u'transform1')

    * 工具:
        >>> ctl.decode("你好世界")
        u'你好世界'
        >>> ctl.MayaObjectData(u"time1")
        <CPMel.tool.MayaObjectData object at 0x0000000053CB32E8>
        >>> ctl.undoBlock(xxx type = func)# Qt撤销的实现
        xxx type = func

    * 视频版教程:	https://www.aboutcg.org/courseDetails/1031/introduce
    * 2.5版本更新 ：
        * 使用了预编译脚本优化了文件体积
        * 修复了一些BUG
"""
from . import initializeMaya

import os
import maya.cmds

MAYAINDEX = int(maya.cmds.about(v=True))

ISDEBUG = True
try:
    PATH = os.path.dirname(os.path.abspath(__file__))
    if type(PATH) == str:
        try:
            PATH = PATH.decode("utf8")
        except UnicodeDecodeError:
            try:
                PATH = PATH.decode("gbk")
            except UnicodeDecodeError:
                try:
                    PATH = PATH.decode("GB18030")
                except UnicodeDecodeError:
                    try:
                        PATH = PATH.decode("GB2312")
                    except UnicodeDecodeError:
                        PATH = unicode(PATH)
    PATH = PATH.encode("utf8").decode("utf8")
except:
    PATH = os.path.dirname(os.path.abspath(__file__))

MAYAPLUG = u'%s\\mayaPlug' % PATH
from . import mayaPlug
from . import core
from . import api
from . import cmds
from . import event
from . import ui
from . import tool
# DELETE #
if ISDEBUG:
    reload(mayaPlug)
    reload(core)
    reload(api)
    reload(cmds)
    reload(event)
    reload(ui)
    reload(tool)
# \DELETE #
cmds.upcommands()
maya.cmds.pluginInfo(cc=cmds.upcommands)
del maya