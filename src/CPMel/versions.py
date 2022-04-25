# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/4/25 19:38
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

Alpha, Beta, Rc, R = (0, 100, 200, 300)


def adv_ver_conv(i):
    adv_ver_conv_table = {
        Alpha: 'alpha',
        Beta: 'beta',
        Rc: 'rc',
        R: "r",
    }
    return adv_ver_conv_table[i]


class VersionInfo(object):
    def __init__(self, major, minor, patch, adv_ver=R, adv_ver_index=0):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.adv_ver = adv_ver
        self.adv_ver_index = adv_ver_index

    def to_str(self):
        s = "{}.{}.{}".format(self.major, self.minor, self.patch)
        if self.adv_ver < R:
            s += "-{}.{}".format(adv_ver_conv(self.adv_ver), self.adv_ver_index)
        return s


def ver_info():
    return VersionInfo(major=3, minor=0, patch=0, adv_ver=Beta, adv_ver_index=2)


def ver_str():
    return ver_info().to_str()


if __name__ == "__main__":
    print(ver_str())
