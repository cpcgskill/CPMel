#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/9 11:24
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import CPMel_Form

reload(CPMel_Form)
import CPMel_Form.item

reload(CPMel_Form.item)
from CPMel_Form import build, item


def test(*args):
    print args


ui = (
    (item.Text, u"Test1"),
    (item.Select, u"Test1"),
    (item.SelectList,),
    (item.Is, u"确认", True),
)

build(title=u"CPMel_Form测试", form=ui, func=test)
