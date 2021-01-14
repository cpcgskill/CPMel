#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/6/27 14:46
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
import maya.cmds as cmds
import re
mode = '''
    def <<node>>(self, *args, **kwargs):
        return self(u"<<node>>", *args, **kwargs)
'''
strings = list()
for i in cmds.allNodeTypes(ia = False):
    strings.append(re.sub("<<node>>", i, mode))

print("".join(strings))