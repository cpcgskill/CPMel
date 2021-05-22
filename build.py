#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/10 22:28
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import os
from CPCLI import *
root = os.path.dirname(os.path.abspath(__file__))
try:
    emptyDir(root + u"/build")
except:
    pass
src = root + u"/src"
release_dir = root + u"/build/release"
debug_dir = root + u"/build/debug"
moves_file = root + u"/moves.txt"

moves(src, release_dir, moves_file)
moves(src, debug_dir, moves_file)


class release(object):
    comms = True
    deletedoc = True
    deletezeroline = True


build(release_dir, config_obj=release)
