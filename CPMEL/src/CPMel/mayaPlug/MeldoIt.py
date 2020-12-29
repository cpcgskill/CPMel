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
import maya.api.OpenMaya as om
import sys
import ctypes

if not hasattr(sys, "cpmel_data"):
    sys.cpmel_data = dict()

maya_useNewAPI = True


class CPMeldoIt(om.MPxCommand):
    doIt_label = "d"
    undoIt_label = "ud"
    doIt_label_long = "doIt"
    undoIt_label_long = "undoIt"
    # is_copy = True

    doIt_def = False
    undoIt_def = False

    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def cmdCreator():
        return CPMeldoIt()

    def doIt(self, args):
        arg_data = om.MArgDatabase(syntaxCreator(), args)
        if arg_data.isFlagSet(self.doIt_label_long) and arg_data.isFlagSet(self.undoIt_label_long):
            doIt_id = long(arg_data.flagArgumentString(self.doIt_label_long, 0))
            undoIt_id = long(arg_data.flagArgumentString(self.undoIt_label_long, 0))
            self.doIt_def = ctypes.cast(doIt_id, ctypes.py_object).value
            self.undoIt_def = ctypes.cast(undoIt_id, ctypes.py_object).value
        else:
            om.MGlobal.displayError('No doItComm and undoItComm')
            return

    def redoIt(self):
        if self.doIt_def and self.undoIt_def:
            self.doIt_def()
        else:
            om.MGlobal.displayError('No doItComm and undoItComm')
            return

    def undoIt(self):
        if self.doIt_def and self.undoIt_def:
            self.undoIt_def()
        else:
            om.MGlobal.displayError('No doItComm and undoItComm')
            return

    def isUndoable(self):
        return True


def syntaxCreator():
    syntax = om.MSyntax()
    syntax.addFlag(CPMeldoIt.doIt_label, CPMeldoIt.doIt_label_long, syntax.kString)
    syntax.addFlag(CPMeldoIt.undoIt_label, CPMeldoIt.undoIt_label_long, syntax.kString)
    return syntax


CPMeldoIt_Name = None


def initializePlugin(mobject):
    global CPMeldoIt_Name
    comm_name = unicode(hash(str(mobject))).replace(u"-", u"_")
    CPMeldoIt_Name = u'CPMeldoIt_' + comm_name
    sys.cpmel_data[u"CPMeldoIt"] = CPMeldoIt_Name
    mplugin = om.MFnPlugin(mobject, "Phantom of the Cang", "0.1")
    try:
        mplugin.registerCommand(CPMeldoIt_Name, CPMeldoIt.cmdCreator, syntaxCreator)
    except:
        sys.stderr.write("Failed to register command:CPMeldoIt")
        raise


def uninitializePlugin(mobject):
    mplugin = om.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(CPMeldoIt_Name)
    except:
        sys.stderr.write("Failed to unregister command:CPMeldoIt")
        raise
