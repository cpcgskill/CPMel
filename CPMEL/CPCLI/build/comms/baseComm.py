#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/10/2 15:32
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
from ..comms import comm


@comm("delete")
def delete(string):
    u"""
    删除命令

    :param string:
    :return:
    """
    return u""


@comm("newcode")
def newCode(string=u""):
    u"""
    生成代码的代码命令

    :param string:
    :return:
    """
    gl_sp = dict()
    loc_sp = dict()
    exec (string, gl_sp, loc_sp)
    try:
        new_code_func = loc_sp["newCode"]
    except KeyError:
        new_code_func = lambda *args: ""
    try:
        return new_code_func()
    except Exception:
        return ""
