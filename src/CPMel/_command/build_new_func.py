# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/15 4:50
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import functools
import warnings

from cpmel._args_conv import args_conv, kwargs_conv, ret_conv, ui_ret_conv
import cpmel._command.commands as commands


def new_func_from_command(c):
    @functools.wraps(c)
    def _(*args, **kwargs):
        args = args_conv(args)
        kwargs = kwargs_conv(kwargs)
        ret = c(*args, **kwargs)
        return ret_conv(ret)

    return _


def new_func_from_list_command(c):
    @functools.wraps(c)
    def _(*args, **kwargs):
        args = args_conv(args)
        kwargs = kwargs_conv(kwargs)
        ret = c(*args, **kwargs)
        if ret is None:
            return []
        return ret_conv(ret)

    return _


def new_func_from_ui_command(c):
    @functools.wraps(c)
    def _(*args, **kwargs):
        args = args_conv(args)
        kwargs = kwargs_conv(kwargs)
        ret = c(*args, **kwargs)
        if (not 'q' in kwargs) and (not 'query' in kwargs):
            return ui_ret_conv(ret)
        return ret

    return _


# cmds.pluginInfo(cc = prplug)
# 不知道为啥在maya2016之后执行这个函数性能会下降很多
def new_func_list_from_module(module):
    # def _(v):
    #     if v is None:
    #         return []
    #     return v

    # commands = {t for i in _(mc.pluginInfo(q=True, ls=True))
    #             for t in _(mc.pluginInfo(i, q=True, c=True)) +
    #             _(mc.pluginInfo(i, q=True, cnc=True)) +
    #             _(mc.pluginInfo(i, q=True, ctc=True))}

    # module = globals()
    #
    # cpmel_commands = set(module.keys())
    # for i in commands - cpmel_commands:
    #     try:
    #         module[i] = node.commandWrap(getattr(mc, i))
    #     except KeyError as ex:
    #         warnings.warn("注册新CPMel命令失败！{}\n".format(ex))

    for n, f in commands.commands.items():
        try:
            module[n] = new_func_from_command(f)
        except KeyError as ex:
            warnings.warn("注册新CPMel命令失败！{}\n".format(ex))
    for n, f in commands.list_commands.items():
        try:
            module[n] = new_func_from_list_command(f)
        except KeyError as ex:
            warnings.warn("注册新CPMel命令失败！{}\n".format(ex))
    for n, f in commands.ui_commands.items():
        try:
            module[n] = new_func_from_ui_command(f)
        except KeyError as ex:
            warnings.warn("注册新CPMel命令失败！{}\n".format(ex))
    for n, f in commands.other_commands.items():
        try:
            module[n] = new_func_from_command(f)
        except KeyError as ex:
            warnings.warn("注册新CPMel命令失败！{}\n".format(ex))
