#!/usr/bin/python
# -*-coding:utf-8 -*-
import re
import sys
import codecs
import pymel.core
import maya.cmds as cmds

PATH = r'D:\Development\MAYA\CPMEL\CPMEL\src\CPMel\cmds'.replace(u"\\", u"/")
sys.path.append(PATH)


def decode(s=''):
    u"""
    字符串解码函数

    :param s:
    :return:
    """
    if not isinstance(s, basestring):
        try:
            s = str(s)
        except:
            s = unicode(s)
    if type(s) == str:
        try:
            return s.decode("UTF-8")
        except UnicodeDecodeError:
            try:
                return s.decode("GB18030")
            except UnicodeDecodeError:
                try:
                    return s.decode("Shift-JIS")
                except UnicodeDecodeError:
                    try:
                        return s.decode("EUC-KR")
                    except UnicodeDecodeError:
                        return unicode(s)
    return s.encode("UTF-8").decode("UTF-8")


import __command_names as names

head = '''\
#!/usr/bin/python
# -*-coding:utf-8 -*-
import CPMel.cmds.node.nodedata as nodedata
def cp_return_template(*args, **kwargs):
    u""":rtype: list|tuple|str|unicode|basestring|nodedata.DagNode|nodedata.AttrObject|nodedata.ArrayAttrObject|nodedata.Components1Base"""
def cp_ui_return_template(*args, **kwargs):
    u""":rtype: nodedata.UIObject"""
def cp_list_return_template(*args, **kwargs):
    u""":rtype: list[tuple|str|unicode|basestring|nodedata.DagNode|nodedata.AttrObject|nodedata.ArrayAttrObject|nodedata.Components1Base]"""
'''
mode = '''\
<<DEF>> = cp_return_template
'''
uimode = '''\
<<DEF>> = cp_ui_return_template
'''
list_mode = '''\
<<DEF>> = cp_list_return_template
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

with codecs.open(PATH + u"/static_cmds.pyi", 'w', 'UTF-8') as f:
    print u"正确执行", fn_str_s.__len__()
    f.write(decode(head + out_str))
