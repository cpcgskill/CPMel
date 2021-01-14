#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/9 11:07
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPMel.core import CPMelToolError
from CPMel.tool import decode, undoBlock
from CPMel.ui import *
from CPMel_Form import *

class Main(CPQWindow):
    def __init__(self, icon=PATH + u"/icon.ico", title=u"CPWindow", form=tuple(), func=lambda *args: 0):
        super(Main, self).__init__()
        icon = decode(icon)
        title = decode(title)
        self.func = undoBlock(func)
        self.weidgets = list()
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        for i in form:
            widget = i[0](*(i[1:]))
            self.main_layout.addWidget(widget)
            self.weidgets.append(widget)
        self.main_layout.addStretch(0)
        self.doIt_bn = QPushButton(u"确认表单已填充-执行")
        self.doIt_bn.clicked.connect(undoBlock(self.doIt))
        self.main_layout.addWidget(self.doIt_bn)
        self.main_layout.addWidget(QLabel(u"本窗口界面由CPMel_Form1.0开发"))

    def doIt(self, *args):
        value = [i.run() for i in self.weidgets]
        self.func(*value)

apps = dict()
def build(appname, icon=PATH + u"/icon.ico", title=u"CPWindow", form=tuple(), func=lambda *args: 0):
    u"""
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :param icon: 图标路径
    :param title: 标题
    :param form: 表单
    :param func: 执行函数 func(表单结果1, 表单结果2, ...)
    :return:
    """
    if appname in apps:
        main_widget = apps[appname]
        deleteWidget(main_widget)
    import os
    if not os.path.isfile(icon):
        raise CPMelToolError(u"图标路径不存在")
    main_widget = Main(icon, title, form, func)
    main_widget.show()
    apps[appname] = main_widget