#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/10 22:16
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import __builtin__

import imp
import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
file_types = [ft for ft, g, t in imp.get_suffixes()]


def findPackage(name="", root=PATH):
    u"""
    查找在root下的名为name的包

    :param name:
    :param root:
    :return:
    """
    package_path = u"%s/%s/__init__.py" % (root, name)
    if os.path.isfile(package_path):
        return package_path


def findModule(name="", root=PATH):
    u"""
    查找在root下的名为name的模块

    :param name:
    :param root:
    :return:
    """
    module_path = u"%s/%s" % (root, name)
    for t in file_types:
        if os.path.isfile(module_path + t):
            return module_path + t


# def CPCLI_GetModule(name):
def find(name="", root=PATH):
    u"""
    查找在root下的名为name的包或者模块

    :param name:
    :param root:
    :return:
    """
    path = findPackage(name=name, root=root)
    if path is None:
        path = findModule(name=name, root=root)
    return path


def finds(name="", root=PATH):
    u"""
    查找root下的name模块，name可能是这样的"xxx.xxx.xxx"所以返回一个这样的列表[(模块名称:xxx.xxx, 模块路径:XXX:/xxx)...]

    :param name:
    :param root:
    :return:
    """
    names = name.split(".")
    paths = list()
    names_len = len(names) - 1
    for ID, i in enumerate(names):
        if ID >= names_len:
            this_path = find(i, root)
        else:
            this_path = findPackage(i, root)
        if this_path is None:
            return None
        paths.append(this_path)
        root = os.path.dirname(os.path.abspath(this_path))
    return paths


__imp__ = __builtin__.__import__


def importwrap(fn):
    def _(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except:
            return __imp__(*args, **kwargs)

    return _


@importwrap
def CPCLI_Imp__import__(name, globals={}, locals={}, fromlist=[], level=-1):
    if level > 0:
        return __imp__(name, globals, locals, fromlist, level)
    if name in sys.modules:
        return __imp__(name, globals, locals, fromlist, level)
    # 发起导入的模块名称
    this_module_name = globals[u"__name__"]

    modules = list()
    module = None
    # 发起导入的模块路径
    if u"__file__" in globals:
        this_module_path = os.path.dirname(os.path.abspath(globals[u"__file__"]))
        if not PATH in this_module_path:
            return __imp__(name, globals, locals, fromlist, level)
        paths = finds(name, this_module_path)
        if paths is None:
            paths = finds(name, PATH)
            if paths is None:
                return __imp__(name, globals, locals, fromlist, level)
            else:
                module = sys.modules[__name__]
                names = name.split(u".")
                for ID, p in enumerate(paths):
                    n = names[:ID + 1]
                    n.insert(0, __name__)
                    n = u".".join(n)
                    if n in sys.modules:
                        _module = sys.modules[n]
                    else:
                        _module = imp.load_source(n, p)
                    if not module is None:
                        setattr(module, names[ID], _module)
                    module = _module
                    modules.append(module)
        else:
            if u"__init__.py" in globals[u"__file__"]:
                this_group_name = this_module_name
            else:
                this_group_name = u".".join(this_module_name.split(u".")[:-1])
            print name, ">>", this_group_name, ">>", globals[u"__file__"]
            names = name.split(u".")
            for ID, p in enumerate(paths):
                n = names[:ID + 1]
                n.insert(0, this_group_name)
                n = u".".join(n)
                if n in sys.modules:
                    _module = sys.modules[n]
                else:
                    _module = imp.load_source(n, p)
                if not module is None:
                    setattr(module, names[ID], _module)
                module = _module
                modules.append(module)
    else:
        paths = finds(name, PATH)
        if paths is None:
            return __imp__(name, globals, locals, fromlist, level)
        module = sys.modules[__name__]
        names = name.split(u".")
        for ID, p in enumerate(paths):
            n = names[:ID + 1]
            n.insert(0, __name__)
            n = u".".join(n)
            if n in sys.modules:
                _module = sys.modules[n]
            else:
                _module = imp.load_source(n, p)
            if not module is None:
                setattr(module, names[ID], _module)
            module = _module
            modules.append(module)
    # print modules, ">>", fromlist
    # 问题在这之后
    if fromlist is None:
        return modules[0]
    for i in fromlist:
        if i == u"*":
            pass
        elif not hasattr(module, i):
            p = find(i, os.path.dirname(os.path.abspath(module.__file__)))
            n = u"%s.%s" % (module.__name__, i)
            if p is None:
                raise ImportError(u"找不到对象 %s" % str(i))
            m = imp.load_source(n, p)
            setattr(module, i, m)

    return modules[-1]


__builtin__.__import__ = CPCLI_Imp__import__
