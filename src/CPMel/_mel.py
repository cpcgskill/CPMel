# -*-coding:utf-8 -*-
"""
:创建时间: 2022/4/18 22:46
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division
import sys
from functools import partial

from maya.mel import eval as maya_eval

from cpmel._args_conv import args_conv, kwargs_conv
from cpmel.exc import *


def _eval(code):
    try:
        return maya_eval(code)
    except RuntimeError as ex:
        raise CPMelException(ex.message)


def _to_array(val):
    return "{%s}" % (",".join((_to_mel(i) for i in val)))


def _to_string(val):
    val = repr(val)
    if val[0] == 'u':
        val = val[1:]
    if val[0] == '"':
        return val
    val = val[1:-1]

    val = val.replace(r"\'", r"'").replace(r'"', r'\"')

    return '"%s"' % val


def _to_int(val):
    return str(val)


def _to_float(val):
    return str(val)


# 类型编码表
type_conv_table = {
    list: _to_array,
    tuple: _to_array,
    set: _to_array,

    float: _to_float,
}

if sys.version_info.major == 2:
    type_conv_table[long] = _to_int
    type_conv_table[int] = _to_int
else:
    type_conv_table[int] = _to_int

if sys.version_info.major == 2:
    type_conv_table[unicode] = _to_string
    type_conv_table[str] = _to_string
else:
    type_conv_table[str] = _to_string


def _to_mel(val):
    typ = type(val)
    if typ in type_conv_table:
        conv_func = type_conv_table[typ]
        return conv_func(val)
    raise CPMelException("无法正确转化输入")


def call_mel_proc(item, *args, **kwargs):
    args = args_conv(args)
    kwargs = kwargs_conv(kwargs)

    args_s = " ".join((_to_mel(i) for i in args))
    kwargs_s = " ".join(("-%s %s" % (k, _to_mel(v)) for k, v in kwargs.items()))
    command_s = "{0} {2} {1};".format(item, args_s, kwargs_s)
    return _eval(command_s)


class Mel(object):
    def __getattr__(self, item):
        f = partial(call_mel_proc, item)
        setattr(self, item, f)
        return f

    def eval(self, code):
        return _eval(code)
