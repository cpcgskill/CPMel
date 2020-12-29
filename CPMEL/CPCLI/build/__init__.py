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
from . import buildclifile
from . import config

thisPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(thisPath)


# build_dir, build_files_file, out_dir = [os.path.abspath(i) for i in sys.argv[1:]]
def main(build_dir, cli_file, out_dir, config_obj = None):
    config.config_obj = config_obj
    build_dir = build_dir.replace("\\", "/")
    cli_file = cli_file.replace("\\", "/")
    out_dir = out_dir.replace("\\", "/")
    build_files = buildclifile.build(cli_file)
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    for i in build_files:
        o_file = out_dir + i
        o_dir_path = os.path.dirname(o_file)
        if not os.path.exists(o_dir_path):
            os.makedirs(o_dir_path)
        file_type = i.split(".")[-1]
        if file_type in compileFiles.fileTypes:
            compileFiles.fileTypes[file_type](build_dir + i, o_file)
        else:
            compileFiles.baseFile(build_dir + i, o_file)
