# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/16 18:06
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import sys
if sys.version_info.major == 2:
    from collections import Iterable, Callable
else:
    from collections.abc import Iterable, Callable

from cpapi.all import (MUuid,
                       MVector, MPoint, MMatrix,
                       MFloatVector, MFloatPoint, MFloatMatrix,
                       MEulerRotation,
                       MDagPath)
import maya.OpenMaya as om1

from cpmel.exc import *


def m_uuid_to_melobject(i):
    return i.asString()


def m_vector_to_melobject(v):
    return v.x, v.y, v.z


def m_point_to_melobject(p):
    if p.w == 1:
        return p.x, p.y, p.z
    else:
        return p.x, p.y, p.z, p.w


def m_matrix_to_melobject(m):
    return tuple((m(r, c) for r in range(4) for c in range(4)))


def m_euler_rotation_to_melobject(e):
    return e.x, e.y, e.z


def m_dag_path_to_melobject(p):
    return p.fullPathName()


def object_type_to_melobject(n):
    return n.__melobject__()


def ui_to_melobject(ui):
    return ui.__melobject__()


# 类型编码表
type_conv_table = {
    om1.MUuid: m_uuid_to_melobject,
    MUuid: m_uuid_to_melobject,

    om1.MPoint: m_point_to_melobject,
    om1.MFloatPoint: m_point_to_melobject,
    MPoint: m_point_to_melobject,
    MFloatPoint: m_point_to_melobject,

    om1.MVector: m_vector_to_melobject,
    om1.MFloatVector: m_vector_to_melobject,
    MVector: m_vector_to_melobject,
    MFloatVector: m_vector_to_melobject,

    om1.MMatrix: m_matrix_to_melobject,
    om1.MFloatMatrix: m_matrix_to_melobject,
    MMatrix: m_matrix_to_melobject,
    MFloatMatrix: m_matrix_to_melobject,

    om1.MEulerRotation: m_euler_rotation_to_melobject,
    MEulerRotation: m_euler_rotation_to_melobject,

    om1.MDagPath: m_dag_path_to_melobject,
    MDagPath: m_dag_path_to_melobject,

    # BaseType: object_type_to_melobject,
    # UI: ui_to_melobject,
}

# 白名单
whitelist = {
    bytes,
    str,
    int,
    float,
    bool,
    type(None),
}
if sys.version_info.major == 2:
    whitelist.add(unicode)
    whitelist.add(long)


def arg_conv(arg):
    arg_t = type(arg)
    if arg_t in whitelist:
        return arg
    # if issubclass(arg_t, BaseType):
    #     return object_type_to_melobject(arg)
    conv_func = type_conv_table.get(arg_t)
    if conv_func is not None:
        return conv_func(arg)
    if hasattr(arg, '__melobject__'):
        return arg.__melobject__()
    if isinstance(arg, Iterable):
        return [arg_conv(i) for i in arg]
    if isinstance(arg, Callable):
        return arg
    raise ArgConvTypeException("args {}: {}".format(type(arg), arg))


def kwarg_conv(arg):
    arg_t = type(arg)
    if arg_t in whitelist:
        return arg
    # if issubclass(arg_t, BaseType):
    #     return object_type_to_melobject(arg)
    conv_func = type_conv_table.get(arg_t)
    if conv_func is not None:
        return conv_func(arg)
    if hasattr(arg, '__melobject__'):
        return arg.__melobject__()
    if isinstance(arg, Iterable):
        return [kwarg_conv(i) for i in arg]
    if isinstance(arg, Callable):
        return arg
    raise ArgConvTypeException("kwargs {}: {}".format(type(arg), arg))


def args_conv(args):
    return [arg_conv(i) for i in args]


def kwargs_conv(kwargs):
    return {k: kwarg_conv(arg) for k, arg in kwargs.items()}


_str_t = type('')


def ret_conv(ret):
    if isinstance(ret, _str_t):
        try:
            return new_object(ret)
        except CPMelException as ex:
            return ret

    # if isinstance(ret, tuple) and len(ret) == 3 and tuple((type(i) for i in ret)) == (float, float, float):
    if isinstance(ret, tuple) and len(ret) == 3:
        return MVector(ret[0], ret[1], ret[2])
    if isinstance(ret, list):
        return [ret_conv(i) for i in ret]
    return ret


def ui_ret_conv(ret):
    if isinstance(ret, _str_t):
        return UI(ret)
    return ret


from cpmel._object_types.core import new_object, UI

if __name__ == "__main__":
    print(list(
        args_conv([1, 2, MFloatPoint(1, 1, 1), MMatrix.newMatrix([
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 1],
        ])])
    ))

    print(
        kwargs_conv({
            "n": "wing",
            "tv": [MVector(1, 1, 1), MVector(1, 1, 1)],
            "rgb": MFloatPoint(1, 1, 1)
        })
    )
