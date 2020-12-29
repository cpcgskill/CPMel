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
在包裹完成之后替换之前的包裹
这部分手动重写以避免自动包裹带来的问题
"""
import maya.cmds as cmds
from ..api import OpenMaya

from . import node
from .node import nodedata
from ..core import metaclass
from . import node
from .node import DgNode, DagNode, AttrObject


@node.commandWrap
def selected(**kwargs):
    u"""

    :param kwargs:
    :return:
    :rtype: list
    """
    return cmds.ls(sl=True, **kwargs)


def isDg(obj):
    u"""
    检查是否为Dg节点

    :param obj:
    :return:
    :rtype: bool
    """
    if isinstance(obj, basestring):
        obj = node.nodedata.newObject(obj)
    return isinstance(obj, node.nodedata.DgNode)


def isDag(obj):
    u"""
    检查是否为Dag节点

    :param obj:
    :return:
    :rtype: bool
    """
    if isinstance(obj, basestring):
        obj = node.nodedata.newObject(obj)
    return isinstance(obj, node.nodedata.DagNode)


def isShape(obj):
    u"""
    检查是否为形状节点

    :param obj:
    :return:
    :rtype: bool
    """
    if isinstance(obj, basestring):
        obj = node.nodedata.newObject(obj)
    if isDag(obj):
        return obj.obj.hasFn(OpenMaya.MFn.kShape)
    else:
        return False


def curveToCv(curve, min_dis=0.001):
    u"""
    将曲线附加到它的Cv点上

    :param curve:曲线
    :param min_dis:最小距离 = 0.001
    :return:
    """
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(curve)
    size = curve.numCvs()
    cv_ids = range(size)
    max_u = curve.numSpans()
    max_size = size - 1
    cv_pts = tuple((curve.getPoint(i) for i in cv_ids))
    while len(cv_ids):
        for i in cv_ids:
            end_pt = cv_pts[i]
            curr_pt = (curve.getPointAtParam(float(i) / max_size * max_u))
            if curr_pt.dis(end_pt) < min_dis:
                cv_ids.remove(i)
            curve.setPoint(i, cv_pts[i] - curr_pt + curve.getPoint(i))


def smoothCurve(curve):
    u"""
    平滑曲线

    :param curve:曲线
    :return:None
    """
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(str(curve))
    pts = tuple((curve.getPoint(i) for i in range(curve.numCvs())))
    if len(pts) < 3:
        return
    [curve.setPoint(i, (pts[i - 1] + pts[i] + pts[i + 1]) / 3) for i in range(1, curve.numCvs() - 1)]


def reconstructionCurve(curve, size=10, d=1):
    u"""
    根据路径重建曲线

    :param curve: 曲线
    :param size: cv点数量 = 10
    :param d: 曲线次方数 = 1
    :return: None
    """
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(curve)
    max_u = curve.numSpans()
    max_size = size - 1
    cmds.curve(str(curve), r=True, p=[tuple(curve.getPointAtParam(float(i) / max_size * max_u)) for i in range(size)],
               d=d)


def attachToModel(mesh=node.Mesh, curve=node.Curve):
    u"""
    附加到模型

    :param mesh: 模型
    :param curve: 曲线
    :return:
    """
    if not isinstance(mesh, node.DgNode):
        mesh = node.newObject(mesh)
    if not isinstance(curve, node.DgNode):
        curve = node.newObject(curve)
    [curve.setPoint(i,
                    mesh.getClosestPointAndFace(
                        curve.getPoint(i, node.Space.world), node.Space.world
                    )[0],
                    node.Space.world
                    ) for i in range(curve.numCvs())]


@node.commandWrap
def duplicate(*args, **kwargs):
    u"""

    :param args:
    :param kwargs:
    :return:
    :rtype: list|str|basestring|DagNode|AttrObject
    """
    kwargs["rc"] = True
    return cmds.duplicate(*args, **kwargs)


@node.commandWrap
def listRelatives(*args, **kwargs):
    u"""
    修改内容：
    -当结果为None时返回一个空列表

    :param args:
    :param kwargs:
    :return:
    :rtype: list|str|basestring|DagNode|AttrObject
    """
    if (not "pa" in kwargs) and (not "path" in kwargs):
        kwargs["pa"] = True
    return cmds.listRelatives(*args, **kwargs)


@node.inCommandWrap
def listAttr(*args, **kwargs):
    u"""

    :param args:
    :param kwargs:
    :return:
    :rtype: list|str|basestring|DagNode|AttrObject
    """
    return cmds.listAttr(*args, **kwargs)


class _CreateNode(object):
    u"""
    创建节点类
    """

    @node.commandWrap
    def __call__(self, *args, **kwargs):
        u"""

        :param args:
        :param kwargs:
        :return:
        :rtype: DagNode
        """
        return cmds.createNode(*args, **kwargs)

    def __getattribute__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            def test(*args, **kwargs):
                return self(item, *args, **kwargs)

            setattr(self, item, test)
            return test

    def AISEnvFacade(self, *args, **kwargs):
        return self(u"AISEnvFacade", *args, **kwargs)

    def AlembicNode(self, *args, **kwargs):
        return self(u"AlembicNode", *args, **kwargs)

    def BifMeshImportNode(self, *args, **kwargs):
        return self(u"BifMeshImportNode", *args, **kwargs)

    def ComputeGlobal(self, *args, **kwargs):
        return self(u"ComputeGlobal", *args, **kwargs)

    def ComputeLocal(self, *args, **kwargs):
        return self(u"ComputeLocal", *args, **kwargs)

    def CustomRigDefaultMappingNode(self, *args, **kwargs):
        return self(u"CustomRigDefaultMappingNode", *args, **kwargs)

    def CustomRigRetargeterNode(self, *args, **kwargs):
        return self(u"CustomRigRetargeterNode", *args, **kwargs)

    def HIKCharacterNode(self, *args, **kwargs):
        return self(u"HIKCharacterNode", *args, **kwargs)

    def HIKCharacterStateClient(self, *args, **kwargs):
        return self(u"HIKCharacterStateClient", *args, **kwargs)

    def HIKControlSetNode(self, *args, **kwargs):
        return self(u"HIKControlSetNode", *args, **kwargs)

    def HIKEffector2State(self, *args, **kwargs):
        return self(u"HIKEffector2State", *args, **kwargs)

    def HIKEffectorFromCharacter(self, *args, **kwargs):
        return self(u"HIKEffectorFromCharacter", *args, **kwargs)

    def HIKFK2State(self, *args, **kwargs):
        return self(u"HIKFK2State", *args, **kwargs)

    def HIKPinning2State(self, *args, **kwargs):
        return self(u"HIKPinning2State", *args, **kwargs)

    def HIKProperty2State(self, *args, **kwargs):
        return self(u"HIKProperty2State", *args, **kwargs)

    def HIKRetargeterNode(self, *args, **kwargs):
        return self(u"HIKRetargeterNode", *args, **kwargs)

    def HIKSK2State(self, *args, **kwargs):
        return self(u"HIKSK2State", *args, **kwargs)

    def HIKSkeletonGeneratorNode(self, *args, **kwargs):
        return self(u"HIKSkeletonGeneratorNode", *args, **kwargs)

    def HIKSolverNode(self, *args, **kwargs):
        return self(u"HIKSolverNode", *args, **kwargs)

    def HIKState2Effector(self, *args, **kwargs):
        return self(u"HIKState2Effector", *args, **kwargs)

    def HIKState2FK(self, *args, **kwargs):
        return self(u"HIKState2FK", *args, **kwargs)

    def HIKState2GlobalSK(self, *args, **kwargs):
        return self(u"HIKState2GlobalSK", *args, **kwargs)

    def HIKState2SK(self, *args, **kwargs):
        return self(u"HIKState2SK", *args, **kwargs)

    def MASH_Audio(self, *args, **kwargs):
        return self(u"MASH_Audio", *args, **kwargs)

    def MASH_BaseNode(self, *args, **kwargs):
        return self(u"MASH_BaseNode", *args, **kwargs)

    def MASH_Blend(self, *args, **kwargs):
        return self(u"MASH_Blend", *args, **kwargs)

    def MASH_BlendDeformer(self, *args, **kwargs):
        return self(u"MASH_BlendDeformer", *args, **kwargs)

    def MASH_Breakout(self, *args, **kwargs):
        return self(u"MASH_Breakout", *args, **kwargs)

    def MASH_BulletSolver(self, *args, **kwargs):
        return self(u"MASH_BulletSolver", *args, **kwargs)

    def MASH_ChannelRandom(self, *args, **kwargs):
        return self(u"MASH_ChannelRandom", *args, **kwargs)

    def MASH_Color(self, *args, **kwargs):
        return self(u"MASH_Color", *args, **kwargs)

    def MASH_Constraint(self, *args, **kwargs):
        return self(u"MASH_Constraint", *args, **kwargs)

    def MASH_Curve(self, *args, **kwargs):
        return self(u"MASH_Curve", *args, **kwargs)

    def MASH_Deformer(self, *args, **kwargs):
        return self(u"MASH_Deformer", *args, **kwargs)

    def MASH_Delay(self, *args, **kwargs):
        return self(u"MASH_Delay", *args, **kwargs)

    def MASH_Distribute(self, *args, **kwargs):
        return self(u"MASH_Distribute", *args, **kwargs)

    def MASH_Dynamics(self, *args, **kwargs):
        return self(u"MASH_Dynamics", *args, **kwargs)

    def MASH_DynamicsInitialState(self, *args, **kwargs):
        return self(u"MASH_DynamicsInitialState", *args, **kwargs)

    def MASH_Explode(self, *args, **kwargs):
        return self(u"MASH_Explode", *args, **kwargs)

    def MASH_Falloff(self, *args, **kwargs):
        return self(u"MASH_Falloff", *args, **kwargs)

    def MASH_Flight(self, *args, **kwargs):
        return self(u"MASH_Flight", *args, **kwargs)

    def MASH_Font(self, *args, **kwargs):
        return self(u"MASH_Font", *args, **kwargs)

    def MASH_Id(self, *args, **kwargs):
        return self(u"MASH_Id", *args, **kwargs)

    def MASH_Influence(self, *args, **kwargs):
        return self(u"MASH_Influence", *args, **kwargs)

    def MASH_Inherit(self, *args, **kwargs):
        return self(u"MASH_Inherit", *args, **kwargs)

    def MASH_InitialState(self, *args, **kwargs):
        return self(u"MASH_InitialState", *args, **kwargs)

    def MASH_Jiggle(self, *args, **kwargs):
        return self(u"MASH_Jiggle", *args, **kwargs)

    def MASH_Legacy(self, *args, **kwargs):
        return self(u"MASH_Legacy", *args, **kwargs)

    def MASH_Maths(self, *args, **kwargs):
        return self(u"MASH_Maths", *args, **kwargs)

    def MASH_MultiCurve(self, *args, **kwargs):
        return self(u"MASH_MultiCurve", *args, **kwargs)

    def MASH_Mute(self, *args, **kwargs):
        return self(u"MASH_Mute", *args, **kwargs)

    def MASH_Noise(self, *args, **kwargs):
        return self(u"MASH_Noise", *args, **kwargs)

    def MASH_Offset(self, *args, **kwargs):
        return self(u"MASH_Offset", *args, **kwargs)

    def MASH_Orient(self, *args, **kwargs):
        return self(u"MASH_Orient", *args, **kwargs)

    def MASH_PfxConnect(self, *args, **kwargs):
        return self(u"MASH_PfxConnect", *args, **kwargs)

    def MASH_Placer(self, *args, **kwargs):
        return self(u"MASH_Placer", *args, **kwargs)

    def MASH_PointToCurve(self, *args, **kwargs):
        return self(u"MASH_PointToCurve", *args, **kwargs)

    def MASH_Points(self, *args, **kwargs):
        return self(u"MASH_Points", *args, **kwargs)

    def MASH_Python(self, *args, **kwargs):
        return self(u"MASH_Python", *args, **kwargs)

    def MASH_Random(self, *args, **kwargs):
        return self(u"MASH_Random", *args, **kwargs)

    def MASH_Replicator(self, *args, **kwargs):
        return self(u"MASH_Replicator", *args, **kwargs)

    def MASH_Repro(self, *args, **kwargs):
        return self(u"MASH_Repro", *args, **kwargs)

    def MASH_ShellDeformer(self, *args, **kwargs):
        return self(u"MASH_ShellDeformer", *args, **kwargs)

    def MASH_Signal(self, *args, **kwargs):
        return self(u"MASH_Signal", *args, **kwargs)

    def MASH_Spring(self, *args, **kwargs):
        return self(u"MASH_Spring", *args, **kwargs)

    def MASH_Strength(self, *args, **kwargs):
        return self(u"MASH_Strength", *args, **kwargs)

    def MASH_Symmetry(self, *args, **kwargs):
        return self(u"MASH_Symmetry", *args, **kwargs)

    def MASH_Time(self, *args, **kwargs):
        return self(u"MASH_Time", *args, **kwargs)

    def MASH_Trails(self, *args, **kwargs):
        return self(u"MASH_Trails", *args, **kwargs)

    def MASH_Transform(self, *args, **kwargs):
        return self(u"MASH_Transform", *args, **kwargs)

    def MASH_Trig(self, *args, **kwargs):
        return self(u"MASH_Trig", *args, **kwargs)

    def MASH_Visibility(self, *args, **kwargs):
        return self(u"MASH_Visibility", *args, **kwargs)

    def MASH_Waiter(self, *args, **kwargs):
        return self(u"MASH_Waiter", *args, **kwargs)

    def MASH_World(self, *args, **kwargs):
        return self(u"MASH_World", *args, **kwargs)

    def ShaderfxGameHair(self, *args, **kwargs):
        return self(u"ShaderfxGameHair", *args, **kwargs)

    def ShaderfxShader(self, *args, **kwargs):
        return self(u"ShaderfxShader", *args, **kwargs)

    def SphereLocator(self, *args, **kwargs):
        return self(u"SphereLocator", *args, **kwargs)

    def StingrayPBS(self, *args, **kwargs):
        return self(u"StingrayPBS", *args, **kwargs)

    def Unfold3DOptimize(self, *args, **kwargs):
        return self(u"Unfold3DOptimize", *args, **kwargs)

    def Unfold3DUnfold(self, *args, **kwargs):
        return self(u"Unfold3DUnfold", *args, **kwargs)

    def aboutToSetValueTestNode(self, *args, **kwargs):
        return self(u"aboutToSetValueTestNode", *args, **kwargs)

    def absOverride(self, *args, **kwargs):
        return self(u"absOverride", *args, **kwargs)

    def absUniqueOverride(self, *args, **kwargs):
        return self(u"absUniqueOverride", *args, **kwargs)

    def addDoubleLinear(self, *args, **kwargs):
        return self(u"addDoubleLinear", *args, **kwargs)

    def addMatrix(self, *args, **kwargs):
        return self(u"addMatrix", *args, **kwargs)

    def adskMaterial(self, *args, **kwargs):
        return self(u"adskMaterial", *args, **kwargs)

    def adskPrepareRenderGlobals(self, *args, **kwargs):
        return self(u"adskPrepareRenderGlobals", *args, **kwargs)

    def aiAOV(self, *args, **kwargs):
        return self(u"aiAOV", *args, **kwargs)

    def aiAOVDriver(self, *args, **kwargs):
        return self(u"aiAOVDriver", *args, **kwargs)

    def aiAOVFilter(self, *args, **kwargs):
        return self(u"aiAOVFilter", *args, **kwargs)

    def aiAbs(self, *args, **kwargs):
        return self(u"aiAbs", *args, **kwargs)

    def aiAdd(self, *args, **kwargs):
        return self(u"aiAdd", *args, **kwargs)

    def aiAmbientOcclusion(self, *args, **kwargs):
        return self(u"aiAmbientOcclusion", *args, **kwargs)

    def aiAreaLight(self, *args, **kwargs):
        return self(u"aiAreaLight", *args, **kwargs)

    def aiAtan(self, *args, **kwargs):
        return self(u"aiAtan", *args, **kwargs)

    def aiAtmosphereVolume(self, *args, **kwargs):
        return self(u"aiAtmosphereVolume", *args, **kwargs)

    def aiBarndoor(self, *args, **kwargs):
        return self(u"aiBarndoor", *args, **kwargs)

    def aiBlackbody(self, *args, **kwargs):
        return self(u"aiBlackbody", *args, **kwargs)

    def aiBump2d(self, *args, **kwargs):
        return self(u"aiBump2d", *args, **kwargs)

    def aiBump3d(self, *args, **kwargs):
        return self(u"aiBump3d", *args, **kwargs)

    def aiCache(self, *args, **kwargs):
        return self(u"aiCache", *args, **kwargs)

    def aiClamp(self, *args, **kwargs):
        return self(u"aiClamp", *args, **kwargs)

    def aiColorConvert(self, *args, **kwargs):
        return self(u"aiColorConvert", *args, **kwargs)

    def aiColorCorrect(self, *args, **kwargs):
        return self(u"aiColorCorrect", *args, **kwargs)

    def aiColorJitter(self, *args, **kwargs):
        return self(u"aiColorJitter", *args, **kwargs)

    def aiColorToFloat(self, *args, **kwargs):
        return self(u"aiColorToFloat", *args, **kwargs)

    def aiCompare(self, *args, **kwargs):
        return self(u"aiCompare", *args, **kwargs)

    def aiComplement(self, *args, **kwargs):
        return self(u"aiComplement", *args, **kwargs)

    def aiComplexIor(self, *args, **kwargs):
        return self(u"aiComplexIor", *args, **kwargs)

    def aiComposite(self, *args, **kwargs):
        return self(u"aiComposite", *args, **kwargs)

    def aiCross(self, *args, **kwargs):
        return self(u"aiCross", *args, **kwargs)

    def aiCurvature(self, *args, **kwargs):
        return self(u"aiCurvature", *args, **kwargs)

    def aiCurveCollector(self, *args, **kwargs):
        return self(u"aiCurveCollector", *args, **kwargs)

    def aiDivide(self, *args, **kwargs):
        return self(u"aiDivide", *args, **kwargs)

    def aiDot(self, *args, **kwargs):
        return self(u"aiDot", *args, **kwargs)

    def aiExp(self, *args, **kwargs):
        return self(u"aiExp", *args, **kwargs)

    def aiFacingRatio(self, *args, **kwargs):
        return self(u"aiFacingRatio", *args, **kwargs)

    def aiFlakes(self, *args, **kwargs):
        return self(u"aiFlakes", *args, **kwargs)

    def aiFlat(self, *args, **kwargs):
        return self(u"aiFlat", *args, **kwargs)

    def aiFloatToInt(self, *args, **kwargs):
        return self(u"aiFloatToInt", *args, **kwargs)

    def aiFog(self, *args, **kwargs):
        return self(u"aiFog", *args, **kwargs)

    def aiFraction(self, *args, **kwargs):
        return self(u"aiFraction", *args, **kwargs)

    def aiGobo(self, *args, **kwargs):
        return self(u"aiGobo", *args, **kwargs)

    def aiHair(self, *args, **kwargs):
        return self(u"aiHair", *args, **kwargs)

    def aiImage(self, *args, **kwargs):
        return self(u"aiImage", *args, **kwargs)

    def aiIsFinite(self, *args, **kwargs):
        return self(u"aiIsFinite", *args, **kwargs)

    def aiLength(self, *args, **kwargs):
        return self(u"aiLength", *args, **kwargs)

    def aiLightBlocker(self, *args, **kwargs):
        return self(u"aiLightBlocker", *args, **kwargs)

    def aiLightDecay(self, *args, **kwargs):
        return self(u"aiLightDecay", *args, **kwargs)

    def aiLightPortal(self, *args, **kwargs):
        return self(u"aiLightPortal", *args, **kwargs)

    def aiLog(self, *args, **kwargs):
        return self(u"aiLog", *args, **kwargs)

    def aiMax(self, *args, **kwargs):
        return self(u"aiMax", *args, **kwargs)

    def aiMeshLight(self, *args, **kwargs):
        return self(u"aiMeshLight", *args, **kwargs)

    def aiMin(self, *args, **kwargs):
        return self(u"aiMin", *args, **kwargs)

    def aiMixShader(self, *args, **kwargs):
        return self(u"aiMixShader", *args, **kwargs)

    def aiModulo(self, *args, **kwargs):
        return self(u"aiModulo", *args, **kwargs)

    def aiMotionVector(self, *args, **kwargs):
        return self(u"aiMotionVector", *args, **kwargs)

    def aiMultiply(self, *args, **kwargs):
        return self(u"aiMultiply", *args, **kwargs)

    def aiNegate(self, *args, **kwargs):
        return self(u"aiNegate", *args, **kwargs)

    def aiNoise(self, *args, **kwargs):
        return self(u"aiNoise", *args, **kwargs)

    def aiNormalMap(self, *args, **kwargs):
        return self(u"aiNormalMap", *args, **kwargs)

    def aiNormalize(self, *args, **kwargs):
        return self(u"aiNormalize", *args, **kwargs)

    def aiOptions(self, *args, **kwargs):
        return self(u"aiOptions", *args, **kwargs)

    def aiPhotometricLight(self, *args, **kwargs):
        return self(u"aiPhotometricLight", *args, **kwargs)

    def aiPhysicalSky(self, *args, **kwargs):
        return self(u"aiPhysicalSky", *args, **kwargs)

    def aiPow(self, *args, **kwargs):
        return self(u"aiPow", *args, **kwargs)

    def aiRandom(self, *args, **kwargs):
        return self(u"aiRandom", *args, **kwargs)

    def aiRange(self, *args, **kwargs):
        return self(u"aiRange", *args, **kwargs)

    def aiRaySwitch(self, *args, **kwargs):
        return self(u"aiRaySwitch", *args, **kwargs)

    def aiReciprocal(self, *args, **kwargs):
        return self(u"aiReciprocal", *args, **kwargs)

    def aiShadowMatte(self, *args, **kwargs):
        return self(u"aiShadowMatte", *args, **kwargs)

    def aiShuffle(self, *args, **kwargs):
        return self(u"aiShuffle", *args, **kwargs)

    def aiSign(self, *args, **kwargs):
        return self(u"aiSign", *args, **kwargs)

    def aiSkin(self, *args, **kwargs):
        return self(u"aiSkin", *args, **kwargs)

    def aiSky(self, *args, **kwargs):
        return self(u"aiSky", *args, **kwargs)

    def aiSkyDomeLight(self, *args, **kwargs):
        return self(u"aiSkyDomeLight", *args, **kwargs)

    def aiSpaceTransform(self, *args, **kwargs):
        return self(u"aiSpaceTransform", *args, **kwargs)

    def aiSqrt(self, *args, **kwargs):
        return self(u"aiSqrt", *args, **kwargs)

    def aiStandIn(self, *args, **kwargs):
        return self(u"aiStandIn", *args, **kwargs)

    def aiStandard(self, *args, **kwargs):
        return self(u"aiStandard", *args, **kwargs)

    def aiStandardHair(self, *args, **kwargs):
        return self(u"aiStandardHair", *args, **kwargs)

    def aiStandardSurface(self, *args, **kwargs):
        return self(u"aiStandardSurface", *args, **kwargs)

    def aiStandardVolume(self, *args, **kwargs):
        return self(u"aiStandardVolume", *args, **kwargs)

    def aiSubstract(self, *args, **kwargs):
        return self(u"aiSubstract", *args, **kwargs)

    def aiSwitch(self, *args, **kwargs):
        return self(u"aiSwitch", *args, **kwargs)

    def aiThinFilm(self, *args, **kwargs):
        return self(u"aiThinFilm", *args, **kwargs)

    def aiTrigo(self, *args, **kwargs):
        return self(u"aiTrigo", *args, **kwargs)

    def aiTriplanar(self, *args, **kwargs):
        return self(u"aiTriplanar", *args, **kwargs)

    def aiTwoSided(self, *args, **kwargs):
        return self(u"aiTwoSided", *args, **kwargs)

    def aiUserDataBool(self, *args, **kwargs):
        return self(u"aiUserDataBool", *args, **kwargs)

    def aiUserDataColor(self, *args, **kwargs):
        return self(u"aiUserDataColor", *args, **kwargs)

    def aiUserDataFloat(self, *args, **kwargs):
        return self(u"aiUserDataFloat", *args, **kwargs)

    def aiUserDataInt(self, *args, **kwargs):
        return self(u"aiUserDataInt", *args, **kwargs)

    def aiUserDataString(self, *args, **kwargs):
        return self(u"aiUserDataString", *args, **kwargs)

    def aiUserDataVec2(self, *args, **kwargs):
        return self(u"aiUserDataVec2", *args, **kwargs)

    def aiUserDataVector(self, *args, **kwargs):
        return self(u"aiUserDataVector", *args, **kwargs)

    def aiUtility(self, *args, **kwargs):
        return self(u"aiUtility", *args, **kwargs)

    def aiUvTransform(self, *args, **kwargs):
        return self(u"aiUvTransform", *args, **kwargs)

    def aiVectorMap(self, *args, **kwargs):
        return self(u"aiVectorMap", *args, **kwargs)

    def aiVolume(self, *args, **kwargs):
        return self(u"aiVolume", *args, **kwargs)

    def aiVolumeCollector(self, *args, **kwargs):
        return self(u"aiVolumeCollector", *args, **kwargs)

    def aiVolumeSampleFloat(self, *args, **kwargs):
        return self(u"aiVolumeSampleFloat", *args, **kwargs)

    def aiVolumeSampleRgb(self, *args, **kwargs):
        return self(u"aiVolumeSampleRgb", *args, **kwargs)

    def aiWireframe(self, *args, **kwargs):
        return self(u"aiWireframe", *args, **kwargs)

    def aiWriteColor(self, *args, **kwargs):
        return self(u"aiWriteColor", *args, **kwargs)

    def aiWriteFloat(self, *args, **kwargs):
        return self(u"aiWriteFloat", *args, **kwargs)

    def aimConstraint(self, *args, **kwargs):
        return self(u"aimConstraint", *args, **kwargs)

    def airField(self, *args, **kwargs):
        return self(u"airField", *args, **kwargs)

    def airManip(self, *args, **kwargs):
        return self(u"airManip", *args, **kwargs)

    def alignCurve(self, *args, **kwargs):
        return self(u"alignCurve", *args, **kwargs)

    def alignManip(self, *args, **kwargs):
        return self(u"alignManip", *args, **kwargs)

    def alignSurface(self, *args, **kwargs):
        return self(u"alignSurface", *args, **kwargs)

    def ambientLight(self, *args, **kwargs):
        return self(u"ambientLight", *args, **kwargs)

    def angleBetween(self, *args, **kwargs):
        return self(u"angleBetween", *args, **kwargs)

    def angleDimension(self, *args, **kwargs):
        return self(u"angleDimension", *args, **kwargs)

    def animBlend(self, *args, **kwargs):
        return self(u"animBlend", *args, **kwargs)

    def animBlendInOut(self, *args, **kwargs):
        return self(u"animBlendInOut", *args, **kwargs)

    def animBlendNodeAdditive(self, *args, **kwargs):
        return self(u"animBlendNodeAdditive", *args, **kwargs)

    def animBlendNodeAdditiveDA(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveDA", *args, **kwargs)

    def animBlendNodeAdditiveDL(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveDL", *args, **kwargs)

    def animBlendNodeAdditiveF(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveF", *args, **kwargs)

    def animBlendNodeAdditiveFA(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveFA", *args, **kwargs)

    def animBlendNodeAdditiveFL(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveFL", *args, **kwargs)

    def animBlendNodeAdditiveI16(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveI16", *args, **kwargs)

    def animBlendNodeAdditiveI32(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveI32", *args, **kwargs)

    def animBlendNodeAdditiveRotation(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveRotation", *args, **kwargs)

    def animBlendNodeAdditiveScale(self, *args, **kwargs):
        return self(u"animBlendNodeAdditiveScale", *args, **kwargs)

    def animBlendNodeBoolean(self, *args, **kwargs):
        return self(u"animBlendNodeBoolean", *args, **kwargs)

    def animBlendNodeEnum(self, *args, **kwargs):
        return self(u"animBlendNodeEnum", *args, **kwargs)

    def animBlendNodeTime(self, *args, **kwargs):
        return self(u"animBlendNodeTime", *args, **kwargs)

    def animClip(self, *args, **kwargs):
        return self(u"animClip", *args, **kwargs)

    def animCurveTA(self, *args, **kwargs):
        return self(u"animCurveTA", *args, **kwargs)

    def animCurveTL(self, *args, **kwargs):
        return self(u"animCurveTL", *args, **kwargs)

    def animCurveTT(self, *args, **kwargs):
        return self(u"animCurveTT", *args, **kwargs)

    def animCurveTU(self, *args, **kwargs):
        return self(u"animCurveTU", *args, **kwargs)

    def animCurveUA(self, *args, **kwargs):
        return self(u"animCurveUA", *args, **kwargs)

    def animCurveUL(self, *args, **kwargs):
        return self(u"animCurveUL", *args, **kwargs)

    def animCurveUT(self, *args, **kwargs):
        return self(u"animCurveUT", *args, **kwargs)

    def animCurveUU(self, *args, **kwargs):
        return self(u"animCurveUU", *args, **kwargs)

    def animLayer(self, *args, **kwargs):
        return self(u"animLayer", *args, **kwargs)

    def anisotropic(self, *args, **kwargs):
        return self(u"anisotropic", *args, **kwargs)

    def annotationShape(self, *args, **kwargs):
        return self(u"annotationShape", *args, **kwargs)

    def aovChildCollection(self, *args, **kwargs):
        return self(u"aovChildCollection", *args, **kwargs)

    def aovCollection(self, *args, **kwargs):
        return self(u"aovCollection", *args, **kwargs)

    def applyAbs2FloatsOverride(self, *args, **kwargs):
        return self(u"applyAbs2FloatsOverride", *args, **kwargs)

    def applyAbs3FloatsOverride(self, *args, **kwargs):
        return self(u"applyAbs3FloatsOverride", *args, **kwargs)

    def applyAbsBoolOverride(self, *args, **kwargs):
        return self(u"applyAbsBoolOverride", *args, **kwargs)

    def applyAbsEnumOverride(self, *args, **kwargs):
        return self(u"applyAbsEnumOverride", *args, **kwargs)

    def applyAbsFloatOverride(self, *args, **kwargs):
        return self(u"applyAbsFloatOverride", *args, **kwargs)

    def applyAbsIntOverride(self, *args, **kwargs):
        return self(u"applyAbsIntOverride", *args, **kwargs)

    def applyAbsOverride(self, *args, **kwargs):
        return self(u"applyAbsOverride", *args, **kwargs)

    def applyAbsStringOverride(self, *args, **kwargs):
        return self(u"applyAbsStringOverride", *args, **kwargs)

    def applyConnectionOverride(self, *args, **kwargs):
        return self(u"applyConnectionOverride", *args, **kwargs)

    def applyOverride(self, *args, **kwargs):
        return self(u"applyOverride", *args, **kwargs)

    def applyRel2FloatsOverride(self, *args, **kwargs):
        return self(u"applyRel2FloatsOverride", *args, **kwargs)

    def applyRel3FloatsOverride(self, *args, **kwargs):
        return self(u"applyRel3FloatsOverride", *args, **kwargs)

    def applyRelFloatOverride(self, *args, **kwargs):
        return self(u"applyRelFloatOverride", *args, **kwargs)

    def applyRelIntOverride(self, *args, **kwargs):
        return self(u"applyRelIntOverride", *args, **kwargs)

    def applyRelOverride(self, *args, **kwargs):
        return self(u"applyRelOverride", *args, **kwargs)

    def arcLengthDimension(self, *args, **kwargs):
        return self(u"arcLengthDimension", *args, **kwargs)

    def areaLight(self, *args, **kwargs):
        return self(u"areaLight", *args, **kwargs)

    def arnoldAOVChildSelector(self, *args, **kwargs):
        return self(u"arnoldAOVChildSelector", *args, **kwargs)

    def arrayMapper(self, *args, **kwargs):
        return self(u"arrayMapper", *args, **kwargs)

    def arrowManip(self, *args, **kwargs):
        return self(u"arrowManip", *args, **kwargs)

    def arubaTessellate(self, *args, **kwargs):
        return self(u"arubaTessellate", *args, **kwargs)

    def assemblyDefinition(self, *args, **kwargs):
        return self(u"assemblyDefinition", *args, **kwargs)

    def assemblyReference(self, *args, **kwargs):
        return self(u"assemblyReference", *args, **kwargs)

    def attachCurve(self, *args, **kwargs):
        return self(u"attachCurve", *args, **kwargs)

    def attachSurface(self, *args, **kwargs):
        return self(u"attachSurface", *args, **kwargs)

    def attrHierarchyTest(self, *args, **kwargs):
        return self(u"attrHierarchyTest", *args, **kwargs)

    def audio(self, *args, **kwargs):
        return self(u"audio", *args, **kwargs)

    def avgCurves(self, *args, **kwargs):
        return self(u"avgCurves", *args, **kwargs)

    def avgCurvesManip(self, *args, **kwargs):
        return self(u"avgCurvesManip", *args, **kwargs)

    def avgNurbsSurfacePoints(self, *args, **kwargs):
        return self(u"avgNurbsSurfacePoints", *args, **kwargs)

    def avgSurfacePoints(self, *args, **kwargs):
        return self(u"avgSurfacePoints", *args, **kwargs)

    def axesActionManip(self, *args, **kwargs):
        return self(u"axesActionManip", *args, **kwargs)

    def ballProjManip(self, *args, **kwargs):
        return self(u"ballProjManip", *args, **kwargs)

    def barnDoorManip(self, *args, **kwargs):
        return self(u"barnDoorManip", *args, **kwargs)

    def baseLattice(self, *args, **kwargs):
        return self(u"baseLattice", *args, **kwargs)

    def basicSelector(self, *args, **kwargs):
        return self(u"basicSelector", *args, **kwargs)

    def bevel(self, *args, **kwargs):
        return self(u"bevel", *args, **kwargs)

    def bevelManip(self, *args, **kwargs):
        return self(u"bevelManip", *args, **kwargs)

    def bevelPlus(self, *args, **kwargs):
        return self(u"bevelPlus", *args, **kwargs)

    def bezierCurve(self, *args, **kwargs):
        return self(u"bezierCurve", *args, **kwargs)

    def bezierCurveToNurbs(self, *args, **kwargs):
        return self(u"bezierCurveToNurbs", *args, **kwargs)

    def bifrostAeroMaterial(self, *args, **kwargs):
        return self(u"bifrostAeroMaterial", *args, **kwargs)

    def bifrostAttrNotifier(self, *args, **kwargs):
        return self(u"bifrostAttrNotifier", *args, **kwargs)

    def bifrostContainer(self, *args, **kwargs):
        return self(u"bifrostContainer", *args, **kwargs)

    def bifrostFoamMaterial(self, *args, **kwargs):
        return self(u"bifrostFoamMaterial", *args, **kwargs)

    def bifrostLiquidMaterial(self, *args, **kwargs):
        return self(u"bifrostLiquidMaterial", *args, **kwargs)

    def bifrostShape(self, *args, **kwargs):
        return self(u"bifrostShape", *args, **kwargs)

    def blendColorSets(self, *args, **kwargs):
        return self(u"blendColorSets", *args, **kwargs)

    def blendColors(self, *args, **kwargs):
        return self(u"blendColors", *args, **kwargs)

    def blendDevice(self, *args, **kwargs):
        return self(u"blendDevice", *args, **kwargs)

    def blendManip(self, *args, **kwargs):
        return self(u"blendManip", *args, **kwargs)

    def blendShape(self, *args, **kwargs):
        return self(u"blendShape", *args, **kwargs)

    def blendTwoAttr(self, *args, **kwargs):
        return self(u"blendTwoAttr", *args, **kwargs)

    def blendWeighted(self, *args, **kwargs):
        return self(u"blendWeighted", *args, **kwargs)

    def blindDataTemplate(self, *args, **kwargs):
        return self(u"blindDataTemplate", *args, **kwargs)

    def blinn(self, *args, **kwargs):
        return self(u"blinn", *args, **kwargs)

    def boneLattice(self, *args, **kwargs):
        return self(u"boneLattice", *args, **kwargs)

    def boolean(self, *args, **kwargs):
        return self(u"boolean", *args, **kwargs)

    def boundary(self, *args, **kwargs):
        return self(u"boundary", *args, **kwargs)

    def brownian(self, *args, **kwargs):
        return self(u"brownian", *args, **kwargs)

    def brush(self, *args, **kwargs):
        return self(u"brush", *args, **kwargs)

    def bulge(self, *args, **kwargs):
        return self(u"bulge", *args, **kwargs)

    def bump2d(self, *args, **kwargs):
        return self(u"bump2d", *args, **kwargs)

    def bump3d(self, *args, **kwargs):
        return self(u"bump3d", *args, **kwargs)

    def buttonManip(self, *args, **kwargs):
        return self(u"buttonManip", *args, **kwargs)

    def cMuscleCreator(self, *args, **kwargs):
        return self(u"cMuscleCreator", *args, **kwargs)

    def cMuscleDebug(self, *args, **kwargs):
        return self(u"cMuscleDebug", *args, **kwargs)

    def cMuscleDirection(self, *args, **kwargs):
        return self(u"cMuscleDirection", *args, **kwargs)

    def cMuscleDisplace(self, *args, **kwargs):
        return self(u"cMuscleDisplace", *args, **kwargs)

    def cMuscleDisplay(self, *args, **kwargs):
        return self(u"cMuscleDisplay", *args, **kwargs)

    def cMuscleFalloff(self, *args, **kwargs):
        return self(u"cMuscleFalloff", *args, **kwargs)

    def cMuscleKeepOut(self, *args, **kwargs):
        return self(u"cMuscleKeepOut", *args, **kwargs)

    def cMuscleMultiCollide(self, *args, **kwargs):
        return self(u"cMuscleMultiCollide", *args, **kwargs)

    def cMuscleObject(self, *args, **kwargs):
        return self(u"cMuscleObject", *args, **kwargs)

    def cMuscleRelative(self, *args, **kwargs):
        return self(u"cMuscleRelative", *args, **kwargs)

    def cMuscleShader(self, *args, **kwargs):
        return self(u"cMuscleShader", *args, **kwargs)

    def cMuscleSmartCollide(self, *args, **kwargs):
        return self(u"cMuscleSmartCollide", *args, **kwargs)

    def cMuscleSmartConstraint(self, *args, **kwargs):
        return self(u"cMuscleSmartConstraint", *args, **kwargs)

    def cMuscleSpline(self, *args, **kwargs):
        return self(u"cMuscleSpline", *args, **kwargs)

    def cMuscleSplineDeformer(self, *args, **kwargs):
        return self(u"cMuscleSplineDeformer", *args, **kwargs)

    def cMuscleStretch(self, *args, **kwargs):
        return self(u"cMuscleStretch", *args, **kwargs)

    def cMuscleSurfAttach(self, *args, **kwargs):
        return self(u"cMuscleSurfAttach", *args, **kwargs)

    def cMuscleSystem(self, *args, **kwargs):
        return self(u"cMuscleSystem", *args, **kwargs)

    def cacheBlend(self, *args, **kwargs):
        return self(u"cacheBlend", *args, **kwargs)

    def cacheFile(self, *args, **kwargs):
        return self(u"cacheFile", *args, **kwargs)

    def caddyManip(self, *args, **kwargs):
        return self(u"caddyManip", *args, **kwargs)

    def caddyManipBase(self, *args, **kwargs):
        return self(u"caddyManipBase", *args, **kwargs)

    def camera(self, *args, **kwargs):
        return self(u"camera", *args, **kwargs)

    def cameraManip(self, *args, **kwargs):
        return self(u"cameraManip", *args, **kwargs)

    def cameraPlaneManip(self, *args, **kwargs):
        return self(u"cameraPlaneManip", *args, **kwargs)

    def cameraSet(self, *args, **kwargs):
        return self(u"cameraSet", *args, **kwargs)

    def cameraView(self, *args, **kwargs):
        return self(u"cameraView", *args, **kwargs)

    def centerManip(self, *args, **kwargs):
        return self(u"centerManip", *args, **kwargs)

    def channels(self, *args, **kwargs):
        return self(u"channels", *args, **kwargs)

    def character(self, *args, **kwargs):
        return self(u"character", *args, **kwargs)

    def characterMap(self, *args, **kwargs):
        return self(u"characterMap", *args, **kwargs)

    def characterOffset(self, *args, **kwargs):
        return self(u"characterOffset", *args, **kwargs)

    def checker(self, *args, **kwargs):
        return self(u"checker", *args, **kwargs)

    def childNode(self, *args, **kwargs):
        return self(u"childNode", *args, **kwargs)

    def choice(self, *args, **kwargs):
        return self(u"choice", *args, **kwargs)

    def chooser(self, *args, **kwargs):
        return self(u"chooser", *args, **kwargs)

    def circleManip(self, *args, **kwargs):
        return self(u"circleManip", *args, **kwargs)

    def circleSweepManip(self, *args, **kwargs):
        return self(u"circleSweepManip", *args, **kwargs)

    def clamp(self, *args, **kwargs):
        return self(u"clamp", *args, **kwargs)

    def clipGhostShape(self, *args, **kwargs):
        return self(u"clipGhostShape", *args, **kwargs)

    def clipLibrary(self, *args, **kwargs):
        return self(u"clipLibrary", *args, **kwargs)

    def clipScheduler(self, *args, **kwargs):
        return self(u"clipScheduler", *args, **kwargs)

    def clipToGhostData(self, *args, **kwargs):
        return self(u"clipToGhostData", *args, **kwargs)

    def closeCurve(self, *args, **kwargs):
        return self(u"closeCurve", *args, **kwargs)

    def closeSurface(self, *args, **kwargs):
        return self(u"closeSurface", *args, **kwargs)

    def closestPointOnMesh(self, *args, **kwargs):
        return self(u"closestPointOnMesh", *args, **kwargs)

    def closestPointOnSurface(self, *args, **kwargs):
        return self(u"closestPointOnSurface", *args, **kwargs)

    def cloth(self, *args, **kwargs):
        return self(u"cloth", *args, **kwargs)

    def cloud(self, *args, **kwargs):
        return self(u"cloud", *args, **kwargs)

    def cluster(self, *args, **kwargs):
        return self(u"cluster", *args, **kwargs)

    def clusterFlexorShape(self, *args, **kwargs):
        return self(u"clusterFlexorShape", *args, **kwargs)

    def clusterHandle(self, *args, **kwargs):
        return self(u"clusterHandle", *args, **kwargs)

    def coiManip(self, *args, **kwargs):
        return self(u"coiManip", *args, **kwargs)

    def collection(self, *args, **kwargs):
        return self(u"collection", *args, **kwargs)

    def collisionModel(self, *args, **kwargs):
        return self(u"collisionModel", *args, **kwargs)

    def colorComposite(self, *args, **kwargs):
        return self(u"colorComposite", *args, **kwargs)

    def colorCondition(self, *args, **kwargs):
        return self(u"colorCondition", *args, **kwargs)

    def colorConstant(self, *args, **kwargs):
        return self(u"colorConstant", *args, **kwargs)

    def colorCorrect(self, *args, **kwargs):
        return self(u"colorCorrect", *args, **kwargs)

    def colorLogic(self, *args, **kwargs):
        return self(u"colorLogic", *args, **kwargs)

    def colorManagementGlobals(self, *args, **kwargs):
        return self(u"colorManagementGlobals", *args, **kwargs)

    def colorMask(self, *args, **kwargs):
        return self(u"colorMask", *args, **kwargs)

    def colorMath(self, *args, **kwargs):
        return self(u"colorMath", *args, **kwargs)

    def colorProfile(self, *args, **kwargs):
        return self(u"colorProfile", *args, **kwargs)

    def combinationShape(self, *args, **kwargs):
        return self(u"combinationShape", *args, **kwargs)

    def compactPlugArrayTest(self, *args, **kwargs):
        return self(u"compactPlugArrayTest", *args, **kwargs)

    def componentManip(self, *args, **kwargs):
        return self(u"componentManip", *args, **kwargs)

    def composeMatrix(self, *args, **kwargs):
        return self(u"composeMatrix", *args, **kwargs)

    def concentricProjManip(self, *args, **kwargs):
        return self(u"concentricProjManip", *args, **kwargs)

    def condition(self, *args, **kwargs):
        return self(u"condition", *args, **kwargs)

    def connectionOverride(self, *args, **kwargs):
        return self(u"connectionOverride", *args, **kwargs)

    def connectionUniqueOverride(self, *args, **kwargs):
        return self(u"connectionUniqueOverride", *args, **kwargs)

    def container(self, *args, **kwargs):
        return self(u"container", *args, **kwargs)

    def containerBase(self, *args, **kwargs):
        return self(u"containerBase", *args, **kwargs)

    def contourProjManip(self, *args, **kwargs):
        return self(u"contourProjManip", *args, **kwargs)

    def contrast(self, *args, **kwargs):
        return self(u"contrast", *args, **kwargs)

    def controller(self, *args, **kwargs):
        return self(u"controller", *args, **kwargs)

    def copyColorSet(self, *args, **kwargs):
        return self(u"copyColorSet", *args, **kwargs)

    def copyUVSet(self, *args, **kwargs):
        return self(u"copyUVSet", *args, **kwargs)

    def cpManip(self, *args, **kwargs):
        return self(u"cpManip", *args, **kwargs)

    def crater(self, *args, **kwargs):
        return self(u"crater", *args, **kwargs)

    def creaseSet(self, *args, **kwargs):
        return self(u"creaseSet", *args, **kwargs)

    def createBPManip(self, *args, **kwargs):
        return self(u"createBPManip", *args, **kwargs)

    def createCVManip(self, *args, **kwargs):
        return self(u"createCVManip", *args, **kwargs)

    def createColorSet(self, *args, **kwargs):
        return self(u"createColorSet", *args, **kwargs)

    def createEPManip(self, *args, **kwargs):
        return self(u"createEPManip", *args, **kwargs)

    def createPtexUV(self, *args, **kwargs):
        return self(u"createPtexUV", *args, **kwargs)

    def createUVSet(self, *args, **kwargs):
        return self(u"createUVSet", *args, **kwargs)

    def cubeManip(self, *args, **kwargs):
        return self(u"cubeManip", *args, **kwargs)

    def cubicProjManip(self, *args, **kwargs):
        return self(u"cubicProjManip", *args, **kwargs)

    def curveEdManip(self, *args, **kwargs):
        return self(u"curveEdManip", *args, **kwargs)

    def curveFromMeshCoM(self, *args, **kwargs):
        return self(u"curveFromMeshCoM", *args, **kwargs)

    def curveFromMeshEdge(self, *args, **kwargs):
        return self(u"curveFromMeshEdge", *args, **kwargs)

    def curveFromSubdivEdge(self, *args, **kwargs):
        return self(u"curveFromSubdivEdge", *args, **kwargs)

    def curveFromSubdivFace(self, *args, **kwargs):
        return self(u"curveFromSubdivFace", *args, **kwargs)

    def curveFromSurfaceBnd(self, *args, **kwargs):
        return self(u"curveFromSurfaceBnd", *args, **kwargs)

    def curveFromSurfaceCoS(self, *args, **kwargs):
        return self(u"curveFromSurfaceCoS", *args, **kwargs)

    def curveFromSurfaceIso(self, *args, **kwargs):
        return self(u"curveFromSurfaceIso", *args, **kwargs)

    def curveInfo(self, *args, **kwargs):
        return self(u"curveInfo", *args, **kwargs)

    def curveIntersect(self, *args, **kwargs):
        return self(u"curveIntersect", *args, **kwargs)

    def curveNormalizerAngle(self, *args, **kwargs):
        return self(u"curveNormalizerAngle", *args, **kwargs)

    def curveNormalizerLinear(self, *args, **kwargs):
        return self(u"curveNormalizerLinear", *args, **kwargs)

    def curveSegmentManip(self, *args, **kwargs):
        return self(u"curveSegmentManip", *args, **kwargs)

    def curveVarGroup(self, *args, **kwargs):
        return self(u"curveVarGroup", *args, **kwargs)

    def curveWarp(self, *args, **kwargs):
        return self(u"curveWarp", *args, **kwargs)

    def cylindricalProjManip(self, *args, **kwargs):
        return self(u"cylindricalProjManip", *args, **kwargs)

    def dagContainer(self, *args, **kwargs):
        return self(u"dagContainer", *args, **kwargs)

    def dagPose(self, *args, **kwargs):
        return self(u"dagPose", *args, **kwargs)

    def dataBlockTest(self, *args, **kwargs):
        return self(u"dataBlockTest", *args, **kwargs)

    def decomposeMatrix(self, *args, **kwargs):
        return self(u"decomposeMatrix", *args, **kwargs)

    def defaultLightList(self, *args, **kwargs):
        return self(u"defaultLightList", *args, **kwargs)

    def defaultRenderUtilityList(self, *args, **kwargs):
        return self(u"defaultRenderUtilityList", *args, **kwargs)

    def defaultRenderingList(self, *args, **kwargs):
        return self(u"defaultRenderingList", *args, **kwargs)

    def defaultShaderList(self, *args, **kwargs):
        return self(u"defaultShaderList", *args, **kwargs)

    def defaultTextureList(self, *args, **kwargs):
        return self(u"defaultTextureList", *args, **kwargs)

    def deformBend(self, *args, **kwargs):
        return self(u"deformBend", *args, **kwargs)

    def deformBendManip(self, *args, **kwargs):
        return self(u"deformBendManip", *args, **kwargs)

    def deformFlare(self, *args, **kwargs):
        return self(u"deformFlare", *args, **kwargs)

    def deformFlareManip(self, *args, **kwargs):
        return self(u"deformFlareManip", *args, **kwargs)

    def deformSine(self, *args, **kwargs):
        return self(u"deformSine", *args, **kwargs)

    def deformSineManip(self, *args, **kwargs):
        return self(u"deformSineManip", *args, **kwargs)

    def deformSquash(self, *args, **kwargs):
        return self(u"deformSquash", *args, **kwargs)

    def deformSquashManip(self, *args, **kwargs):
        return self(u"deformSquashManip", *args, **kwargs)

    def deformTwist(self, *args, **kwargs):
        return self(u"deformTwist", *args, **kwargs)

    def deformTwistManip(self, *args, **kwargs):
        return self(u"deformTwistManip", *args, **kwargs)

    def deformWave(self, *args, **kwargs):
        return self(u"deformWave", *args, **kwargs)

    def deformWaveManip(self, *args, **kwargs):
        return self(u"deformWaveManip", *args, **kwargs)

    def deleteColorSet(self, *args, **kwargs):
        return self(u"deleteColorSet", *args, **kwargs)

    def deleteComponent(self, *args, **kwargs):
        return self(u"deleteComponent", *args, **kwargs)

    def deleteUVSet(self, *args, **kwargs):
        return self(u"deleteUVSet", *args, **kwargs)

    def deltaMush(self, *args, **kwargs):
        return self(u"deltaMush", *args, **kwargs)

    def detachCurve(self, *args, **kwargs):
        return self(u"detachCurve", *args, **kwargs)

    def detachSurface(self, *args, **kwargs):
        return self(u"detachSurface", *args, **kwargs)

    def directedDisc(self, *args, **kwargs):
        return self(u"directedDisc", *args, **kwargs)

    def directionManip(self, *args, **kwargs):
        return self(u"directionManip", *args, **kwargs)

    def directionalLight(self, *args, **kwargs):
        return self(u"directionalLight", *args, **kwargs)

    def discManip(self, *args, **kwargs):
        return self(u"discManip", *args, **kwargs)

    def diskCache(self, *args, **kwargs):
        return self(u"diskCache", *args, **kwargs)

    def displacementShader(self, *args, **kwargs):
        return self(u"displacementShader", *args, **kwargs)

    def displayLayer(self, *args, **kwargs):
        return self(u"displayLayer", *args, **kwargs)

    def displayLayerManager(self, *args, **kwargs):
        return self(u"displayLayerManager", *args, **kwargs)

    def displayPoints(self, *args, **kwargs):
        return self(u"displayPoints", *args, **kwargs)

    def distanceBetween(self, *args, **kwargs):
        return self(u"distanceBetween", *args, **kwargs)

    def distanceDimShape(self, *args, **kwargs):
        return self(u"distanceDimShape", *args, **kwargs)

    def distanceManip(self, *args, **kwargs):
        return self(u"distanceManip", *args, **kwargs)

    def dof(self, *args, **kwargs):
        return self(u"dof", *args, **kwargs)

    def dofManip(self, *args, **kwargs):
        return self(u"dofManip", *args, **kwargs)

    def doubleShadingSwitch(self, *args, **kwargs):
        return self(u"doubleShadingSwitch", *args, **kwargs)

    def dpBirailSrf(self, *args, **kwargs):
        return self(u"dpBirailSrf", *args, **kwargs)

    def dragField(self, *args, **kwargs):
        return self(u"dragField", *args, **kwargs)

    def dropoffLocator(self, *args, **kwargs):
        return self(u"dropoffLocator", *args, **kwargs)

    def dropoffManip(self, *args, **kwargs):
        return self(u"dropoffManip", *args, **kwargs)

    def dynAttenuationManip(self, *args, **kwargs):
        return self(u"dynAttenuationManip", *args, **kwargs)

    def dynController(self, *args, **kwargs):
        return self(u"dynController", *args, **kwargs)

    def dynGlobals(self, *args, **kwargs):
        return self(u"dynGlobals", *args, **kwargs)

    def dynHolder(self, *args, **kwargs):
        return self(u"dynHolder", *args, **kwargs)

    def dynSpreadManip(self, *args, **kwargs):
        return self(u"dynSpreadManip", *args, **kwargs)

    def dynamicConstraint(self, *args, **kwargs):
        return self(u"dynamicConstraint", *args, **kwargs)

    def editMetadata(self, *args, **kwargs):
        return self(u"editMetadata", *args, **kwargs)

    def editsManager(self, *args, **kwargs):
        return self(u"editsManager", *args, **kwargs)

    def emitterManip(self, *args, **kwargs):
        return self(u"emitterManip", *args, **kwargs)

    def enableManip(self, *args, **kwargs):
        return self(u"enableManip", *args, **kwargs)

    def envBall(self, *args, **kwargs):
        return self(u"envBall", *args, **kwargs)

    def envChrome(self, *args, **kwargs):
        return self(u"envChrome", *args, **kwargs)

    def envCube(self, *args, **kwargs):
        return self(u"envCube", *args, **kwargs)

    def envFacade(self, *args, **kwargs):
        return self(u"envFacade", *args, **kwargs)

    def envFog(self, *args, **kwargs):
        return self(u"envFog", *args, **kwargs)

    def envSky(self, *args, **kwargs):
        return self(u"envSky", *args, **kwargs)

    def envSphere(self, *args, **kwargs):
        return self(u"envSphere", *args, **kwargs)

    def environmentFog(self, *args, **kwargs):
        return self(u"environmentFog", *args, **kwargs)

    def eulerToQuat(self, *args, **kwargs):
        return self(u"eulerToQuat", *args, **kwargs)

    def explodeNurbsShell(self, *args, **kwargs):
        return self(u"explodeNurbsShell", *args, **kwargs)

    def expression(self, *args, **kwargs):
        return self(u"expression", *args, **kwargs)

    def extendCurve(self, *args, **kwargs):
        return self(u"extendCurve", *args, **kwargs)

    def extendCurveDistanceManip(self, *args, **kwargs):
        return self(u"extendCurveDistanceManip", *args, **kwargs)

    def extendSurface(self, *args, **kwargs):
        return self(u"extendSurface", *args, **kwargs)

    def extendSurfaceDistanceManip(self, *args, **kwargs):
        return self(u"extendSurfaceDistanceManip", *args, **kwargs)

    def extrude(self, *args, **kwargs):
        return self(u"extrude", *args, **kwargs)

    def extrudeManip(self, *args, **kwargs):
        return self(u"extrudeManip", *args, **kwargs)

    def facade(self, *args, **kwargs):
        return self(u"facade", *args, **kwargs)

    def ffBlendSrf(self, *args, **kwargs):
        return self(u"ffBlendSrf", *args, **kwargs)

    def ffBlendSrfObsolete(self, *args, **kwargs):
        return self(u"ffBlendSrfObsolete", *args, **kwargs)

    def ffFilletSrf(self, *args, **kwargs):
        return self(u"ffFilletSrf", *args, **kwargs)

    def ffd(self, *args, **kwargs):
        return self(u"ffd", *args, **kwargs)

    def fieldManip(self, *args, **kwargs):
        return self(u"fieldManip", *args, **kwargs)

    def fieldsManip(self, *args, **kwargs):
        return self(u"fieldsManip", *args, **kwargs)

    def file(self, *args, **kwargs):
        return self(u"file", *args, **kwargs)

    def filletCurve(self, *args, **kwargs):
        return self(u"filletCurve", *args, **kwargs)

    def fitBspline(self, *args, **kwargs):
        return self(u"fitBspline", *args, **kwargs)

    def flexorShape(self, *args, **kwargs):
        return self(u"flexorShape", *args, **kwargs)

    def floatComposite(self, *args, **kwargs):
        return self(u"floatComposite", *args, **kwargs)

    def floatCondition(self, *args, **kwargs):
        return self(u"floatCondition", *args, **kwargs)

    def floatConstant(self, *args, **kwargs):
        return self(u"floatConstant", *args, **kwargs)

    def floatCorrect(self, *args, **kwargs):
        return self(u"floatCorrect", *args, **kwargs)

    def floatLogic(self, *args, **kwargs):
        return self(u"floatLogic", *args, **kwargs)

    def floatMask(self, *args, **kwargs):
        return self(u"floatMask", *args, **kwargs)

    def floatMath(self, *args, **kwargs):
        return self(u"floatMath", *args, **kwargs)

    def flow(self, *args, **kwargs):
        return self(u"flow", *args, **kwargs)

    def fluidEmitter(self, *args, **kwargs):
        return self(u"fluidEmitter", *args, **kwargs)

    def fluidShape(self, *args, **kwargs):
        return self(u"fluidShape", *args, **kwargs)

    def fluidSliceManip(self, *args, **kwargs):
        return self(u"fluidSliceManip", *args, **kwargs)

    def fluidTexture2D(self, *args, **kwargs):
        return self(u"fluidTexture2D", *args, **kwargs)

    def fluidTexture3D(self, *args, **kwargs):
        return self(u"fluidTexture3D", *args, **kwargs)

    def follicle(self, *args, **kwargs):
        return self(u"follicle", *args, **kwargs)

    def forceUpdateManip(self, *args, **kwargs):
        return self(u"forceUpdateManip", *args, **kwargs)

    def fosterParent(self, *args, **kwargs):
        return self(u"fosterParent", *args, **kwargs)

    def fourByFourMatrix(self, *args, **kwargs):
        return self(u"fourByFourMatrix", *args, **kwargs)

    def fractal(self, *args, **kwargs):
        return self(u"fractal", *args, **kwargs)

    def frameCache(self, *args, **kwargs):
        return self(u"frameCache", *args, **kwargs)

    def freePointManip(self, *args, **kwargs):
        return self(u"freePointManip", *args, **kwargs)

    def freePointTriadManip(self, *args, **kwargs):
        return self(u"freePointTriadManip", *args, **kwargs)

    def gameFbxExporter(self, *args, **kwargs):
        return self(u"gameFbxExporter", *args, **kwargs)

    def gammaCorrect(self, *args, **kwargs):
        return self(u"gammaCorrect", *args, **kwargs)

    def geoConnectable(self, *args, **kwargs):
        return self(u"geoConnectable", *args, **kwargs)

    def geoConnector(self, *args, **kwargs):
        return self(u"geoConnector", *args, **kwargs)

    def geomBind(self, *args, **kwargs):
        return self(u"geomBind", *args, **kwargs)

    def geometryConstraint(self, *args, **kwargs):
        return self(u"geometryConstraint", *args, **kwargs)

    def geometryFilter(self, *args, **kwargs):
        return self(u"geometryFilter", *args, **kwargs)

    def geometryOnLineManip(self, *args, **kwargs):
        return self(u"geometryOnLineManip", *args, **kwargs)

    def geometryVarGroup(self, *args, **kwargs):
        return self(u"geometryVarGroup", *args, **kwargs)

    def globalCacheControl(self, *args, **kwargs):
        return self(u"globalCacheControl", *args, **kwargs)

    def globalStitch(self, *args, **kwargs):
        return self(u"globalStitch", *args, **kwargs)

    def gpuCache(self, *args, **kwargs):
        return self(u"gpuCache", *args, **kwargs)

    def granite(self, *args, **kwargs):
        return self(u"granite", *args, **kwargs)

    def gravityField(self, *args, **kwargs):
        return self(u"gravityField", *args, **kwargs)

    def greasePencilSequence(self, *args, **kwargs):
        return self(u"greasePencilSequence", *args, **kwargs)

    def greasePlane(self, *args, **kwargs):
        return self(u"greasePlane", *args, **kwargs)

    def greasePlaneRenderShape(self, *args, **kwargs):
        return self(u"greasePlaneRenderShape", *args, **kwargs)

    def grid(self, *args, **kwargs):
        return self(u"grid", *args, **kwargs)

    def groupId(self, *args, **kwargs):
        return self(u"groupId", *args, **kwargs)

    def groupParts(self, *args, **kwargs):
        return self(u"groupParts", *args, **kwargs)

    def guide(self, *args, **kwargs):
        return self(u"guide", *args, **kwargs)

    def hairConstraint(self, *args, **kwargs):
        return self(u"hairConstraint", *args, **kwargs)

    def hairPhysicalShader(self, *args, **kwargs):
        return self(u"hairPhysicalShader", *args, **kwargs)

    def hairSystem(self, *args, **kwargs):
        return self(u"hairSystem", *args, **kwargs)

    def hairTubeShader(self, *args, **kwargs):
        return self(u"hairTubeShader", *args, **kwargs)

    def hardenPoint(self, *args, **kwargs):
        return self(u"hardenPoint", *args, **kwargs)

    def hardwareRenderGlobals(self, *args, **kwargs):
        return self(u"hardwareRenderGlobals", *args, **kwargs)

    def hardwareRenderingGlobals(self, *args, **kwargs):
        return self(u"hardwareRenderingGlobals", *args, **kwargs)

    def heightField(self, *args, **kwargs):
        return self(u"heightField", *args, **kwargs)

    def hierarchyTestNode1(self, *args, **kwargs):
        return self(u"hierarchyTestNode1", *args, **kwargs)

    def hierarchyTestNode2(self, *args, **kwargs):
        return self(u"hierarchyTestNode2", *args, **kwargs)

    def hierarchyTestNode3(self, *args, **kwargs):
        return self(u"hierarchyTestNode3", *args, **kwargs)

    def hikEffector(self, *args, **kwargs):
        return self(u"hikEffector", *args, **kwargs)

    def hikFKJoint(self, *args, **kwargs):
        return self(u"hikFKJoint", *args, **kwargs)

    def hikFloorContactMarker(self, *args, **kwargs):
        return self(u"hikFloorContactMarker", *args, **kwargs)

    def hikGroundPlane(self, *args, **kwargs):
        return self(u"hikGroundPlane", *args, **kwargs)

    def hikHandle(self, *args, **kwargs):
        return self(u"hikHandle", *args, **kwargs)

    def hikIKEffector(self, *args, **kwargs):
        return self(u"hikIKEffector", *args, **kwargs)

    def hikSolver(self, *args, **kwargs):
        return self(u"hikSolver", *args, **kwargs)

    def historySwitch(self, *args, **kwargs):
        return self(u"historySwitch", *args, **kwargs)

    def holdMatrix(self, *args, **kwargs):
        return self(u"holdMatrix", *args, **kwargs)

    def hsvToRgb(self, *args, **kwargs):
        return self(u"hsvToRgb", *args, **kwargs)

    def hwReflectionMap(self, *args, **kwargs):
        return self(u"hwReflectionMap", *args, **kwargs)

    def hwRenderGlobals(self, *args, **kwargs):
        return self(u"hwRenderGlobals", *args, **kwargs)

    def hyperGraphInfo(self, *args, **kwargs):
        return self(u"hyperGraphInfo", *args, **kwargs)

    def hyperLayout(self, *args, **kwargs):
        return self(u"hyperLayout", *args, **kwargs)

    def hyperView(self, *args, **kwargs):
        return self(u"hyperView", *args, **kwargs)

    def igBrushManip(self, *args, **kwargs):
        return self(u"igBrushManip", *args, **kwargs)

    def igmDescription(self, *args, **kwargs):
        return self(u"igmDescription", *args, **kwargs)

    def ik2Bsolver(self, *args, **kwargs):
        return self(u"ik2Bsolver", *args, **kwargs)

    def ikEffector(self, *args, **kwargs):
        return self(u"ikEffector", *args, **kwargs)

    def ikHandle(self, *args, **kwargs):
        return self(u"ikHandle", *args, **kwargs)

    def ikMCsolver(self, *args, **kwargs):
        return self(u"ikMCsolver", *args, **kwargs)

    def ikPASolver(self, *args, **kwargs):
        return self(u"ikPASolver", *args, **kwargs)

    def ikRPManip(self, *args, **kwargs):
        return self(u"ikRPManip", *args, **kwargs)

    def ikRPsolver(self, *args, **kwargs):
        return self(u"ikRPsolver", *args, **kwargs)

    def ikSCsolver(self, *args, **kwargs):
        return self(u"ikSCsolver", *args, **kwargs)

    def ikSplineManip(self, *args, **kwargs):
        return self(u"ikSplineManip", *args, **kwargs)

    def ikSplineSolver(self, *args, **kwargs):
        return self(u"ikSplineSolver", *args, **kwargs)

    def ikSpringSolver(self, *args, **kwargs):
        return self(u"ikSpringSolver", *args, **kwargs)

    def ikSystem(self, *args, **kwargs):
        return self(u"ikSystem", *args, **kwargs)

    def imagePlane(self, *args, **kwargs):
        return self(u"imagePlane", *args, **kwargs)

    def implicitBox(self, *args, **kwargs):
        return self(u"implicitBox", *args, **kwargs)

    def implicitCone(self, *args, **kwargs):
        return self(u"implicitCone", *args, **kwargs)

    def implicitSphere(self, *args, **kwargs):
        return self(u"implicitSphere", *args, **kwargs)

    def indexManip(self, *args, **kwargs):
        return self(u"indexManip", *args, **kwargs)

    def insertKnotCurve(self, *args, **kwargs):
        return self(u"insertKnotCurve", *args, **kwargs)

    def insertKnotSurface(self, *args, **kwargs):
        return self(u"insertKnotSurface", *args, **kwargs)

    def instancer(self, *args, **kwargs):
        return self(u"instancer", *args, **kwargs)

    def intersectSurface(self, *args, **kwargs):
        return self(u"intersectSurface", *args, **kwargs)

    def inverseMatrix(self, *args, **kwargs):
        return self(u"inverseMatrix", *args, **kwargs)

    def isoparmManip(self, *args, **kwargs):
        return self(u"isoparmManip", *args, **kwargs)

    def jiggle(self, *args, **kwargs):
        return self(u"jiggle", *args, **kwargs)

    def joint(self, *args, **kwargs):
        return self(u"joint", *args, **kwargs)

    def jointCluster(self, *args, **kwargs):
        return self(u"jointCluster", *args, **kwargs)

    def jointClusterManip(self, *args, **kwargs):
        return self(u"jointClusterManip", *args, **kwargs)

    def jointFfd(self, *args, **kwargs):
        return self(u"jointFfd", *args, **kwargs)

    def jointLattice(self, *args, **kwargs):
        return self(u"jointLattice", *args, **kwargs)

    def jointTranslateManip(self, *args, **kwargs):
        return self(u"jointTranslateManip", *args, **kwargs)

    def keyframeRegionManip(self, *args, **kwargs):
        return self(u"keyframeRegionManip", *args, **kwargs)

    def keyingGroup(self, *args, **kwargs):
        return self(u"keyingGroup", *args, **kwargs)

    def lambert(self, *args, **kwargs):
        return self(u"lambert", *args, **kwargs)

    def lattice(self, *args, **kwargs):
        return self(u"lattice", *args, **kwargs)

    def layeredShader(self, *args, **kwargs):
        return self(u"layeredShader", *args, **kwargs)

    def layeredTexture(self, *args, **kwargs):
        return self(u"layeredTexture", *args, **kwargs)

    def leastSquaresModifier(self, *args, **kwargs):
        return self(u"leastSquaresModifier", *args, **kwargs)

    def leather(self, *args, **kwargs):
        return self(u"leather", *args, **kwargs)

    def lightEditor(self, *args, **kwargs):
        return self(u"lightEditor", *args, **kwargs)

    def lightFog(self, *args, **kwargs):
        return self(u"lightFog", *args, **kwargs)

    def lightGroup(self, *args, **kwargs):
        return self(u"lightGroup", *args, **kwargs)

    def lightInfo(self, *args, **kwargs):
        return self(u"lightInfo", *args, **kwargs)

    def lightItem(self, *args, **kwargs):
        return self(u"lightItem", *args, **kwargs)

    def lightItemBase(self, *args, **kwargs):
        return self(u"lightItemBase", *args, **kwargs)

    def lightLinker(self, *args, **kwargs):
        return self(u"lightLinker", *args, **kwargs)

    def lightList(self, *args, **kwargs):
        return self(u"lightList", *args, **kwargs)

    def lightManip(self, *args, **kwargs):
        return self(u"lightManip", *args, **kwargs)

    def lightsChildCollection(self, *args, **kwargs):
        return self(u"lightsChildCollection", *args, **kwargs)

    def lightsCollection(self, *args, **kwargs):
        return self(u"lightsCollection", *args, **kwargs)

    def lightsCollectionSelector(self, *args, **kwargs):
        return self(u"lightsCollectionSelector", *args, **kwargs)

    def limitManip(self, *args, **kwargs):
        return self(u"limitManip", *args, **kwargs)

    def lineManip(self, *args, **kwargs):
        return self(u"lineManip", *args, **kwargs)

    def lineModifier(self, *args, **kwargs):
        return self(u"lineModifier", *args, **kwargs)

    def listItem(self, *args, **kwargs):
        return self(u"listItem", *args, **kwargs)

    def locator(self, *args, **kwargs):
        return self(u"locator", *args, **kwargs)

    def lodGroup(self, *args, **kwargs):
        return self(u"lodGroup", *args, **kwargs)

    def lodThresholds(self, *args, **kwargs):
        return self(u"lodThresholds", *args, **kwargs)

    def loft(self, *args, **kwargs):
        return self(u"loft", *args, **kwargs)

    def lookAt(self, *args, **kwargs):
        return self(u"lookAt", *args, **kwargs)

    def luminance(self, *args, **kwargs):
        return self(u"luminance", *args, **kwargs)

    def makeGroup(self, *args, **kwargs):
        return self(u"makeGroup", *args, **kwargs)

    def makeIllustratorCurves(self, *args, **kwargs):
        return self(u"makeIllustratorCurves", *args, **kwargs)

    def makeNurbCircle(self, *args, **kwargs):
        return self(u"makeNurbCircle", *args, **kwargs)

    def makeNurbCone(self, *args, **kwargs):
        return self(u"makeNurbCone", *args, **kwargs)

    def makeNurbCube(self, *args, **kwargs):
        return self(u"makeNurbCube", *args, **kwargs)

    def makeNurbCylinder(self, *args, **kwargs):
        return self(u"makeNurbCylinder", *args, **kwargs)

    def makeNurbPlane(self, *args, **kwargs):
        return self(u"makeNurbPlane", *args, **kwargs)

    def makeNurbSphere(self, *args, **kwargs):
        return self(u"makeNurbSphere", *args, **kwargs)

    def makeNurbTorus(self, *args, **kwargs):
        return self(u"makeNurbTorus", *args, **kwargs)

    def makeNurbsSquare(self, *args, **kwargs):
        return self(u"makeNurbsSquare", *args, **kwargs)

    def makeTextCurves(self, *args, **kwargs):
        return self(u"makeTextCurves", *args, **kwargs)

    def makeThreePointCircularArc(self, *args, **kwargs):
        return self(u"makeThreePointCircularArc", *args, **kwargs)

    def makeThreePointCircularArcManip(self, *args, **kwargs):
        return self(u"makeThreePointCircularArcManip", *args, **kwargs)

    def makeTwoPointCircularArc(self, *args, **kwargs):
        return self(u"makeTwoPointCircularArc", *args, **kwargs)

    def makeTwoPointCircularArcManip(self, *args, **kwargs):
        return self(u"makeTwoPointCircularArcManip", *args, **kwargs)

    def mandelbrot(self, *args, **kwargs):
        return self(u"mandelbrot", *args, **kwargs)

    def mandelbrot3D(self, *args, **kwargs):
        return self(u"mandelbrot3D", *args, **kwargs)

    def manip2DContainer(self, *args, **kwargs):
        return self(u"manip2DContainer", *args, **kwargs)

    def manipContainer(self, *args, **kwargs):
        return self(u"manipContainer", *args, **kwargs)

    def marble(self, *args, **kwargs):
        return self(u"marble", *args, **kwargs)

    def markerManip(self, *args, **kwargs):
        return self(u"markerManip", *args, **kwargs)

    def materialFacade(self, *args, **kwargs):
        return self(u"materialFacade", *args, **kwargs)

    def materialInfo(self, *args, **kwargs):
        return self(u"materialInfo", *args, **kwargs)

    def materialOverride(self, *args, **kwargs):
        return self(u"materialOverride", *args, **kwargs)

    def membrane(self, *args, **kwargs):
        return self(u"membrane", *args, **kwargs)

    def mesh(self, *args, **kwargs):
        return self(u"mesh", *args, **kwargs)

    def meshVarGroup(self, *args, **kwargs):
        return self(u"meshVarGroup", *args, **kwargs)

    def motionPath(self, *args, **kwargs):
        return self(u"motionPath", *args, **kwargs)

    def motionPathManip(self, *args, **kwargs):
        return self(u"motionPathManip", *args, **kwargs)

    def motionTrail(self, *args, **kwargs):
        return self(u"motionTrail", *args, **kwargs)

    def motionTrailShape(self, *args, **kwargs):
        return self(u"motionTrailShape", *args, **kwargs)

    def mountain(self, *args, **kwargs):
        return self(u"mountain", *args, **kwargs)

    def moveBezierHandleManip(self, *args, **kwargs):
        return self(u"moveBezierHandleManip", *args, **kwargs)

    def moveVertexManip(self, *args, **kwargs):
        return self(u"moveVertexManip", *args, **kwargs)

    def movie(self, *args, **kwargs):
        return self(u"movie", *args, **kwargs)

    def mpBirailSrf(self, *args, **kwargs):
        return self(u"mpBirailSrf", *args, **kwargs)

    def multDoubleLinear(self, *args, **kwargs):
        return self(u"multDoubleLinear", *args, **kwargs)

    def multMatrix(self, *args, **kwargs):
        return self(u"multMatrix", *args, **kwargs)

    def multilisterLight(self, *args, **kwargs):
        return self(u"multilisterLight", *args, **kwargs)

    def multiplyDivide(self, *args, **kwargs):
        return self(u"multiplyDivide", *args, **kwargs)

    def mute(self, *args, **kwargs):
        return self(u"mute", *args, **kwargs)

    def nCloth(self, *args, **kwargs):
        return self(u"nCloth", *args, **kwargs)

    def nComponent(self, *args, **kwargs):
        return self(u"nComponent", *args, **kwargs)

    def nParticle(self, *args, **kwargs):
        return self(u"nParticle", *args, **kwargs)

    def nRigid(self, *args, **kwargs):
        return self(u"nRigid", *args, **kwargs)

    def nearestPointOnCurve(self, *args, **kwargs):
        return self(u"nearestPointOnCurve", *args, **kwargs)

    def network(self, *args, **kwargs):
        return self(u"network", *args, **kwargs)

    def newtonField(self, *args, **kwargs):
        return self(u"newtonField", *args, **kwargs)

    def newtonManip(self, *args, **kwargs):
        return self(u"newtonManip", *args, **kwargs)

    def nexManip(self, *args, **kwargs):
        return self(u"nexManip", *args, **kwargs)

    def nodeGraphEditorBookmarkInfo(self, *args, **kwargs):
        return self(u"nodeGraphEditorBookmarkInfo", *args, **kwargs)

    def nodeGraphEditorBookmarks(self, *args, **kwargs):
        return self(u"nodeGraphEditorBookmarks", *args, **kwargs)

    def nodeGraphEditorInfo(self, *args, **kwargs):
        return self(u"nodeGraphEditorInfo", *args, **kwargs)

    def noise(self, *args, **kwargs):
        return self(u"noise", *args, **kwargs)

    def nonLinear(self, *args, **kwargs):
        return self(u"nonLinear", *args, **kwargs)

    def normalConstraint(self, *args, **kwargs):
        return self(u"normalConstraint", *args, **kwargs)

    def nucleus(self, *args, **kwargs):
        return self(u"nucleus", *args, **kwargs)

    def nurbsCurve(self, *args, **kwargs):
        return self(u"nurbsCurve", *args, **kwargs)

    def nurbsCurveToBezier(self, *args, **kwargs):
        return self(u"nurbsCurveToBezier", *args, **kwargs)

    def nurbsSurface(self, *args, **kwargs):
        return self(u"nurbsSurface", *args, **kwargs)

    def nurbsTessellate(self, *args, **kwargs):
        return self(u"nurbsTessellate", *args, **kwargs)

    def nurbsToSubdiv(self, *args, **kwargs):
        return self(u"nurbsToSubdiv", *args, **kwargs)

    def nurbsToSubdivProc(self, *args, **kwargs):
        return self(u"nurbsToSubdivProc", *args, **kwargs)

    def objectAttrFilter(self, *args, **kwargs):
        return self(u"objectAttrFilter", *args, **kwargs)

    def objectBinFilter(self, *args, **kwargs):
        return self(u"objectBinFilter", *args, **kwargs)

    def objectFilter(self, *args, **kwargs):
        return self(u"objectFilter", *args, **kwargs)

    def objectGrpToComp(self, *args, **kwargs):
        return self(u"objectGrpToComp", *args, **kwargs)

    def objectMultiFilter(self, *args, **kwargs):
        return self(u"objectMultiFilter", *args, **kwargs)

    def objectNameFilter(self, *args, **kwargs):
        return self(u"objectNameFilter", *args, **kwargs)

    def objectRenderFilter(self, *args, **kwargs):
        return self(u"objectRenderFilter", *args, **kwargs)

    def objectScriptFilter(self, *args, **kwargs):
        return self(u"objectScriptFilter", *args, **kwargs)

    def objectSet(self, *args, **kwargs):
        return self(u"objectSet", *args, **kwargs)

    def objectTypeFilter(self, *args, **kwargs):
        return self(u"objectTypeFilter", *args, **kwargs)

    def ocean(self, *args, **kwargs):
        return self(u"ocean", *args, **kwargs)

    def oceanShader(self, *args, **kwargs):
        return self(u"oceanShader", *args, **kwargs)

    def offsetCos(self, *args, **kwargs):
        return self(u"offsetCos", *args, **kwargs)

    def offsetCosManip(self, *args, **kwargs):
        return self(u"offsetCosManip", *args, **kwargs)

    def offsetCurve(self, *args, **kwargs):
        return self(u"offsetCurve", *args, **kwargs)

    def offsetCurveManip(self, *args, **kwargs):
        return self(u"offsetCurveManip", *args, **kwargs)

    def offsetDeformer(self, *args, **kwargs):
        return self(u"offsetDeformer", *args, **kwargs)

    def offsetSurface(self, *args, **kwargs):
        return self(u"offsetSurface", *args, **kwargs)

    def offsetSurfaceManip(self, *args, **kwargs):
        return self(u"offsetSurfaceManip", *args, **kwargs)

    def oldBlindDataBase(self, *args, **kwargs):
        return self(u"oldBlindDataBase", *args, **kwargs)

    def oldGeometryConstraint(self, *args, **kwargs):
        return self(u"oldGeometryConstraint", *args, **kwargs)

    def oldNormalConstraint(self, *args, **kwargs):
        return self(u"oldNormalConstraint", *args, **kwargs)

    def oldTangentConstraint(self, *args, **kwargs):
        return self(u"oldTangentConstraint", *args, **kwargs)

    def opticalFX(self, *args, **kwargs):
        return self(u"opticalFX", *args, **kwargs)

    def orientConstraint(self, *args, **kwargs):
        return self(u"orientConstraint", *args, **kwargs)

    def orientationMarker(self, *args, **kwargs):
        return self(u"orientationMarker", *args, **kwargs)

    def override(self, *args, **kwargs):
        return self(u"override", *args, **kwargs)

    def pairBlend(self, *args, **kwargs):
        return self(u"pairBlend", *args, **kwargs)

    def paramDimension(self, *args, **kwargs):
        return self(u"paramDimension", *args, **kwargs)

    def parentConstraint(self, *args, **kwargs):
        return self(u"parentConstraint", *args, **kwargs)

    def particle(self, *args, **kwargs):
        return self(u"particle", *args, **kwargs)

    def particleAgeMapper(self, *args, **kwargs):
        return self(u"particleAgeMapper", *args, **kwargs)

    def particleCloud(self, *args, **kwargs):
        return self(u"particleCloud", *args, **kwargs)

    def particleColorMapper(self, *args, **kwargs):
        return self(u"particleColorMapper", *args, **kwargs)

    def particleIncandMapper(self, *args, **kwargs):
        return self(u"particleIncandMapper", *args, **kwargs)

    def particleSamplerInfo(self, *args, **kwargs):
        return self(u"particleSamplerInfo", *args, **kwargs)

    def particleTranspMapper(self, *args, **kwargs):
        return self(u"particleTranspMapper", *args, **kwargs)

    def partition(self, *args, **kwargs):
        return self(u"partition", *args, **kwargs)

    def passContributionMap(self, *args, **kwargs):
        return self(u"passContributionMap", *args, **kwargs)

    def passMatrix(self, *args, **kwargs):
        return self(u"passMatrix", *args, **kwargs)

    def pfxHair(self, *args, **kwargs):
        return self(u"pfxHair", *args, **kwargs)

    def pfxToon(self, *args, **kwargs):
        return self(u"pfxToon", *args, **kwargs)

    def phong(self, *args, **kwargs):
        return self(u"phong", *args, **kwargs)

    def phongE(self, *args, **kwargs):
        return self(u"phongE", *args, **kwargs)

    def pivot2dManip(self, *args, **kwargs):
        return self(u"pivot2dManip", *args, **kwargs)

    def pivotAndOrientManip(self, *args, **kwargs):
        return self(u"pivotAndOrientManip", *args, **kwargs)

    def place2dTexture(self, *args, **kwargs):
        return self(u"place2dTexture", *args, **kwargs)

    def place3dTexture(self, *args, **kwargs):
        return self(u"place3dTexture", *args, **kwargs)

    def placerTool(self, *args, **kwargs):
        return self(u"placerTool", *args, **kwargs)

    def planarProjManip(self, *args, **kwargs):
        return self(u"planarProjManip", *args, **kwargs)

    def planarTrimSurface(self, *args, **kwargs):
        return self(u"planarTrimSurface", *args, **kwargs)

    def plusMinusAverage(self, *args, **kwargs):
        return self(u"plusMinusAverage", *args, **kwargs)

    def pointConstraint(self, *args, **kwargs):
        return self(u"pointConstraint", *args, **kwargs)

    def pointEmitter(self, *args, **kwargs):
        return self(u"pointEmitter", *args, **kwargs)

    def pointLight(self, *args, **kwargs):
        return self(u"pointLight", *args, **kwargs)

    def pointMatrixMult(self, *args, **kwargs):
        return self(u"pointMatrixMult", *args, **kwargs)

    def pointOnCurveInfo(self, *args, **kwargs):
        return self(u"pointOnCurveInfo", *args, **kwargs)

    def pointOnCurveManip(self, *args, **kwargs):
        return self(u"pointOnCurveManip", *args, **kwargs)

    def pointOnLineManip(self, *args, **kwargs):
        return self(u"pointOnLineManip", *args, **kwargs)

    def pointOnPolyConstraint(self, *args, **kwargs):
        return self(u"pointOnPolyConstraint", *args, **kwargs)

    def pointOnSurfManip(self, *args, **kwargs):
        return self(u"pointOnSurfManip", *args, **kwargs)

    def pointOnSurfaceInfo(self, *args, **kwargs):
        return self(u"pointOnSurfaceInfo", *args, **kwargs)

    def pointOnSurfaceManip(self, *args, **kwargs):
        return self(u"pointOnSurfaceManip", *args, **kwargs)

    def poleVectorConstraint(self, *args, **kwargs):
        return self(u"poleVectorConstraint", *args, **kwargs)

    def polyAppend(self, *args, **kwargs):
        return self(u"polyAppend", *args, **kwargs)

    def polyAppendVertex(self, *args, **kwargs):
        return self(u"polyAppendVertex", *args, **kwargs)

    def polyAutoProj(self, *args, **kwargs):
        return self(u"polyAutoProj", *args, **kwargs)

    def polyAutoProjManip(self, *args, **kwargs):
        return self(u"polyAutoProjManip", *args, **kwargs)

    def polyAverageVertex(self, *args, **kwargs):
        return self(u"polyAverageVertex", *args, **kwargs)

    def polyBevel(self, *args, **kwargs):
        return self(u"polyBevel", *args, **kwargs)

    def polyBevel2(self, *args, **kwargs):
        return self(u"polyBevel2", *args, **kwargs)

    def polyBevel3(self, *args, **kwargs):
        return self(u"polyBevel3", *args, **kwargs)

    def polyBlindData(self, *args, **kwargs):
        return self(u"polyBlindData", *args, **kwargs)

    def polyBoolOp(self, *args, **kwargs):
        return self(u"polyBoolOp", *args, **kwargs)

    def polyBridgeEdge(self, *args, **kwargs):
        return self(u"polyBridgeEdge", *args, **kwargs)

    def polyCBoolOp(self, *args, **kwargs):
        return self(u"polyCBoolOp", *args, **kwargs)

    def polyCaddyManip(self, *args, **kwargs):
        return self(u"polyCaddyManip", *args, **kwargs)

    def polyChipOff(self, *args, **kwargs):
        return self(u"polyChipOff", *args, **kwargs)

    def polyCircularize(self, *args, **kwargs):
        return self(u"polyCircularize", *args, **kwargs)

    def polyClean(self, *args, **kwargs):
        return self(u"polyClean", *args, **kwargs)

    def polyCloseBorder(self, *args, **kwargs):
        return self(u"polyCloseBorder", *args, **kwargs)

    def polyCollapseEdge(self, *args, **kwargs):
        return self(u"polyCollapseEdge", *args, **kwargs)

    def polyCollapseF(self, *args, **kwargs):
        return self(u"polyCollapseF", *args, **kwargs)

    def polyColorDel(self, *args, **kwargs):
        return self(u"polyColorDel", *args, **kwargs)

    def polyColorMod(self, *args, **kwargs):
        return self(u"polyColorMod", *args, **kwargs)

    def polyColorPerVertex(self, *args, **kwargs):
        return self(u"polyColorPerVertex", *args, **kwargs)

    def polyCone(self, *args, **kwargs):
        return self(u"polyCone", *args, **kwargs)

    def polyConnectComponents(self, *args, **kwargs):
        return self(u"polyConnectComponents", *args, **kwargs)

    def polyContourProj(self, *args, **kwargs):
        return self(u"polyContourProj", *args, **kwargs)

    def polyCopyUV(self, *args, **kwargs):
        return self(u"polyCopyUV", *args, **kwargs)

    def polyCrease(self, *args, **kwargs):
        return self(u"polyCrease", *args, **kwargs)

    def polyCreaseEdge(self, *args, **kwargs):
        return self(u"polyCreaseEdge", *args, **kwargs)

    def polyCreateFace(self, *args, **kwargs):
        return self(u"polyCreateFace", *args, **kwargs)

    def polyCreateToolManip(self, *args, **kwargs):
        return self(u"polyCreateToolManip", *args, **kwargs)

    def polyCube(self, *args, **kwargs):
        return self(u"polyCube", *args, **kwargs)

    def polyCut(self, *args, **kwargs):
        return self(u"polyCut", *args, **kwargs)

    def polyCutManip(self, *args, **kwargs):
        return self(u"polyCutManip", *args, **kwargs)

    def polyCutManipContainer(self, *args, **kwargs):
        return self(u"polyCutManipContainer", *args, **kwargs)

    def polyCylProj(self, *args, **kwargs):
        return self(u"polyCylProj", *args, **kwargs)

    def polyCylinder(self, *args, **kwargs):
        return self(u"polyCylinder", *args, **kwargs)

    def polyDelEdge(self, *args, **kwargs):
        return self(u"polyDelEdge", *args, **kwargs)

    def polyDelFacet(self, *args, **kwargs):
        return self(u"polyDelFacet", *args, **kwargs)

    def polyDelVertex(self, *args, **kwargs):
        return self(u"polyDelVertex", *args, **kwargs)

    def polyDisc(self, *args, **kwargs):
        return self(u"polyDisc", *args, **kwargs)

    def polyDuplicateEdge(self, *args, **kwargs):
        return self(u"polyDuplicateEdge", *args, **kwargs)

    def polyEdgeToCurve(self, *args, **kwargs):
        return self(u"polyEdgeToCurve", *args, **kwargs)

    def polyEditEdgeFlow(self, *args, **kwargs):
        return self(u"polyEditEdgeFlow", *args, **kwargs)

    def polyExtrudeEdge(self, *args, **kwargs):
        return self(u"polyExtrudeEdge", *args, **kwargs)

    def polyExtrudeFace(self, *args, **kwargs):
        return self(u"polyExtrudeFace", *args, **kwargs)

    def polyExtrudeVertex(self, *args, **kwargs):
        return self(u"polyExtrudeVertex", *args, **kwargs)

    def polyFlipEdge(self, *args, **kwargs):
        return self(u"polyFlipEdge", *args, **kwargs)

    def polyFlipUV(self, *args, **kwargs):
        return self(u"polyFlipUV", *args, **kwargs)

    def polyGear(self, *args, **kwargs):
        return self(u"polyGear", *args, **kwargs)

    def polyHelix(self, *args, **kwargs):
        return self(u"polyHelix", *args, **kwargs)

    def polyHoleFace(self, *args, **kwargs):
        return self(u"polyHoleFace", *args, **kwargs)

    def polyLayoutUV(self, *args, **kwargs):
        return self(u"polyLayoutUV", *args, **kwargs)

    def polyMapCut(self, *args, **kwargs):
        return self(u"polyMapCut", *args, **kwargs)

    def polyMapDel(self, *args, **kwargs):
        return self(u"polyMapDel", *args, **kwargs)

    def polyMapSew(self, *args, **kwargs):
        return self(u"polyMapSew", *args, **kwargs)

    def polyMapSewMove(self, *args, **kwargs):
        return self(u"polyMapSewMove", *args, **kwargs)

    def polyMappingManip(self, *args, **kwargs):
        return self(u"polyMappingManip", *args, **kwargs)

    def polyMergeEdge(self, *args, **kwargs):
        return self(u"polyMergeEdge", *args, **kwargs)

    def polyMergeFace(self, *args, **kwargs):
        return self(u"polyMergeFace", *args, **kwargs)

    def polyMergeUV(self, *args, **kwargs):
        return self(u"polyMergeUV", *args, **kwargs)

    def polyMergeVert(self, *args, **kwargs):
        return self(u"polyMergeVert", *args, **kwargs)

    def polyMergeVertsManip(self, *args, **kwargs):
        return self(u"polyMergeVertsManip", *args, **kwargs)

    def polyMirror(self, *args, **kwargs):
        return self(u"polyMirror", *args, **kwargs)

    def polyMirrorManipContainer(self, *args, **kwargs):
        return self(u"polyMirrorManipContainer", *args, **kwargs)

    def polyModifierManip(self, *args, **kwargs):
        return self(u"polyModifierManip", *args, **kwargs)

    def polyModifierManipContainer(self, *args, **kwargs):
        return self(u"polyModifierManipContainer", *args, **kwargs)

    def polyMoveEdge(self, *args, **kwargs):
        return self(u"polyMoveEdge", *args, **kwargs)

    def polyMoveFace(self, *args, **kwargs):
        return self(u"polyMoveFace", *args, **kwargs)

    def polyMoveFacetUV(self, *args, **kwargs):
        return self(u"polyMoveFacetUV", *args, **kwargs)

    def polyMoveUV(self, *args, **kwargs):
        return self(u"polyMoveUV", *args, **kwargs)

    def polyMoveUVManip(self, *args, **kwargs):
        return self(u"polyMoveUVManip", *args, **kwargs)

    def polyMoveVertex(self, *args, **kwargs):
        return self(u"polyMoveVertex", *args, **kwargs)

    def polyMoveVertexManip(self, *args, **kwargs):
        return self(u"polyMoveVertexManip", *args, **kwargs)

    def polyNormal(self, *args, **kwargs):
        return self(u"polyNormal", *args, **kwargs)

    def polyNormalPerVertex(self, *args, **kwargs):
        return self(u"polyNormalPerVertex", *args, **kwargs)

    def polyNormalizeUV(self, *args, **kwargs):
        return self(u"polyNormalizeUV", *args, **kwargs)

    def polyOptUvs(self, *args, **kwargs):
        return self(u"polyOptUvs", *args, **kwargs)

    def polyPassThru(self, *args, **kwargs):
        return self(u"polyPassThru", *args, **kwargs)

    def polyPinUV(self, *args, **kwargs):
        return self(u"polyPinUV", *args, **kwargs)

    def polyPipe(self, *args, **kwargs):
        return self(u"polyPipe", *args, **kwargs)

    def polyPlanarProj(self, *args, **kwargs):
        return self(u"polyPlanarProj", *args, **kwargs)

    def polyPlane(self, *args, **kwargs):
        return self(u"polyPlane", *args, **kwargs)

    def polyPlatonic(self, *args, **kwargs):
        return self(u"polyPlatonic", *args, **kwargs)

    def polyPlatonicSolid(self, *args, **kwargs):
        return self(u"polyPlatonicSolid", *args, **kwargs)

    def polyPoke(self, *args, **kwargs):
        return self(u"polyPoke", *args, **kwargs)

    def polyPokeManip(self, *args, **kwargs):
        return self(u"polyPokeManip", *args, **kwargs)

    def polyPrimitiveMisc(self, *args, **kwargs):
        return self(u"polyPrimitiveMisc", *args, **kwargs)

    def polyPrism(self, *args, **kwargs):
        return self(u"polyPrism", *args, **kwargs)

    def polyProj(self, *args, **kwargs):
        return self(u"polyProj", *args, **kwargs)

    def polyProjManip(self, *args, **kwargs):
        return self(u"polyProjManip", *args, **kwargs)

    def polyProjectCurve(self, *args, **kwargs):
        return self(u"polyProjectCurve", *args, **kwargs)

    def polyPyramid(self, *args, **kwargs):
        return self(u"polyPyramid", *args, **kwargs)

    def polyQuad(self, *args, **kwargs):
        return self(u"polyQuad", *args, **kwargs)

    def polyReduce(self, *args, **kwargs):
        return self(u"polyReduce", *args, **kwargs)

    def polyRemesh(self, *args, **kwargs):
        return self(u"polyRemesh", *args, **kwargs)

    def polyRetopo(self, *args, **kwargs):
        return self(u"polyRetopo", *args, **kwargs)

    def polySelectEditFeedbackManip(self, *args, **kwargs):
        return self(u"polySelectEditFeedbackManip", *args, **kwargs)

    def polySeparate(self, *args, **kwargs):
        return self(u"polySeparate", *args, **kwargs)

    def polySewEdge(self, *args, **kwargs):
        return self(u"polySewEdge", *args, **kwargs)

    def polySmooth(self, *args, **kwargs):
        return self(u"polySmooth", *args, **kwargs)

    def polySmoothFace(self, *args, **kwargs):
        return self(u"polySmoothFace", *args, **kwargs)

    def polySmoothProxy(self, *args, **kwargs):
        return self(u"polySmoothProxy", *args, **kwargs)

    def polySoftEdge(self, *args, **kwargs):
        return self(u"polySoftEdge", *args, **kwargs)

    def polySphProj(self, *args, **kwargs):
        return self(u"polySphProj", *args, **kwargs)

    def polySphere(self, *args, **kwargs):
        return self(u"polySphere", *args, **kwargs)

    def polySpinEdge(self, *args, **kwargs):
        return self(u"polySpinEdge", *args, **kwargs)

    def polySplit(self, *args, **kwargs):
        return self(u"polySplit", *args, **kwargs)

    def polySplitEdge(self, *args, **kwargs):
        return self(u"polySplitEdge", *args, **kwargs)

    def polySplitRing(self, *args, **kwargs):
        return self(u"polySplitRing", *args, **kwargs)

    def polySplitToolManip1(self, *args, **kwargs):
        return self(u"polySplitToolManip1", *args, **kwargs)

    def polySplitVert(self, *args, **kwargs):
        return self(u"polySplitVert", *args, **kwargs)

    def polyStraightenUVBorder(self, *args, **kwargs):
        return self(u"polyStraightenUVBorder", *args, **kwargs)

    def polySubdEdge(self, *args, **kwargs):
        return self(u"polySubdEdge", *args, **kwargs)

    def polySubdFace(self, *args, **kwargs):
        return self(u"polySubdFace", *args, **kwargs)

    def polySuperShape(self, *args, **kwargs):
        return self(u"polySuperShape", *args, **kwargs)

    def polyToSubdiv(self, *args, **kwargs):
        return self(u"polyToSubdiv", *args, **kwargs)

    def polyToolFeedbackManip(self, *args, **kwargs):
        return self(u"polyToolFeedbackManip", *args, **kwargs)

    def polyTorus(self, *args, **kwargs):
        return self(u"polyTorus", *args, **kwargs)

    def polyTransfer(self, *args, **kwargs):
        return self(u"polyTransfer", *args, **kwargs)

    def polyTriangulate(self, *args, **kwargs):
        return self(u"polyTriangulate", *args, **kwargs)

    def polyTweak(self, *args, **kwargs):
        return self(u"polyTweak", *args, **kwargs)

    def polyTweakUV(self, *args, **kwargs):
        return self(u"polyTweakUV", *args, **kwargs)

    def polyUVRectangle(self, *args, **kwargs):
        return self(u"polyUVRectangle", *args, **kwargs)

    def polyUnite(self, *args, **kwargs):
        return self(u"polyUnite", *args, **kwargs)

    def polyVertexNormalManip(self, *args, **kwargs):
        return self(u"polyVertexNormalManip", *args, **kwargs)

    def polyWedgeFace(self, *args, **kwargs):
        return self(u"polyWedgeFace", *args, **kwargs)

    def poseInterpolator(self, *args, **kwargs):
        return self(u"poseInterpolator", *args, **kwargs)

    def poseInterpolatorManager(self, *args, **kwargs):
        return self(u"poseInterpolatorManager", *args, **kwargs)

    def positionMarker(self, *args, **kwargs):
        return self(u"positionMarker", *args, **kwargs)

    def postProcessList(self, *args, **kwargs):
        return self(u"postProcessList", *args, **kwargs)

    def precompExport(self, *args, **kwargs):
        return self(u"precompExport", *args, **kwargs)

    def premultiply(self, *args, **kwargs):
        return self(u"premultiply", *args, **kwargs)

    def projectCurve(self, *args, **kwargs):
        return self(u"projectCurve", *args, **kwargs)

    def projectTangent(self, *args, **kwargs):
        return self(u"projectTangent", *args, **kwargs)

    def projectTangentManip(self, *args, **kwargs):
        return self(u"projectTangentManip", *args, **kwargs)

    def projection(self, *args, **kwargs):
        return self(u"projection", *args, **kwargs)

    def projectionManip(self, *args, **kwargs):
        return self(u"projectionManip", *args, **kwargs)

    def projectionMultiManip(self, *args, **kwargs):
        return self(u"projectionMultiManip", *args, **kwargs)

    def projectionUVManip(self, *args, **kwargs):
        return self(u"projectionUVManip", *args, **kwargs)

    def propModManip(self, *args, **kwargs):
        return self(u"propModManip", *args, **kwargs)

    def propMoveTriadManip(self, *args, **kwargs):
        return self(u"propMoveTriadManip", *args, **kwargs)

    def proxyManager(self, *args, **kwargs):
        return self(u"proxyManager", *args, **kwargs)

    def psdFileTex(self, *args, **kwargs):
        return self(u"psdFileTex", *args, **kwargs)

    def quadPtOnLineManip(self, *args, **kwargs):
        return self(u"quadPtOnLineManip", *args, **kwargs)

    def quadShadingSwitch(self, *args, **kwargs):
        return self(u"quadShadingSwitch", *args, **kwargs)

    def quatAdd(self, *args, **kwargs):
        return self(u"quatAdd", *args, **kwargs)

    def quatConjugate(self, *args, **kwargs):
        return self(u"quatConjugate", *args, **kwargs)

    def quatInvert(self, *args, **kwargs):
        return self(u"quatInvert", *args, **kwargs)

    def quatNegate(self, *args, **kwargs):
        return self(u"quatNegate", *args, **kwargs)

    def quatNormalize(self, *args, **kwargs):
        return self(u"quatNormalize", *args, **kwargs)

    def quatProd(self, *args, **kwargs):
        return self(u"quatProd", *args, **kwargs)

    def quatSub(self, *args, **kwargs):
        return self(u"quatSub", *args, **kwargs)

    def quatToEuler(self, *args, **kwargs):
        return self(u"quatToEuler", *args, **kwargs)

    def radialField(self, *args, **kwargs):
        return self(u"radialField", *args, **kwargs)

    def ramp(self, *args, **kwargs):
        return self(u"ramp", *args, **kwargs)

    def rampShader(self, *args, **kwargs):
        return self(u"rampShader", *args, **kwargs)

    def rbfSrf(self, *args, **kwargs):
        return self(u"rbfSrf", *args, **kwargs)

    def rbfSrfManip(self, *args, **kwargs):
        return self(u"rbfSrfManip", *args, **kwargs)

    def rebuildCurve(self, *args, **kwargs):
        return self(u"rebuildCurve", *args, **kwargs)

    def rebuildSurface(self, *args, **kwargs):
        return self(u"rebuildSurface", *args, **kwargs)

    def record(self, *args, **kwargs):
        return self(u"record", *args, **kwargs)

    def reference(self, *args, **kwargs):
        return self(u"reference", *args, **kwargs)

    def relOverride(self, *args, **kwargs):
        return self(u"relOverride", *args, **kwargs)

    def relUniqueOverride(self, *args, **kwargs):
        return self(u"relUniqueOverride", *args, **kwargs)

    def remapColor(self, *args, **kwargs):
        return self(u"remapColor", *args, **kwargs)

    def remapHsv(self, *args, **kwargs):
        return self(u"remapHsv", *args, **kwargs)

    def remapValue(self, *args, **kwargs):
        return self(u"remapValue", *args, **kwargs)

    def renderBox(self, *args, **kwargs):
        return self(u"renderBox", *args, **kwargs)

    def renderCone(self, *args, **kwargs):
        return self(u"renderCone", *args, **kwargs)

    def renderGlobals(self, *args, **kwargs):
        return self(u"renderGlobals", *args, **kwargs)

    def renderGlobalsList(self, *args, **kwargs):
        return self(u"renderGlobalsList", *args, **kwargs)

    def renderLayer(self, *args, **kwargs):
        return self(u"renderLayer", *args, **kwargs)

    def renderLayerManager(self, *args, **kwargs):
        return self(u"renderLayerManager", *args, **kwargs)

    def renderPass(self, *args, **kwargs):
        return self(u"renderPass", *args, **kwargs)

    def renderPassSet(self, *args, **kwargs):
        return self(u"renderPassSet", *args, **kwargs)

    def renderQuality(self, *args, **kwargs):
        return self(u"renderQuality", *args, **kwargs)

    def renderRect(self, *args, **kwargs):
        return self(u"renderRect", *args, **kwargs)

    def renderSettingsChildCollection(self, *args, **kwargs):
        return self(u"renderSettingsChildCollection", *args, **kwargs)

    def renderSettingsCollection(self, *args, **kwargs):
        return self(u"renderSettingsCollection", *args, **kwargs)

    def renderSetup(self, *args, **kwargs):
        return self(u"renderSetup", *args, **kwargs)

    def renderSetupLayer(self, *args, **kwargs):
        return self(u"renderSetupLayer", *args, **kwargs)

    def renderSphere(self, *args, **kwargs):
        return self(u"renderSphere", *args, **kwargs)

    def renderTarget(self, *args, **kwargs):
        return self(u"renderTarget", *args, **kwargs)

    def renderedImageSource(self, *args, **kwargs):
        return self(u"renderedImageSource", *args, **kwargs)

    def reorderUVSet(self, *args, **kwargs):
        return self(u"reorderUVSet", *args, **kwargs)

    def resolution(self, *args, **kwargs):
        return self(u"resolution", *args, **kwargs)

    def resultCurveTimeToAngular(self, *args, **kwargs):
        return self(u"resultCurveTimeToAngular", *args, **kwargs)

    def resultCurveTimeToLinear(self, *args, **kwargs):
        return self(u"resultCurveTimeToLinear", *args, **kwargs)

    def resultCurveTimeToTime(self, *args, **kwargs):
        return self(u"resultCurveTimeToTime", *args, **kwargs)

    def resultCurveTimeToUnitless(self, *args, **kwargs):
        return self(u"resultCurveTimeToUnitless", *args, **kwargs)

    def reverse(self, *args, **kwargs):
        return self(u"reverse", *args, **kwargs)

    def reverseCurve(self, *args, **kwargs):
        return self(u"reverseCurve", *args, **kwargs)

    def reverseCurveManip(self, *args, **kwargs):
        return self(u"reverseCurveManip", *args, **kwargs)

    def reverseSurface(self, *args, **kwargs):
        return self(u"reverseSurface", *args, **kwargs)

    def reverseSurfaceManip(self, *args, **kwargs):
        return self(u"reverseSurfaceManip", *args, **kwargs)

    def revolve(self, *args, **kwargs):
        return self(u"revolve", *args, **kwargs)

    def revolveManip(self, *args, **kwargs):
        return self(u"revolveManip", *args, **kwargs)

    def revolvedPrimitiveManip(self, *args, **kwargs):
        return self(u"revolvedPrimitiveManip", *args, **kwargs)

    def rgbToHsv(self, *args, **kwargs):
        return self(u"rgbToHsv", *args, **kwargs)

    def rigidBody(self, *args, **kwargs):
        return self(u"rigidBody", *args, **kwargs)

    def rigidConstraint(self, *args, **kwargs):
        return self(u"rigidConstraint", *args, **kwargs)

    def rigidSolver(self, *args, **kwargs):
        return self(u"rigidSolver", *args, **kwargs)

    def rock(self, *args, **kwargs):
        return self(u"rock", *args, **kwargs)

    def rotateHelper(self, *args, **kwargs):
        return self(u"rotateHelper", *args, **kwargs)

    def rotateLimitsManip(self, *args, **kwargs):
        return self(u"rotateLimitsManip", *args, **kwargs)

    def rotateManip(self, *args, **kwargs):
        return self(u"rotateManip", *args, **kwargs)

    def rotateUV2dManip(self, *args, **kwargs):
        return self(u"rotateUV2dManip", *args, **kwargs)

    def roundConstantRadius(self, *args, **kwargs):
        return self(u"roundConstantRadius", *args, **kwargs)

    def roundConstantRadiusManip(self, *args, **kwargs):
        return self(u"roundConstantRadiusManip", *args, **kwargs)

    def roundRadiusCrvManip(self, *args, **kwargs):
        return self(u"roundRadiusCrvManip", *args, **kwargs)

    def roundRadiusManip(self, *args, **kwargs):
        return self(u"roundRadiusManip", *args, **kwargs)

    def sampler(self, *args, **kwargs):
        return self(u"sampler", *args, **kwargs)

    def samplerInfo(self, *args, **kwargs):
        return self(u"samplerInfo", *args, **kwargs)

    def scaleConstraint(self, *args, **kwargs):
        return self(u"scaleConstraint", *args, **kwargs)

    def scaleLimitsManip(self, *args, **kwargs):
        return self(u"scaleLimitsManip", *args, **kwargs)

    def scaleManip(self, *args, **kwargs):
        return self(u"scaleManip", *args, **kwargs)

    def scaleUV2dManip(self, *args, **kwargs):
        return self(u"scaleUV2dManip", *args, **kwargs)

    def screenAlignedCircleManip(self, *args, **kwargs):
        return self(u"screenAlignedCircleManip", *args, **kwargs)

    def script(self, *args, **kwargs):
        return self(u"script", *args, **kwargs)

    def scriptManip(self, *args, **kwargs):
        return self(u"scriptManip", *args, **kwargs)

    def sculpt(self, *args, **kwargs):
        return self(u"sculpt", *args, **kwargs)

    def selectionListOperator(self, *args, **kwargs):
        return self(u"selectionListOperator", *args, **kwargs)

    def selector(self, *args, **kwargs):
        return self(u"selector", *args, **kwargs)

    def sequenceManager(self, *args, **kwargs):
        return self(u"sequenceManager", *args, **kwargs)

    def sequencer(self, *args, **kwargs):
        return self(u"sequencer", *args, **kwargs)

    def setRange(self, *args, **kwargs):
        return self(u"setRange", *args, **kwargs)

    def shaderGlow(self, *args, **kwargs):
        return self(u"shaderGlow", *args, **kwargs)

    def shaderOverride(self, *args, **kwargs):
        return self(u"shaderOverride", *args, **kwargs)

    def shadingEngine(self, *args, **kwargs):
        return self(u"shadingEngine", *args, **kwargs)

    def shadingMap(self, *args, **kwargs):
        return self(u"shadingMap", *args, **kwargs)

    def shapeEditorManager(self, *args, **kwargs):
        return self(u"shapeEditorManager", *args, **kwargs)

    def shellDeformer(self, *args, **kwargs):
        return self(u"shellDeformer", *args, **kwargs)

    def shellTessellate(self, *args, **kwargs):
        return self(u"shellTessellate", *args, **kwargs)

    def shot(self, *args, **kwargs):
        return self(u"shot", *args, **kwargs)

    def shrinkWrap(self, *args, **kwargs):
        return self(u"shrinkWrap", *args, **kwargs)

    def simpleSelector(self, *args, **kwargs):
        return self(u"simpleSelector", *args, **kwargs)

    def simpleTestNode(self, *args, **kwargs):
        return self(u"simpleTestNode", *args, **kwargs)

    def simpleVolumeShader(self, *args, **kwargs):
        return self(u"simpleVolumeShader", *args, **kwargs)

    def simplexNoise(self, *args, **kwargs):
        return self(u"simplexNoise", *args, **kwargs)

    def singleShadingSwitch(self, *args, **kwargs):
        return self(u"singleShadingSwitch", *args, **kwargs)

    def sketchPlane(self, *args, **kwargs):
        return self(u"sketchPlane", *args, **kwargs)

    def skinBinding(self, *args, **kwargs):
        return self(u"skinBinding", *args, **kwargs)

    def skinCluster(self, *args, **kwargs):
        return self(u"skinCluster", *args, **kwargs)

    def smoothCurve(self, *args, **kwargs):
        return self(u"smoothCurve", *args, **kwargs)

    def smoothTangentSrf(self, *args, **kwargs):
        return self(u"smoothTangentSrf", *args, **kwargs)

    def snapUV2dManip(self, *args, **kwargs):
        return self(u"snapUV2dManip", *args, **kwargs)

    def snapshot(self, *args, **kwargs):
        return self(u"snapshot", *args, **kwargs)

    def snapshotShape(self, *args, **kwargs):
        return self(u"snapshotShape", *args, **kwargs)

    def snow(self, *args, **kwargs):
        return self(u"snow", *args, **kwargs)

    def softMod(self, *args, **kwargs):
        return self(u"softMod", *args, **kwargs)

    def softModHandle(self, *args, **kwargs):
        return self(u"softModHandle", *args, **kwargs)

    def softModManip(self, *args, **kwargs):
        return self(u"softModManip", *args, **kwargs)

    def solidFractal(self, *args, **kwargs):
        return self(u"solidFractal", *args, **kwargs)

    def spBirailSrf(self, *args, **kwargs):
        return self(u"spBirailSrf", *args, **kwargs)

    def sphericalProjManip(self, *args, **kwargs):
        return self(u"sphericalProjManip", *args, **kwargs)

    def spotCylinderManip(self, *args, **kwargs):
        return self(u"spotCylinderManip", *args, **kwargs)

    def spotLight(self, *args, **kwargs):
        return self(u"spotLight", *args, **kwargs)

    def spotManip(self, *args, **kwargs):
        return self(u"spotManip", *args, **kwargs)

    def spring(self, *args, **kwargs):
        return self(u"spring", *args, **kwargs)

    def squareSrf(self, *args, **kwargs):
        return self(u"squareSrf", *args, **kwargs)

    def squareSrfManip(self, *args, **kwargs):
        return self(u"squareSrfManip", *args, **kwargs)

    def stencil(self, *args, **kwargs):
        return self(u"stencil", *args, **kwargs)

    def stereoRigCamera(self, *args, **kwargs):
        return self(u"stereoRigCamera", *args, **kwargs)

    def stitchAsNurbsShell(self, *args, **kwargs):
        return self(u"stitchAsNurbsShell", *args, **kwargs)

    def stitchSrf(self, *args, **kwargs):
        return self(u"stitchSrf", *args, **kwargs)

    def stitchSrfManip(self, *args, **kwargs):
        return self(u"stitchSrfManip", *args, **kwargs)

    def stroke(self, *args, **kwargs):
        return self(u"stroke", *args, **kwargs)

    def strokeGlobals(self, *args, **kwargs):
        return self(u"strokeGlobals", *args, **kwargs)

    def stucco(self, *args, **kwargs):
        return self(u"stucco", *args, **kwargs)

    def styleCurve(self, *args, **kwargs):
        return self(u"styleCurve", *args, **kwargs)

    def subCurve(self, *args, **kwargs):
        return self(u"subCurve", *args, **kwargs)

    def subSurface(self, *args, **kwargs):
        return self(u"subSurface", *args, **kwargs)

    def subdAddTopology(self, *args, **kwargs):
        return self(u"subdAddTopology", *args, **kwargs)

    def subdAutoProj(self, *args, **kwargs):
        return self(u"subdAutoProj", *args, **kwargs)

    def subdBlindData(self, *args, **kwargs):
        return self(u"subdBlindData", *args, **kwargs)

    def subdCleanTopology(self, *args, **kwargs):
        return self(u"subdCleanTopology", *args, **kwargs)

    def subdHierBlind(self, *args, **kwargs):
        return self(u"subdHierBlind", *args, **kwargs)

    def subdLayoutUV(self, *args, **kwargs):
        return self(u"subdLayoutUV", *args, **kwargs)

    def subdMapCut(self, *args, **kwargs):
        return self(u"subdMapCut", *args, **kwargs)

    def subdMapSewMove(self, *args, **kwargs):
        return self(u"subdMapSewMove", *args, **kwargs)

    def subdMappingManip(self, *args, **kwargs):
        return self(u"subdMappingManip", *args, **kwargs)

    def subdPlanarProj(self, *args, **kwargs):
        return self(u"subdPlanarProj", *args, **kwargs)

    def subdProjManip(self, *args, **kwargs):
        return self(u"subdProjManip", *args, **kwargs)

    def subdTweak(self, *args, **kwargs):
        return self(u"subdTweak", *args, **kwargs)

    def subdTweakUV(self, *args, **kwargs):
        return self(u"subdTweakUV", *args, **kwargs)

    def subdiv(self, *args, **kwargs):
        return self(u"subdiv", *args, **kwargs)

    def subdivCollapse(self, *args, **kwargs):
        return self(u"subdivCollapse", *args, **kwargs)

    def subdivComponentId(self, *args, **kwargs):
        return self(u"subdivComponentId", *args, **kwargs)

    def subdivReverseFaces(self, *args, **kwargs):
        return self(u"subdivReverseFaces", *args, **kwargs)

    def subdivSurfaceVarGroup(self, *args, **kwargs):
        return self(u"subdivSurfaceVarGroup", *args, **kwargs)

    def subdivToNurbs(self, *args, **kwargs):
        return self(u"subdivToNurbs", *args, **kwargs)

    def subdivToPoly(self, *args, **kwargs):
        return self(u"subdivToPoly", *args, **kwargs)

    def substance(self, *args, **kwargs):
        return self(u"substance", *args, **kwargs)

    def substanceOutput(self, *args, **kwargs):
        return self(u"substanceOutput", *args, **kwargs)

    def surfaceEdManip(self, *args, **kwargs):
        return self(u"surfaceEdManip", *args, **kwargs)

    def surfaceInfo(self, *args, **kwargs):
        return self(u"surfaceInfo", *args, **kwargs)

    def surfaceLuminance(self, *args, **kwargs):
        return self(u"surfaceLuminance", *args, **kwargs)

    def surfaceShader(self, *args, **kwargs):
        return self(u"surfaceShader", *args, **kwargs)

    def surfaceVarGroup(self, *args, **kwargs):
        return self(u"surfaceVarGroup", *args, **kwargs)

    def svgToPoly(self, *args, **kwargs):
        return self(u"svgToPoly", *args, **kwargs)

    def symmetryConstraint(self, *args, **kwargs):
        return self(u"symmetryConstraint", *args, **kwargs)

    def tangentConstraint(self, *args, **kwargs):
        return self(u"tangentConstraint", *args, **kwargs)

    def tension(self, *args, **kwargs):
        return self(u"tension", *args, **kwargs)

    def texLattice(self, *args, **kwargs):
        return self(u"texLattice", *args, **kwargs)

    def texLatticeDeformManip(self, *args, **kwargs):
        return self(u"texLatticeDeformManip", *args, **kwargs)

    def texMoveShellManip(self, *args, **kwargs):
        return self(u"texMoveShellManip", *args, **kwargs)

    def texSmoothManip(self, *args, **kwargs):
        return self(u"texSmoothManip", *args, **kwargs)

    def texSmudgeUVManip(self, *args, **kwargs):
        return self(u"texSmudgeUVManip", *args, **kwargs)

    def textButtonManip(self, *args, **kwargs):
        return self(u"textButtonManip", *args, **kwargs)

    def textManip2D(self, *args, **kwargs):
        return self(u"textManip2D", *args, **kwargs)

    def texture3dManip(self, *args, **kwargs):
        return self(u"texture3dManip", *args, **kwargs)

    def textureBakeSet(self, *args, **kwargs):
        return self(u"textureBakeSet", *args, **kwargs)

    def textureDeformer(self, *args, **kwargs):
        return self(u"textureDeformer", *args, **kwargs)

    def textureDeformerHandle(self, *args, **kwargs):
        return self(u"textureDeformerHandle", *args, **kwargs)

    def textureToGeom(self, *args, **kwargs):
        return self(u"textureToGeom", *args, **kwargs)

    def time(self, *args, **kwargs):
        return self(u"time", *args, **kwargs)

    def timeEditor(self, *args, **kwargs):
        return self(u"timeEditor", *args, **kwargs)

    def timeEditorAnimSource(self, *args, **kwargs):
        return self(u"timeEditorAnimSource", *args, **kwargs)

    def timeEditorClip(self, *args, **kwargs):
        return self(u"timeEditorClip", *args, **kwargs)

    def timeEditorClipBase(self, *args, **kwargs):
        return self(u"timeEditorClipBase", *args, **kwargs)

    def timeEditorClipEvaluator(self, *args, **kwargs):
        return self(u"timeEditorClipEvaluator", *args, **kwargs)

    def timeEditorInterpolator(self, *args, **kwargs):
        return self(u"timeEditorInterpolator", *args, **kwargs)

    def timeEditorTracks(self, *args, **kwargs):
        return self(u"timeEditorTracks", *args, **kwargs)

    def timeFunction(self, *args, **kwargs):
        return self(u"timeFunction", *args, **kwargs)

    def timeToUnitConversion(self, *args, **kwargs):
        return self(u"timeToUnitConversion", *args, **kwargs)

    def timeWarp(self, *args, **kwargs):
        return self(u"timeWarp", *args, **kwargs)

    def toggleManip(self, *args, **kwargs):
        return self(u"toggleManip", *args, **kwargs)

    def toggleOnLineManip(self, *args, **kwargs):
        return self(u"toggleOnLineManip", *args, **kwargs)

    def toolDrawManip(self, *args, **kwargs):
        return self(u"toolDrawManip", *args, **kwargs)

    def toolDrawManip2D(self, *args, **kwargs):
        return self(u"toolDrawManip2D", *args, **kwargs)

    def toonLineAttributes(self, *args, **kwargs):
        return self(u"toonLineAttributes", *args, **kwargs)

    def towPointOnCurveManip(self, *args, **kwargs):
        return self(u"towPointOnCurveManip", *args, **kwargs)

    def towPointOnSurfaceManip(self, *args, **kwargs):
        return self(u"towPointOnSurfaceManip", *args, **kwargs)

    def trackInfoManager(self, *args, **kwargs):
        return self(u"trackInfoManager", *args, **kwargs)

    def trans2dManip(self, *args, **kwargs):
        return self(u"trans2dManip", *args, **kwargs)

    def transUV2dManip(self, *args, **kwargs):
        return self(u"transUV2dManip", *args, **kwargs)

    def transferAttributes(self, *args, **kwargs):
        return self(u"transferAttributes", *args, **kwargs)

    def transform(self, *args, **kwargs):
        return self(u"transform", *args, **kwargs)

    def transformGeometry(self, *args, **kwargs):
        return self(u"transformGeometry", *args, **kwargs)

    def translateLimitsManip(self, *args, **kwargs):
        return self(u"translateLimitsManip", *args, **kwargs)

    def translateManip(self, *args, **kwargs):
        return self(u"translateManip", *args, **kwargs)

    def translateUVManip(self, *args, **kwargs):
        return self(u"translateUVManip", *args, **kwargs)

    def transposeMatrix(self, *args, **kwargs):
        return self(u"transposeMatrix", *args, **kwargs)

    def trim(self, *args, **kwargs):
        return self(u"trim", *args, **kwargs)

    def trimManip(self, *args, **kwargs):
        return self(u"trimManip", *args, **kwargs)

    def trimWithBoundaries(self, *args, **kwargs):
        return self(u"trimWithBoundaries", *args, **kwargs)

    def triplanarProjManip(self, *args, **kwargs):
        return self(u"triplanarProjManip", *args, **kwargs)

    def tripleShadingSwitch(self, *args, **kwargs):
        return self(u"tripleShadingSwitch", *args, **kwargs)

    def trsInsertManip(self, *args, **kwargs):
        return self(u"trsInsertManip", *args, **kwargs)

    def trsManip(self, *args, **kwargs):
        return self(u"trsManip", *args, **kwargs)

    def turbulenceField(self, *args, **kwargs):
        return self(u"turbulenceField", *args, **kwargs)

    def turbulenceManip(self, *args, **kwargs):
        return self(u"turbulenceManip", *args, **kwargs)

    def tweak(self, *args, **kwargs):
        return self(u"tweak", *args, **kwargs)

    def type(self, *args, **kwargs):
        return self(u"type", *args, **kwargs)

    def typeExtrude(self, *args, **kwargs):
        return self(u"typeExtrude", *args, **kwargs)

    def typeManip(self, *args, **kwargs):
        return self(u"typeManip", *args, **kwargs)

    def uniformField(self, *args, **kwargs):
        return self(u"uniformField", *args, **kwargs)

    def unitConversion(self, *args, **kwargs):
        return self(u"unitConversion", *args, **kwargs)

    def unitToTimeConversion(self, *args, **kwargs):
        return self(u"unitToTimeConversion", *args, **kwargs)

    def unknown(self, *args, **kwargs):
        return self(u"unknown", *args, **kwargs)

    def unknownDag(self, *args, **kwargs):
        return self(u"unknownDag", *args, **kwargs)

    def unknownTransform(self, *args, **kwargs):
        return self(u"unknownTransform", *args, **kwargs)

    def unpremultiply(self, *args, **kwargs):
        return self(u"unpremultiply", *args, **kwargs)

    def untrim(self, *args, **kwargs):
        return self(u"untrim", *args, **kwargs)

    def useBackground(self, *args, **kwargs):
        return self(u"useBackground", *args, **kwargs)

    def uv2dManip(self, *args, **kwargs):
        return self(u"uv2dManip", *args, **kwargs)

    def uvChooser(self, *args, **kwargs):
        return self(u"uvChooser", *args, **kwargs)

    def valueOverride(self, *args, **kwargs):
        return self(u"valueOverride", *args, **kwargs)

    def vectorAdjust(self, *args, **kwargs):
        return self(u"vectorAdjust", *args, **kwargs)

    def vectorExtrude(self, *args, **kwargs):
        return self(u"vectorExtrude", *args, **kwargs)

    def vectorProduct(self, *args, **kwargs):
        return self(u"vectorProduct", *args, **kwargs)

    def vectorRenderGlobals(self, *args, **kwargs):
        return self(u"vectorRenderGlobals", *args, **kwargs)

    def vertexBakeSet(self, *args, **kwargs):
        return self(u"vertexBakeSet", *args, **kwargs)

    def viewColorManager(self, *args, **kwargs):
        return self(u"viewColorManager", *args, **kwargs)

    def volumeAxisField(self, *args, **kwargs):
        return self(u"volumeAxisField", *args, **kwargs)

    def volumeBindManip(self, *args, **kwargs):
        return self(u"volumeBindManip", *args, **kwargs)

    def volumeFog(self, *args, **kwargs):
        return self(u"volumeFog", *args, **kwargs)

    def volumeLight(self, *args, **kwargs):
        return self(u"volumeLight", *args, **kwargs)

    def volumeNoise(self, *args, **kwargs):
        return self(u"volumeNoise", *args, **kwargs)

    def volumeShader(self, *args, **kwargs):
        return self(u"volumeShader", *args, **kwargs)

    def vortexField(self, *args, **kwargs):
        return self(u"vortexField", *args, **kwargs)

    def water(self, *args, **kwargs):
        return self(u"water", *args, **kwargs)

    def weightGeometryFilter(self, *args, **kwargs):
        return self(u"weightGeometryFilter", *args, **kwargs)

    def wire(self, *args, **kwargs):
        return self(u"wire", *args, **kwargs)

    def wood(self, *args, **kwargs):
        return self(u"wood", *args, **kwargs)

    def wrap(self, *args, **kwargs):
        return self(u"wrap", *args, **kwargs)

    def wtAddMatrix(self, *args, **kwargs):
        return self(u"wtAddMatrix", *args, **kwargs)

    def xformManip(self, *args, **kwargs):
        return self(u"xformManip", *args, **kwargs)

    def xgmArchiveGuide(self, *args, **kwargs):
        return self(u"xgmArchiveGuide", *args, **kwargs)

    def xgmCardGuide(self, *args, **kwargs):
        return self(u"xgmCardGuide", *args, **kwargs)

    def xgmConnectivity(self, *args, **kwargs):
        return self(u"xgmConnectivity", *args, **kwargs)

    def xgmCurveToSpline(self, *args, **kwargs):
        return self(u"xgmCurveToSpline", *args, **kwargs)

    def xgmDescription(self, *args, **kwargs):
        return self(u"xgmDescription", *args, **kwargs)

    def xgmGuide(self, *args, **kwargs):
        return self(u"xgmGuide", *args, **kwargs)

    def xgmGuideManip(self, *args, **kwargs):
        return self(u"xgmGuideManip", *args, **kwargs)

    def xgmGuideSculptManip(self, *args, **kwargs):
        return self(u"xgmGuideSculptManip", *args, **kwargs)

    def xgmHairMapping(self, *args, **kwargs):
        return self(u"xgmHairMapping", *args, **kwargs)

    def xgmMakeGuide(self, *args, **kwargs):
        return self(u"xgmMakeGuide", *args, **kwargs)

    def xgmModifierBase(self, *args, **kwargs):
        return self(u"xgmModifierBase", *args, **kwargs)

    def xgmModifierClump(self, *args, **kwargs):
        return self(u"xgmModifierClump", *args, **kwargs)

    def xgmModifierCollision(self, *args, **kwargs):
        return self(u"xgmModifierCollision", *args, **kwargs)

    def xgmModifierCut(self, *args, **kwargs):
        return self(u"xgmModifierCut", *args, **kwargs)

    def xgmModifierDisplacement(self, *args, **kwargs):
        return self(u"xgmModifierDisplacement", *args, **kwargs)

    def xgmModifierGuide(self, *args, **kwargs):
        return self(u"xgmModifierGuide", *args, **kwargs)

    def xgmModifierLinearWire(self, *args, **kwargs):
        return self(u"xgmModifierLinearWire", *args, **kwargs)

    def xgmModifierNoise(self, *args, **kwargs):
        return self(u"xgmModifierNoise", *args, **kwargs)

    def xgmModifierScale(self, *args, **kwargs):
        return self(u"xgmModifierScale", *args, **kwargs)

    def xgmModifierSculpt(self, *args, **kwargs):
        return self(u"xgmModifierSculpt", *args, **kwargs)

    def xgmNurbsPatch(self, *args, **kwargs):
        return self(u"xgmNurbsPatch", *args, **kwargs)

    def xgmPalette(self, *args, **kwargs):
        return self(u"xgmPalette", *args, **kwargs)

    def xgmPatch(self, *args, **kwargs):
        return self(u"xgmPatch", *args, **kwargs)

    def xgmPointsManip(self, *args, **kwargs):
        return self(u"xgmPointsManip", *args, **kwargs)

    def xgmPointsViewer(self, *args, **kwargs):
        return self(u"xgmPointsViewer", *args, **kwargs)

    def xgmSeExpr(self, *args, **kwargs):
        return self(u"xgmSeExpr", *args, **kwargs)

    def xgmSphereGuide(self, *args, **kwargs):
        return self(u"xgmSphereGuide", *args, **kwargs)

    def xgmSplineBase(self, *args, **kwargs):
        return self(u"xgmSplineBase", *args, **kwargs)

    def xgmSplineCache(self, *args, **kwargs):
        return self(u"xgmSplineCache", *args, **kwargs)

    def xgmSplineDescription(self, *args, **kwargs):
        return self(u"xgmSplineDescription", *args, **kwargs)

    def xgmSplineGuide(self, *args, **kwargs):
        return self(u"xgmSplineGuide", *args, **kwargs)

    def xgmSubdPatch(self, *args, **kwargs):
        return self(u"xgmSubdPatch", *args, **kwargs)


createNode = _CreateNode()
