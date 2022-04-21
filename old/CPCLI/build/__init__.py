#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/9/29 14:55
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
import sys
import os
import shutil
from . import compileFiles
from . import config
from ..utils import readFile, writeFile, formattedPath, emptyDir

thisPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(thisPath)


# build_dir, build_files_file, out_dir = [os.path.abspath(i) for i in sys.argv[1:]]
def build(src,config_obj=None):
    config.config_obj = config_obj
    src = formattedPath(src)
    files = [formattedPath("%s/%s" % (root, file)) for root, dirs, files in os.walk(src) for file in files]
    for i in files:
        file_type = i.split(u".")[-1]
        if file_type in compileFiles.fileTypes:
            compileFiles.fileTypes[file_type](i)
        else:
            compileFiles.baseFile(i)
