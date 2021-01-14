#!/usr/bin/python
# -*-coding:utf-8 -*-
# :创建时间: 2020/5/18 23:57
# :作者: 苍之幻灵
# :我的主页: https://cpcgskill.com
# :QQ: 2921251087
# :爱发电: https://afdian.net/@Phantom_of_the_Cang
# :aboutcg: https://www.aboutcg.org/teacher/54335
# :bilibili: https://space.bilibili.com/351598127
from cpweidgets import CPMel as om


class MItCurveCV(om.MItCurveCV):
    def __init__(self, *args, **kwargs):
        super(MItCurveCV, self).__init__(*args, **kwargs)
        self.__CP_is_start = True

    def __iter__(self):
        self.reset()
        self.__CP_is_start = True
        return self

    def next(self):
        if self.__CP_is_start:
            self.__CP_is_start = False
        else:
            super(MItCurveCV, self).next()
        if self.isDone():
            raise StopIteration
        else:
            item = self
            return item





MDagPathArray(10, MDagPath())
