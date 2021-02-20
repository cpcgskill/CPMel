#!/usr/bin/python
# -*-coding:utf-8 -*
u"""
:创建时间: 2020/5/18 23:57
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
"""
import os
import sys
from .. import PATH
import maya.utils as utils
import traceback
from .. import ISDEBUG


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


class CPMelErrorBase(Exception):
    def __init__(self, *args):
        self.args = [decode(i) for i in args]

    def getNews(self, exceptionType, exceptionObject, traceBack):
        return self.__class__.__name__ + u" CPMEL<" + PATH + u"> : " + u"".join(self.args)

    def __unicode__(self):
        return u"".join(self.args)


class CPMelScriptError(CPMelErrorBase):
    def getNews(self, exceptionType, exceptionObject, traceBack):
        tbStack = traceback.extract_tb(traceBack)
        # format like MEL error with line number
        if tbStack:
            file, line, func, text = tbStack[-1]
            result = u'%s: file %s line %s: %s' % (exceptionType.__name__, file, line, u"".join(self.args))
        else:
            result = u''.join(self.args)
        return result


class CPMelToolError(CPMelErrorBase):
    def getNews(self, exceptionType, exceptionObject, traceBack):
        return u"".join(self.args)


#
# global exceptionT
# global exceptionO
# global traceBa


class CPMelError(CPMelErrorBase):
    def getNews(self, exceptionType, exceptionObject, traceBack):
        strs = list()
        strs.append(exceptionObject.__class__.__name__ + u" : ")
        for i in exceptionObject.args:
            strs.append(u"    " + i)
        i = 1
        while traceBack:
            strs.append(u"Stack {}:".format(i))
            tracebackCode = traceBack.tb_frame.f_code
            tb_lineno = traceBack.tb_lineno
            co_filename = tracebackCode.co_filename
            co_name = tracebackCode.co_name
            if os.path.isfile(co_filename):
                try:
                    with open(co_filename, "r") as f:
                        lines = f.readlines()
                        code = u"".join(
                            [decode(t) for t in lines[max(tb_lineno - 3, 0):min(tb_lineno + 3, len(lines) - 1)]])

                        strs.append(u"    file <{}>  object {} line {}:".format(co_filename,
                                                                                co_name,
                                                                                tb_lineno)
                                    )
                        fgx = "-" * 120
                        strs.append(fgx)
                        strs.append(code)
                        strs.append(fgx)
                except:
                    strs.append(u"    file <{}>  object {} line {}:".format(co_filename,
                                                                            co_name,
                                                                            tb_lineno))
            else:
                strs.append(u"    file <{}>  object {} line {}:".format(co_filename,
                                                                        co_name,
                                                                        tb_lineno))
            traceBack = traceBack.tb_next
            i += 1
        return u'\n'.join([decode(i) for i in strs])


Back = None


def formatGuiException(exceptionType, exceptionObject, traceBack, detail=2):
    global Back
    Back = traceBack
    if isinstance(exceptionObject, CPMelErrorBase):
        try:
            return exceptionObject.getNews(exceptionType, exceptionObject, traceBack)
        except:
            pass
    else:
        try:
            strs = list()
            strs.append(exceptionObject.__class__.__name__ + u" : ")
            for i in exceptionObject.args:
                strs.append(u"    " + decode(i))
            i = 1
            while traceBack:
                strs.append(u"Stack {}:".format(i))
                tracebackCode = traceBack.tb_frame.f_code
                tb_lineno = traceBack.tb_lineno
                co_filename = tracebackCode.co_filename
                co_name = tracebackCode.co_name
                if os.path.isfile(co_filename):
                    try:
                        with open(co_filename, "r") as f:
                            lines = f.readlines()
                            code = u"".join([decode(t) for t in
                                             lines[max(tb_lineno - 3, 0):min(tb_lineno + 3, len(lines) - 1)]])

                            strs.append(u"    file <{}>  object {} line {}:".format(co_filename,
                                                                                    co_name,
                                                                                    tb_lineno)
                                        )
                            fgx = "-" * 120
                            strs.append(fgx)
                            strs.append(code)
                            strs.append(fgx)
                    except:
                        strs.append(u"    file <{}>  object {} line {}:".format(co_filename,
                                                                                co_name,
                                                                                tb_lineno))
                else:
                    strs.append(u"    file <{}>  object {} line {}:".format(co_filename,
                                                                            co_name,
                                                                            tb_lineno))
                traceBack = traceBack.tb_next
                i += 1
            return u'\n'.join([decode(i) for i in strs])
        except:
            pass
    return maya_formatGuiException(exceptionType, exceptionObject, traceBack, detail)


#
#
# if not ISDOC:
if utils._formatGuiException.__module__ != __name__:
    maya_formatGuiException = utils._formatGuiException
    utils.formatGuiException = formatGuiException
    utils._formatGuiException = formatGuiException
# else:
#     pass
#
#
# def init():
#     global maya_formatGuiException
#     maya_formatGuiException = utils._formatGuiException
#     utils.formatGuiException = formatGuiException
#
#
#
# def uninit():
#     global maya_formatGuiException
#     utils._formatGuiException = maya_formatGuiException
#     utils.formatGuiException = maya_formatGuiException
