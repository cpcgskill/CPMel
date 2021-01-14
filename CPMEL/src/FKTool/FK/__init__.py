# !/usr/bin/python
# -*-coding:utf-8 -*
u"""
>>> 创建时间
    2020-11-15 09:41:44
>>> 作者
    苍之幻灵

本模块使用newnode开发
newnode作者
    苍之幻灵
苍之幻灵主页
    www.cpcgskill.com
苍之幻灵QQ
    2921251087
苍之幻灵爱发电
    https://afdian.net/@Phantom_of_the_Cang
苍之幻灵aboutcg
    https://www.aboutcg.org/teacher/54335
苍之幻灵bilibili
    https://space.bilibili.com/351598127
"""

from .FK import FK


def connect(out_object, in_object):
    o = FK(start_str=u"%sto%s_" % (str(out_object), str(in_object)))
    o.tocpmel()
    o.connect(out_object, in_object)
