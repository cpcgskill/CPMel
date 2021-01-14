#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/9 11:01
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
*关于本库:
    本库基于CPMel2.5版本开发请确保你的环境里有这个库
    :下载链接: https://www.cpcgskill.com/cpmel
    本库的设定是可以以尽可能快的速度完成界面开发。
    以上确认需要使用这个库之后往下

*一个简单的案例:
from CPMel_Form import build, item
def test(*args):
    print args
ui = (
    (item.Text, u"Test1"),
    (item.Select, u"Test1"),
    (item.SelectList, ),
)
build(u'TestAPP', form=ui, func=test)
*ui元组:
    从上面可以看到ui变量中没一个元素都是一个元组其中第一个都是CPMel_Form.item模块下的属性这个是用来指定构建什么组件的,
    例如item.Text将会构建一个文本输入框具体见最后介绍
    而之后的参数皆为参数
    例如(item.Text, u"Test1")中u“Test1”就会指定默认值
*build函数:
    从上面可以看到build提供了将一个元组转化为界面的功能
    *以下是build函数的介绍：
        build函数提供将表单(列表 or 元组)编译为界面的功能

        :param icon: 图标路径
        :param title: 标题
        :param form: 表单
        :param func: 执行函数 func(表单结果1, 表单结果2, ...)
        :return:
*build函数中的func:
    输入的执行函数会在用户对表单填充完成之后由用户主动执行。
    这个函数需要接受与输入的表单对应的参数，每一个组件提供一个参数。
    每个组件对应什么值见最后
*组件:
    在CPMel_Form中每一个组件对应一个窗口组件与执行函数参数以下为对应列表：
    item.Text 一个文本输入框 unicode字符串  参数 可选的默认字符串
    item.Select 一个接受选择的文本输入框 unicode字符串 参数 可选的默认字符串
    item.SelectList 一个接受选择列表的多行文本输入框 unicode字符串列表 参数 无
    item.Is 一个单选按钮 True or False 参数 无
"""
import os

DEBUG = False
PATH = os.path.dirname(os.path.abspath(__file__))

import CPMel_Form.item as item
import CPMel_Form.core as core

if DEBUG:
    reload(item)
    reload(core)
from CPMel_Form.core import build
import CPMel_Form.item as item
