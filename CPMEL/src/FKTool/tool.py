#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/14 22:05
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from cpweidgets import CPMel as cc


def main(is_newc=False):
    print is_newc
    sel = cc.selected(type="joint")
    if is_newc:
        cc.select(cl=True)
        for t in sel:
            cons = list()
            jins = cc.listRelatives(t, ad=True, type="joint")
            jins.append(t)
            for i in jins[::-1]:
                grp = cc.createNode.transform()
                con = cc.circle(nr=(1, 0, 0), ch=0)[0]
                cc.parent(con, grp)
                cc.delete(cc.parentConstraint(i, grp))
                cc.delete(cc.scaleConstraint(i, grp))
                i.jointOrient.set((0, 0, 0))
                i.segmentScaleCompensate.set(0)
                cc.parentConstraint(con, i)
                cc.scaleConstraint(con, i)
                cons.append((grp, con))
            for c, p in zip(cons[:-1], cons[1:]):
                cc.parent(p[0], c[1])
    else:
        for i in sel:
            grp = cc.createNode.transform()
            con = cc.circle(nr=(1, 0, 0), ch=0)[0]
            cc.parent(con, grp)
            cc.delete(cc.parentConstraint(i, grp))
            cc.delete(cc.scaleConstraint(i, grp))
            i.jointOrient.set((0, 0, 0))
            i.segmentScaleCompensate.set(0)
            cc.parentConstraint(con, i)
            cc.scaleConstraint(con, i)