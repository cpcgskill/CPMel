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

mode = '''
@node.commandWrap
def <<DEF>>(*args, **kwargs):
    u"""
    :rtype: list|str|basestring|DagNode|AttrObject|ArrayAttrObject|Components1Base
    """
    return cmds.<<DEF>>(*args, **kwargs)'''
uimode = '''
@node.uiCommandWrap
def <<DEF>>(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.<<DEF>>(*args, **kwargs)'''
fn_str_s = list()
obj_names = list()
uicmds = set(names.windows.Windows) | set(names.windows.Panels) | set(names.windows.Controls) | set(
    names.windows.Layouts) | set(names.windows.Menus) | set(names.windows.Misc_UI)
cmdss = ({i for i in dir(cmds) if re.match(r"__", i) is None} - uicmds)
print ("joint" in cmdss)
for name in cmdss:
    add_def_name_str = re.sub(r"<<DEF>>", name, mode)
    fn_str_s.append(add_def_name_str)
    obj_names.append(name)

for name in uicmds:
    add_def_name_str = re.sub(r"<<DEF>>", name, uimode)
    fn_str_s.append(add_def_name_str)
    obj_names.append(name)

fn_strs = ''.join(fn_str_s)
all_strs = "__all__ = [%s]" % (', '.join(['"%s"' % i for i in obj_names]))
out_str = '\n'.join([fn_strs, all_strs])

with codecs.open(PATH + u"/cmdsfn.txt", 'w', 'UTF-8') as f:
    print u"正确执行", fn_str_s.__len__()
    f.write(out_str)
# # flags = [i for i in cmds.help(name).split('\n') if len(i) > 0 and not re.match(r'.*?-.*?-', i) is None]
# # i = flags[0]
# # sp_strs = i.split()
# def close():
#     print "close"
# win = cmds.window(cc = "close()")
#
# cmds.showWindow(win)
