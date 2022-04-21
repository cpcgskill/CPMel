#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/12/7 2:46
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
config_obj = None
def get(key, _def):
    if hasattr(config_obj, key):
        return getattr(config_obj, key)
    return _def
