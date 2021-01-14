#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/9 11:03
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from functools import partial

import CPMel.cmds as cc
from CPMel.tool import decode, undoBlock
from CPMel.ui import *

class Object(QWidget):
    def __init__(self):
        super(Object, self).__init__()

    def run(self):
        return object


class Text(Object):
    def __init__(self, text=u""):
        text = decode(text)
        super(Text, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.text = QLineEdit(text)
        self.main_layout.addWidget(self.text)

    def run(self):
        return self.text.text()


class Select(Object):
    def __init__(self, text=u""):
        text = decode(text)
        super(Select, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.text = QLineEdit(text)
        self.load_bn = QPushButton(u"载入")
        _ = partial(self.load)
        self.load_bn.clicked.connect(lambda *args: _())
        self.main_layout.addWidget(self.text)
        self.main_layout.addWidget(self.load_bn)

    @undoBlock
    def load(self):
        sel = cc.ls(sl=True)
        if len(sel) < 1:
            raise cc.CPMelToolError(u"选择一个物体")
        self.text.setText(str(sel[0]))

    def run(self):
        return self.text.text()


class SelectList(Object):
    def __init__(self):
        super(SelectList, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.texts = QTextEdit()
        self.texts.setMaximumHeight(60)
        self.load_bn = QPushButton(u"载入")
        self.load_bn.clicked.connect(lambda *args: self.load())
        self.main_layout.addWidget(self.texts)
        self.main_layout.addWidget(self.load_bn)

    @undoBlock
    def load(self):
        sel = cc.ls(sl=True)
        self.texts.setText(u"\n".join([str(i) for i in sel]))

    def run(self):
        return self.texts.placeholderText().split("\n")


class Is(Object):
    def __init__(self, info=u"", default_state=False):
        info = decode(info)
        super(Is, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.query = QCheckBox(info, self)
        self.query.setChecked(default_state)
        self.main_layout.addWidget(self.query)

    def run(self):
        return self.query.isChecked()
