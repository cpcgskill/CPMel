#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/5 14:35
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import os
import uuid
import hashlib


def decode(s=''):
    u"""
    字符串解码函数

    :param s:
    :type s:str|unicode
    :return:
    :rtype: unicode
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


def readFile(path):
    u"""

    :param path:
    :type path:unicode
    :return:
    :rtype: bytes
    """
    with open(path, "rb") as f:
        return f.read()


def writeFile(path, bytes):
    u"""

    :param path:
    :type path: unicode
    :param bytes:
    :type bytes: bytes|unicode
    :return:
    :rtype: None
    """
    if isinstance(bytes, unicode):
        bytes = bytes.encode(encoding="utf-8")
    with open(path, "wb") as f:
        f.write(bytes)


def formattedPath(path):
    path = decode(path)
    path = path.replace(u"\\", u"/")
    if path[-1] == u"/":
        path = path[:-1]
    return path.replace(u"\\", u"/")


def uid():
    return uuid.uuid4().hex


def uidname():
    return u"_" + uid()


def hashString(string):
    u"""

    :param string:
    :type string: str
    :return:
    """
    md5 = hashlib.md5()
    md5.update(bytes(decode(string).encode("utf-8")))
    return md5.hexdigest()


def mkdir(dirname):
    u"""

    :param dirname:
    :type dirname: str|unicode
    :return:
    """
    dirnames = dirname.split(u"/")
    for i in range(1, len(dirnames)):
        dirname = u"/".join(dirnames[:i + 1])
        if not os.path.isdir(dirname):
            os.mkdir(dirname)


def copyDir(start_dir, aims_dir):
    start_dir = decode(start_dir)
    aims_dir = decode(aims_dir)
    start_dir = start_dir.replace(u"\\", u"/")
    aims_dir = aims_dir.replace(u"\\", u"/")
    mkdir(aims_dir)
    start_dir_path_size = len(start_dir)
    walk = [(decode(root), dirs, files) for root, dirs, files in os.walk(start_dir)]
    for root, dirs, files in walk:
        for dir in dirs:
            dir = decode(dir)
            dir = aims_dir + (u"%s/%s" % (root, dir))[start_dir_path_size:]
            mkdir(dir)
    for root, dirs, files in walk:
        for file in files:
            file = decode(file)
            file = u"%s/%s" % (root, file)
            file = file[start_dir_path_size:]
            writeFile(aims_dir + file, readFile(start_dir + file))


def emptyDir(dir):
    dir = formattedPath(dir)
    walk = [i for i in os.walk(dir)]
    walk.reverse()
    for root, dirs, files in walk:
        for file in files:
            os.remove(formattedPath("%s/%s" % (root, file)))
    for root, dirs, files in walk:
        for dir in dirs:
            os.rmdir(formattedPath("%s/%s" % (root, dir)))


def reDir(dir):
    if os.path.exists(dir):
        emptyDir(dir)
        os.rmdir(formattedPath(dir))
