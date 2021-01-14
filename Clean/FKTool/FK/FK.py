# !/usr/bin/python
# -*-coding:utf-8 -*
u"""
>>> 创建时间
    2020-11-15 09:41:44
>>> 作者
    苍之幻灵

本模块使用newnode开发
newnode作者
    苍之幻灵
苍之幻灵主页
    www.cpcgskill.com
苍之幻灵QQ
    2921251087
苍之幻灵爱发电
    https://afdian.net/@Phantom_of_the_Cang
苍之幻灵aboutcg
    https://www.aboutcg.org/teacher/54335
苍之幻灵bilibili
    https://space.bilibili.com/351598127
"""


from maya.api.OpenMaya import MSelectionList
from maya.cmds import createNode, setAttr, objExists, connectAttr, attributeQuery
class FK(object):
    def __init__(self, start_str = u"", end_str = u""):
        # 创建节点
        selectObject = MSelectionList()
        clear = selectObject.clear
        selectObject.add(createNode("decomposeMatrix", n = u"{}decomposeMatrix1{}".format(start_str, end_str)))
        self.node_decomposeMatrix1 = selectObject.getSelectionStrings(0)[0]
        clear()
        selectObject.add(createNode("multMatrix", n = u"{}multMatrix1{}".format(start_str, end_str)))
        self.node_multMatrix1 = selectObject.getSelectionStrings(0)[0]
        clear()
        # 添加属性
        # 设置属性
        if attributeQuery("caching", node = self.node_multMatrix1, ex = True):
           setAttr(self.node_multMatrix1 + ".caching", False)
        if attributeQuery("frozen", node = self.node_multMatrix1, ex = True):
           setAttr(self.node_multMatrix1 + ".frozen", False)
        if attributeQuery("nodeState", node = self.node_multMatrix1, ex = True):
           setAttr(self.node_multMatrix1 + ".nodeState", 0)
        if attributeQuery("frozenAffected", node = self.node_multMatrix1, ex = True):
           setAttr(self.node_multMatrix1 + ".frozenAffected", False)
        if attributeQuery("caching", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".caching", False)
        if attributeQuery("frozen", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".frozen", False)
        if attributeQuery("nodeState", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".nodeState", 0)
        if attributeQuery("frozenAffected", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".frozenAffected", False)
        if attributeQuery("inputRotateOrder", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".inputRotateOrder", 0)
        if attributeQuery("outputTranslateX", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputTranslateX", 0.0)
        if attributeQuery("outputTranslateY", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputTranslateY", 0.0)
        if attributeQuery("outputTranslateZ", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputTranslateZ", 0.0)
        if attributeQuery("outputRotateX", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputRotateX", 0.0)
        if attributeQuery("outputRotateY", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputRotateY", -0.0)
        if attributeQuery("outputRotateZ", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputRotateZ", 0.0)
        if attributeQuery("outputScaleX", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputScaleX", 1.0)
        if attributeQuery("outputScaleY", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputScaleY", 1.0)
        if attributeQuery("outputScaleZ", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputScaleZ", 1.0)
        if attributeQuery("outputShearX", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputShearX", 0.0)
        if attributeQuery("outputShearY", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputShearY", 0.0)
        if attributeQuery("outputShearZ", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputShearZ", 0.0)
        if attributeQuery("outputQuatX", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputQuatX", 0.0)
        if attributeQuery("outputQuatY", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputQuatY", 0.0)
        if attributeQuery("outputQuatZ", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputQuatZ", 0.0)
        if attributeQuery("outputQuatW", node = self.node_decomposeMatrix1, ex = True):
           setAttr(self.node_decomposeMatrix1 + ".outputQuatW", 1.0)
        # 连接属性
        connectAttr(self.node_multMatrix1 + ".matrixSum", self.node_decomposeMatrix1 + ".inputMatrix")
    def topymel(self):
        import pymel.core as pm
        [setattr(self, k, pm.PyNode(v)) for k, v in self.__dict__.items() if objExists(v)]
    def tocpmel(self):
        from cpweidgets import CPMel as cc
        [setattr(self, k, cc.newObject(v)) for k, v in self.__dict__.items() if objExists(v)]

    def connect(self, out_obj, in_obj):
        connectAttr(out_obj + ".worldMatrix[0]", self.node_multMatrix1 + ".matrixIn[0]")
        connectAttr(in_obj + ".parentInverseMatrix[0]", self.node_multMatrix1 + ".matrixIn[1]")
        connectAttr(self.node_decomposeMatrix1 + ".outputTranslate", in_obj + ".translate")
        connectAttr(self.node_decomposeMatrix1 + ".outputRotate", in_obj + ".rotate")
        connectAttr(self.node_decomposeMatrix1 + ".outputScale", in_obj + ".scale")
        connectAttr(self.node_decomposeMatrix1 + ".outputShear", in_obj + ".shear")