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
import functools



def newClass(name, bases, attrs):
    u"""
    构建元类使用此元类的类在创建时自动创建对象

    :param name:
    :param bases:
    :param attrs:
    :return:
    """
    cls = type(name, bases, attrs)
    return cls()



def createClass(name, bases, attrs):
    u"""
    创建器元类
    以此为元类的类在创建时将不会自动调用__init__

    :param name:
    :param bases:
    :param attrs:
    :return:
    """
    cls = type(name, bases, attrs)
    return functools.partial(cls.__new__, cls)
