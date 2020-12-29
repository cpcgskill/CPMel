#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/10/12 8:56
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
import os
import re
import shutil
import glob
import codecs


PATH = os.path.dirname(os.path.abspath(__file__))
# 有as的正则表达式
# import +[A-Za-z_][A-Za-z0-9._]* +as +[A-Za-z0-9._]+
re_o = re.compile(r"(from|import) +(.*)")

index = 0


def getModeName(root, path):
    if "CPMel_Form" in path:
        print 1
    mode_names = path[len(root) + 1:].split(u"/")
    if mode_names[-1] == u"__init__.py":
        return u".".join(mode_names[:-1])
    else:
        mode_names[-1] = mode_names[-1].split(u".py")[0]
        return u".".join(mode_names)


def build(src_dir=u"", out_dir=u"", name=u"def_name"):
    src_dir = src_dir.replace(u"\\", u"/")
    out_dir = out_dir.replace(u"\\", u"/") + u"/" + name
    shutil.copytree(src_dir, out_dir)
    with open(PATH + u"/static/__init__.py", "rb") as rf:
        with codecs.open(out_dir + u"/__init__.py", "wb") as wf:
            wf.write(rf.read())
    return
    _ = [((root + u"/" + file).replace(u"\\", u"/"), root.replace(u"\\", u"/")) for root, dirs, files in
         os.walk(out_dir) for file in files if u".py" in file]
    mode_dict = {getModeName(out_dir, k): k[len(out_dir):] for k, v in _}
    print 1
    for root, dirs, files in os.walk(out_dir):
        root = root.replace(u"\\", u"/")
        # print("root", root)  # 当前目录路径
        # print("dirs", dirs)  # 当前路径下所有子目录
        # print("files", files)  # 当前路径下所有非目录子文件
        for t in files:
            path = u"%s/%s" % (root, t)
            # print path
            if not re.match(r".*\.py$", path) is None:
                # print path
                with codecs.open(path, "r", encoding="utf-8") as f:
                    string = f.read()

                def _(m):
                    global index
                    index += 1
                    print "ID:", index
                    head = m.string[m.regs[1][0]:m.regs[1][1]]
                    boody = m.string[m.regs[2][0]:m.regs[2][1]]
                    if head == u"import":
                        if boody.find(u" as ") < 0:
                            end = u""
                        else:
                            end = boody[boody.find(u" as "):]
                            boody = boody[:boody.find(u" as ")]
                    else:
                        if boody.find(u" import ") < 0:
                            end = u""
                        else:
                            end = boody[boody.find(u" import "):]
                            boody = boody[:boody.find(u" import ")]
                    boody = boody.replace(u"\r", u"").replace(u"\n", u"")
                    end = end.replace(u"\r", u"").replace(u"\n", u"")
                    # end = m.string[m.regs[3][0]:m.regs[3][1]]
                    if index == 217:
                        pass
                    print path, head, "<<", boody, ">>", end

                    if head == u"from":
                        boody = boody.split(u".")
                        if boody[0] == u"":
                            return u"%s %s %s" % (head, u".".join(boody), end)
                        mode_root = boody[0]
                        if os.path.isfile(u"%s/%s.py" % (out_dir, mode_root)) or \
                                os.path.isfile(u"%s/%s.pyd" % (out_dir, mode_root)) or \
                                os.path.isfile(u"%s/%s.pyc" % (out_dir, mode_root)) or \
                                os.path.isfile(u"%s/%s.pyo" % (out_dir, mode_root)) or \
                                os.path.isfile(u"%s/%s/__init__.py" % (out_dir, mode_root)):
                            boody.insert(0, name)
                        return u"%s %s %s" % (head, u".".join(boody), end)
                    if head == u"import":
                        if end.find(u" as ") == 0:
                            boody = boody.split(u".")
                            mode_root = boody[0]
                            if os.path.isfile(u"%s/%s.py" % (out_dir, mode_root)) or \
                                    os.path.isfile(u"%s/%s.pyd" % (out_dir, mode_root)) or \
                                    os.path.isfile(u"%s/%s.pyc" % (out_dir, mode_root)) or \
                                    os.path.isfile(u"%s/%s.pyo" % (out_dir, mode_root)) or \
                                    os.path.isfile(u"%s/%s/__init__.py" % (out_dir, mode_root)):
                                boody.insert(0, name)
                            return u"%s %s %s" % (head, u".".join(boody), end)
                        else:
                            build_boody = list()
                            for i in re.split(r", *", boody):
                                i = i.split('.')
                                mode_root = i[0]
                                if os.path.isfile(u"%s/%s.py" % (out_dir, mode_root)) or \
                                        os.path.isfile(u"%s/%s.pyd" % (out_dir, mode_root)) or \
                                        os.path.isfile(u"%s/%s.pyc" % (out_dir, mode_root)) or \
                                        os.path.isfile(u"%s/%s.pyo" % (out_dir, mode_root)) or \
                                        os.path.isfile(u"%s/%s/__init__.py" % (out_dir, mode_root)):
                                    build_boody.append(u"import " + name + u"." + u".".join(i) + u'\r\n')
                                    for ID, l in enumerate(i):
                                        build_boody.append(
                                            u".".join(i[:ID + 1]) + u" = __import__(\"" + name + u"." + u".".join(
                                                i[:ID + 1]) + u"\")" + u'\r\n')
                                else:
                                    build_boody.append(u"import " + u".".join(i) + u'\r\n')
                            return u"".join(build_boody)
                    return u"%s %s %s" % (head, boody, end)

                string = re_o.sub(_, string)
                with codecs.open(path, "w", encoding="utf-8") as f:
                    f.write(string)
