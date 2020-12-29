#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
>>> 创建时间
    2020/7/28 14:34
>>> 作者
    苍之幻灵
>>> 我的主页
    http://www.cpcgskill.com
>>> QQ
    2921251087
>>> 爱发电
    https://afdian.net/@Phantom_of_the_Cang
>>> aboutcg
    https://www.aboutcg.org/teacher/54335
>>> bilibili
    https://space.bilibili.com/351598127
"""
from cpweidgets import CPMel as cc

cc.nodeType( 'camera', derived=True, isTypeName=True )

for i in cc.allNodeTypes(includeAbstract = True):
    try:
        cc.delete(cc.createNode(i))
    except:
        pass