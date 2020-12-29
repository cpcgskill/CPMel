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
from ..api import OpenMayaUI

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
except ImportError:
    try:
        from PySide2.QtGui import *
        from PySide2.QtCore import *
        from PySide2.QtWidgets import *
    except ImportError:
        from PySide.QtGui import *
        from PySide.QtCore import *

try:
    from shiboken2 import *
except ImportError:
    from shiboken import *
try:
    mui = wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QWidget)
except:
    mui = None

deleteWidget = delete

class CPwindow(QWidget):
    @staticmethod
    def newMui():
        win = cmds.window()
        return wrapInstance(long(OpenMayaUI.MQtUtil.findWindow(win)), QWidget)

    def __init__(self):
        self.maya_window = self.newMui()
        self._main_layout = QVBoxLayout(self.maya_window)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        super(CPwindow, self).__init__()
        self._main_layout.addWidget(self)
        self.main_layout = QVBoxLayout(self)

    def show(self):
        super(CPwindow, self).show()
        self.maya_window.show()

    def close(self):
        super(CPwindow, self).close()
        self.maya_window.close()

    def setWindowTitle(self, p_str):
        self.maya_window.setWindowTitle(p_str)

    def windowTitle(self):
        return self.maya_window.windowTitle()

    def setWindowIcon(self, icon):
        return self.maya_window.setWindowIcon(icon)

    def windowIcon(self):
        return self.maya_window.windowIcon()

    def resize(self, size):
        self.maya_window.resize(size)

    def size(self):
        return self.maya_window.size()

    def paintEvent(self, event):
        super(CPwindow, self).resize(self.maya_window.size())

    def deleteWindow(self):
        super(CPwindow, self).close()
        delete(self.maya_window)


class CPQWindow(QWidget):
    u"""
    由CPMel重建的QWidget对象可以自动的将自身设置为Maya主窗口的子对象

    """

    def __init__(self, *args):
        super(CPQWindow, self).__init__(*args)
        self.setParent(mui)
        self.setWindowFlags(Qt.Window)
        self.main_layout = QVBoxLayout(self)

    def deleteWindow(self):
        super(CPQWindow, self).close()
        delete(self)


class CPQWidget(QWidget):
    u"""
    对CPQWindow的重写
    不再构建self.main_layout
    """

    def __init__(self, *args):
        super(CPQWidget, self).__init__(*args)
        self.setParent(mui)
        self.setWindowFlags(Qt.Window)

    def deleteWindow(self):
        super(CPQWidget, self).close()
        delete(self)


class FrameBlock(QWidget):
    u"""
    可折叠框架实现

    """

    class Bn(QPushButton):
        def __init__(self, *args):
            super(FrameBlock.Bn, self).__init__()
            self.__is_turn_on = False

            def _(*args):
                self.__is_turn_on = not self.__is_turn_on

            self.clicked.connect(_)
            self.setStyleSheet("text-align: left;")
            self.setMaximumHeight(20)

        def setIsTurnOn(self, bool):
            self.__is_turn_on = bool

        def isTurnOn(self):
            return self.__is_turn_on

    class Block(QWidget):
        def __init__(self, widget=QWidget):
            super(FrameBlock.Block, self).__init__()
            self.main_layout = QVBoxLayout(self)
            self.main_layout.addWidget(widget)

        def paintEvent(self, event):
            super(FrameBlock.Block, self).paintEvent(event)
            p = QPainter(self)
            p.setPen(Qt.NoPen)
            p.setBrush(QBrush(QColor(0, 0, 0, 15)))
            p.drawRoundRect(self.rect(), 5, 5)
            p.end()

    def __init__(self, name, widget, status=False):
        u"""


        :param name: 标题
        :param widget: QWidget 对象
        :param status: 默认状态
        """
        super(FrameBlock, self).__init__()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.__bn = FrameBlock.Bn()
        self.__bn.setIsTurnOn(status)
        self.name = name
        self.__bn.clicked.connect(self.upwidget)
        self.main_layout.addWidget(self.__bn)
        self.widget = FrameBlock.Block(widget)
        self.main_layout.addWidget(self.widget)
        self.upwidget()

    def unfold(self):
        self.__bn.setIsTurnOn(True)
        self.upwidget()

    def fold(self):
        self.__bn.setIsTurnOn(False)
        self.upwidget()

    def upwidget(self, *args):
        if self.__bn.isTurnOn():
            self.__bn.setText(self.name)
            self.widget.show()
        else:
            self.__bn.setText(self.name + u"...")
            self.widget.close()


def getFileName():
    u"""
    获得文件路径

    :return: unicode is None
    """
    path = QFileDialog.getOpenFileName()
    if len(path) < 3:
        return None
    return path


def getDirectoryName():
    u"""
    获得文件夹路径

    :return: unicode is None
    """
    path = QFileDialog.getExistingDirectory()
    if len(path) < 3:
        return None
    return path


def input(title=u'输入', message=u'>>>', text=u''):
    u"""
    创建一个接受字符串输入的输入框

    :param title: 标题
    :param message: 消息
    :param text: 默认参数
    :return: unicode is None
    """
    v, is_ok = QInputDialog.getText(mui, title, message, text)
    if is_ok:
        return v
    return None


def inputInt(title=u'输入', message=u'>>>', text=0):
    u"""
    创建一个接受整数输入的输入框

    :param title: 标题
    :param message: 消息
    :param text: 默认参数
    :return: unicode is None
    """
    v, is_ok = QInputDialog.getInt(mui, title, message, text)
    if is_ok:
        return v
    return None


def inputDouble(title=u'输入', message=u'>>>', text=0.0):
    u"""
    创建一个接受浮点输入的输入框

    :param title: 标题
    :param message: 消息
    :param text: 默认参数
    :return: unicode is None
    """
    v, is_ok = QInputDialog.getDouble(mui, title, message, text)
    if is_ok:
        return v
    return None


def inputFloat(title=u'输入', message=u'>>>', text=0.0):
    u"""
    创建一个接受浮点输入的输入框

    :param title: 标题
    :param message: 消息
    :param text: 默认参数
    :return: unicode is None
    """
    return inputDouble(title, message, text)


def inputMultiLineText(title=u'输入', message=u'>>>', text=u''):
    u"""
    创建一个接受字符串输入的多行输入框

    :param title: 标题
    :param message: 消息
    :param text: 默认参数
    :return: unicode is None
    """
    v, is_ok = QInputDialog.getMultiLineText(mui, title, message, text)
    if is_ok:
        return v
    return None


def confirm(title=u'确认', message=u''):
    u"""
    确认对话框

    :param title: 标题
    :param message: 消息
    :return: bool
    """
    reply = QMessageBox.question(mui, title, message,
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.StandardButton.No:
        return False
    else:
        return True
