#!/usr/bin/python
# -*-coding:utf-8 -*-
import re
import sys
import codecs
import pymel.core
import maya.cmds as cmds

PATH = r'D:\Development\MAYA\CPMEL\CPMEL\src\CPMel\cmds'.replace(u"\\", u"/")
sys.path.append(PATH)

import __command_names as names
head='''\
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
from . import node
from .node import commandWrap, uiCommandWrap
from . import FrontPackage as cmds
from .node.nodedata import DagNode, AttrObject, ArrayAttrObject, Components1Base, UIObject


def listWrap(fn):
    def _(*args, **kwargs):
        o = fn(*args, **kwargs)
        if o is None:
            return []
        return o

    _.__name__ = fn.__name__
    _.__doc__ = fn.__doc__
    return _

'''
list_mode = '''\
@commandWrap
@listWrap
def <<DEF>>(*args, **kwargs):
    u""":rtype: list"""
    return cmds.<<DEF>>(*args, **kwargs)
'''
mode = '''\
@commandWrap
def <<DEF>>(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.<<DEF>>(*args, **kwargs)
'''
uimode = '''\
@uiCommandWrap
def <<DEF>>(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.<<DEF>>(*args, **kwargs)
'''
fn_str_s = list()
obj_names = set()
uicmds = set(names.windows.Windows) | set(names.windows.Panels) | set(names.windows.Controls) | set(
    names.windows.Layouts) | set(names.windows.Menus) | set(names.windows.Misc_UI)
cmdss = ({i for i in dir(cmds) if re.match(r"__", i) is None} - uicmds)
list_cmdss = [i for i in cmdss if i.find("list") == 0]
cmdss = list(set(cmdss) - set(list_cmdss))

for name in cmdss:
    add_def_name_str = re.sub(r"<<DEF>>", name, mode)
    fn_str_s.append(add_def_name_str)
    obj_names.add(name)
for name in list_cmdss:
    add_def_name_str = re.sub(r"<<DEF>>", name, list_mode)
    fn_str_s.append(add_def_name_str)
    obj_names.add(name)

for name in uicmds:
    add_def_name_str = re.sub(r"<<DEF>>", name, uimode)
    fn_str_s.append(add_def_name_str)
    obj_names.add(name)

fn_strs = ''.join(fn_str_s)
all_strs = "__all__ = [%s]" % (', '.join(['"%s"' % i for i in obj_names]))
out_str = '\n'.join([fn_strs, all_strs])

with codecs.open(PATH + u"/cmdsfn.txt", 'w', 'UTF-8') as f:
    print u"正确执行", fn_str_s.__len__()
    f.write(decode(head + out_str))