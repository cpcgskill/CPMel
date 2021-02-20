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
import warnings
# DELETE #
from .. import ISDEBUG

if ISDEBUG:
    from . import node
    from . import FrontPackage
    from . import static_cmds
    from . import AfterPackage
    from . import melproc

    reload(node)
    reload(FrontPackage)
    reload(static_cmds)
    reload(AfterPackage)
    reload(melproc)
# \DELETE #
from . import node
from .node.basedata import *
from .node.nodedata import newObject, Global, Components1Base, Components2Base, Components3Base
from .FrontPackage import *
from .static_cmds import *
from .AfterPackage import *
from ..core import addCommand, Command
from .melproc import mel
from ..core import *


# cmds.pluginInfo(cc = prplug)
# 不知道为啥在maya2016之后执行这个函数性能会下降很多
def upcommands():
    def _(v):
        if v is None:
            return []
        return v

    commands = {t for i in _(cmds.pluginInfo(q=True, ls=True))
                for t in _(cmds.pluginInfo(i, q=True, c=True)) +
                _(cmds.pluginInfo(i, q=True, cnc=True)) +
                _(cmds.pluginInfo(i, q=True, ctc=True))}

    module = globals()

    cpmel_commands = set(module.keys())
    for i in commands - cpmel_commands:
        try:
            module[i] = node.commandWrap(getattr(cmds, i))
        except KeyError as ex:
            warnings.warn(u"注册新CPMel命令失败！" + str(ex) + u"\n")
