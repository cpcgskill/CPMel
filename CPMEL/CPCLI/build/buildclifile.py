#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/10 22:51
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import re
re_o = re.compile(r"\s*")
def build(file_path):
    with open(file_path, "r") as f:
        string = f.read()
        return [re_o.sub(u"", i) for i in string.split("\n") if len(i)]
