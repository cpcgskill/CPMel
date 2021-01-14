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
class its(object):
    def __init__(self, *args):
        self.__its = tuple(((t for t in i) for i in args))
        self.__obj_size = len(args)

    def __iter__(self):
        return self

    def next(self):
        objs = tuple((i.next() for i in self.__its))
        if len(objs) != self.__obj_size:
            raise StopIteration
        return objs



def MAyyayIt(obj):
    return (obj[i] for i in range(obj.length()))



#
# class MAyyayIt(object):
#     def __init__(self, obj):
#         self.__CP_current_pos = 0
#         self.__obj = obj
#
#     def __iter__(self):
#         self.__CP_current_pos = 0
#         return self
#
#     def next(self):
#         if self.__CP_current_pos < self.__obj.length():
#             item = self.__obj[self.__CP_current_pos]
#             self.__CP_current_pos += 1
#             return item
#         raise StopIteration


class MItForIt(object):
    def __init__(self, obj):
        self.__CP_is_start = True
        self.__obj = obj
        self.__obj.reset()

    def next(self):
        if self.__CP_is_start:
            self.__CP_is_start = False
        else:
            self.__obj.next()
        if self.__obj.isDone():
            raise StopIteration
        else:
            return self.__obj
