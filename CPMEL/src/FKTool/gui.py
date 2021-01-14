#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/15 20:03
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPMel_Form import build, item
import FKTool.tool as tool

def newgui():
    form = [
        (item.Is, u"为子关节创建控制器", True)
    ]
    build(form=form, title=u"幻灵FK绑定工具", func=tool.main)
