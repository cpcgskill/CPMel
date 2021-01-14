#!/usr/bin/python
# -*-coding:utf-8 -*-
import re
import codecs
# import init_maya
import maya.cmds as cmds
import __command_names as names

mode = '''
@node.commandWrap
def <<DEF>>(*args, **kwargs):
    u"""
<<DOC>>
    :param args: 
    :param kwargs: 
    :return: 
    """
    return cmds.<<DEF>>(*args, **kwargs)
'''
uimode = '''
@node.uiCommandWrap
def <<DEF>>(*args, **kwargs):
    u"""
<<DOC>>
    :param args: 
    :param kwargs: 
    :return: 
    """
    return cmds.<<DEF>>(*args, **kwargs)
'''
fn_str_s = list()
obj_names = list()
uicmds = set(names.windows.Windows) | set(names.windows.Panels) | set(names.windows.Controls) | set(names.windows.Layouts) | set(names.windows.Menus) | set(names.windows.Misc_UI)
cmdss = ({i for i in dir(cmds) if re.match(r"__", i) is None} - uicmds)
print ("joint" in cmdss)
for name in cmdss:
    try:
        doc = '\n'.join(["    %s" % i for i in cmds.help(name).split('\n')])
    except:
        continue
    else:
        add_doc_str = re.sub(r"<<DOC>>", doc, mode)
        add_def_name_str = re.sub(r"<<DEF>>", name, add_doc_str)
        fn_str_s.append(add_def_name_str)
        obj_names.append(name)

for name in uicmds:
    doc = '\n'.join(["    %s" % i for i in cmds.help(name).split('\n')])
    add_doc_str = re.sub(r"<<DOC>>", doc, uimode)
    add_def_name_str = re.sub(r"<<DEF>>", name, add_doc_str)
    fn_str_s.append(add_def_name_str)
    obj_names.append(name)

fn_strs = '\n'.join(fn_str_s)
all_strs = "__all__ = [%s]"%(', '.join(['"%s"'%i for i in obj_names]))
out_str = '\n'.join([fn_strs, all_strs])


PATH = u''.join(['%s\\'%i for i in __file__.split('\\')][:-1])
with codecs.open(PATH + u"cmdsfn.txt", 'w', 'UTF-8') as f:
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
