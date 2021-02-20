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

mode = u'''\
    def <<node>>(self, *args, **kwargs):
        return self(u"<<node>>", *args, **kwargs)'''
strings = list()
nodes = cmds.allNodeTypes(ia=False)
nodes = [i for i in nodes if i.find(u"MASH") != 0]
nodes = [i for i in nodes if i.find(u"xgm") != 0]
nodes = [i for i in nodes if i.find(u"xgen") != 0]
nodes = [i for i in nodes if i.find(u"ai") != 0]
nodes = [i for i in nodes if i.find(u"AI") != 0]
nodes = [i for i in nodes if i.find(u"HIK") != 0]
nodes = [i for i in nodes if i.find(u"Boss") != 0]
nodes = [i for i in nodes if i.find(u"bifrost") != 0]
nodes = [i for i in nodes if len(i) < 20]
nodes = [i for i in nodes if len(i) > 3]

for i in nodes:
    strings.append(re.sub("<<node>>", i, mode))

print(u"\n".join(strings))
