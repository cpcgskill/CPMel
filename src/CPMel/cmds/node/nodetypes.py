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
CPMel.cmds模块节点类型定义
"""
import array

import maya.cmds as cmds
import maya.mel as mel

from . import basedata
from ...api import apiwrap
from ... import core as cmcore
from .nodedata import *
from .basedata import *
from ...api.OpenMaya import *
from ...api.OpenMayaAnim import *

__all__ = ["Transform", "MeshVtx", "MeshEdge", "MeshFace", "Mesh", "CurveCv", "Curve", "SurfaceCv", "Surface",
           "SkinCluster"]

ScriptUtil = MScriptUtil()


class Transform(DagNode):
    __metaclass__ = ObjectMetadef(MFn.kTransform)

    def __init__(self, obj=MObject, uuid=MUuid, uuid_s=u""):
        super(Transform, self).__init__(obj, uuid, uuid_s)
        # path = self.fn.dagPath()
        # int_p = ScriptUtil.asUintPtr()
        # path.numberOfShapesDirectlyBelow(int_p)
        # shape_size = ScriptUtil.getUint(int_p)
        # if shape_size > 0:
        #     path.extendToShapeDirectlyBelow(0)
        #     self.shape =  Global.objToNode(path.node())
        # else:
        #     self.shape = None

    def __getattribute__(self, item):
        u"""
        .访问操作

        :param item:
        :return:
        """
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            try:
                return self.attr(item)
            except cmcore.CPMelErrorBase:
                try:
                    return getattr(self.getShape(), item)
                except cmcore.CPMelErrorBase:
                    raise cmcore.CPMelError(u"找不到属性")

    def getShape(self, index=0):
        path = self.fn.dagPath()
        int_p = ScriptUtil.asUintPtr()
        path.numberOfShapesDirectlyBelow(int_p)
        shape_size = ScriptUtil.getUint(int_p)
        if shape_size > 0:
            path.extendToShapeDirectlyBelow(index)
            return Global.objToNode(path.node())
        else:
            raise cmcore.CPMelError(u"没有形状节点")

    def getShapes(self):
        path = self.fn.dagPath()
        int_p = ScriptUtil.asUintPtr()
        path.numberOfShapesDirectlyBelow(int_p)
        shape_size = ScriptUtil.getUint(int_p)
        if shape_size > 0:
            objs = list()
            for i in range(shape_size):
                path = self.fn.dagPath()
                path.extendToShapeDirectlyBelow(i)
                obj = self.Globalfunction.objToNode(path.node())
                objs.append(obj)
            return objs
        else:
            return []

    def cp__getFnClass(self):
        u"""
        获得当前函数集
        :return: MFn
        :rtype: MFnDependencyNode
        """
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnTransform(path)

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u"""
        返回节点这个类是否支持这个节点

        :param path: api1.0 MObject 指向一个节点的MObject
        :return: bool
        """
        return path.hasFn(MFn.kTransform)


class MeshVtx(Components1Base):
    components_type_str = "vtx"
    __metaclass__ = componentsTypesMetadef

    def cp__init_componenrs(self):
        dag, obj = self.Globalfunction.nameToMDagPath(self.compile())
        self.it = MItMeshVertex(dag, obj)

    @Components1Base.IsSingleComponent
    def verticesToFace(self):
        return self.node.verticesToFace(self.index)

    @Components1Base.IsSingleComponent
    def verticesToEdge(self):
        return self.node.verticesToEdge(self.index)

    @Components1Base.IsSingleComponent
    def verticesToVertices(self):
        return self.node.verticesToVertices(self.index)

    @Components1Base.IsSingleComponent
    def setPoint(self, point, space=basedata.Space.object):
        return self.node.setPoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getPoint(self.index, space)


class MeshEdge(Components1Base):
    components_type_str = "e"
    __metaclass__ = componentsTypesMetadef

    def cp__init_componenrs(self):
        dag, obj = self.Globalfunction.nameToMDagPath(self.compile())
        self.it = MItMeshEdge(dag, obj)

    @Components1Base.IsSingleComponent
    def edgeToFace(self):
        return self.node.edgeToFace(self.index)

    @Components1Base.IsSingleComponent
    def edgeToEdge(self):
        return self.node.edgeToEdge(self.index)

    @Components1Base.IsSingleComponent
    def edgeToVertices(self):
        return self.node.edgeToVertices(self.index)

    @Components1Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        # if not isinstance(point, MPoint):
        #     point = MPoint(point[0], point[1], point[2])
        # doIts = list()
        # undoIts = list()
        # for i in self.it:
        #     m_point = self.it.center(space)
        #     point0 = self.it.point(0, space)
        #     point1 = self.it.point(1, space)
        #     doIts.append(
        #             functools.partial(self.it.setPoint, point + (point0 - m_point), 0, space)
        #             )
        #     doIts.append(
        #             functools.partial(self.it.setPoint, point + (point1 - m_point), 1, space)
        #             )
        #     undoIts.append(
        #             functools.partial(self.it.setPoint, point0, 0, space)
        #             )
        #     undoIts.append(
        #             functools.partial(self.it.setPoint, point1, 1, space)
        #             )
        # doIts.append(self.it.updateSurface)
        # undoIts.append(self.it.updateSurface)
        # cmcore.addCommands(doIts, undoIts)
        return self.node.setEdgePoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.setEdgePoint(self.index, space)


class MeshFace(Components1Base):
    components_type_str = "f"
    __metaclass__ = componentsTypesMetadef

    @Components1Base.IsSingleComponent
    def faceToFace(self):
        return self.node.faceToFace(self.index)

    @Components1Base.IsSingleComponent
    def faceToEdge(self):
        return self.node.faceToEdge(self.index)

    @Components1Base.IsSingleComponent
    def faceToVertices(self):
        return self.node.faceToVertices(self.index)

    # def setPoint(self, point = basedata.Double3):
    #     pass
    @Components1Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        return self.node.setFacePoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getFacePoint(space)


class Mesh(DagNode):
    __metaclass__ = ObjectMetadef(MFn.kMesh)

    def __init__(self, *args):
        super(Mesh, self).__init__(*args)
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        self.it_vtx = MItMeshVertex(path)
        self.it_e = MItMeshEdge(path)
        self.it_f = MItMeshPolygon(path)
        self.vtx = MeshVtx(self)
        self.vtx.cp__init_componenrs()
        self.e = MeshEdge(self)
        self.e.cp__init_componenrs()
        self.f = MeshFace(self)
        self.f.cp__init_componenrs()

    def cp__getFnClass(self):
        u"""
        获得当前函数集
        :return: MFn
        """
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnMesh(path)

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u"""
        返回节点这个类是否支持这个节点

        :param path: api1.0 MObject 指向一个节点的MObject
        :return: bool
        """
        return path.hasFn(MFn.kMesh)

    #
    # def components__vtx(self, rang = None):
    #     return  Components1(self, MeshVtx, "vtx", rang)
    #
    # @property
    # def vtx(self):
    #     return self.components__vtx()

    @property
    def MeshVertex(self):
        return apiwrap.MeshVertex("%s.vtx[*]" % self.name())

    def vertexToFace(self, index=0):
        u"""
        获得连接到输入顶点的面

        :param index:
        :return:
        :rtype: list
        """
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_vtx.getConnectedFaces(ids)
        return basedata.IntArray(ids)

    def vertexToEdge(self, index=0):
        u"""
        获得连接到输入顶点的边

        :param index:
        :return:
        :rtype: list
        """
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_vtx.getConnectedEdges(ids)
        return basedata.IntArray(ids)

    def vertexTovertex(self, index=0):
        u"""
        获得围绕输入顶点的顶点

        :param index:
        :return:
        :rtype: list
        """
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_vtx.getConnectedVertices(ids)
        ids.append(index)
        return basedata.IntArray(ids)

    def edgeToFace(self, index=0):
        u"""
        获得连接的输入边的面

        :param index:
        :return:
        :rtype: list
        """
        self.it_e.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_e.getConnectedFaces(ids)
        return basedata.IntArray(ids)

    def edgeToEdge(self, index=0):
        u"""
        获得围绕输入边的边

        :param index:
        :return:
        :rtype: list
        """
        self.it_e.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_e.getConnectedEdges(ids)
        ids.append(index)
        return basedata.IntArray(ids)

    def edgeTovertex(self, index=0):
        u"""
        获得连接的输入边的顶点

        :param index:
        :return:
        :rtype: list
        """
        # self.node = Mesh
        # return MFnMesh()
        int_2_ptr = ScriptUtil.asInt2Ptr()
        self.fn.getEdgeVertices(index, int_2_ptr)
        ids = (ScriptUtil.getInt2ArrayItem(int_2_ptr, 0, 0),
               ScriptUtil.getInt2ArrayItem(int_2_ptr, 0, 1))
        return ids

    def faceToFace(self, index=0):
        u"""
        获得围绕输入面的面

        :param index:
        :return:
        :rtype: list
        """
        self.it_f.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_f.getConnectedFaces(ids)
        ids.append(index)
        return basedata.IntArray(ids)

    def faceToEdge(self, index=0):
        u"""
        获得连接的输入面的边

        :param index:
        :return:
        :rtype: list
        """
        self.it_f.setIndex(index, ScriptUtil.asIntPtr())
        idsa = MIntArray()
        self.it_f.getEdges(idsa)
        # idsb = MIntArray()
        # self.it_f.getConnectedEdges(idsb)
        # tuple((idsa.append(i) for i in idsb))
        return basedata.IntArray(idsa)

    def faceToVertex(self, index=0):
        u"""
        获得连接的输入面的顶点

        :param index:
        :return:
        :rtype: list
        """
        #
        # self.it_f.setIndex(index, ScriptUtil.asIntPtr())
        # ids = MIntArray()
        # self.it_f.getConnectedVertices(ids)
        return basedata.IntArray([t for i in self.faceToEdge(index) for t in self.edgeTovertex(i)])

    def VerticesIsBoundary(self, index):
        u"""
        检查输入的顶点是否为边界点

        :param index:
        :return:
        :rtype: list
        """
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        return self.it_vtx.onBoundary()

    def setPoint(self, index, point, space=basedata.Space.object):
        u"""
        设置顶点位置

        :param index: 顶点ID
        :param point: 位置参数
        :param space: 变换空间
        :return:
        """
        if not isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        unpoint = MPoint()
        self.fn.getPoint(index, unpoint, space)

        def doIt():
            self.functionSet().setPoint(index, point, space)

        def undoIt():
            self.functionSet().setPoint(index, unpoint, space)

        return cmcore.addCommand(doIt, undoIt)

    def getPoint(self, index, space=basedata.Space.object):
        u"""
        获得顶点位置

        :param index: 顶点ID
        :param space: 变换空间
        :return:
        :rtype:basedata.Double3
        """
        point = MPoint()
        self.fn.getPoint(index, point, space)
        return basedata.Double3(point)

    def setPoints(self, points, space=basedata.Space.object):
        u"""
        设置所有顶点位置

        :param points: 点位置列表
        :param space: 变换空间
        :return:
        """
        point_size = len(points)
        if len(points) != self.fn.numVertices():
            raise cmcore.CPMelError(u"输入的点数量与模型顶点数不一致")
        if not isinstance(points, MPointArray):
            m_points = MPointArray(point_size)
            [m_points.set(ID, i[0], i[1], i[2]) for ID, i in enumerate(points)]
            points = m_points
        unpoints = MPointArray()
        self.fn.getPoints(unpoints, space)

        def doIt():
            self.functionSet().setPoints(points, space)

        def undoIt():
            self.functionSet().setPoints(unpoints, space)

        return cmcore.addCommand(doIt, undoIt)

    def getPoints(self, space=basedata.Space.object):
        u"""
        获得所有顶点位置

        :param space: 变换空间
        :return: MPointArray
        """
        points = MPointArray()
        self.fn.getPoints(points, space)
        return basedata.NewDouble3s(points)

    def setEdgePoint(self, index=0, point=basedata.Double3, space=basedata.Space.object):
        u"""
        设置边位置
        :param index:
        :param point:
        :param space:
        :return:
        """
        if not isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        strat_id, end_id = self.edgeToVertices(index)
        strat_point = MPoint()
        self.fn.getPoint(strat_id, strat_point, space)
        end_point = MPoint()
        self.fn.getPoint(end_id, end_point, space)
        mid_point = (strat_point + end_point) * 0.5
        do_strat_point = (point + (strat_point - mid_point))
        do_end_point = (point + (end_point - mid_point))

        def doIt():
            fn = self.functionSet()
            fn.setPoint(strat_id, do_strat_point, space)
            fn.setPoint(end_id, do_end_point, space)

        def undoIt():
            fn = self.functionSet()
            fn.setPoint(strat_id, strat_point, space)
            fn.setPoint(end_id, end_point, space)

        return cmcore.addCommand(doIt, undoIt)

    def getEdgePoint(self, index=0, space=basedata.Space.object):
        u"""
        获得边位置

        :param index:
        :param space:
        :return:
        """
        strat_id, end_id = self.edgeToVertices(index)
        strat_point = self.getPoint(strat_id, space)
        end_point = self.getPoint(end_id, space)
        mid_point = (strat_point + end_point) * 0.5
        return basedata.Double3(mid_point)

    def setFacePoint(self, index=0, point=basedata.Double3, space=basedata.Space.object):
        u"""
        设置面位置

        :param index:
        :param point:
        :param space:
        :return:
        """
        if not isinstance(point, MVector):
            point = MVector(point[0], point[1], point[2])
        ids = self.faceToVertex(index)
        strat_points = list()
        for i in ids:
            strat_point = MPoint()
            self.fn.getPoint(i, strat_point, space)
            strat_points.append(strat_point)

        m_point = MPoint()
        for i in strat_points:
            m_point = i + m_point

        m_point = m_point / len(ids)

        end_points = list()
        for i in xrange(len(ids)):
            end_points.append(MPoint(strat_points[i] - m_point + point))

        def doIt():
            fn = self.functionSet()
            for i in xrange(len(ids)):
                fn.setPoint(ids[i], end_points[i], space)

        def undoIt():
            fn = self.functionSet()
            for i in xrange(len(ids)):
                fn.setPoint(ids[i], strat_points[i], space)

        return cmcore.addCommand(doIt, undoIt)

    def getFacePoint(self, index=0, space=basedata.Space.object):
        u"""
        获得面位置

        :param index:
        :param space:
        :return:
        """
        self.it_f.setIndex(index, ScriptUtil.asIntPtr())
        point = self.it_f.center(space)
        return basedata.Double3(point)

    def getClosestPointAndFace(self, point=basedata.Double3, space=basedata.Space.object):
        u"""
        获得最近点与最近面ID

        :param point: 输入的Double3
        :param space: 在什么空间下运行
        :return: Double3，面ID
        """
        if not isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        out_point = MPoint()
        closest_face_id = ScriptUtil.asIntPtr()
        self.fn.getClosestPoint(point, out_point, space, closest_face_id)
        return (basedata.Double3(out_point), ScriptUtil.getInt(closest_face_id))

    def getClosestPoitnAndVertices(self, point=basedata.Double3, space=basedata.Space.object):
        u"""
        返回最近点与最近顶点ID

        :param point: 输入的Double3
        :param space: 在什么空间下运行
        :return: Double3，点ID
        """
        if not isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        c_point = MPoint()
        closest_face_id = ScriptUtil.asIntPtr()
        self.fn.getClosestPoint(point, c_point, space, closest_face_id)
        faceid = ScriptUtil.getInt(closest_face_id)
        ids = MIntArray()
        self.fn.getPolygonVertices(faceid, ids)

        def _(i):
            pt = MPoint()
            self.fn.getPoint(i, pt, space)
            return point.distanceTo(pt)

        return (basedata.Double3(c_point), min(((i, _(i)) for i in ids), key=lambda i: i[1])[0])


class CurveCv(Components1Base):
    components_type_str = "cv"
    __metaclass__ = componentsTypesMetadef

    @Components1Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        return self.node.setPoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getPoint(self.index, space)


class Curve(DagNode):
    __metaclass__ = ObjectMetadef(MFn.kCurve)

    def __init__(self, *args):
        super(Curve, self).__init__(*args)
        self.cv = CurveCv(self)
        self.cv.cp__init_componenrs()

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u"""
        返回节点这个类是否支持这个节点

        :param path: api1.0 MObject 指向一个节点的MObject
        :return: bool
        """
        return path.hasFn(MFn.kCurve)

    def cp__getFnClass(self):
        u"""
        获得当前函数集
        :return: MFn
        """
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnNurbsCurve(path)

    def setPoint(self, index=0, point=basedata.Double3, space=basedata.Space.object):
        u"""
        设置指定CV点的位置

        :param index:
        :param point:
        :param space:
        :return:
        """
        if not isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        unpoint = MPoint()
        self.fn.getCV(index, unpoint)
        self.fn.setCV(index, point, space)

        def doIt():
            fn = self.functionSet()
            fn.setCV(index, point, space)
            fn.updateCurve()

        def undoIt():
            fn = self.functionSet()
            fn.setCV(index, unpoint, space)
            fn.updateCurve()

        return cmcore.addCommand(doIt, undoIt)

    def getPoint(self, index=0, space=basedata.Space.object):
        u"""
        获得CV点的位置

        :param index:
        :param space:
        :return:
        """
        point = MPoint()
        self.fn.getCV(index, point, space)
        return basedata.Double3(point)

    def setPoints(self, points, space=basedata.Space.object):
        u"""
        设置所有CV点的位置

        :param points:
        :param space:
        :return:
        """

        point_size = len(points)
        num_cvsize = self.numCvs()
        if len(points) != num_cvsize:
            raise cmcore.CPMelError(u"输入的点数量与曲线点数不一致")
        if not isinstance(points, MPointArray):
            m_points = MPointArray(point_size)
            [m_points.set(ID, i[0], i[1], i[2]) for ID, i in enumerate(points)]
            points = m_points
        un_points = MPointArray()
        self.fn.getCVs(un_points, space)

        def doIt():
            fn = self.functionSet()
            fn.setCVs(points, space)
            fn.updateCurve()

        def undoIt():
            fn = self.functionSet()
            fn.setCVs(un_points, space)
            fn.updateCurve()

        cmcore.addCommand(doIt, undoIt)

    def getPoints(self, space=basedata.Space.object):
        u"""
        获得所有CV点的位置

        :param space:
        :return:
        """
        points = MPointArray()
        self.fn.getCVs(points, space)
        return NewDouble3s(points)

    def numCvs(self):
        u"""
        返回此曲线的CV数

        :return:
        """
        return self.fn.numCVs()

    def numSpans(self):
        u"""
        返回此曲线的跨度数

        :return:
        """
        return self.fn.numSpans()

    def numKnots(self):
        u"""
        返回此曲线的结数

        :return:
        """
        return self.fn.numKnots()

    def degree(self):
        u"""
        返回此曲线的度数

        :return:
        """
        return self.fn.degree()

    def getPointAtParam(self, u, space=basedata.Space.object):
        u"""
        返回曲线上给定参数值处的空间点

        :param u:
        :param space:
        :return:
        """
        point = MPoint()
        self.fn.getPointAtParam(u, point, space)
        return basedata.Double3(point)

    def findLengthFromParam(self, u):
        u"""
        返回与曲线上给定参数值相对应的沿曲线的长度

        :param u:
        :return:
        """
        return self.fn.findLengthFromParam(u)

    def findParamFromLength(self, u):
        u"""
        返回与曲线上给定沿曲线的长度相对应的参数值

        :param u:
        :return:
        """
        return self.fn.findParamFromLength(u)

    def closestPoint(self, point=basedata.Double3, space=basedata.Space.object, tolerance=0.00001):
        u"""
        此方法确定曲线上最接近给定点的点。

        :param point: 测试点
        :param space: 指定此操作的坐标系
        :param tolerance: 计算中允许的误差量（ε值）
        :return:
        """
        if isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        u = ScriptUtil.asIntPtr()
        point = self.fn.closestPoint(point, u, tolerance, space)
        return (basedata.Double3(point), ScriptUtil.getInt(u))


class SurfaceCv(Components2Base):
    components_type_str = "cv"
    __metaclass__ = componentsTypesMetadef

    @Components2Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        return self.node.setPoint(self.indexu, self.indexv, point, space)

    @Components2Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getPoint(self.indexu, self.indexv, space)


class Surface(DagNode):
    __metaclass__ = ObjectMetadef(MFn.kNurbsSurface)

    def __init__(self, *args):
        super(Surface, self).__init__(*args)
        self.cv = SurfaceCv(self)
        self.cv.cp__init_componenrs()

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u"""
        返回节点这个类是否支持这个节点

        :param path: api1.0 MObject 指向一个节点的MObject
        :return: bool
        """
        return path.hasFn(MFn.kNurbsSurface)

    def cp__getFnClass(self):
        u"""
        获得当前函数集
        :return: MFn
        """
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnNurbsSurface(path)

    def setPoint(self, indexU=0, indexV=0, point=basedata.Double3, space=basedata.Space.object):
        u"""
        设置CV点位置

        :param indexU:
        :param indexV:
        :param point:
        :param space:
        :return:
        """
        if not isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        unpoint = MPoint()
        self.fn.getCV(indexU, indexV, unpoint, space)

        def doIt():
            fn = self.functionSet()
            fn.setCV(indexU, indexV, point, space)
            fn.updateSurface()

        def undoIt():
            fn = self.functionSet()
            fn.setCV(indexU, indexV, unpoint, space)
            fn.updateSurface()

        return cmcore.addCommand(doIt, undoIt)

    def getPoint(self, indexU=0, indexV=0, space=basedata.Space.object):
        u"""
        获得CV点位置

        :param indexU:
        :param indexV:
        :param space:
        :return:
        """
        point = MPoint()
        self.fn.getCV(indexU, indexV, point, space)
        return basedata.Double3(point)

    def numSpansInU(self):
        u"""
        返回u方向上的跨度数

        :return:
        """
        return self.fn.numSpansInU()

    def numSpansInV(self):
        u"""
        返回v方向上的跨度数

        :return:
        """
        return self.fn.numSpansInV()

    def numCVsInU(self):
        u"""
        返回U方向上的CV数量（度+跨度）

        :return:
        """
        return self.fn.numCVsInU()

    def numCVsInV(self):
        u"""
        返回V方向上的CV数量（度+跨度）

        :return:
        """
        return self.fn.numCVsInV()


class WeightGeometryFilter(DgNode):
    __metaclass__ = ObjectMetadef(MFn.kWeightGeometryFilt)

    def cp__getFnClass(self):
        u"""
        获得当前函数集
        :return: MFn
        """
        return MFnWeightGeometryFilter(self.obj)

    def getWeights(self, geo):
        u"""
        获得变形器权重

        :param geo: 组件 例:xxx.vtx
        :return:
        """
        geo = str(geo)
        if geo.find(".") < 0:
            raise cmcore.CPMelError(u"需要组件")
        # 建立一个组件选择列表
        sel_list = MSelectionList()
        try:
            sel_list.add(str(geo))
        except RuntimeError:
            raise cmcore.CPMelError(u"对象不存在")
        if int(sel_list.length()) > 1:
            raise cmcore.CPMelError(u"不在一个mesh或者其他对象上")
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)

        weights = MFloatArray()
        self.fn.getWeights(path, comp, weights)
        return FloatArray(weights)

    def setWeights(self, geo, weights):
        u"""
        设置变形器权重

        :param geo: 组件 例:xxx.vtx
        :param weights: 权重列表
        :return:
        """
        geo = str(geo)
        if geo.find(".") < 0:
            raise cmcore.CPMelError(u"需要组件")
        # 建立一个组件选择列表
        sel_list = MSelectionList()
        try:
            sel_list.add(str(geo))
        except RuntimeError:
            raise cmcore.CPMelError(u"对象不存在")
        if int(sel_list.length()) > 1:
            raise cmcore.CPMelError(u"不在一个mesh或者其他对象上")
        try:
            weights = FloatArray(weights)
        except TypeError:
            raise cmcore.CPMelError(u"weight 不是浮点数组")
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        m_weights = MFloatArray()
        un_weights = MFloatArray()
        tuple((m_weights.append(i) for i in weights))
        self.fn.getWeights(path, comp, un_weights)

        def doIt():
            self.functionSet().setWeight(path, comp, m_weights)

        def undoIt():
            self.functionSet().setWeight(path, comp, un_weights)

        cmcore.addCommand(doIt, undoIt)


class SkinCluster(WeightGeometryFilter):
    __metaclass__ = ObjectMetadef(MFn.kSkinClusterFilter)

    def cp__getFnClass(self):
        u"""
        获得当前函数集
        :return: MFn
        """
        return MFnSkinCluster(self.obj)

    @staticmethod
    def isCurrentNodeType(obj=MObject):
        u"""
        返回节点这个类是否支持这个节点

        :param obj: api1.0 MObject 指向一个节点的MObject
        :return: bool
        """
        return obj.hasFn(MFn.kSkinClusterFilter)

    def getPaint(self):
        u"""
        绘制权重

        :param weights:
        :return:
        """
        return cmds.getAttr(str(self) + ".paintWeights")

    def setPaint(self, weights):
        u"""
        绘制权重

        :param weights:
        :return:
        """
        return cmds.setAttr(str(self) + ".paintWeights", weights, type="doubleArray")

    paint = property(getPaint, setPaint)

    def rePaint(self):
        u"""
        重绘制权重

        :return:
        """
        ctx = cmds.currentCtx()
        if ctx == 'artAttrSkinContext':
            mel.eval(u"setSmoothSkinInfluence(\"%s\")" % cmds.artAttrSkinPaintCtx(ctx, q=True, inf=True))

    def getWeights(self, geo, inf):
        u"""
        获得骨骼蒙皮权重

        :param geo: 组件 例:xxx.vtx
        :param inf: 关节索引
        :return:
        :rtype:list
        """
        geo = str(geo)
        if geo.find(".") < 0:
            raise cmcore.CPMelError(u"需要组件")
        try:
            inf = basedata.IntArray(inf)
        except TypeError:
            raise cmcore.CPMelError(u"inf 不是整形数组")
        # 建立一个组件选择列表
        sel_list = MSelectionList()
        try:
            sel_list.add(str(geo))
        except RuntimeError:
            raise cmcore.CPMelError(u"对象不存在")
        if int(sel_list.length()) > 1:
            raise cmcore.CPMelError(u"不在一个mesh或者其他对象上")
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)

        m_inf = MIntArray()
        ScriptUtil.createIntArrayFromList(inf, m_inf)
        m_weigth = MDoubleArray()
        self.fn.getWeights(path, comp, m_inf, m_weigth)
        return FloatArray(m_weigth)

    def setWeights(self, geo, inf, weigths):
        u"""
        获得骨骼蒙皮权重

        :param geo: 组件 例:xxx.vtx
        :param inf: 关节索引
        :param weigths: 权重数组
        :return:
        """
        geo = str(geo)
        if geo.find(".") < 0:
            raise cmcore.CPMelError(u"需要组件")
        try:
            inf = FloatArray(inf)
        except TypeError:
            raise cmcore.CPMelError(u"inf 不是整形数组")
        try:
            weigths = FloatArray(weigths)
        except TypeError:
            raise cmcore.CPMelError(u"weight 不是浮点数组")
        # 建立一个组件选择列表
        sel_list = MSelectionList()
        try:
            sel_list.add(geo)
        except RuntimeError:
            raise cmcore.CPMelError(u"对象不存在")
        if int(sel_list.length()) > 1:
            raise cmcore.CPMelError(u"不在一个mesh或者其他对象上")
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)

        m_inf = MIntArray()
        ScriptUtil.createIntArrayFromList(inf, m_inf)
        m_weigth = MDoubleArray()
        tuple((m_weigth.append(i) for i in weigths))
        # # 撤销的权重

        # unWeights = MDoubleArray()
        # self.fn.getWeights(path, comp, unWeights, un_inf)
        un_weights = MDoubleArray()
        un_inf = MIntArray()
        test_dag_array = MDagPathArray()
        self.fn.influenceObjects(test_dag_array)
        tuple(
            (un_inf.append(i) for i in xrange(
                len(test_dag_array)
            )
             )
        )
        self.fn.setWeights(path, comp, m_inf, m_weigth, True, un_weights)

        def doIt():
            self.functionSet().setWeights(path, comp, m_inf, m_weigth)

        def undoIt():
            self.functionSet().setWeights(path, comp, un_inf, un_weights)

        cmcore.defAddCommandList(doIt, undoIt)
        return

    def getBlendWeights(self, geo):
        u"""
        获得权重已混合权重

        :param geo: 组件
        :return:
        :rtype:list
        """
        geo = str(geo)
        if geo.find(".") < 0:
            raise cmcore.CPMelError(u"需要组件")
        # 建立一个组件选择列表
        sel_list = MSelectionList()
        try:
            sel_list.add(geo)
        except RuntimeError:
            raise cmcore.CPMelError(u"对象不存在")
        if int(sel_list.length()) > 1:
            raise cmcore.CPMelError(u"不在一个mesh或者其他对象上")
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        un_weight = MDoubleArray()
        self.fn.getBlendWeights(path, comp, un_weight)
        return FloatArray(un_weight)

    def setBlendWeights(self, geo, weigth):
        u"""
        设置权重已混合权重

        :param geo: 组件
        :param weigth: 权重数组
        :return:
        """
        geo = str(geo)
        if geo.find(".") < 0:
            raise cmcore.CPMelError(u"需要组件")
        try:
            weigth = array.array("f", weigth)
        except TypeError:
            raise cmcore.CPMelError(u"weight 不是浮点数组")
        # 建立一个组件选择列表
        sel_list = MSelectionList()
        try:
            sel_list.add(geo)
        except RuntimeError:
            raise cmcore.CPMelError(u"对象不存在")
        if int(sel_list.length()) > 1:
            raise cmcore.CPMelError(u"不在一个mesh或者其他对象上")
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        m_weigth = MDoubleArray()
        tuple((m_weigth.append(i) for i in weigth))
        un_weight = MDoubleArray()
        self.fn.getBlendWeights(path, comp, un_weight)

        self.fn.setBlendWeights(path, comp, m_weigth)

        def doIt():
            self.functionSet().setBlendWeights(path, comp, m_weigth)

        def undoIt():
            self.functionSet().setBlendWeights(path, comp, un_weight)

        cmcore.defAddCommandList(doIt, undoIt)
        return
