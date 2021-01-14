#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/14 15:08
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import os
import re
from .utils import readFile, writeFile, formattedPath, emptyDir

re_o = re.compile(r"\s*")

def moves(start_dir, aims_dir, cli_file):
    start_dir = start_dir
    aims_dir = aims_dir
    cli_file = formattedPath(cli_file)
    if os.path.exists(aims_dir):
        emptyDir(aims_dir)
    move_files = [re_o.sub(u"", i) for i in readFile(cli_file).split("\n") if len(i)]
    for i in move_files:
        i_file = formattedPath("%s/%s" % (start_dir, i))
        o_file = formattedPath("%s/%s" % (aims_dir, i))
        o_dir_path = os.path.dirname(o_file)
        if not os.path.exists(o_dir_path):
            os.makedirs(o_dir_path)
        writeFile(readFile(i_file), o_file)
