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
import maya.cmds as cmds
from .error import CPMelErrorBase, CPMelScriptError, CPMelToolError, CPMelError



def defAddCommandList(doIt, undoIt):
    u"""
    将两个函数添加到命令队列里

    :param doIt:
    :param undoIt:
    :return:
    """
    if callable(doIt) and callable(undoIt):
        try:
            cmds.CPMeldoIt(d = id(doIt), ud = id(undoIt))
        except Exception as ex:
            raise CPMelError(u"添加命令错误")
        return
    else:
        raise CPMelError(u"doIt 或者 undoIt 是不可执行的对象")



def addCommand(doIt, undoIt):
    u"""
    将两个函数转化为命令并执行

    :param doIt:
    :param undoIt:
    :return:
    """
    if callable(doIt) and callable(undoIt):
        try:
            cmds.CPMeldoIt(d = id(doIt), ud = id(undoIt))
        except Exception as ex:
            raise CPMelError(u"添加命令错误")
        # try:
        return doIt()
        # except Exception as ex:
        #     raise CPMelError(u"执行命令错误 " + decode(ex))
    else:
        raise CPMelError(u"doIt 或者 undoIt 是不可执行的对象")



def addCommands(doIts, undoIts):
    u"""
    将两个函数列表转化为命令并执行

    :param doIt:
    :param undoIt:
    :return:
    """

    def doIt():
        tuple((i() for i in doIts if callable(i)))

    def undoIt():
        tuple((i() for i in undoIts if callable(i)))

    try:
        cmds.CPMeldoIt(d = id(doIt), ud = id(undoIt))
    except Exception as ex:
        raise CPMelError(u"添加命令错误")
    # try:
    return doIt()
    # except Exception as ex:
    #     raise CPMelError(u"执行命令错误 " + str(ex))



class Command(object):
    u"""
    命令类
    示例：
    class CommandTest(Command):
        def doIt(self, *args, **kwargs):
            print "doIt"

        def redoIt(self, *args, **kwargs):
            print "redoIt"
            return None

        def undoIt(self, *args, **kwargs):
            print "undoIt"

    """
    isundo = True

    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)
        if self.isundo:
            self.doIt(*args, **kwargs)
            return addCommand(self.redoIt, self.undoIt)
        else:
            return self.doIt(*args, **kwargs)

    def doIt(self, *args, **kwargs):
        u"""
        执行

        :param args:
        :param kwargs:
        :return:
        """
        pass

    def redoIt(self, *args, **kwargs):
        u"""
        重做

        :param args:
        :param kwargs:
        :return:
        """
        pass

    def undoIt(self, *args, **kwargs):
        u"""
        撤销

        :param args:
        :param kwargs:
        :return:
        """
        pass
