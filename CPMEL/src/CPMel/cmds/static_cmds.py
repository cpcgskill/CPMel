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
"""
from . import node
from .node import commandWrap, uiCommandWrap
from . import FrontPackage as cmds
from .node.nodedata import DagNode, AttrObject, ArrayAttrObject, Components1Base, UIObject


def listWrap(fn):
    def _(*args, **kwargs):
        o = fn(*args, **kwargs)
        if o is None:
            return []
        return o

    _.__name__ = fn.__name__
    _.__doc__ = fn.__doc__
    return _

@commandWrap
def insertListItem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.insertListItem(*args, **kwargs)
@commandWrap
def RenderSequence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderSequence(*args, **kwargs)
@commandWrap
def lookThru(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lookThru(*args, **kwargs)
@commandWrap
def ClosestPointOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClosestPointOn(*args, **kwargs)
@commandWrap
def SurfaceFlow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceFlow(*args, **kwargs)
@commandWrap
def doubleProfileBirailSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.doubleProfileBirailSurface(*args, **kwargs)
@commandWrap
def NodeEditorRestoreLastClosedTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorRestoreLastClosedTab(*args, **kwargs)
@commandWrap
def NamespaceEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NamespaceEditor(*args, **kwargs)
@commandWrap
def pixelMove(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pixelMove(*args, **kwargs)
@commandWrap
def TexSculptDeactivateBrushStrength(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSculptDeactivateBrushStrength(*args, **kwargs)
@commandWrap
def RemoveWire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveWire(*args, **kwargs)
@commandWrap
def PolyExtrudeVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrudeVertices(*args, **kwargs)
@commandWrap
def DistributeShells(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DistributeShells(*args, **kwargs)
@commandWrap
def BevelPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BevelPolygon(*args, **kwargs)
@commandWrap
def IKHandleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IKHandleTool(*args, **kwargs)
@commandWrap
def geometryReplaceCacheFramesOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryReplaceCacheFramesOpt(*args, **kwargs)
@commandWrap
def SubstituteGeometryOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubstituteGeometryOptions(*args, **kwargs)
@commandWrap
def HypershadeDeleteAllCamerasAndImagePlanes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteAllCamerasAndImagePlanes(*args, **kwargs)
@commandWrap
def clearCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clearCache(*args, **kwargs)
@commandWrap
def dR_viewLeft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewLeft(*args, **kwargs)
@commandWrap
def XgmSetFreezeBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetFreezeBrushTool(*args, **kwargs)
@commandWrap
def CreateHairOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateHairOptions(*args, **kwargs)
@commandWrap
def SwapBlendShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SwapBlendShapeOptions(*args, **kwargs)
@commandWrap
def XgCreateIgSplineEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgCreateIgSplineEditor(*args, **kwargs)
@commandWrap
def polyDelVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyDelVertex(*args, **kwargs)
@commandWrap
def NodeEditorDeleteNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorDeleteNodes(*args, **kwargs)
@commandWrap
def SelectUVTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVTool(*args, **kwargs)
@commandWrap
def OutlinerToggleTimeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleTimeEditor(*args, **kwargs)
@commandWrap
def SeparatePolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SeparatePolygon(*args, **kwargs)
@commandWrap
def XgPreview(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgPreview(*args, **kwargs)
@commandWrap
def polyBoolOp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyBoolOp(*args, **kwargs)
@commandWrap
def SelectShortestEdgePathTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectShortestEdgePathTool(*args, **kwargs)
@commandWrap
def LightCentricLightLinkingEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LightCentricLightLinkingEditor(*args, **kwargs)
@commandWrap
def dR_gridAllTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_gridAllTGL(*args, **kwargs)
@commandWrap
def TogglePanZoomPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePanZoomPress(*args, **kwargs)
@commandWrap
def xformConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xformConstraint(*args, **kwargs)
@commandWrap
def copyKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.copyKey(*args, **kwargs)
@commandWrap
def CopySkinWeightsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopySkinWeightsOptions(*args, **kwargs)
@commandWrap
def NodeEditorGraphDownstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphDownstream(*args, **kwargs)
@commandWrap
def ProfilerToolCpuView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolCpuView(*args, **kwargs)
@commandWrap
def polyInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyInfo(*args, **kwargs)
@commandWrap
def ProfilerToolReset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolReset(*args, **kwargs)
@commandWrap
def dR_selectModeDisableTweakMarquee(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectModeDisableTweakMarquee(*args, **kwargs)
@commandWrap
def QualityDisplayMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.QualityDisplayMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def ShowControllers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowControllers(*args, **kwargs)
@commandWrap
def dR_moveTweakTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_moveTweakTool(*args, **kwargs)
@commandWrap
def ScaleKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleKeys(*args, **kwargs)
@commandWrap
def XgmSplineSelectReplaceBySelectedFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineSelectReplaceBySelectedFaces(*args, **kwargs)
@commandWrap
def PinSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PinSelection(*args, **kwargs)
@commandWrap
def PerspGraphOutlinerLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PerspGraphOutlinerLayout(*args, **kwargs)
@commandWrap
def CreateIllustratorCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateIllustratorCurves(*args, **kwargs)
@commandWrap
def UVPlanarProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVPlanarProjectionOptions(*args, **kwargs)
@commandWrap
def DoUnghost(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DoUnghost(*args, **kwargs)
@commandWrap
def AddOceanPreviewPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddOceanPreviewPlane(*args, **kwargs)
@commandWrap
def BreakLightLinks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BreakLightLinks(*args, **kwargs)
@commandWrap
def CreateContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateContainerOptions(*args, **kwargs)
@commandWrap
def CreateClusterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateClusterOptions(*args, **kwargs)
@commandWrap
def softSelectOptionsCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.softSelectOptionsCtx(*args, **kwargs)
@commandWrap
def AddFaceDivisionsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddFaceDivisionsOptions(*args, **kwargs)
@commandWrap
def ctxTraverse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ctxTraverse(*args, **kwargs)
@commandWrap
def TangentsClamped(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsClamped(*args, **kwargs)
@commandWrap
def dR_extrudeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_extrudeTool(*args, **kwargs)
@commandWrap
def ToggleIKHandleSnap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleIKHandleSnap(*args, **kwargs)
@commandWrap
def HypershadeRefreshAllSwatchesOnDisk(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRefreshAllSwatchesOnDisk(*args, **kwargs)
@commandWrap
def CreateAreaLightOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateAreaLightOptions(*args, **kwargs)
@commandWrap
def dR_curveSnapPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_curveSnapPress(*args, **kwargs)
@commandWrap
def dR_nexCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_nexCmd(*args, **kwargs)
@commandWrap
def PreInfinityCycleOffset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreInfinityCycleOffset(*args, **kwargs)
@commandWrap
def polyPipe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPipe(*args, **kwargs)
@commandWrap
def xgmBindPatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmBindPatches(*args, **kwargs)
@commandWrap
def TogglePaintAtDepth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePaintAtDepth(*args, **kwargs)
@commandWrap
def CreatePond(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePond(*args, **kwargs)
@commandWrap
def bevelPlus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bevelPlus(*args, **kwargs)
@commandWrap
def AddBlendShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBlendShapeOptions(*args, **kwargs)
@commandWrap
def BatchRenderOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BatchRenderOptions(*args, **kwargs)
@commandWrap
def adskAssetListUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.adskAssetListUI(*args, **kwargs)
@commandWrap
def tangentConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.tangentConstraint(*args, **kwargs)
@commandWrap
def dispatchGenericCommand(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dispatchGenericCommand(*args, **kwargs)
@commandWrap
def renderSetup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetup(*args, **kwargs)
@commandWrap
def HypershadeGraphClearGraph(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphClearGraph(*args, **kwargs)
@commandWrap
def XgmSetSmoothBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetSmoothBrushTool(*args, **kwargs)
@commandWrap
def CreatePolygonSVG(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSVG(*args, **kwargs)
@commandWrap
def EnterEditModeRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnterEditModeRelease(*args, **kwargs)
@commandWrap
def hide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hide(*args, **kwargs)
@commandWrap
def itemFilterType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.itemFilterType(*args, **kwargs)
@commandWrap
def RandomizeFolliclesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RandomizeFolliclesOptions(*args, **kwargs)
@commandWrap
def suitePrefs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.suitePrefs(*args, **kwargs)
@commandWrap
def OpenScene(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OpenScene(*args, **kwargs)
@commandWrap
def DeleteSelectedContainers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteSelectedContainers(*args, **kwargs)
@commandWrap
def WarpImageOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WarpImageOptions(*args, **kwargs)
@commandWrap
def SelectSimilarOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectSimilarOptions(*args, **kwargs)
@commandWrap
def XgmSplineCacheReplace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheReplace(*args, **kwargs)
@commandWrap
def StitchEdgesToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StitchEdgesToolOptions(*args, **kwargs)
@commandWrap
def allNodeTypes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.allNodeTypes(*args, **kwargs)
@commandWrap
def dR_targetWeldPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_targetWeldPress(*args, **kwargs)
@commandWrap
def GoalOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoalOptions(*args, **kwargs)
@commandWrap
def nurbsUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsUVSet(*args, **kwargs)
@commandWrap
def NodeEditorRedockTornOffTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorRedockTornOffTab(*args, **kwargs)
@commandWrap
def SelectAllLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllLights(*args, **kwargs)
@commandWrap
def CreateEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateEmitter(*args, **kwargs)
@commandWrap
def CombinePolygons(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CombinePolygons(*args, **kwargs)
@commandWrap
def Create2DContainerEmitterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create2DContainerEmitterOptions(*args, **kwargs)
@commandWrap
def AddKeysToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddKeysToolOptions(*args, **kwargs)
@commandWrap
def duplicateSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.duplicateSurface(*args, **kwargs)
@commandWrap
def CreatePolygonCubeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonCubeOptions(*args, **kwargs)
@commandWrap
def IntersectCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IntersectCurve(*args, **kwargs)
@commandWrap
def nClothDeleteHistory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothDeleteHistory(*args, **kwargs)
@commandWrap
def SewUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SewUVs(*args, **kwargs)
@commandWrap
def SelectUVOverlappingComponentsPerObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVOverlappingComponentsPerObject(*args, **kwargs)
@commandWrap
def PruneWire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PruneWire(*args, **kwargs)
@commandWrap
def TimeEditorUnmuteAllTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorUnmuteAllTracks(*args, **kwargs)
@commandWrap
def ShowHotbox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowHotbox(*args, **kwargs)
@commandWrap
def cacheFileTrack(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cacheFileTrack(*args, **kwargs)
@commandWrap
def FBXResetImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXResetImport(*args, **kwargs)
@commandWrap
def GhostObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GhostObject(*args, **kwargs)
@commandWrap
def NodeEditorPickWalkUp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPickWalkUp(*args, **kwargs)
@commandWrap
def TimeEditorMuteSelectedTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorMuteSelectedTracks(*args, **kwargs)
@commandWrap
def RemoveBlendShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBlendShape(*args, **kwargs)
@commandWrap
def ThreeBottomSplitViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ThreeBottomSplitViewArrangement(*args, **kwargs)
@commandWrap
def NodeEditorGridToggleVisibility(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGridToggleVisibility(*args, **kwargs)
@commandWrap
def FullHotboxDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FullHotboxDisplay(*args, **kwargs)
@commandWrap
def LayerRelationshipEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LayerRelationshipEditor(*args, **kwargs)
@commandWrap
def CreatePolygonCone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonCone(*args, **kwargs)
@commandWrap
def BufferCurveSnapshot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BufferCurveSnapshot(*args, **kwargs)
@commandWrap
def ProjectTangent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProjectTangent(*args, **kwargs)
@commandWrap
def curveOnSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveOnSurface(*args, **kwargs)
@commandWrap
def DeltaMush(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeltaMush(*args, **kwargs)
@commandWrap
def ConvertSelectionToVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToVertices(*args, **kwargs)
@commandWrap
def RoundTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RoundTool(*args, **kwargs)
@commandWrap
def HideFluids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideFluids(*args, **kwargs)
@commandWrap
def ProjectCurveOnSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProjectCurveOnSurfaceOptions(*args, **kwargs)
@commandWrap
def notifyPostRedo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.notifyPostRedo(*args, **kwargs)
@commandWrap
def Group(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Group(*args, **kwargs)
@commandWrap
def setInputDeviceMapping(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setInputDeviceMapping(*args, **kwargs)
@commandWrap
def ToggleToolbox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleToolbox(*args, **kwargs)
@commandWrap
def CreatePolygonUltraShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonUltraShape(*args, **kwargs)
@commandWrap
def shapePanel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shapePanel(*args, **kwargs)
@commandWrap
def DeleteChannels(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteChannels(*args, **kwargs)
@commandWrap
def PublishNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishNode(*args, **kwargs)
@commandWrap
def NodeEditorReduceTraversalDepth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorReduceTraversalDepth(*args, **kwargs)
@commandWrap
def ShowDeformers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowDeformers(*args, **kwargs)
@commandWrap
def IPRRenderIntoNewWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IPRRenderIntoNewWindow(*args, **kwargs)
@commandWrap
def InteractiveBindSkinOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InteractiveBindSkinOptions(*args, **kwargs)
@commandWrap
def LassoTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LassoTool(*args, **kwargs)
@commandWrap
def FlareOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FlareOptions(*args, **kwargs)
@commandWrap
def particleInstancer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.particleInstancer(*args, **kwargs)
@commandWrap
def cMuscleWeightPrune(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleWeightPrune(*args, **kwargs)
@commandWrap
def ProfilerToolToggleRecording(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolToggleRecording(*args, **kwargs)
@commandWrap
def AttachCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachCurve(*args, **kwargs)
@commandWrap
def createPtexUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPtexUV(*args, **kwargs)
@commandWrap
def FilePathEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FilePathEditor(*args, **kwargs)
@commandWrap
def HideUnselectedCVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideUnselectedCVs(*args, **kwargs)
@commandWrap
def adskSceneMetadataCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.adskSceneMetadataCmd(*args, **kwargs)
@commandWrap
def addMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.addMetadata(*args, **kwargs)
@commandWrap
def replaceCacheFrames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.replaceCacheFrames(*args, **kwargs)
@commandWrap
def BakeSpringAnimation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeSpringAnimation(*args, **kwargs)
@commandWrap
def MoveRotateScaleToolToggleSnapRelativeMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveRotateScaleToolToggleSnapRelativeMode(*args, **kwargs)
@commandWrap
def findDeformers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.findDeformers(*args, **kwargs)
@commandWrap
def SetFocusToCommandLine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFocusToCommandLine(*args, **kwargs)
@commandWrap
def ShapeEditorDuplicateTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShapeEditorDuplicateTarget(*args, **kwargs)
@commandWrap
def HypershadeMoveTabUp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeMoveTabUp(*args, **kwargs)
@commandWrap
def ScriptPaintToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScriptPaintToolOptions(*args, **kwargs)
@commandWrap
def texSelectContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texSelectContext(*args, **kwargs)
@commandWrap
def PlaybackToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PlaybackToggle(*args, **kwargs)
@commandWrap
def dynSelectCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynSelectCtx(*args, **kwargs)
@commandWrap
def DeleteAllControllers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllControllers(*args, **kwargs)
@commandWrap
def UnpublishRootTransform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnpublishRootTransform(*args, **kwargs)
@commandWrap
def UVCentricUVLinkingEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVCentricUVLinkingEditor(*args, **kwargs)
@commandWrap
def NewSceneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NewSceneOptions(*args, **kwargs)
@commandWrap
def SurfaceBooleanUnionToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceBooleanUnionToolOptions(*args, **kwargs)
@commandWrap
def referenceEdit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.referenceEdit(*args, **kwargs)
@commandWrap
def polyMirrorFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMirrorFace(*args, **kwargs)
@commandWrap
def SubdivProxyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivProxyOptions(*args, **kwargs)
@commandWrap
def xgmSplinePreset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplinePreset(*args, **kwargs)
@commandWrap
def OutlinerRenameSelectedItem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerRenameSelectedItem(*args, **kwargs)
@commandWrap
def dR_rotateRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_rotateRelease(*args, **kwargs)
@commandWrap
def art3dPaintCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.art3dPaintCtx(*args, **kwargs)
@commandWrap
def fltLightPoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fltLightPoints(*args, **kwargs)
@commandWrap
def PolygonHardenEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonHardenEdge(*args, **kwargs)
@commandWrap
def perCameraVisibility(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.perCameraVisibility(*args, **kwargs)
@commandWrap
def CreateHairCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateHairCache(*args, **kwargs)
@commandWrap
def TranslateToolWithSnapMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TranslateToolWithSnapMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def deleteUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deleteUI(*args, **kwargs)
@commandWrap
def CameraModeOrthographic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CameraModeOrthographic(*args, **kwargs)
@commandWrap
def HypershadeSelectUtilities(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectUtilities(*args, **kwargs)
@commandWrap
def ilrImportVertexColorsCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrImportVertexColorsCmd(*args, **kwargs)
@commandWrap
def curveBezierCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveBezierCtx(*args, **kwargs)
@commandWrap
def DeleteAllClusters(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllClusters(*args, **kwargs)
@commandWrap
def RemoveBrushSharing(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBrushSharing(*args, **kwargs)
@commandWrap
def WireToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WireToolOptions(*args, **kwargs)
@commandWrap
def nucleusGetnClothExample(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusGetnClothExample(*args, **kwargs)
@commandWrap
def TimeEditorRippleEditTogglePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorRippleEditTogglePress(*args, **kwargs)
@commandWrap
def ToggleLayerBar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleLayerBar(*args, **kwargs)
@commandWrap
def ToggleModelEditorBars(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleModelEditorBars(*args, **kwargs)
@commandWrap
def ShowNURBSCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowNURBSCurves(*args, **kwargs)
@commandWrap
def CreatePolygonCylinderOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonCylinderOptions(*args, **kwargs)
@commandWrap
def ilrHwBakeVisualizerCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrHwBakeVisualizerCmd(*args, **kwargs)
@commandWrap
def FBXLoadMBImportPresetFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXLoadMBImportPresetFile(*args, **kwargs)
@commandWrap
def SnapKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapKeys(*args, **kwargs)
@commandWrap
def SelectIsolate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectIsolate(*args, **kwargs)
@commandWrap
def ConvertSelectionToUVBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToUVBorder(*args, **kwargs)
@commandWrap
def NodeEditorCreateIterateCompound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCreateIterateCompound(*args, **kwargs)
@commandWrap
def ApplySettingsToLastStroke(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ApplySettingsToLastStroke(*args, **kwargs)
@commandWrap
def RaiseMainWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RaiseMainWindow(*args, **kwargs)
@commandWrap
def DetachVertexComponent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachVertexComponent(*args, **kwargs)
@commandWrap
def CreateConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateConstraintOptions(*args, **kwargs)
@commandWrap
def SplitEdgeRingToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitEdgeRingToolOptions(*args, **kwargs)
@commandWrap
def HideNURBSCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideNURBSCurves(*args, **kwargs)
@commandWrap
def STRSTweakModeOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.STRSTweakModeOn(*args, **kwargs)
@commandWrap
def WrinkleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WrinkleTool(*args, **kwargs)
@commandWrap
def ConvertSelectionToVertexFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToVertexFaces(*args, **kwargs)
@commandWrap
def ShowNRigids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowNRigids(*args, **kwargs)
@commandWrap
def SculptMeshUnfreezeAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptMeshUnfreezeAll(*args, **kwargs)
@commandWrap
def InvertSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InvertSelection(*args, **kwargs)
@commandWrap
def ShowHairSystems(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowHairSystems(*args, **kwargs)
@commandWrap
def RigidBindSkinOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RigidBindSkinOptions(*args, **kwargs)
@commandWrap
def polyColorDel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyColorDel(*args, **kwargs)
@commandWrap
def CreatePolygonGearOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonGearOptions(*args, **kwargs)
@commandWrap
def SelectUVNonOverlappingComponentsPerObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVNonOverlappingComponentsPerObject(*args, **kwargs)
@commandWrap
def DisplayIntermediateObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayIntermediateObjects(*args, **kwargs)
@commandWrap
def ilrRenderCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrRenderCmd(*args, **kwargs)
@commandWrap
def ShowNCloths(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowNCloths(*args, **kwargs)
@commandWrap
def MergeVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeVertices(*args, **kwargs)
@commandWrap
def ConnectNodeToIKFK(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConnectNodeToIKFK(*args, **kwargs)
@commandWrap
def hikRigAlign(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikRigAlign(*args, **kwargs)
@commandWrap
def hikManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikManip(*args, **kwargs)
@commandWrap
def polyCollapseEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCollapseEdge(*args, **kwargs)
@commandWrap
def SymmetrizeUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SymmetrizeUV(*args, **kwargs)
@commandWrap
def CreatePolygonPyramidOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPyramidOptions(*args, **kwargs)
@commandWrap
def TrimTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TrimTool(*args, **kwargs)
@commandWrap
def TangentsFlat(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsFlat(*args, **kwargs)
@commandWrap
def timeEditorTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorTracks(*args, **kwargs)
@commandWrap
def FlipTubeDirection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FlipTubeDirection(*args, **kwargs)
@commandWrap
def AnimLayerRelationshipEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AnimLayerRelationshipEditor(*args, **kwargs)
@commandWrap
def dR_viewBack(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewBack(*args, **kwargs)
@commandWrap
def imageWindowEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.imageWindowEditor(*args, **kwargs)
@commandWrap
def CreateAmbientLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateAmbientLight(*args, **kwargs)
@commandWrap
def polyCompare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCompare(*args, **kwargs)
@commandWrap
def softMod(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.softMod(*args, **kwargs)
@commandWrap
def AddSelectionAsCombinationTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddSelectionAsCombinationTarget(*args, **kwargs)
@commandWrap
def dgtimer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgtimer(*args, **kwargs)
@commandWrap
def CreateCurveFromPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCurveFromPoly(*args, **kwargs)
@commandWrap
def Vortex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Vortex(*args, **kwargs)
@commandWrap
def texScaleContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texScaleContext(*args, **kwargs)
@commandWrap
def snapTogetherCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.snapTogetherCtx(*args, **kwargs)
@commandWrap
def stringArrayIntersector(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stringArrayIntersector(*args, **kwargs)
@commandWrap
def ToggleShelf(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleShelf(*args, **kwargs)
@commandWrap
def CreateOcean(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateOcean(*args, **kwargs)
@commandWrap
def timerX(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timerX(*args, **kwargs)
@commandWrap
def PreviousManipulatorHandle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreviousManipulatorHandle(*args, **kwargs)
@commandWrap
def NonSacredTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NonSacredTool(*args, **kwargs)
@commandWrap
def transferShadingSets(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.transferShadingSets(*args, **kwargs)
@commandWrap
def AddBifrostGuide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostGuide(*args, **kwargs)
@commandWrap
def ReversePolygonNormalsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReversePolygonNormalsOptions(*args, **kwargs)
@commandWrap
def DisableTimeChangeUndoConsolidation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableTimeChangeUndoConsolidation(*args, **kwargs)
@commandWrap
def GraphEditorNormalizedView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorNormalizedView(*args, **kwargs)
@commandWrap
def SetMeshSmoothTargetTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshSmoothTargetTool(*args, **kwargs)
@commandWrap
def stitchSurfacePoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stitchSurfacePoints(*args, **kwargs)
@commandWrap
def PixelMoveRight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PixelMoveRight(*args, **kwargs)
@commandWrap
def trackCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.trackCtx(*args, **kwargs)
@commandWrap
def ProfilerToolShowSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolShowSelected(*args, **kwargs)
@commandWrap
def NURBSSmoothnessFineOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessFineOptions(*args, **kwargs)
@commandWrap
def dR_activeHandleXYZ(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_activeHandleXYZ(*args, **kwargs)
@commandWrap
def EnableParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableParticles(*args, **kwargs)
@commandWrap
def undo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.undo(*args, **kwargs)
@commandWrap
def subdLayoutUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdLayoutUV(*args, **kwargs)
@commandWrap
def u3dTopoValid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.u3dTopoValid(*args, **kwargs)
@commandWrap
def AssignHairConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignHairConstraintOptions(*args, **kwargs)
@commandWrap
def CustomPolygonDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CustomPolygonDisplay(*args, **kwargs)
@commandWrap
def loadPlugin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.loadPlugin(*args, **kwargs)
@commandWrap
def PointOnPolyConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PointOnPolyConstraintOptions(*args, **kwargs)
@commandWrap
def OneClickAcknowledge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickAcknowledge(*args, **kwargs)
@commandWrap
def CreateDirectionalLightOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateDirectionalLightOptions(*args, **kwargs)
@commandWrap
def dR_tweakRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_tweakRelease(*args, **kwargs)
@commandWrap
def EnableAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableAll(*args, **kwargs)
@commandWrap
def SelectAllJoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllJoints(*args, **kwargs)
@commandWrap
def nearestPointOnMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nearestPointOnMesh(*args, **kwargs)
@commandWrap
def shaderfx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shaderfx(*args, **kwargs)
@commandWrap
def showManipCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.showManipCtx(*args, **kwargs)
@commandWrap
def ShowGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowGeometry(*args, **kwargs)
@commandWrap
def SurfaceFlowOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceFlowOptions(*args, **kwargs)
@commandWrap
def vectorize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.vectorize(*args, **kwargs)
@commandWrap
def OutlinerToggleAssignedMaterials(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleAssignedMaterials(*args, **kwargs)
@commandWrap
def CreatePolygonSphericalHarmonicsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSphericalHarmonicsOptions(*args, **kwargs)
@commandWrap
def DeleteAllNParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllNParticles(*args, **kwargs)
@commandWrap
def TestTextureOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TestTextureOptions(*args, **kwargs)
@commandWrap
def HypershadeOpenBrowserWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenBrowserWindow(*args, **kwargs)
@commandWrap
def polyDelEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyDelEdge(*args, **kwargs)
@commandWrap
def SelectSimilar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectSimilar(*args, **kwargs)
@commandWrap
def clipMatching(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clipMatching(*args, **kwargs)
@commandWrap
def XgmSetSelectBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetSelectBrushTool(*args, **kwargs)
@commandWrap
def NormalizeUVsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NormalizeUVsOptions(*args, **kwargs)
@commandWrap
def AddDynamicBuoyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddDynamicBuoyOptions(*args, **kwargs)
@commandWrap
def makebot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.makebot(*args, **kwargs)
@commandWrap
def surfaceShaderList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.surfaceShaderList(*args, **kwargs)
@commandWrap
def makeLive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.makeLive(*args, **kwargs)
@commandWrap
def fluidDeleteCacheFrames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidDeleteCacheFrames(*args, **kwargs)
@commandWrap
def ExtrudeFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtrudeFace(*args, **kwargs)
@commandWrap
def TimeEditorClipScaleStart(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipScaleStart(*args, **kwargs)
@commandWrap
def ExportOfflineFileOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportOfflineFileOptions(*args, **kwargs)
@commandWrap
def RepeatLastActionAtMousePosition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RepeatLastActionAtMousePosition(*args, **kwargs)
@commandWrap
def AnimationSweep(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AnimationSweep(*args, **kwargs)
@commandWrap
def CutCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutCurve(*args, **kwargs)
@commandWrap
def matchTransform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.matchTransform(*args, **kwargs)
@commandWrap
def DeleteAttribute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAttribute(*args, **kwargs)
@commandWrap
def polySplitCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySplitCtx(*args, **kwargs)
@commandWrap
def HypergraphIncreaseDepth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypergraphIncreaseDepth(*args, **kwargs)
@commandWrap
def FrameSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FrameSelected(*args, **kwargs)
@commandWrap
def TimeEditorSceneAuthoringToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorSceneAuthoringToggle(*args, **kwargs)
@commandWrap
def getProcArguments(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getProcArguments(*args, **kwargs)
@commandWrap
def BakeNonDefHistoryOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeNonDefHistoryOptions(*args, **kwargs)
@commandWrap
def DecreaseCheckerDensity(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DecreaseCheckerDensity(*args, **kwargs)
@commandWrap
def ChangeEdgeWidth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ChangeEdgeWidth(*args, **kwargs)
@commandWrap
def ModifyPaintValuePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyPaintValuePress(*args, **kwargs)
@commandWrap
def HypershadeGraphRemoveSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphRemoveSelected(*args, **kwargs)
@commandWrap
def BakeCustomPivotOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeCustomPivotOptions(*args, **kwargs)
@commandWrap
def AddBifrostCamera(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostCamera(*args, **kwargs)
@commandWrap
def scaleKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scaleKey(*args, **kwargs)
@commandWrap
def xgmCopyDescription(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCopyDescription(*args, **kwargs)
@commandWrap
def nClothCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothCacheOpt(*args, **kwargs)
@commandWrap
def CreateCharacter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCharacter(*args, **kwargs)
@commandWrap
def dR_quadDrawRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_quadDrawRelease(*args, **kwargs)
@commandWrap
def addAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.addAttr(*args, **kwargs)
@commandWrap
def WireTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WireTool(*args, **kwargs)
@commandWrap
def setUITemplate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setUITemplate(*args, **kwargs)
@commandWrap
def pathAnimation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pathAnimation(*args, **kwargs)
@commandWrap
def StraightenUVBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StraightenUVBorder(*args, **kwargs)
@commandWrap
def createPolySphereCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolySphereCtx(*args, **kwargs)
@commandWrap
def TogglePolyNonPlanarFaceDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyNonPlanarFaceDisplay(*args, **kwargs)
@commandWrap
def CreateRigidBodySolver(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateRigidBodySolver(*args, **kwargs)
@commandWrap
def flagTest(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.flagTest(*args, **kwargs)
@commandWrap
def ShatterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShatterOptions(*args, **kwargs)
@commandWrap
def snapshotBeadCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.snapshotBeadCtx(*args, **kwargs)
@commandWrap
def ToggleVisibilityAndKeepSelectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleVisibilityAndKeepSelectionOptions(*args, **kwargs)
@commandWrap
def iterOnNurbs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.iterOnNurbs(*args, **kwargs)
@commandWrap
def CreatePolygonSoccerBallOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSoccerBallOptions(*args, **kwargs)
@commandWrap
def UVCreateSnapshot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVCreateSnapshot(*args, **kwargs)
@commandWrap
def ShowAttributeEditorOrChannelBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowAttributeEditorOrChannelBox(*args, **kwargs)
@commandWrap
def PaintEffectsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsToolOptions(*args, **kwargs)
@commandWrap
def HardwareRenderBuffer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HardwareRenderBuffer(*args, **kwargs)
@commandWrap
def LoadHIKPropertySetState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LoadHIKPropertySetState(*args, **kwargs)
@commandWrap
def ShowShadingGroupAttributeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowShadingGroupAttributeEditor(*args, **kwargs)
@commandWrap
def readTake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.readTake(*args, **kwargs)
@commandWrap
def GraphEditorAbsoluteView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorAbsoluteView(*args, **kwargs)
@commandWrap
def HypershadePinSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePinSelected(*args, **kwargs)
@commandWrap
def renderThumbnailUpdate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderThumbnailUpdate(*args, **kwargs)
@commandWrap
def ShowMeshImprintToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshImprintToolOptions(*args, **kwargs)
@commandWrap
def CopySkinWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopySkinWeights(*args, **kwargs)
@commandWrap
def CurveSmoothnessRough(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveSmoothnessRough(*args, **kwargs)
@commandWrap
def HIKFullBodyMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKFullBodyMode(*args, **kwargs)
@commandWrap
def popListItem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.popListItem(*args, **kwargs)
@commandWrap
def ToggleModelingToolkit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleModelingToolkit(*args, **kwargs)
@commandWrap
def containerTemplate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.containerTemplate(*args, **kwargs)
@commandWrap
def TransferAttributeValuesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransferAttributeValuesOptions(*args, **kwargs)
@commandWrap
def polyListComponentConversion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyListComponentConversion(*args, **kwargs)
@commandWrap
def HypershadeGraphAddSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphAddSelected(*args, **kwargs)
@commandWrap
def nClothReplaceFrames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothReplaceFrames(*args, **kwargs)
@commandWrap
def ToggleKeepHardEdgeCulling(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleKeepHardEdgeCulling(*args, **kwargs)
@commandWrap
def TransformNoSelectOffTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransformNoSelectOffTool(*args, **kwargs)
@commandWrap
def keyframeRegionCurrentTimeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionCurrentTimeCtx(*args, **kwargs)
@commandWrap
def TimeEditorClipTrimStart(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipTrimStart(*args, **kwargs)
@commandWrap
def xgmSelectedPrims(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSelectedPrims(*args, **kwargs)
@commandWrap
def AddBoatLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBoatLocator(*args, **kwargs)
@commandWrap
def dR_vertSelectLocked(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_vertSelectLocked(*args, **kwargs)
@commandWrap
def SelectToolMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectToolMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def dR_extrudeBevelRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_extrudeBevelRelease(*args, **kwargs)
@commandWrap
def AddPondDynamicBuoy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPondDynamicBuoy(*args, **kwargs)
@commandWrap
def FBXExportReferencedAssetsContent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportReferencedAssetsContent(*args, **kwargs)
@commandWrap
def freeze(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.freeze(*args, **kwargs)
@commandWrap
def FrameAllInAllViews(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FrameAllInAllViews(*args, **kwargs)
@commandWrap
def SelectUVNonOverlappingComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVNonOverlappingComponents(*args, **kwargs)
@commandWrap
def RegionKeysTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RegionKeysTool(*args, **kwargs)
@commandWrap
def GpuCacheExportSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GpuCacheExportSelection(*args, **kwargs)
@commandWrap
def ExportOfflineFileFromRefEd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportOfflineFileFromRefEd(*args, **kwargs)
@commandWrap
def lassoContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lassoContext(*args, **kwargs)
@commandWrap
def ToggleLatticePoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleLatticePoints(*args, **kwargs)
@commandWrap
def ToggleFaceMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFaceMetadata(*args, **kwargs)
@commandWrap
def OutTangentAuto(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutTangentAuto(*args, **kwargs)
@commandWrap
def FBXImportHardEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportHardEdges(*args, **kwargs)
@commandWrap
def addExtension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.addExtension(*args, **kwargs)
@commandWrap
def xgmPartBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPartBrushToolCmd(*args, **kwargs)
@commandWrap
def NodeEditorCreateCompound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCreateCompound(*args, **kwargs)
@commandWrap
def PolygonBooleanDifference(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonBooleanDifference(*args, **kwargs)
@commandWrap
def ToggleBorderEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleBorderEdges(*args, **kwargs)
@commandWrap
def CreateNURBSCubeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSCubeOptions(*args, **kwargs)
@commandWrap
def polyMergeFacet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMergeFacet(*args, **kwargs)
@commandWrap
def ThreeRightSplitViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ThreeRightSplitViewArrangement(*args, **kwargs)
@commandWrap
def polyMergeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMergeEdge(*args, **kwargs)
@commandWrap
def movieInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.movieInfo(*args, **kwargs)
@commandWrap
def ToggleAttributeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleAttributeEditor(*args, **kwargs)
@commandWrap
def ToggleToolSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleToolSettings(*args, **kwargs)
@commandWrap
def ReattachSkeletonJoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReattachSkeletonJoints(*args, **kwargs)
@commandWrap
def dR_DoCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_DoCmd(*args, **kwargs)
@commandWrap
def CharacterAnimationEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CharacterAnimationEditor(*args, **kwargs)
@commandWrap
def EnableNucleuses(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableNucleuses(*args, **kwargs)
@commandWrap
def ikSplineHandleCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikSplineHandleCtx(*args, **kwargs)
@commandWrap
def nurbsBoolean(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsBoolean(*args, **kwargs)
@commandWrap
def CreatePolyFromPreview(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolyFromPreview(*args, **kwargs)
@commandWrap
def CreateConstraintClipOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateConstraintClipOptions(*args, **kwargs)
@commandWrap
def SetBifrostInitialState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetBifrostInitialState(*args, **kwargs)
@commandWrap
def dR_meshColorOverrideTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_meshColorOverrideTGL(*args, **kwargs)
@commandWrap
def PaintEffectsPanel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsPanel(*args, **kwargs)
@commandWrap
def editDisplayLayerMembers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.editDisplayLayerMembers(*args, **kwargs)
@commandWrap
def UngroupOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UngroupOptions(*args, **kwargs)
@commandWrap
def TimeEditorCreateClipOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateClipOptions(*args, **kwargs)
@commandWrap
def TexSculptInvertPin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSculptInvertPin(*args, **kwargs)
@commandWrap
def invertShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.invertShape(*args, **kwargs)
@commandWrap
def NCreateEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NCreateEmitter(*args, **kwargs)
@commandWrap
def SculptSubdivsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptSubdivsToolOptions(*args, **kwargs)
@commandWrap
def SmoothingLevelIncrease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothingLevelIncrease(*args, **kwargs)
@commandWrap
def nClothMakeCollideOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothMakeCollideOptions(*args, **kwargs)
@commandWrap
def SelectUVMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVMask(*args, **kwargs)
@commandWrap
def ToggleXGenDisplayHUD(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleXGenDisplayHUD(*args, **kwargs)
@commandWrap
def copyFlexor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.copyFlexor(*args, **kwargs)
@commandWrap
def InitialFluidStates(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InitialFluidStates(*args, **kwargs)
@commandWrap
def xgmMelRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmMelRender(*args, **kwargs)
@commandWrap
def GraphEditorDisplayTangentActive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorDisplayTangentActive(*args, **kwargs)
@commandWrap
def SelectToggleMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectToggleMode(*args, **kwargs)
@commandWrap
def isolateSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.isolateSelect(*args, **kwargs)
@commandWrap
def PickColorDeactivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickColorDeactivate(*args, **kwargs)
@commandWrap
def skeletonEmbed(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.skeletonEmbed(*args, **kwargs)
@commandWrap
def SculptGeometryTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptGeometryTool(*args, **kwargs)
@commandWrap
def HyperGraphPanelRedoViewChange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HyperGraphPanelRedoViewChange(*args, **kwargs)
@commandWrap
def BifMeshExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BifMeshExport(*args, **kwargs)
@commandWrap
def GridUVOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GridUVOptions(*args, **kwargs)
@commandWrap
def UpdateReferenceSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UpdateReferenceSurface(*args, **kwargs)
@commandWrap
def reorderDeformers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reorderDeformers(*args, **kwargs)
@commandWrap
def NormalizeUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NormalizeUVs(*args, **kwargs)
@commandWrap
def Snap2PointsTo2PointsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Snap2PointsTo2PointsOptions(*args, **kwargs)
@commandWrap
def ImportWorkspaceFiles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ImportWorkspaceFiles(*args, **kwargs)
@commandWrap
def SaveScene(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveScene(*args, **kwargs)
@commandWrap
def CreatePose(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePose(*args, **kwargs)
@commandWrap
def ShowMarkers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMarkers(*args, **kwargs)
@commandWrap
def OutlinerExpandAllSelectedItems(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerExpandAllSelectedItems(*args, **kwargs)
@commandWrap
def ConvertSelectionToUVPerimeter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToUVPerimeter(*args, **kwargs)
@commandWrap
def OutlinerToggleShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleShapes(*args, **kwargs)
@commandWrap
def MapUVBorderOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MapUVBorderOptions(*args, **kwargs)
@commandWrap
def MoveSewUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveSewUVs(*args, **kwargs)
@commandWrap
def polyAutoProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyAutoProjection(*args, **kwargs)
@commandWrap
def copyNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.copyNode(*args, **kwargs)
@commandWrap
def EmitFromObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EmitFromObject(*args, **kwargs)
@commandWrap
def FBXPushSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXPushSettings(*args, **kwargs)
@commandWrap
def globalStitch(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.globalStitch(*args, **kwargs)
@commandWrap
def ShowMeshSculptToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshSculptToolOptions(*args, **kwargs)
@commandWrap
def TogglePolyDisplayHardEdgesColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyDisplayHardEdgesColor(*args, **kwargs)
@commandWrap
def meshIntersectTest(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.meshIntersectTest(*args, **kwargs)
@commandWrap
def CharacterSetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CharacterSetEditor(*args, **kwargs)
@commandWrap
def DuplicateNURBSPatchesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateNURBSPatchesOptions(*args, **kwargs)
@commandWrap
def FBXImportConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportConstraints(*args, **kwargs)
@commandWrap
def HypershadeOpenSpreadSheetWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenSpreadSheetWindow(*args, **kwargs)
@commandWrap
def ReferenceEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReferenceEditor(*args, **kwargs)
@commandWrap
def XgmSetCutBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetCutBrushTool(*args, **kwargs)
@commandWrap
def angleBetween(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.angleBetween(*args, **kwargs)
@commandWrap
def NParticleToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NParticleToolOptions(*args, **kwargs)
@commandWrap
def SnapToCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToCurve(*args, **kwargs)
@commandWrap
def RedoPreviousIPRRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RedoPreviousIPRRender(*args, **kwargs)
@commandWrap
def VisualizeMetadataOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.VisualizeMetadataOptions(*args, **kwargs)
@commandWrap
def getParticleAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getParticleAttr(*args, **kwargs)
@commandWrap
def ShapeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShapeEditor(*args, **kwargs)
@commandWrap
def ToggleMeshFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMeshFaces(*args, **kwargs)
@commandWrap
def ToggleCurrentContainerHud(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCurrentContainerHud(*args, **kwargs)
@commandWrap
def CreateHairCacheOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateHairCacheOptions(*args, **kwargs)
@commandWrap
def GetFKIdFromEffectorId(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetFKIdFromEffectorId(*args, **kwargs)
@commandWrap
def HypershadeSortByTime(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSortByTime(*args, **kwargs)
@commandWrap
def xgmSplineSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplineSelect(*args, **kwargs)
@commandWrap
def SmoothingDisplayShowBoth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothingDisplayShowBoth(*args, **kwargs)
@commandWrap
def texMoveUVShellContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texMoveUVShellContext(*args, **kwargs)
@commandWrap
def GetHIKMatrixDecomposition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKMatrixDecomposition(*args, **kwargs)
@commandWrap
def NodeEditorPickWalkRight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPickWalkRight(*args, **kwargs)
@commandWrap
def nurbsEditUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsEditUV(*args, **kwargs)
@commandWrap
def getFluidAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getFluidAttr(*args, **kwargs)
@commandWrap
def AssignHairConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignHairConstraint(*args, **kwargs)
@commandWrap
def ResampleCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResampleCurve(*args, **kwargs)
@commandWrap
def syncSculptCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.syncSculptCache(*args, **kwargs)
@commandWrap
def PolygonSelectionConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonSelectionConstraints(*args, **kwargs)
@commandWrap
def ShapeEditorNewGroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShapeEditorNewGroup(*args, **kwargs)
@commandWrap
def dgdirty(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgdirty(*args, **kwargs)
@commandWrap
def DeleteKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteKeys(*args, **kwargs)
@commandWrap
def DuplicateFaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateFaceOptions(*args, **kwargs)
@commandWrap
def polyProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyProjection(*args, **kwargs)
@commandWrap
def SelectObjectsIlluminatedByLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectObjectsIlluminatedByLight(*args, **kwargs)
@commandWrap
def IncreaseGammaCoarse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncreaseGammaCoarse(*args, **kwargs)
@commandWrap
def PolygonCollapseFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonCollapseFaces(*args, **kwargs)
@commandWrap
def toggleDisplacement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.toggleDisplacement(*args, **kwargs)
@commandWrap
def CreateSubdivCube(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivCube(*args, **kwargs)
@commandWrap
def ConvertSelectionToFacePerimeter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToFacePerimeter(*args, **kwargs)
@commandWrap
def AddToContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddToContainerOptions(*args, **kwargs)
@commandWrap
def dR_objectTemplateTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_objectTemplateTGL(*args, **kwargs)
@commandWrap
def HypershadeToggleZoomOut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleZoomOut(*args, **kwargs)
@commandWrap
def FreeformFilletOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FreeformFilletOptions(*args, **kwargs)
@commandWrap
def CreatePolygonSphericalHarmonics(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSphericalHarmonics(*args, **kwargs)
@commandWrap
def OpenCloseCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OpenCloseCurveOptions(*args, **kwargs)
@commandWrap
def dR_objectEdgesOnlyTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_objectEdgesOnlyTGL(*args, **kwargs)
@commandWrap
def GraphEditorLockChannel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorLockChannel(*args, **kwargs)
@commandWrap
def UnitizeUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnitizeUVs(*args, **kwargs)
@commandWrap
def SetInitialStateOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetInitialStateOptions(*args, **kwargs)
@commandWrap
def NURBSTexturePlacementTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSTexturePlacementTool(*args, **kwargs)
@commandWrap
def CreaseProxyEdgeToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreaseProxyEdgeToolOptions(*args, **kwargs)
@commandWrap
def MakeBoatsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeBoatsOptions(*args, **kwargs)
@commandWrap
def UndoViewChange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UndoViewChange(*args, **kwargs)
@commandWrap
def mrShaderManager(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mrShaderManager(*args, **kwargs)
@commandWrap
def EPCurveToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EPCurveToolOptions(*args, **kwargs)
@commandWrap
def ToggleBackfaceCulling(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleBackfaceCulling(*args, **kwargs)
@commandWrap
def DisconnectJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisconnectJoint(*args, **kwargs)
@commandWrap
def XgCreateDescription(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgCreateDescription(*args, **kwargs)
@commandWrap
def editDisplayLayerGlobals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.editDisplayLayerGlobals(*args, **kwargs)
@commandWrap
def ToggleObjectDetails(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleObjectDetails(*args, **kwargs)
@commandWrap
def PaintFluidsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintFluidsToolOptions(*args, **kwargs)
@commandWrap
def PublishRootTransformOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishRootTransformOptions(*args, **kwargs)
@commandWrap
def FBXProperties(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXProperties(*args, **kwargs)
@commandWrap
def HypershadeConvertToFileTextureOptionBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeConvertToFileTextureOptionBox(*args, **kwargs)
@commandWrap
def editRenderLayerMembers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.editRenderLayerMembers(*args, **kwargs)
@commandWrap
def ilrHwTextureCacheCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrHwTextureCacheCmd(*args, **kwargs)
@commandWrap
def setParticleAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setParticleAttr(*args, **kwargs)
@commandWrap
def TwoSideBySideViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TwoSideBySideViewArrangement(*args, **kwargs)
@commandWrap
def ToggleShowBufferCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleShowBufferCurves(*args, **kwargs)
@commandWrap
def ToggleFastInteraction(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFastInteraction(*args, **kwargs)
@commandWrap
def ikSpringSolverCallbacks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikSpringSolverCallbacks(*args, **kwargs)
@commandWrap
def unknownNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.unknownNode(*args, **kwargs)
@commandWrap
def SmoothingLevelDecrease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothingLevelDecrease(*args, **kwargs)
@commandWrap
def scaleComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scaleComponents(*args, **kwargs)
@commandWrap
def translator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.translator(*args, **kwargs)
@commandWrap
def simplify(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.simplify(*args, **kwargs)
@commandWrap
def assignShaderToType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.assignShaderToType(*args, **kwargs)
@commandWrap
def ToggleFrameRate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFrameRate(*args, **kwargs)
@commandWrap
def HideNRigids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideNRigids(*args, **kwargs)
@commandWrap
def DetachSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachSurfacesOptions(*args, **kwargs)
@commandWrap
def HideCameraManipulators(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideCameraManipulators(*args, **kwargs)
@commandWrap
def xgmPoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPoints(*args, **kwargs)
@commandWrap
def ShowMeshAmplifyToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshAmplifyToolOptions(*args, **kwargs)
@commandWrap
def MergeCharacterSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeCharacterSet(*args, **kwargs)
@commandWrap
def ParticleFill(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParticleFill(*args, **kwargs)
@commandWrap
def threePointArcCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.threePointArcCtx(*args, **kwargs)
@commandWrap
def subdMapCut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdMapCut(*args, **kwargs)
@commandWrap
def NodeEditorUnpinSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorUnpinSelected(*args, **kwargs)
@commandWrap
def TimeEditorAddToSoloSelectedTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorAddToSoloSelectedTracks(*args, **kwargs)
@commandWrap
def partition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.partition(*args, **kwargs)
@commandWrap
def flow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.flow(*args, **kwargs)
@commandWrap
def CreateReferenceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateReferenceOptions(*args, **kwargs)
@commandWrap
def dgPerformance(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgPerformance(*args, **kwargs)
@commandWrap
def EnableMemoryCaching(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableMemoryCaching(*args, **kwargs)
@commandWrap
def polyCreateFacet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCreateFacet(*args, **kwargs)
@commandWrap
def RenderTextureRangeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderTextureRangeOptions(*args, **kwargs)
@commandWrap
def xgmSetArchiveSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSetArchiveSize(*args, **kwargs)
@commandWrap
def UnlockContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnlockContainer(*args, **kwargs)
@commandWrap
def polyWedgeFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyWedgeFace(*args, **kwargs)
@commandWrap
def CreateVolumeLightOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateVolumeLightOptions(*args, **kwargs)
@commandWrap
def ConformPolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConformPolygonOptions(*args, **kwargs)
@commandWrap
def dR_preferencesTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_preferencesTGL(*args, **kwargs)
@commandWrap
def encodeString(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.encodeString(*args, **kwargs)
@commandWrap
def InsertKnotOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertKnotOptions(*args, **kwargs)
@commandWrap
def ImportOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ImportOptions(*args, **kwargs)
@commandWrap
def IntersectCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IntersectCurveOptions(*args, **kwargs)
@commandWrap
def PickWalkUseController(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkUseController(*args, **kwargs)
@commandWrap
def CreateCluster(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCluster(*args, **kwargs)
@commandWrap
def RemoveConstraintTargetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveConstraintTargetOptions(*args, **kwargs)
@commandWrap
def ConnectJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConnectJoint(*args, **kwargs)
@commandWrap
def RestoreUIElements(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RestoreUIElements(*args, **kwargs)
@commandWrap
def circularFillet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.circularFillet(*args, **kwargs)
@commandWrap
def MoveTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveTool(*args, **kwargs)
@commandWrap
def ModifyStampDepthPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyStampDepthPress(*args, **kwargs)
@commandWrap
def melProcSpreadsheet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.melProcSpreadsheet(*args, **kwargs)
@commandWrap
def CycleBackgroundColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CycleBackgroundColor(*args, **kwargs)
@commandWrap
def SelectAllRigidConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllRigidConstraints(*args, **kwargs)
@commandWrap
def ShowMeshFillToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshFillToolOptions(*args, **kwargs)
@commandWrap
def ikSystemInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikSystemInfo(*args, **kwargs)
@commandWrap
def MirrorSubdivSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorSubdivSurface(*args, **kwargs)
@commandWrap
def Create3DContainerEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create3DContainerEmitter(*args, **kwargs)
@commandWrap
def ModelingPanelUndoViewChange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModelingPanelUndoViewChange(*args, **kwargs)
@commandWrap
def dR_rotateTweakTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_rotateTweakTool(*args, **kwargs)
@commandWrap
def buildSendToBackburnerDialog(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.buildSendToBackburnerDialog(*args, **kwargs)
@commandWrap
def RebuildSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RebuildSurfaces(*args, **kwargs)
@commandWrap
def AddPondBoatLocatorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPondBoatLocatorOptions(*args, **kwargs)
@commandWrap
def xgmPresetSnapshotContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPresetSnapshotContext(*args, **kwargs)
@commandWrap
def sbs_IsSubstanceRelocalized(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_IsSubstanceRelocalized(*args, **kwargs)
@commandWrap
def InteractiveBindSkin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InteractiveBindSkin(*args, **kwargs)
@commandWrap
def xgmGrabBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGrabBrushToolCmd(*args, **kwargs)
@commandWrap
def mayaDpiSettingAction(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mayaDpiSettingAction(*args, **kwargs)
@commandWrap
def NodeEditorPickWalkLeft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPickWalkLeft(*args, **kwargs)
@commandWrap
def SelectFacetMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectFacetMask(*args, **kwargs)
@commandWrap
def SplitPolygonTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitPolygonTool(*args, **kwargs)
@commandWrap
def memoryDiag(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.memoryDiag(*args, **kwargs)
@commandWrap
def newton(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.newton(*args, **kwargs)
@commandWrap
def BakeSimulationOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeSimulationOptions(*args, **kwargs)
@commandWrap
def GoToMaxFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoToMaxFrame(*args, **kwargs)
@commandWrap
def UnpublishChildAnchor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnpublishChildAnchor(*args, **kwargs)
@commandWrap
def air(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.air(*args, **kwargs)
@commandWrap
def SendToUnrealAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendToUnrealAll(*args, **kwargs)
@commandWrap
def ToggleAutoFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleAutoFrame(*args, **kwargs)
@commandWrap
def AlembicImportOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicImportOptions(*args, **kwargs)
@commandWrap
def CreateVolumeCube(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateVolumeCube(*args, **kwargs)
@commandWrap
def GetHIKNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKNode(*args, **kwargs)
@commandWrap
def ToggleAutoSmooth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleAutoSmooth(*args, **kwargs)
@commandWrap
def NodeEditorToggleCreateNodePane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleCreateNodePane(*args, **kwargs)
@commandWrap
def TimeEditorCreateAdditiveLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateAdditiveLayer(*args, **kwargs)
@commandWrap
def NextSkinPaintMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NextSkinPaintMode(*args, **kwargs)
@commandWrap
def polyGeoSampler(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyGeoSampler(*args, **kwargs)
@commandWrap
def iprEngine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.iprEngine(*args, **kwargs)
@commandWrap
def uvSnapshot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.uvSnapshot(*args, **kwargs)
@commandWrap
def subdToNurbs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdToNurbs(*args, **kwargs)
@commandWrap
def HideObjectGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideObjectGeometry(*args, **kwargs)
@commandWrap
def xgmClumpBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmClumpBrushToolCmd(*args, **kwargs)
@commandWrap
def FreeTangentWeight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FreeTangentWeight(*args, **kwargs)
@commandWrap
def HypershadeUpdatePSDNetworks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeUpdatePSDNetworks(*args, **kwargs)
@commandWrap
def AddFloorContactPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddFloorContactPlane(*args, **kwargs)
@commandWrap
def renderSetupLocalOverride(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetupLocalOverride(*args, **kwargs)
@commandWrap
def SelectAllFollicles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllFollicles(*args, **kwargs)
@commandWrap
def dirmap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dirmap(*args, **kwargs)
@commandWrap
def fluidReplaceFramesOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidReplaceFramesOpt(*args, **kwargs)
@commandWrap
def DeleteAllPoses(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllPoses(*args, **kwargs)
@commandWrap
def imfPlugins(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.imfPlugins(*args, **kwargs)
@commandWrap
def FlipTriangleEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FlipTriangleEdge(*args, **kwargs)
@commandWrap
def polyAverageVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyAverageVertex(*args, **kwargs)
@commandWrap
def TimeEditorClipResetTiming(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipResetTiming(*args, **kwargs)
@commandWrap
def containerPublish(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.containerPublish(*args, **kwargs)
@commandWrap
def ilrClearTextureCacheCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrClearTextureCacheCmd(*args, **kwargs)
@commandWrap
def GraphDeleteOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphDeleteOptions(*args, **kwargs)
@commandWrap
def HypershadeGraphRemoveUpstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphRemoveUpstream(*args, **kwargs)
@commandWrap
def dbmessage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dbmessage(*args, **kwargs)
@commandWrap
def NURBSTexturePlacementToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSTexturePlacementToolOptions(*args, **kwargs)
@commandWrap
def snapMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.snapMode(*args, **kwargs)
@commandWrap
def polySplitRing(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySplitRing(*args, **kwargs)
@commandWrap
def HideNCloths(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideNCloths(*args, **kwargs)
@commandWrap
def xgmNoiseBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmNoiseBrushContext(*args, **kwargs)
@commandWrap
def MediumQualityDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MediumQualityDisplay(*args, **kwargs)
@commandWrap
def Tension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Tension(*args, **kwargs)
@commandWrap
def HideTexturePlacements(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideTexturePlacements(*args, **kwargs)
@commandWrap
def HIKSelectedMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKSelectedMode(*args, **kwargs)
@commandWrap
def HypershadeDisplayAsLargeSwatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayAsLargeSwatches(*args, **kwargs)
@commandWrap
def XgmSplineSelectConvertToFreeze(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineSelectConvertToFreeze(*args, **kwargs)
@commandWrap
def FBXImportQuaternion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportQuaternion(*args, **kwargs)
@commandWrap
def DisableGlobalStitch(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableGlobalStitch(*args, **kwargs)
@commandWrap
def PreferencesWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreferencesWindow(*args, **kwargs)
@commandWrap
def evalEcho(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.evalEcho(*args, **kwargs)
@commandWrap
def UVUnstackShellsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVUnstackShellsOptions(*args, **kwargs)
@commandWrap
def blendShapePanel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blendShapePanel(*args, **kwargs)
@commandWrap
def dR_renderLastTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_renderLastTGL(*args, **kwargs)
@commandWrap
def tolerance(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.tolerance(*args, **kwargs)
@commandWrap
def HideStrokePathCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideStrokePathCurves(*args, **kwargs)
@commandWrap
def HypershadeSetTraversalDepthZero(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSetTraversalDepthZero(*args, **kwargs)
@commandWrap
def SmoothTangent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothTangent(*args, **kwargs)
@commandWrap
def arcLengthDimension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.arcLengthDimension(*args, **kwargs)
@commandWrap
def PasteSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PasteSelected(*args, **kwargs)
@commandWrap
def SelectNone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectNone(*args, **kwargs)
@commandWrap
def clipEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clipEditor(*args, **kwargs)
@commandWrap
def NodeEditorCopyConnectionsOnPaste(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCopyConnectionsOnPaste(*args, **kwargs)
@commandWrap
def ChangeVertexSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ChangeVertexSize(*args, **kwargs)
@commandWrap
def RotateUVsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateUVsOptions(*args, **kwargs)
@commandWrap
def XgmSetCombBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetCombBrushTool(*args, **kwargs)
@commandWrap
def SaveCurrentWorkspace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveCurrentWorkspace(*args, **kwargs)
@commandWrap
def unfold(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.unfold(*args, **kwargs)
@commandWrap
def MakeLive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeLive(*args, **kwargs)
@commandWrap
def HIKComputeReference(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKComputeReference(*args, **kwargs)
@commandWrap
def PolyConvertToLoopAndDelete(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyConvertToLoopAndDelete(*args, **kwargs)
@commandWrap
def SelectAllTransforms(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllTransforms(*args, **kwargs)
@commandWrap
def ToggleEdgeMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleEdgeMetadata(*args, **kwargs)
@commandWrap
def fluidMergeCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidMergeCache(*args, **kwargs)
@commandWrap
def ToggleContainerCentric(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleContainerCentric(*args, **kwargs)
@commandWrap
def ReplaceObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReplaceObjects(*args, **kwargs)
@commandWrap
def CreateCharacterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCharacterOptions(*args, **kwargs)
@commandWrap
def SineOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SineOptions(*args, **kwargs)
@commandWrap
def ExtendSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendSurfaces(*args, **kwargs)
@commandWrap
def dR_selConstraintEdgeRing(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selConstraintEdgeRing(*args, **kwargs)
@commandWrap
def cMuscleSplineBind(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleSplineBind(*args, **kwargs)
@commandWrap
def PoseEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PoseEditor(*args, **kwargs)
@commandWrap
def AddEdgeDivisionsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddEdgeDivisionsOptions(*args, **kwargs)
@commandWrap
def ToggleCurrentFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCurrentFrame(*args, **kwargs)
@commandWrap
def aimConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.aimConstraint(*args, **kwargs)
@commandWrap
def AddCurvesToHairSystem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddCurvesToHairSystem(*args, **kwargs)
@commandWrap
def UncreaseSubdivSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UncreaseSubdivSurface(*args, **kwargs)
@commandWrap
def reverseSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reverseSurface(*args, **kwargs)
@commandWrap
def SymmetrizeSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SymmetrizeSelection(*args, **kwargs)
@commandWrap
def fluidAppend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidAppend(*args, **kwargs)
@commandWrap
def HideBoundingBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideBoundingBox(*args, **kwargs)
@commandWrap
def rehash(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rehash(*args, **kwargs)
@commandWrap
def ModifyUVVectorRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyUVVectorRelease(*args, **kwargs)
@commandWrap
def ReattachSkeleton(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReattachSkeleton(*args, **kwargs)
@commandWrap
def PaintGridOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintGridOptions(*args, **kwargs)
@commandWrap
def polyUVCoverage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUVCoverage(*args, **kwargs)
@commandWrap
def cMuscleWeightDefault(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleWeightDefault(*args, **kwargs)
@commandWrap
def SetCurrentUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetCurrentUVSet(*args, **kwargs)
@commandWrap
def CreateWake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateWake(*args, **kwargs)
@commandWrap
def isConnected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.isConnected(*args, **kwargs)
@commandWrap
def SnapToMeshCenterRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToMeshCenterRelease(*args, **kwargs)
@commandWrap
def polySewEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySewEdge(*args, **kwargs)
@commandWrap
def setKeyPath(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setKeyPath(*args, **kwargs)
@commandWrap
def StitchSurfacePointsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StitchSurfacePointsOptions(*args, **kwargs)
@commandWrap
def TogglePolygonFaceTriangles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolygonFaceTriangles(*args, **kwargs)
@commandWrap
def polyQuad(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyQuad(*args, **kwargs)
@commandWrap
def CreatePolygonSphereOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSphereOptions(*args, **kwargs)
@commandWrap
def attachCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attachCache(*args, **kwargs)
@commandWrap
def preloadRefEd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.preloadRefEd(*args, **kwargs)
@commandWrap
def FBXImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImport(*args, **kwargs)
@commandWrap
def SculptReferenceVectorMarkingMenuPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptReferenceVectorMarkingMenuPress(*args, **kwargs)
@commandWrap
def DeformerSetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeformerSetEditor(*args, **kwargs)
@commandWrap
def NodeEditorSelectConnected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorSelectConnected(*args, **kwargs)
@commandWrap
def UVNormalBasedProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVNormalBasedProjectionOptions(*args, **kwargs)
@commandWrap
def cacheAppendOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cacheAppendOpt(*args, **kwargs)
@commandWrap
def GetHIKParentId(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKParentId(*args, **kwargs)
@commandWrap
def deformerEvaluator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deformerEvaluator(*args, **kwargs)
@commandWrap
def TangentsAuto(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsAuto(*args, **kwargs)
@commandWrap
def ToggleCullingVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCullingVertices(*args, **kwargs)
@commandWrap
def ResetSoftSelectOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetSoftSelectOptions(*args, **kwargs)
@commandWrap
def dR_vertLockSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_vertLockSelected(*args, **kwargs)
@commandWrap
def UVSnapTogetherOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVSnapTogetherOptions(*args, **kwargs)
@commandWrap
def polyPlanarProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPlanarProjection(*args, **kwargs)
@commandWrap
def AttachSubdivSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachSubdivSurfaceOptions(*args, **kwargs)
@commandWrap
def AddPondDynamicBuoyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPondDynamicBuoyOptions(*args, **kwargs)
@commandWrap
def BakeTopologyToTargets(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeTopologyToTargets(*args, **kwargs)
@commandWrap
def TimeEditorRippleEditToggleRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorRippleEditToggleRelease(*args, **kwargs)
@commandWrap
def ExpressionEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExpressionEditor(*args, **kwargs)
@commandWrap
def ArtPaintAttrTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintAttrTool(*args, **kwargs)
@commandWrap
def loft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.loft(*args, **kwargs)
@commandWrap
def dagObjectCompare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dagObjectCompare(*args, **kwargs)
@commandWrap
def TimeEditorToggleSnapToClipPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorToggleSnapToClipPress(*args, **kwargs)
@commandWrap
def DeleteAllSculptObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllSculptObjects(*args, **kwargs)
@commandWrap
def polyMapCut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMapCut(*args, **kwargs)
@commandWrap
def greasePencil(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.greasePencil(*args, **kwargs)
@commandWrap
def ReverseCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReverseCurve(*args, **kwargs)
@commandWrap
def DetachSkin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachSkin(*args, **kwargs)
@commandWrap
def meshReorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.meshReorder(*args, **kwargs)
@commandWrap
def runup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.runup(*args, **kwargs)
@commandWrap
def SelectTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectTool(*args, **kwargs)
@commandWrap
def connectDynamic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.connectDynamic(*args, **kwargs)
@commandWrap
def ToggleUVEditorUVStatisticsHUD(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVEditorUVStatisticsHUD(*args, **kwargs)
@commandWrap
def FBXExportColladaFrameRate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportColladaFrameRate(*args, **kwargs)
@commandWrap
def MoveNormalToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveNormalToolOptions(*args, **kwargs)
@commandWrap
def sculpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sculpt(*args, **kwargs)
@commandWrap
def clearNClothStartState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clearNClothStartState(*args, **kwargs)
@commandWrap
def NodeEditorHideAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorHideAttributes(*args, **kwargs)
@commandWrap
def polyEditEdgeFlow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyEditEdgeFlow(*args, **kwargs)
@commandWrap
def polyPlatonic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPlatonic(*args, **kwargs)
@commandWrap
def selectedNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectedNodes(*args, **kwargs)
@commandWrap
def OutTangentLinear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutTangentLinear(*args, **kwargs)
@commandWrap
def PointOnCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PointOnCurveOptions(*args, **kwargs)
@commandWrap
def projectionContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.projectionContext(*args, **kwargs)
@commandWrap
def IncrementFluidCenter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncrementFluidCenter(*args, **kwargs)
@commandWrap
def dR_cameraToPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_cameraToPoly(*args, **kwargs)
@commandWrap
def SetNormalAngle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetNormalAngle(*args, **kwargs)
@commandWrap
def NodeEditorPinByDefault(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPinByDefault(*args, **kwargs)
@commandWrap
def roundCRCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.roundCRCtx(*args, **kwargs)
@commandWrap
def FBXExportQuickSelectSetAsCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportQuickSelectSetAsCache(*args, **kwargs)
@commandWrap
def SurfaceBooleanSubtractTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceBooleanSubtractTool(*args, **kwargs)
@commandWrap
def OneClickMenuExecute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickMenuExecute(*args, **kwargs)
@commandWrap
def cylinder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cylinder(*args, **kwargs)
@commandWrap
def MirrorDeformerWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorDeformerWeights(*args, **kwargs)
@commandWrap
def GetHIKEffectorName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKEffectorName(*args, **kwargs)
@commandWrap
def defaultLightListCheckBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.defaultLightListCheckBox(*args, **kwargs)
@commandWrap
def dR_selectSimilar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectSimilar(*args, **kwargs)
@commandWrap
def subdEditUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdEditUV(*args, **kwargs)
@commandWrap
def polyCopyUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCopyUV(*args, **kwargs)
@commandWrap
def characterize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.characterize(*args, **kwargs)
@commandWrap
def cone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cone(*args, **kwargs)
@commandWrap
def MakeCurvesDynamicOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeCurvesDynamicOptions(*args, **kwargs)
@commandWrap
def DuplicateSpecialOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateSpecialOptions(*args, **kwargs)
@commandWrap
def RotateToolWithSnapMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateToolWithSnapMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def NextKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NextKey(*args, **kwargs)
@commandWrap
def mouse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mouse(*args, **kwargs)
@commandWrap
def webViewCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.webViewCmd(*args, **kwargs)
@commandWrap
def colorManagementPrefs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.colorManagementPrefs(*args, **kwargs)
@commandWrap
def keyTangent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyTangent(*args, **kwargs)
@commandWrap
def GlobalStitch(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GlobalStitch(*args, **kwargs)
@commandWrap
def PaintEffectPanelActivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectPanelActivate(*args, **kwargs)
@commandWrap
def copySkinWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.copySkinWeights(*args, **kwargs)
@commandWrap
def SetMeshRepeatTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshRepeatTool(*args, **kwargs)
@commandWrap
def dR_selectTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectTool(*args, **kwargs)
@commandWrap
def CycleThroughCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CycleThroughCameras(*args, **kwargs)
@commandWrap
def DistributeShellsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DistributeShellsOptions(*args, **kwargs)
@commandWrap
def SimplifyCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SimplifyCurve(*args, **kwargs)
@commandWrap
def SelectToolOptionsMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectToolOptionsMarkingMenu(*args, **kwargs)
@commandWrap
def AddBifrostChannelField(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostChannelField(*args, **kwargs)
@commandWrap
def XgBatchExportArchive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgBatchExportArchive(*args, **kwargs)
@commandWrap
def dR_loadRecentFile1(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_loadRecentFile1(*args, **kwargs)
@commandWrap
def MoveNormalTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveNormalTool(*args, **kwargs)
@commandWrap
def dR_loadRecentFile3(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_loadRecentFile3(*args, **kwargs)
@commandWrap
def dR_loadRecentFile4(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_loadRecentFile4(*args, **kwargs)
@commandWrap
def setAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setAttr(*args, **kwargs)
@commandWrap
def dgeval(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgeval(*args, **kwargs)
@commandWrap
def createNurbsCylinderCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsCylinderCtx(*args, **kwargs)
@commandWrap
def polyUVOverlap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUVOverlap(*args, **kwargs)
@commandWrap
def polyTestPop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyTestPop(*args, **kwargs)
@commandWrap
def bulletRigidSets(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bulletRigidSets(*args, **kwargs)
@commandWrap
def ShareOneBrush(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShareOneBrush(*args, **kwargs)
@commandWrap
def CameraModePerspective(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CameraModePerspective(*args, **kwargs)
@commandWrap
def HypershadeCollapseAsset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCollapseAsset(*args, **kwargs)
@commandWrap
def projectTangent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.projectTangent(*args, **kwargs)
@commandWrap
def UVContourStretchProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVContourStretchProjection(*args, **kwargs)
@commandWrap
def PixelMoveUp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PixelMoveUp(*args, **kwargs)
@commandWrap
def ShowMeshWaxToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshWaxToolOptions(*args, **kwargs)
@commandWrap
def SelectAllCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllCameras(*args, **kwargs)
@commandWrap
def NodeEditorShapeMenuStateAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorShapeMenuStateAll(*args, **kwargs)
@commandWrap
def AssignOfflineFileOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignOfflineFileOptions(*args, **kwargs)
@commandWrap
def ScaleToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleToolOptions(*args, **kwargs)
@commandWrap
def PolygonSoftenHardenOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonSoftenHardenOptions(*args, **kwargs)
@commandWrap
def ShowAllUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowAllUI(*args, **kwargs)
@commandWrap
def SetKeyPath(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKeyPath(*args, **kwargs)
@commandWrap
def EnableExpressions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableExpressions(*args, **kwargs)
@commandWrap
def ExtrudeFaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtrudeFaceOptions(*args, **kwargs)
@commandWrap
def AddInfluenceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddInfluenceOptions(*args, **kwargs)
@commandWrap
def SelectMultiComponentMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectMultiComponentMask(*args, **kwargs)
@commandWrap
def FBXExportScaleFactor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportScaleFactor(*args, **kwargs)
@commandWrap
def dR_slideOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_slideOff(*args, **kwargs)
@commandWrap
def NodeEditorToggleAttrFilter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleAttrFilter(*args, **kwargs)
@commandWrap
def AssignOfflineFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignOfflineFile(*args, **kwargs)
@commandWrap
def setFluidAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setFluidAttr(*args, **kwargs)
@commandWrap
def xgmCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCache(*args, **kwargs)
@commandWrap
def convertTessellation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.convertTessellation(*args, **kwargs)
@commandWrap
def LockNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LockNormals(*args, **kwargs)
@commandWrap
def hwReflectionMap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hwReflectionMap(*args, **kwargs)
@commandWrap
def XgmSplineCacheExportOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheExportOptions(*args, **kwargs)
@commandWrap
def SwapBlendShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SwapBlendShape(*args, **kwargs)
@commandWrap
def LoadHIKEffectorSetState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LoadHIKEffectorSetState(*args, **kwargs)
@commandWrap
def HypershadeExportSelectedNetwork(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeExportSelectedNetwork(*args, **kwargs)
@commandWrap
def NodeEditorSetLargeNodeSwatchSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorSetLargeNodeSwatchSize(*args, **kwargs)
@commandWrap
def OutlinerToggleConnected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleConnected(*args, **kwargs)
@commandWrap
def greasePencilHelper(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.greasePencilHelper(*args, **kwargs)
@commandWrap
def PolyExtrudeEdgesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrudeEdgesOptions(*args, **kwargs)
@commandWrap
def glRenderEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.glRenderEditor(*args, **kwargs)
@commandWrap
def customerInvolvementProgram(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.customerInvolvementProgram(*args, **kwargs)
@commandWrap
def HotkeyPreferencesWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HotkeyPreferencesWindow(*args, **kwargs)
@commandWrap
def GraphDelete(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphDelete(*args, **kwargs)
@commandWrap
def internalVar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.internalVar(*args, **kwargs)
@commandWrap
def FBXGetTakeComment(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXGetTakeComment(*args, **kwargs)
@commandWrap
def ExtendCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendCurve(*args, **kwargs)
@commandWrap
def SelectAllNURBSCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllNURBSCurves(*args, **kwargs)
@commandWrap
def TexSewActivateBrushSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSewActivateBrushSize(*args, **kwargs)
@commandWrap
def GeometryConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GeometryConstraintOptions(*args, **kwargs)
@commandWrap
def FBXExportBakeComplexStep(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportBakeComplexStep(*args, **kwargs)
@commandWrap
def Birail3Options(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Birail3Options(*args, **kwargs)
@commandWrap
def character(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.character(*args, **kwargs)
@commandWrap
def OneClickMotionBuilderSendToCurrentScene(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickMotionBuilderSendToCurrentScene(*args, **kwargs)
@commandWrap
def ShowLastHidden(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowLastHidden(*args, **kwargs)
@commandWrap
def dragAttrContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dragAttrContext(*args, **kwargs)
@commandWrap
def findType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.findType(*args, **kwargs)
@commandWrap
def DuplicateCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateCurve(*args, **kwargs)
@commandWrap
def bezierAnchorState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bezierAnchorState(*args, **kwargs)
@commandWrap
def dR_connectPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_connectPress(*args, **kwargs)
@commandWrap
def DeleteCurrentUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteCurrentUVSet(*args, **kwargs)
@commandWrap
def CopyMeshAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyMeshAttributes(*args, **kwargs)
@commandWrap
def NodeEditorAddOnNodeCreate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorAddOnNodeCreate(*args, **kwargs)
@commandWrap
def DeleteHistory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteHistory(*args, **kwargs)
@commandWrap
def ColorPreferencesWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ColorPreferencesWindow(*args, **kwargs)
@commandWrap
def HypershadeTestTextureOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeTestTextureOptions(*args, **kwargs)
@commandWrap
def removeMultiInstance(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.removeMultiInstance(*args, **kwargs)
@commandWrap
def dR_alwaysOnTopTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_alwaysOnTopTGL(*args, **kwargs)
@commandWrap
def CutUVs3D(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutUVs3D(*args, **kwargs)
@commandWrap
def TimeEditorCreateAudioTracksAtEnd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateAudioTracksAtEnd(*args, **kwargs)
@commandWrap
def PointOnCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PointOnCurve(*args, **kwargs)
@commandWrap
def rotate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rotate(*args, **kwargs)
@commandWrap
def AlignUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlignUV(*args, **kwargs)
@commandWrap
def PasteKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PasteKeys(*args, **kwargs)
@commandWrap
def polyProjectCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyProjectCurve(*args, **kwargs)
@commandWrap
def PaintEffectPanelDeactivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectPanelDeactivate(*args, **kwargs)
@commandWrap
def HypershadeOpenConnectWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenConnectWindow(*args, **kwargs)
@commandWrap
def XgmSetPlaceBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetPlaceBrushToolOption(*args, **kwargs)
@commandWrap
def XgGuideTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgGuideTool(*args, **kwargs)
@commandWrap
def subdToBlind(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdToBlind(*args, **kwargs)
@commandWrap
def extendFluid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.extendFluid(*args, **kwargs)
@commandWrap
def ShowMeshGrabToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshGrabToolOptions(*args, **kwargs)
@commandWrap
def polyCrease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCrease(*args, **kwargs)
@commandWrap
def VortexOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.VortexOptions(*args, **kwargs)
@commandWrap
def MergeEdgeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeEdgeTool(*args, **kwargs)
@commandWrap
def PickWalkLeftSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkLeftSelect(*args, **kwargs)
@commandWrap
def dR_viewJointsTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewJointsTGL(*args, **kwargs)
@commandWrap
def XgmCreateInteractiveGroomSplines(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmCreateInteractiveGroomSplines(*args, **kwargs)
@commandWrap
def CoarserSubdivLevel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CoarserSubdivLevel(*args, **kwargs)
@commandWrap
def TimeEditorFbxExportAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorFbxExportAll(*args, **kwargs)
@commandWrap
def pluginDisplayFilter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pluginDisplayFilter(*args, **kwargs)
@commandWrap
def FBXLoadImportPresetFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXLoadImportPresetFile(*args, **kwargs)
@commandWrap
def TemplateObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TemplateObject(*args, **kwargs)
@commandWrap
def JointToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.JointToolOptions(*args, **kwargs)
@commandWrap
def CombinePolygonsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CombinePolygonsOptions(*args, **kwargs)
@commandWrap
def polySplit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySplit(*args, **kwargs)
@commandWrap
def MakeMotorBoatsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeMotorBoatsOptions(*args, **kwargs)
@commandWrap
def CircularFilletOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CircularFilletOptions(*args, **kwargs)
@commandWrap
def ToggleAutoActivateBodyPart(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleAutoActivateBodyPart(*args, **kwargs)
@commandWrap
def createRenderLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createRenderLayer(*args, **kwargs)
@commandWrap
def MatchUVsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MatchUVsOptions(*args, **kwargs)
@commandWrap
def CutKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutKeys(*args, **kwargs)
@commandWrap
def polySetVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySetVertices(*args, **kwargs)
@commandWrap
def OutlinerToggleDAGOnly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleDAGOnly(*args, **kwargs)
@commandWrap
def NodeEditorConnectOnDrop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorConnectOnDrop(*args, **kwargs)
@commandWrap
def nexQuadDrawContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexQuadDrawContext(*args, **kwargs)
@commandWrap
def polyWarpImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyWarpImage(*args, **kwargs)
@commandWrap
def curveEditorCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveEditorCtx(*args, **kwargs)
@commandWrap
def HypershadeMoveTabLeft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeMoveTabLeft(*args, **kwargs)
@commandWrap
def ExtractFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtractFace(*args, **kwargs)
@commandWrap
def Loft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Loft(*args, **kwargs)
@commandWrap
def sbs_GetGraphsNamesFromSubstanceNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetGraphsNamesFromSubstanceNode(*args, **kwargs)
@commandWrap
def EnableDynamicConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableDynamicConstraints(*args, **kwargs)
@commandWrap
def CVCurveTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CVCurveTool(*args, **kwargs)
@commandWrap
def DeleteAllFluids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllFluids(*args, **kwargs)
@commandWrap
def nodePreset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nodePreset(*args, **kwargs)
@commandWrap
def animDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.animDisplay(*args, **kwargs)
@commandWrap
def HideLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideLights(*args, **kwargs)
@commandWrap
def clipSchedulerOutliner(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clipSchedulerOutliner(*args, **kwargs)
@commandWrap
def GetSettingsFromSelectedStroke(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetSettingsFromSelectedStroke(*args, **kwargs)
@commandWrap
def dR_paintRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_paintRelease(*args, **kwargs)
@commandWrap
def DecreaseExposureCoarse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DecreaseExposureCoarse(*args, **kwargs)
@commandWrap
def ToggleOutliner(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleOutliner(*args, **kwargs)
@commandWrap
def SculptSurfacesTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptSurfacesTool(*args, **kwargs)
@commandWrap
def nurbsSquare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsSquare(*args, **kwargs)
@commandWrap
def TimeEditorToggleTimeCursorRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorToggleTimeCursorRelease(*args, **kwargs)
@commandWrap
def nClothCreateOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothCreateOptions(*args, **kwargs)
@commandWrap
def HypershadePerspLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePerspLayout(*args, **kwargs)
@commandWrap
def TagAsControllerParent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TagAsControllerParent(*args, **kwargs)
@commandWrap
def PreviousKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreviousKey(*args, **kwargs)
@commandWrap
def PreviousFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreviousFrame(*args, **kwargs)
@commandWrap
def muMessageAdd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.muMessageAdd(*args, **kwargs)
@commandWrap
def commandEcho(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.commandEcho(*args, **kwargs)
@commandWrap
def UVSphericalProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVSphericalProjection(*args, **kwargs)
@commandWrap
def polyDelFacet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyDelFacet(*args, **kwargs)
@commandWrap
def ToggleTextureBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleTextureBorder(*args, **kwargs)
@commandWrap
def Flare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Flare(*args, **kwargs)
@commandWrap
def pose(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pose(*args, **kwargs)
@commandWrap
def RemoveInbetween(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveInbetween(*args, **kwargs)
@commandWrap
def selectPref(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectPref(*args, **kwargs)
@commandWrap
def FBXGetTakeIndex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXGetTakeIndex(*args, **kwargs)
@commandWrap
def SelectAllWires(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllWires(*args, **kwargs)
@commandWrap
def polyColorMod(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyColorMod(*args, **kwargs)
@commandWrap
def AddToCurrentScene3dsMax(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddToCurrentScene3dsMax(*args, **kwargs)
@commandWrap
def AddSelectionAsTargetShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddSelectionAsTargetShape(*args, **kwargs)
@commandWrap
def DistanceTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DistanceTool(*args, **kwargs)
@commandWrap
def ToggleIsolateSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleIsolateSelect(*args, **kwargs)
@commandWrap
def polyCloseBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCloseBorder(*args, **kwargs)
@commandWrap
def AutoProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AutoProjectionOptions(*args, **kwargs)
@commandWrap
def MakeHoleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeHoleTool(*args, **kwargs)
@commandWrap
def FrameSelectedInAllViews(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FrameSelectedInAllViews(*args, **kwargs)
@commandWrap
def ToggleCapsLockDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCapsLockDisplay(*args, **kwargs)
@commandWrap
def XgmSetDirectionBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetDirectionBrushToolOption(*args, **kwargs)
@commandWrap
def GetHIKNodeName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKNodeName(*args, **kwargs)
@commandWrap
def DeleteTextureReferenceObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteTextureReferenceObject(*args, **kwargs)
@commandWrap
def GetHairExample(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHairExample(*args, **kwargs)
@commandWrap
def attachGeometryCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attachGeometryCache(*args, **kwargs)
@commandWrap
def RemoveInfluence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveInfluence(*args, **kwargs)
@commandWrap
def SelectUVFrontFacingComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVFrontFacingComponents(*args, **kwargs)
@commandWrap
def SelectAllNParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllNParticles(*args, **kwargs)
@commandWrap
def SelectLinesMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectLinesMask(*args, **kwargs)
@commandWrap
def AddBifrostKillplane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostKillplane(*args, **kwargs)
@commandWrap
def SelectedAnimLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectedAnimLayer(*args, **kwargs)
@commandWrap
def SnapPointToPoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapPointToPoint(*args, **kwargs)
@commandWrap
def SmoothPolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothPolygonOptions(*args, **kwargs)
@commandWrap
def CreateSoftBodyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSoftBodyOptions(*args, **kwargs)
@commandWrap
def UIModeMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UIModeMarkingMenu(*args, **kwargs)
@commandWrap
def HideWrapInfluences(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideWrapInfluences(*args, **kwargs)
@commandWrap
def ExtendFluid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendFluid(*args, **kwargs)
@commandWrap
def PlaybackForward(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PlaybackForward(*args, **kwargs)
@commandWrap
def dbpeek(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dbpeek(*args, **kwargs)
@commandWrap
def TimeEditorClipTrimEnd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipTrimEnd(*args, **kwargs)
@commandWrap
def toolHasOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.toolHasOptions(*args, **kwargs)
@commandWrap
def MatchPivots(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MatchPivots(*args, **kwargs)
@commandWrap
def AddInfluence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddInfluence(*args, **kwargs)
@commandWrap
def polyColorSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyColorSet(*args, **kwargs)
@commandWrap
def curveIntersect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveIntersect(*args, **kwargs)
@commandWrap
def DeltaMushOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeltaMushOptions(*args, **kwargs)
@commandWrap
def filletCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.filletCurve(*args, **kwargs)
@commandWrap
def ShowObjectGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowObjectGeometry(*args, **kwargs)
@commandWrap
def PencilCurveTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PencilCurveTool(*args, **kwargs)
@commandWrap
def DecrementFluidCenter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DecrementFluidCenter(*args, **kwargs)
@commandWrap
def OpenCloseCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OpenCloseCurve(*args, **kwargs)
@commandWrap
def xgmSplineBaseDensityScaleChangeCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplineBaseDensityScaleChangeCmd(*args, **kwargs)
@commandWrap
def CutUVsWithoutHotkey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutUVsWithoutHotkey(*args, **kwargs)
@commandWrap
def pointOnCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointOnCurve(*args, **kwargs)
@commandWrap
def CameraSetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CameraSetEditor(*args, **kwargs)
@commandWrap
def RenderFlagsWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderFlagsWindow(*args, **kwargs)
@commandWrap
def SetPreferredAngle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetPreferredAngle(*args, **kwargs)
@commandWrap
def nClothReplaceFramesOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothReplaceFramesOpt(*args, **kwargs)
@commandWrap
def U3DBrushSizeOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.U3DBrushSizeOff(*args, **kwargs)
@commandWrap
def symmetricModelling(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.symmetricModelling(*args, **kwargs)
@commandWrap
def SetShrinkWrapInnerObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetShrinkWrapInnerObject(*args, **kwargs)
@commandWrap
def UVAutomaticProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVAutomaticProjection(*args, **kwargs)
@commandWrap
def RenderSetupWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderSetupWindow(*args, **kwargs)
@commandWrap
def ToggleMultiColorFeedback(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMultiColorFeedback(*args, **kwargs)
@commandWrap
def transformCompare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.transformCompare(*args, **kwargs)
@commandWrap
def InteractiveSplitToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InteractiveSplitToolOptions(*args, **kwargs)
@commandWrap
def selectType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectType(*args, **kwargs)
@commandWrap
def CopyKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyKeys(*args, **kwargs)
@commandWrap
def ShowMeshRepeatToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshRepeatToolOptions(*args, **kwargs)
@commandWrap
def SetFluidAttrFromCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFluidAttrFromCurveOptions(*args, **kwargs)
@commandWrap
def CurveUtilitiesMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveUtilitiesMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def CurveEditTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveEditTool(*args, **kwargs)
@commandWrap
def dR_wireframeSmoothTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_wireframeSmoothTGL(*args, **kwargs)
@commandWrap
def BrushPresetBlendShapeOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetBlendShapeOff(*args, **kwargs)
@commandWrap
def polyColorBlindData(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyColorBlindData(*args, **kwargs)
@commandWrap
def RelaxInitialState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RelaxInitialState(*args, **kwargs)
@commandWrap
def SetKeyVertexColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKeyVertexColor(*args, **kwargs)
@commandWrap
def CancelBatchRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CancelBatchRender(*args, **kwargs)
@commandWrap
def SmoothCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothCurveOptions(*args, **kwargs)
@commandWrap
def dR_modeMulti(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_modeMulti(*args, **kwargs)
@commandWrap
def HypershadeRevertSelectedSwatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRevertSelectedSwatches(*args, **kwargs)
@commandWrap
def dR_viewXrayTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewXrayTGL(*args, **kwargs)
@commandWrap
def dR_selConstraintOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selConstraintOff(*args, **kwargs)
@commandWrap
def SoloLastOutput(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SoloLastOutput(*args, **kwargs)
@commandWrap
def paramLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.paramLocator(*args, **kwargs)
@commandWrap
def polyMoveEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMoveEdge(*args, **kwargs)
@commandWrap
def lightList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lightList(*args, **kwargs)
@commandWrap
def distanceDimension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.distanceDimension(*args, **kwargs)
@commandWrap
def CreateShrinkWrap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateShrinkWrap(*args, **kwargs)
@commandWrap
def SetMeshSmoothTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshSmoothTool(*args, **kwargs)
@commandWrap
def NodeEditorBackToParent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorBackToParent(*args, **kwargs)
@commandWrap
def XgPreRendering(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgPreRendering(*args, **kwargs)
@commandWrap
def ArtPaintSelectToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintSelectToolOptions(*args, **kwargs)
@commandWrap
def SetAsCombinationTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetAsCombinationTarget(*args, **kwargs)
@commandWrap
def Fire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Fire(*args, **kwargs)
@commandWrap
def RefineSelectedComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RefineSelectedComponents(*args, **kwargs)
@commandWrap
def dR_targetWeldRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_targetWeldRelease(*args, **kwargs)
@commandWrap
def SelectAllDynamicConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllDynamicConstraints(*args, **kwargs)
@commandWrap
def FBXLoadExportPresetFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXLoadExportPresetFile(*args, **kwargs)
@commandWrap
def HypershadeDeleteAllUtilities(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteAllUtilities(*args, **kwargs)
@commandWrap
def AddToCurrentSceneMotionBuilder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddToCurrentSceneMotionBuilder(*args, **kwargs)
@commandWrap
def MirrorJointOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorJointOptions(*args, **kwargs)
@commandWrap
def EnterEditMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnterEditMode(*args, **kwargs)
@commandWrap
def BoundaryOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BoundaryOptions(*args, **kwargs)
@commandWrap
def dR_setRelaxAffectsAuto(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_setRelaxAffectsAuto(*args, **kwargs)
@commandWrap
def artAttrTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artAttrTool(*args, **kwargs)
@commandWrap
def PaintOperationMarkingMenuRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintOperationMarkingMenuRelease(*args, **kwargs)
@commandWrap
def emit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.emit(*args, **kwargs)
@commandWrap
def delete(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.delete(*args, **kwargs)
@commandWrap
def trim(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.trim(*args, **kwargs)
@commandWrap
def ShowNURBSSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowNURBSSurfaces(*args, **kwargs)
@commandWrap
def ExportDeformerWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportDeformerWeights(*args, **kwargs)
@commandWrap
def graphSelectContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.graphSelectContext(*args, **kwargs)
@commandWrap
def Create3DContainerEmitterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create3DContainerEmitterOptions(*args, **kwargs)
@commandWrap
def nClothReplaceCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothReplaceCacheOpt(*args, **kwargs)
@commandWrap
def NodeEditorGraphClearGraph(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphClearGraph(*args, **kwargs)
@commandWrap
def polyMapSewMove(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMapSewMove(*args, **kwargs)
@commandWrap
def GraphEditorDisableCurveSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorDisableCurveSelection(*args, **kwargs)
@commandWrap
def TimeEditorUnmuteSelectedTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorUnmuteSelectedTracks(*args, **kwargs)
@commandWrap
def polyCircularizeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCircularizeEdge(*args, **kwargs)
@commandWrap
def BrushPresetReplaceShading(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetReplaceShading(*args, **kwargs)
@commandWrap
def CreateHair(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateHair(*args, **kwargs)
@commandWrap
def NextManipulatorHandle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NextManipulatorHandle(*args, **kwargs)
@commandWrap
def licenseCheck(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.licenseCheck(*args, **kwargs)
@commandWrap
def UnmirrorSmoothProxy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnmirrorSmoothProxy(*args, **kwargs)
@commandWrap
def CreateSoftBody(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSoftBody(*args, **kwargs)
@commandWrap
def HypershadeOpenUVEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenUVEditorWindow(*args, **kwargs)
@commandWrap
def mpBirailCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mpBirailCtx(*args, **kwargs)
@commandWrap
def polyPlatonicSolid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPlatonicSolid(*args, **kwargs)
@commandWrap
def insertJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.insertJoint(*args, **kwargs)
@commandWrap
def ShareUVInstances(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShareUVInstances(*args, **kwargs)
@commandWrap
def changeSubdivComponentDisplayLevel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.changeSubdivComponentDisplayLevel(*args, **kwargs)
@commandWrap
def SculptMeshDeactivateBrushStrength(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptMeshDeactivateBrushStrength(*args, **kwargs)
@commandWrap
def polySelectEditCtxDataCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySelectEditCtxDataCmd(*args, **kwargs)
@commandWrap
def ProfilerToolThreadView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolThreadView(*args, **kwargs)
@commandWrap
def LevelOfDetailGroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LevelOfDetailGroup(*args, **kwargs)
@commandWrap
def PostInfinityCycleOffset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PostInfinityCycleOffset(*args, **kwargs)
@commandWrap
def ShowMeshGrabUVToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshGrabUVToolOptions(*args, **kwargs)
@commandWrap
def PasteVertexSkinWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PasteVertexSkinWeights(*args, **kwargs)
@commandWrap
def artAttrCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artAttrCtx(*args, **kwargs)
@commandWrap
def ShowMeshSmearToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshSmearToolOptions(*args, **kwargs)
@commandWrap
def Create3DContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create3DContainer(*args, **kwargs)
@commandWrap
def roll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.roll(*args, **kwargs)
@commandWrap
def TimeEditorClipScaleEnd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipScaleEnd(*args, **kwargs)
@commandWrap
def setAttrMapping(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setAttrMapping(*args, **kwargs)
@commandWrap
def pairBlend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pairBlend(*args, **kwargs)
@commandWrap
def xgmCombBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCombBrushContext(*args, **kwargs)
@commandWrap
def frameBufferName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.frameBufferName(*args, **kwargs)
@commandWrap
def HypershadeEditPSDFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeEditPSDFile(*args, **kwargs)
@commandWrap
def LockContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LockContainer(*args, **kwargs)
@commandWrap
def RebuildCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RebuildCurveOptions(*args, **kwargs)
@commandWrap
def HideGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideGeometry(*args, **kwargs)
@commandWrap
def drag(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.drag(*args, **kwargs)
@commandWrap
def SnapToGridRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToGridRelease(*args, **kwargs)
@commandWrap
def fileDialog(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fileDialog(*args, **kwargs)
@commandWrap
def sysFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sysFile(*args, **kwargs)
@commandWrap
def MatchTranslation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MatchTranslation(*args, **kwargs)
@commandWrap
def MoveRotateScaleToolToggleSnapMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveRotateScaleToolToggleSnapMode(*args, **kwargs)
@commandWrap
def PlaybackStop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PlaybackStop(*args, **kwargs)
@commandWrap
def ToggleEdgeIDs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleEdgeIDs(*args, **kwargs)
@commandWrap
def TangentsPlateau(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsPlateau(*args, **kwargs)
@commandWrap
def IncreaseCheckerDensity(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncreaseCheckerDensity(*args, **kwargs)
@commandWrap
def combinationShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.combinationShape(*args, **kwargs)
@commandWrap
def xgmPointsContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPointsContext(*args, **kwargs)
@commandWrap
def xgmExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmExport(*args, **kwargs)
@commandWrap
def SoftModDeformerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SoftModDeformerOptions(*args, **kwargs)
@commandWrap
def objExists(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.objExists(*args, **kwargs)
@commandWrap
def currentTime(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.currentTime(*args, **kwargs)
@commandWrap
def xgmSplineGeometryConvert(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplineGeometryConvert(*args, **kwargs)
@commandWrap
def dpBirailCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dpBirailCtx(*args, **kwargs)
@commandWrap
def connectJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.connectJoint(*args, **kwargs)
@commandWrap
def shadingConnection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shadingConnection(*args, **kwargs)
@commandWrap
def ScaleToolMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleToolMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def hikRigSync(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikRigSync(*args, **kwargs)
@commandWrap
def findKeyframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.findKeyframe(*args, **kwargs)
@commandWrap
def polyCreateFacetCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCreateFacetCtx(*args, **kwargs)
@commandWrap
def attributeQuery(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attributeQuery(*args, **kwargs)
@commandWrap
def nParticle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nParticle(*args, **kwargs)
@commandWrap
def PaintEffectsToPolyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsToPolyOptions(*args, **kwargs)
@commandWrap
def HypershadeCreateContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCreateContainerOptions(*args, **kwargs)
@commandWrap
def SculptPolygonsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptPolygonsTool(*args, **kwargs)
@commandWrap
def dgTimerSpreadsheet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgTimerSpreadsheet(*args, **kwargs)
@commandWrap
def TimeEditorUnsoloAllTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorUnsoloAllTracks(*args, **kwargs)
@commandWrap
def CurveUtilitiesMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveUtilitiesMarkingMenu(*args, **kwargs)
@commandWrap
def ilrInternalVar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrInternalVar(*args, **kwargs)
@commandWrap
def PolyExtrudeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrudeOptions(*args, **kwargs)
@commandWrap
def CreateSubdivRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivRegion(*args, **kwargs)
@commandWrap
def createPolySoccerBallCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolySoccerBallCtx(*args, **kwargs)
@commandWrap
def scriptCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scriptCtx(*args, **kwargs)
@commandWrap
def ToggleViewCube(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleViewCube(*args, **kwargs)
@commandWrap
def fluidDeleteCacheFramesOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidDeleteCacheFramesOpt(*args, **kwargs)
@commandWrap
def SelectUVOverlappingComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVOverlappingComponents(*args, **kwargs)
@commandWrap
def AnimationTurntable(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AnimationTurntable(*args, **kwargs)
@commandWrap
def SetIKFKKeyframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetIKFKKeyframe(*args, **kwargs)
@commandWrap
def ExportOfflineFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportOfflineFile(*args, **kwargs)
@commandWrap
def VisorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.VisorWindow(*args, **kwargs)
@commandWrap
def CreateVolumeLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateVolumeLight(*args, **kwargs)
@commandWrap
def manipMoveContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipMoveContext(*args, **kwargs)
@commandWrap
def constructionHistory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.constructionHistory(*args, **kwargs)
@commandWrap
def ConformPolygonNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConformPolygonNormals(*args, **kwargs)
@commandWrap
def ScaleToolWithSnapMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleToolWithSnapMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def polyAppend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyAppend(*args, **kwargs)
@commandWrap
def XgmSetSelectBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetSelectBrushToolOption(*args, **kwargs)
@commandWrap
def CreatePolygonPipeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPipeOptions(*args, **kwargs)
@commandWrap
def AddBifrostEmissionRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostEmissionRegion(*args, **kwargs)
@commandWrap
def crashInfoCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.crashInfoCmd(*args, **kwargs)
@commandWrap
def multiProfileBirailSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.multiProfileBirailSurface(*args, **kwargs)
@commandWrap
def disconnectAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.disconnectAttr(*args, **kwargs)
@commandWrap
def manipMoveLimitsCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipMoveLimitsCtx(*args, **kwargs)
@commandWrap
def ArchiveSceneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArchiveSceneOptions(*args, **kwargs)
@commandWrap
def DeviceEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeviceEditor(*args, **kwargs)
@commandWrap
def ToggleFaceNormalDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFaceNormalDisplay(*args, **kwargs)
@commandWrap
def BakeChannelOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeChannelOptions(*args, **kwargs)
@commandWrap
def OutlinerToggleShowMuteInformation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleShowMuteInformation(*args, **kwargs)
@commandWrap
def TimeEditorOpenContentBrowser(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorOpenContentBrowser(*args, **kwargs)
@commandWrap
def autoKeyframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.autoKeyframe(*args, **kwargs)
@commandWrap
def ExportSkinWeightMapsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportSkinWeightMapsOptions(*args, **kwargs)
@commandWrap
def HideFur(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideFur(*args, **kwargs)
@commandWrap
def XgmSetNoiseBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetNoiseBrushTool(*args, **kwargs)
@commandWrap
def HypershadePinByDefault(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePinByDefault(*args, **kwargs)
@commandWrap
def DeleteHair(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteHair(*args, **kwargs)
@commandWrap
def dR_modeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_modeEdge(*args, **kwargs)
@commandWrap
def TimeEditorCreateAudioClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateAudioClip(*args, **kwargs)
@commandWrap
def NodeEditorCreateForEachCompound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCreateForEachCompound(*args, **kwargs)
@commandWrap
def SetDrivenKeyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetDrivenKeyOptions(*args, **kwargs)
@commandWrap
def CreatePartition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePartition(*args, **kwargs)
@commandWrap
def performanceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.performanceOptions(*args, **kwargs)
@commandWrap
def HIKSetSelectionKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKSetSelectionKey(*args, **kwargs)
@commandWrap
def IntersectSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IntersectSurfacesOptions(*args, **kwargs)
@commandWrap
def ToggleFaceNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFaceNormals(*args, **kwargs)
@commandWrap
def PaintEffectsToNurbs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsToNurbs(*args, **kwargs)
@commandWrap
def DoUnghostOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DoUnghostOptions(*args, **kwargs)
@commandWrap
def TangentsStepped(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsStepped(*args, **kwargs)
@commandWrap
def manipScaleContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipScaleContext(*args, **kwargs)
@commandWrap
def DeleteConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteConstraints(*args, **kwargs)
@commandWrap
def XgmSplineCacheEnableSelectedCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheEnableSelectedCache(*args, **kwargs)
@commandWrap
def ResampleCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResampleCurveOptions(*args, **kwargs)
@commandWrap
def ToggleNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleNormals(*args, **kwargs)
@commandWrap
def TimeEditorToggleMuteSelectedTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorToggleMuteSelectedTracks(*args, **kwargs)
@commandWrap
def nBase(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nBase(*args, **kwargs)
@commandWrap
def PreInfinityLinear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreInfinityLinear(*args, **kwargs)
@commandWrap
def ExportSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportSelection(*args, **kwargs)
@commandWrap
def ConvertSelectionToEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToEdges(*args, **kwargs)
@commandWrap
def InsertKeysTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertKeysTool(*args, **kwargs)
@commandWrap
def filterExpand(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.filterExpand(*args, **kwargs)
@commandWrap
def CreatePolygonUltraShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonUltraShapeOptions(*args, **kwargs)
@commandWrap
def TemplateBrushSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TemplateBrushSettings(*args, **kwargs)
@commandWrap
def ReorderVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReorderVertex(*args, **kwargs)
@commandWrap
def ctxAbort(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ctxAbort(*args, **kwargs)
@commandWrap
def selectKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectKey(*args, **kwargs)
@commandWrap
def colorManagementCatalog(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.colorManagementCatalog(*args, **kwargs)
@commandWrap
def dR_setRelaxAffectsInterior(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_setRelaxAffectsInterior(*args, **kwargs)
@commandWrap
def U3DBrushSizeOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.U3DBrushSizeOn(*args, **kwargs)
@commandWrap
def retimeKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.retimeKeyCtx(*args, **kwargs)
@commandWrap
def CreateNURBSSphereOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSSphereOptions(*args, **kwargs)
@commandWrap
def CreateNURBSSquare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSSquare(*args, **kwargs)
@commandWrap
def OutlinerToggleNamespace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleNamespace(*args, **kwargs)
@commandWrap
def LockTangentWeight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LockTangentWeight(*args, **kwargs)
@commandWrap
def SetMeshGrabTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshGrabTool(*args, **kwargs)
@commandWrap
def popPinning(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.popPinning(*args, **kwargs)
@commandWrap
def ToggleDisplacement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleDisplacement(*args, **kwargs)
@commandWrap
def nexConnectContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexConnectContext(*args, **kwargs)
@commandWrap
def ShowModelingUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowModelingUI(*args, **kwargs)
@commandWrap
def xgmGuideSculptContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGuideSculptContext(*args, **kwargs)
@commandWrap
def TogglePolyCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyCount(*args, **kwargs)
@commandWrap
def OneClickExecute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickExecute(*args, **kwargs)
@commandWrap
def bifSaveFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bifSaveFrame(*args, **kwargs)
@commandWrap
def HypershadeOpenRenderViewWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenRenderViewWindow(*args, **kwargs)
@commandWrap
def curveRGBColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveRGBColor(*args, **kwargs)
@commandWrap
def GraphEditorUnlockChannel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorUnlockChannel(*args, **kwargs)
@commandWrap
def PanelPreferencesWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PanelPreferencesWindow(*args, **kwargs)
@commandWrap
def OneClickDisconnect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickDisconnect(*args, **kwargs)
@commandWrap
def PostInfinityLinear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PostInfinityLinear(*args, **kwargs)
@commandWrap
def view2dToolCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.view2dToolCtx(*args, **kwargs)
@commandWrap
def BestPlaneTexturingTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BestPlaneTexturingTool(*args, **kwargs)
@commandWrap
def copyAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.copyAttr(*args, **kwargs)
@commandWrap
def SetFluidAttrFromCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFluidAttrFromCurve(*args, **kwargs)
@commandWrap
def DisplayUVWireframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayUVWireframe(*args, **kwargs)
@commandWrap
def GetHIKChildId(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKChildId(*args, **kwargs)
@commandWrap
def subdMatchTopology(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdMatchTopology(*args, **kwargs)
@commandWrap
def XgExportArchive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgExportArchive(*args, **kwargs)
@commandWrap
def uniform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.uniform(*args, **kwargs)
@commandWrap
def ViewAlongAxisNegativeZ(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewAlongAxisNegativeZ(*args, **kwargs)
@commandWrap
def ViewAlongAxisNegativeX(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewAlongAxisNegativeX(*args, **kwargs)
@commandWrap
def HypershadeSelectConnected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectConnected(*args, **kwargs)
@commandWrap
def TimeEditorCreateAnimTracksAtEnd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateAnimTracksAtEnd(*args, **kwargs)
@commandWrap
def SetVertexNormalOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetVertexNormalOptions(*args, **kwargs)
@commandWrap
def subdListComponentConversion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdListComponentConversion(*args, **kwargs)
@commandWrap
def UVContourStretchProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVContourStretchProjectionOptions(*args, **kwargs)
@commandWrap
def blend2(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blend2(*args, **kwargs)
@commandWrap
def gpuCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.gpuCache(*args, **kwargs)
@commandWrap
def EnableNRigids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableNRigids(*args, **kwargs)
@commandWrap
def pointOnPolyConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointOnPolyConstraint(*args, **kwargs)
@commandWrap
def AddToCharacterSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddToCharacterSet(*args, **kwargs)
@commandWrap
def TwoPointArcTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TwoPointArcTool(*args, **kwargs)
@commandWrap
def WedgePolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WedgePolygonOptions(*args, **kwargs)
@commandWrap
def PrelightPolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PrelightPolygonOptions(*args, **kwargs)
@commandWrap
def HypershadeDuplicateShadingNetwork(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDuplicateShadingNetwork(*args, **kwargs)
@commandWrap
def nurbsCopyUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsCopyUVSet(*args, **kwargs)
@commandWrap
def UVSphericalProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVSphericalProjectionOptions(*args, **kwargs)
@commandWrap
def HIKPinTranslate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKPinTranslate(*args, **kwargs)
@commandWrap
def pause(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pause(*args, **kwargs)
@commandWrap
def CreatePolygonDiscOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonDiscOptions(*args, **kwargs)
@commandWrap
def CreateWrap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateWrap(*args, **kwargs)
@commandWrap
def GraphEditorStackedView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorStackedView(*args, **kwargs)
@commandWrap
def dR_selectRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectRelease(*args, **kwargs)
@commandWrap
def HypershadeTransferAttributeValuesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeTransferAttributeValuesOptions(*args, **kwargs)
@commandWrap
def BrushPresetBlendOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetBlendOff(*args, **kwargs)
@commandWrap
def FBXResamplingRate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXResamplingRate(*args, **kwargs)
@commandWrap
def targetWeldCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.targetWeldCtx(*args, **kwargs)
@commandWrap
def PolygonBooleanIntersection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonBooleanIntersection(*args, **kwargs)
@commandWrap
def polyHole(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyHole(*args, **kwargs)
@commandWrap
def SpreadSheetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SpreadSheetEditor(*args, **kwargs)
@commandWrap
def FBXRead(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXRead(*args, **kwargs)
@commandWrap
def commandPort(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.commandPort(*args, **kwargs)
@commandWrap
def OutlinerToggleOrganizeByClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleOrganizeByClip(*args, **kwargs)
@commandWrap
def OrientConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OrientConstraintOptions(*args, **kwargs)
@commandWrap
def PublishConnections(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishConnections(*args, **kwargs)
@commandWrap
def polyPinUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPinUV(*args, **kwargs)
@commandWrap
def RandomizeShellsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RandomizeShellsOptions(*args, **kwargs)
@commandWrap
def dR_pointSnapRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_pointSnapRelease(*args, **kwargs)
@commandWrap
def ArtPaintBlendShapeWeightsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintBlendShapeWeightsToolOptions(*args, **kwargs)
@commandWrap
def muMessageDelete(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.muMessageDelete(*args, **kwargs)
@commandWrap
def PartitionEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PartitionEditor(*args, **kwargs)
@commandWrap
def TimeEditorClipHoldToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipHoldToggle(*args, **kwargs)
@commandWrap
def geometryReplaceCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryReplaceCacheOpt(*args, **kwargs)
@commandWrap
def NodeEditorCopy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCopy(*args, **kwargs)
@commandWrap
def ArcLengthTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArcLengthTool(*args, **kwargs)
@commandWrap
def cycleCheck(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cycleCheck(*args, **kwargs)
@commandWrap
def SendAsNewScenePrintStudio(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendAsNewScenePrintStudio(*args, **kwargs)
@commandWrap
def ModifyOpacityPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyOpacityPress(*args, **kwargs)
@commandWrap
def Import(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Import(*args, **kwargs)
@commandWrap
def dynExpression(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynExpression(*args, **kwargs)
@commandWrap
def nClothCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothCache(*args, **kwargs)
@commandWrap
def renderSetupFind(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetupFind(*args, **kwargs)
@commandWrap
def AssignOfflineFileFromRefEd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignOfflineFileFromRefEd(*args, **kwargs)
@commandWrap
def rotationInterpolation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rotationInterpolation(*args, **kwargs)
@commandWrap
def changeSubdivRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.changeSubdivRegion(*args, **kwargs)
@commandWrap
def SculptMeshInvertFreeze(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptMeshInvertFreeze(*args, **kwargs)
@commandWrap
def ConvertSelectionToUVShell(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToUVShell(*args, **kwargs)
@commandWrap
def DeleteAllStaticChannels(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllStaticChannels(*args, **kwargs)
@commandWrap
def EmitFluidFromObjectOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EmitFluidFromObjectOptions(*args, **kwargs)
@commandWrap
def createDisplayLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createDisplayLayer(*args, **kwargs)
@commandWrap
def RenderOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderOptions(*args, **kwargs)
@commandWrap
def polyCylindricalProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCylindricalProjection(*args, **kwargs)
@commandWrap
def MoveToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveToolOptions(*args, **kwargs)
@commandWrap
def memory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.memory(*args, **kwargs)
@commandWrap
def polyNormalizeUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyNormalizeUV(*args, **kwargs)
@commandWrap
def appendListItem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.appendListItem(*args, **kwargs)
@commandWrap
def polyBlindData(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyBlindData(*args, **kwargs)
@commandWrap
def PointConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PointConstraint(*args, **kwargs)
@commandWrap
def GridOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GridOptions(*args, **kwargs)
@commandWrap
def AddInBetweenTargetShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddInBetweenTargetShapeOptions(*args, **kwargs)
@commandWrap
def ToggleUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVs(*args, **kwargs)
@commandWrap
def dR_bridgeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_bridgeTool(*args, **kwargs)
@commandWrap
def timeEditorPanel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorPanel(*args, **kwargs)
@commandWrap
def ExportSelectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportSelectionOptions(*args, **kwargs)
@commandWrap
def AddDivisions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddDivisions(*args, **kwargs)
@commandWrap
def readPDC(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.readPDC(*args, **kwargs)
@commandWrap
def addPP(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.addPP(*args, **kwargs)
@commandWrap
def polyLayoutUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyLayoutUV(*args, **kwargs)
@commandWrap
def FBXUICallBack(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXUICallBack(*args, **kwargs)
@commandWrap
def OffsetSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetSurfaces(*args, **kwargs)
@commandWrap
def SelectPreviousObjectsMotionBuilder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectPreviousObjectsMotionBuilder(*args, **kwargs)
@commandWrap
def CreatePoseInterpolatorEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePoseInterpolatorEditor(*args, **kwargs)
@commandWrap
def NodeEditorConnectSelectedNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorConnectSelectedNodes(*args, **kwargs)
@commandWrap
def ChangeUVSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ChangeUVSize(*args, **kwargs)
@commandWrap
def CreateClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateClip(*args, **kwargs)
@commandWrap
def OrientJointOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OrientJointOptions(*args, **kwargs)
@commandWrap
def hikGetNodeIdFromName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikGetNodeIdFromName(*args, **kwargs)
@commandWrap
def AttachBrushToCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachBrushToCurves(*args, **kwargs)
@commandWrap
def ShowMeshMaskToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshMaskToolOptions(*args, **kwargs)
@commandWrap
def PolyBrushMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyBrushMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def RenameAttribute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenameAttribute(*args, **kwargs)
@commandWrap
def sphere(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sphere(*args, **kwargs)
@commandWrap
def FourViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FourViewArrangement(*args, **kwargs)
@commandWrap
def AddTimeWarp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddTimeWarp(*args, **kwargs)
@commandWrap
def aliasAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.aliasAttr(*args, **kwargs)
@commandWrap
def dR_bridgeRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_bridgeRelease(*args, **kwargs)
@commandWrap
def ShowLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowLights(*args, **kwargs)
@commandWrap
def NodeEditorAdditiveGraphingMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorAdditiveGraphingMode(*args, **kwargs)
@commandWrap
def HypershadeSetTraversalDepthUnlim(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSetTraversalDepthUnlim(*args, **kwargs)
@commandWrap
def PokePolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PokePolygonOptions(*args, **kwargs)
@commandWrap
def ToggleMeshUVBorders(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMeshUVBorders(*args, **kwargs)
@commandWrap
def HideDeformers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideDeformers(*args, **kwargs)
@commandWrap
def deformer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deformer(*args, **kwargs)
@commandWrap
def BrushAnimationMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushAnimationMarkingMenu(*args, **kwargs)
@commandWrap
def PinSelectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PinSelectionOptions(*args, **kwargs)
@commandWrap
def SelectLightsShadowingObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectLightsShadowingObject(*args, **kwargs)
@commandWrap
def SetKeyAnimated(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKeyAnimated(*args, **kwargs)
@commandWrap
def xgmPushOver(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPushOver(*args, **kwargs)
@commandWrap
def dR_graphEditorTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_graphEditorTGL(*args, **kwargs)
@commandWrap
def ToggleViewAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleViewAxis(*args, **kwargs)
@commandWrap
def OutlinerWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerWindow(*args, **kwargs)
@commandWrap
def ToggleEditPoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleEditPoints(*args, **kwargs)
@commandWrap
def stroke(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stroke(*args, **kwargs)
@commandWrap
def CreateEmptyUVSetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateEmptyUVSetOptions(*args, **kwargs)
@commandWrap
def XgmCreateInteractiveGroomSplinesOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmCreateInteractiveGroomSplinesOption(*args, **kwargs)
@commandWrap
def HypershadeDisplayAsSmallSwatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayAsSmallSwatches(*args, **kwargs)
@commandWrap
def ReplaceObjectsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReplaceObjectsOptions(*args, **kwargs)
@commandWrap
def UndoCanvas(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UndoCanvas(*args, **kwargs)
@commandWrap
def rebuildCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rebuildCurve(*args, **kwargs)
@commandWrap
def CreateVolumeCone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateVolumeCone(*args, **kwargs)
@commandWrap
def instanceable(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.instanceable(*args, **kwargs)
@commandWrap
def xgmFileRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmFileRender(*args, **kwargs)
@commandWrap
def extendSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.extendSurface(*args, **kwargs)
@commandWrap
def SnapPointToPointOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapPointToPointOptions(*args, **kwargs)
@commandWrap
def renderSetupSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetupSelect(*args, **kwargs)
@commandWrap
def HypershadeSelectDownStream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectDownStream(*args, **kwargs)
@commandWrap
def dR_modeObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_modeObject(*args, **kwargs)
@commandWrap
def ToggleLocalRotationAxes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleLocalRotationAxes(*args, **kwargs)
@commandWrap
def renderManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderManip(*args, **kwargs)
@commandWrap
def ToggleZoomInMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleZoomInMode(*args, **kwargs)
@commandWrap
def FBXImportScaleFactor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportScaleFactor(*args, **kwargs)
@commandWrap
def Birail1Options(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Birail1Options(*args, **kwargs)
@commandWrap
def Gravity(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Gravity(*args, **kwargs)
@commandWrap
def evalNoSelectNotify(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.evalNoSelectNotify(*args, **kwargs)
@commandWrap
def HypershadeSortReverseOrder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSortReverseOrder(*args, **kwargs)
@commandWrap
def dR_safeFrameTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_safeFrameTGL(*args, **kwargs)
@commandWrap
def nClothAppend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothAppend(*args, **kwargs)
@commandWrap
def setDrivenKeyframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setDrivenKeyframe(*args, **kwargs)
@commandWrap
def geomToBBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geomToBBox(*args, **kwargs)
@commandWrap
def createPolyHelixCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyHelixCtx(*args, **kwargs)
@commandWrap
def getRenderTasks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getRenderTasks(*args, **kwargs)
@commandWrap
def twoPointArcCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.twoPointArcCtx(*args, **kwargs)
@commandWrap
def MakePondBoats(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakePondBoats(*args, **kwargs)
@commandWrap
def skinCluster(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.skinCluster(*args, **kwargs)
@commandWrap
def EditFluidResolutionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EditFluidResolutionOptions(*args, **kwargs)
@commandWrap
def LayoutUVAlong(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LayoutUVAlong(*args, **kwargs)
@commandWrap
def surfaceSampler(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.surfaceSampler(*args, **kwargs)
@commandWrap
def PolygonBooleanDifferenceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonBooleanDifferenceOptions(*args, **kwargs)
@commandWrap
def bakeSimulation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bakeSimulation(*args, **kwargs)
@commandWrap
def ModifyPaintValueRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyPaintValueRelease(*args, **kwargs)
@commandWrap
def dynControl(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynControl(*args, **kwargs)
@commandWrap
def nexMultiCutCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexMultiCutCtx(*args, **kwargs)
@commandWrap
def date(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.date(*args, **kwargs)
@commandWrap
def ViewAlongAxisY(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewAlongAxisY(*args, **kwargs)
@commandWrap
def TimeEditorCreatePoseClipOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreatePoseClipOptions(*args, **kwargs)
@commandWrap
def repeatLast(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.repeatLast(*args, **kwargs)
@commandWrap
def displacementToPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displacementToPoly(*args, **kwargs)
@commandWrap
def SelectToolOptionsMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectToolOptionsMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def NodeEditorPaste(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPaste(*args, **kwargs)
@commandWrap
def goal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.goal(*args, **kwargs)
@commandWrap
def ConvertSelectionToUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToUVs(*args, **kwargs)
@commandWrap
def SingleViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SingleViewArrangement(*args, **kwargs)
@commandWrap
def FreezeTransformationsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FreezeTransformationsOptions(*args, **kwargs)
@commandWrap
def ToggleGrid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleGrid(*args, **kwargs)
@commandWrap
def AssumePreferredAngleOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssumePreferredAngleOptions(*args, **kwargs)
@commandWrap
def squareSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.squareSurface(*args, **kwargs)
@commandWrap
def texSelectShortestPathCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texSelectShortestPathCtx(*args, **kwargs)
@commandWrap
def FBXImportUpAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportUpAxis(*args, **kwargs)
@commandWrap
def AlignCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlignCurve(*args, **kwargs)
@commandWrap
def HypershadeShowDirectoriesAndFiles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShowDirectoriesAndFiles(*args, **kwargs)
@commandWrap
def PickWalkRight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkRight(*args, **kwargs)
@commandWrap
def CreateCameraOnlyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCameraOnlyOptions(*args, **kwargs)
@commandWrap
def HypershadeUnpinSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeUnpinSelected(*args, **kwargs)
@commandWrap
def subdMapSewMove(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdMapSewMove(*args, **kwargs)
@commandWrap
def ToggleUnsharedUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUnsharedUVs(*args, **kwargs)
@commandWrap
def xgmSplineQuery(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplineQuery(*args, **kwargs)
@commandWrap
def HideMarkers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideMarkers(*args, **kwargs)
@commandWrap
def AppendToPolygonToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AppendToPolygonToolOptions(*args, **kwargs)
@commandWrap
def crashInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.crashInfo(*args, **kwargs)
@commandWrap
def EnableConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableConstraints(*args, **kwargs)
@commandWrap
def greasePencilCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.greasePencilCtx(*args, **kwargs)
@commandWrap
def dR_softSelDistanceTypeGlobal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_softSelDistanceTypeGlobal(*args, **kwargs)
@commandWrap
def dynamicConstraintRemove(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynamicConstraintRemove(*args, **kwargs)
@commandWrap
def HypershadeCreateAsset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCreateAsset(*args, **kwargs)
@commandWrap
def HypershadeSelectCamerasAndImagePlanes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectCamerasAndImagePlanes(*args, **kwargs)
@commandWrap
def CutUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutUVs(*args, **kwargs)
@commandWrap
def AimConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AimConstraint(*args, **kwargs)
@commandWrap
def DeleteAllConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllConstraints(*args, **kwargs)
@commandWrap
def igBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.igBrushContext(*args, **kwargs)
@commandWrap
def RandomizeShells(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RandomizeShells(*args, **kwargs)
@commandWrap
def PublishChildAnchorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishChildAnchorOptions(*args, **kwargs)
@commandWrap
def poleVectorConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.poleVectorConstraint(*args, **kwargs)
@commandWrap
def ShowStrokes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowStrokes(*args, **kwargs)
@commandWrap
def ArtPaintSelectTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintSelectTool(*args, **kwargs)
@commandWrap
def DeleteExpressions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteExpressions(*args, **kwargs)
@commandWrap
def projectCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.projectCurve(*args, **kwargs)
@commandWrap
def polyClean(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyClean(*args, **kwargs)
@commandWrap
def arrayMapper(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.arrayMapper(*args, **kwargs)
@commandWrap
def CreateTextureDeformerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateTextureDeformerOptions(*args, **kwargs)
@commandWrap
def group(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.group(*args, **kwargs)
@commandWrap
def dR_snapToBackfacesTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_snapToBackfacesTGL(*args, **kwargs)
@commandWrap
def ToggleVertMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleVertMetadata(*args, **kwargs)
@commandWrap
def melOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.melOptions(*args, **kwargs)
@commandWrap
def ConnectToTime(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConnectToTime(*args, **kwargs)
@commandWrap
def MakeCollideOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeCollideOptions(*args, **kwargs)
@commandWrap
def DynamicRelationshipEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DynamicRelationshipEditor(*args, **kwargs)
@commandWrap
def ExtrudeVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtrudeVertex(*args, **kwargs)
@commandWrap
def createPolyTorusCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyTorusCtx(*args, **kwargs)
@commandWrap
def MatchUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MatchUVs(*args, **kwargs)
@commandWrap
def AnimationSweepOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AnimationSweepOptions(*args, **kwargs)
@commandWrap
def ExportAnimOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportAnimOptions(*args, **kwargs)
@commandWrap
def AutobindContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AutobindContainerOptions(*args, **kwargs)
@commandWrap
def UpdateBindingSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UpdateBindingSet(*args, **kwargs)
@commandWrap
def SelectPreviousObjectsMudbox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectPreviousObjectsMudbox(*args, **kwargs)
@commandWrap
def nucleusDisplayNComponentNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusDisplayNComponentNodes(*args, **kwargs)
@commandWrap
def FBXExportLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportLights(*args, **kwargs)
@commandWrap
def particleFill(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.particleFill(*args, **kwargs)
@commandWrap
def LastActionTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LastActionTool(*args, **kwargs)
@commandWrap
def AddOceanDynamicLocatorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddOceanDynamicLocatorOptions(*args, **kwargs)
@commandWrap
def playbackOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.playbackOptions(*args, **kwargs)
@commandWrap
def instance(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.instance(*args, **kwargs)
@commandWrap
def SetKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKey(*args, **kwargs)
@commandWrap
def xgmPrimSelectionContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPrimSelectionContext(*args, **kwargs)
@commandWrap
def nClothReplaceCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothReplaceCache(*args, **kwargs)
@commandWrap
def setKeyframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setKeyframe(*args, **kwargs)
@commandWrap
def nop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nop(*args, **kwargs)
@commandWrap
def TogglePolyDisplayHardEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyDisplayHardEdges(*args, **kwargs)
@commandWrap
def DeleteUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteUVs(*args, **kwargs)
@commandWrap
def GraphEditorAlwaysDisplayTangents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorAlwaysDisplayTangents(*args, **kwargs)
@commandWrap
def MakePaintable(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakePaintable(*args, **kwargs)
@commandWrap
def CreateClipOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateClipOptions(*args, **kwargs)
@commandWrap
def AddWrapInfluence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddWrapInfluence(*args, **kwargs)
@commandWrap
def flushIdleQueue(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.flushIdleQueue(*args, **kwargs)
@commandWrap
def OffsetCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetCurve(*args, **kwargs)
@commandWrap
def ilrBatchRenderCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrBatchRenderCmd(*args, **kwargs)
@commandWrap
def AppendToHairCacheOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AppendToHairCacheOptions(*args, **kwargs)
@commandWrap
def animView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.animView(*args, **kwargs)
@commandWrap
def attachNclothCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attachNclothCache(*args, **kwargs)
@commandWrap
def attrCompatibility(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attrCompatibility(*args, **kwargs)
@commandWrap
def ToggleIKSolvers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleIKSolvers(*args, **kwargs)
@commandWrap
def HideSelectedObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideSelectedObjects(*args, **kwargs)
@commandWrap
def NodeEditorCreateDoWhileCompound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCreateDoWhileCompound(*args, **kwargs)
@commandWrap
def dimWhen(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dimWhen(*args, **kwargs)
@commandWrap
def shadingNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shadingNode(*args, **kwargs)
@commandWrap
def viewSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.viewSet(*args, **kwargs)
@commandWrap
def TimeEditorSetZeroKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorSetZeroKey(*args, **kwargs)
@commandWrap
def SelectSharedColorInstances(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectSharedColorInstances(*args, **kwargs)
@commandWrap
def cacheFileCombine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cacheFileCombine(*args, **kwargs)
@commandWrap
def CreateEmitterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateEmitterOptions(*args, **kwargs)
@commandWrap
def CreateContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateContainer(*args, **kwargs)
@commandWrap
def PolygonCopy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonCopy(*args, **kwargs)
@commandWrap
def lsThroughFilter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lsThroughFilter(*args, **kwargs)
@commandWrap
def ActivateGlobalScreenSliderModeMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ActivateGlobalScreenSliderModeMarkingMenu(*args, **kwargs)
@commandWrap
def SetWorkingFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetWorkingFrame(*args, **kwargs)
@commandWrap
def mayaPreviewRenderIntoNewWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mayaPreviewRenderIntoNewWindow(*args, **kwargs)
@commandWrap
def DeleteCurrentWorkspace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteCurrentWorkspace(*args, **kwargs)
@commandWrap
def FBXImportOCMerge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportOCMerge(*args, **kwargs)
@commandWrap
def PaintVertexColorTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintVertexColorTool(*args, **kwargs)
@commandWrap
def scaleConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scaleConstraint(*args, **kwargs)
@commandWrap
def RenameCurrentUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenameCurrentUVSet(*args, **kwargs)
@commandWrap
def replaceCacheFramesOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.replaceCacheFramesOpt(*args, **kwargs)
@commandWrap
def CopyFlexor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyFlexor(*args, **kwargs)
@commandWrap
def LockCurveLength(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LockCurveLength(*args, **kwargs)
@commandWrap
def AddBifrostAdaptiveMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostAdaptiveMesh(*args, **kwargs)
@commandWrap
def SetDrivenKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetDrivenKey(*args, **kwargs)
@commandWrap
def polyQueryBlindData(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyQueryBlindData(*args, **kwargs)
@commandWrap
def xgmFreezeBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmFreezeBrushToolCmd(*args, **kwargs)
@commandWrap
def bindSkin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bindSkin(*args, **kwargs)
@commandWrap
def container(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.container(*args, **kwargs)
@commandWrap
def SubdividePolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdividePolygon(*args, **kwargs)
@commandWrap
def dopeSheetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dopeSheetEditor(*args, **kwargs)
@commandWrap
def QuickRigEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.QuickRigEditor(*args, **kwargs)
@commandWrap
def itemFilter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.itemFilter(*args, **kwargs)
@commandWrap
def polyShortestPathCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyShortestPathCtx(*args, **kwargs)
@commandWrap
def PolygonBooleanUnionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonBooleanUnionOptions(*args, **kwargs)
@commandWrap
def TestTexture(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TestTexture(*args, **kwargs)
@commandWrap
def colorAtPoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.colorAtPoint(*args, **kwargs)
@commandWrap
def freezeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.freezeOptions(*args, **kwargs)
@commandWrap
def polyCutCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCutCtx(*args, **kwargs)
@commandWrap
def superCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.superCtx(*args, **kwargs)
@commandWrap
def xgmInterpSetup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmInterpSetup(*args, **kwargs)
@commandWrap
def DeleteUVsWithoutHotkey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteUVsWithoutHotkey(*args, **kwargs)
@commandWrap
def deleteGeometryCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deleteGeometryCache(*args, **kwargs)
@commandWrap
def PolyMergeEdgesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyMergeEdgesOptions(*args, **kwargs)
@commandWrap
def CreateJiggleOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateJiggleOptions(*args, **kwargs)
@commandWrap
def SetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetEditor(*args, **kwargs)
@commandWrap
def polyAppendVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyAppendVertex(*args, **kwargs)
@commandWrap
def ShowTexturePlacements(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowTexturePlacements(*args, **kwargs)
@commandWrap
def hikGetNodeCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikGetNodeCount(*args, **kwargs)
@commandWrap
def NodeEditorPublishCompound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPublishCompound(*args, **kwargs)
@commandWrap
def GoToWorkingFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoToWorkingFrame(*args, **kwargs)
@commandWrap
def InsertEdgeLoopToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertEdgeLoopToolOptions(*args, **kwargs)
@commandWrap
def KeyBlendShapeTargetsWeight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.KeyBlendShapeTargetsWeight(*args, **kwargs)
@commandWrap
def CreateUVsBasedOnCamera(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateUVsBasedOnCamera(*args, **kwargs)
@commandWrap
def fluidVoxelInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidVoxelInfo(*args, **kwargs)
@commandWrap
def SmoothHairCurvesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothHairCurvesOptions(*args, **kwargs)
@commandWrap
def NewtonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NewtonOptions(*args, **kwargs)
@commandWrap
def lsUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lsUI(*args, **kwargs)
@commandWrap
def xgmSetGuideCVCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSetGuideCVCount(*args, **kwargs)
@commandWrap
def NodeEditorCloseAllTabs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCloseAllTabs(*args, **kwargs)
@commandWrap
def FBXProperty(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXProperty(*args, **kwargs)
@commandWrap
def ShowClusters(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowClusters(*args, **kwargs)
@commandWrap
def NodeEditorConnectionStyleCorner(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorConnectionStyleCorner(*args, **kwargs)
@commandWrap
def ParentOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParentOptions(*args, **kwargs)
@commandWrap
def AssetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssetEditor(*args, **kwargs)
@commandWrap
def characterMap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.characterMap(*args, **kwargs)
@commandWrap
def PaintOperationMarkingMenuPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintOperationMarkingMenuPress(*args, **kwargs)
@commandWrap
def dR_edgedFacesTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_edgedFacesTGL(*args, **kwargs)
@commandWrap
def alignSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.alignSurface(*args, **kwargs)
@commandWrap
def BreakShadowLinks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BreakShadowLinks(*args, **kwargs)
@commandWrap
def HypershadeRenameTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRenameTab(*args, **kwargs)
@commandWrap
def ilrCreateSharedUVCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrCreateSharedUVCmd(*args, **kwargs)
@commandWrap
def CreateSculptDeformerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSculptDeformerOptions(*args, **kwargs)
@commandWrap
def TumbleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TumbleTool(*args, **kwargs)
@commandWrap
def RigidBodySolver(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RigidBodySolver(*args, **kwargs)
@commandWrap
def FrameAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FrameAll(*args, **kwargs)
@commandWrap
def buildFurFiles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.buildFurFiles(*args, **kwargs)
@commandWrap
def psdExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.psdExport(*args, **kwargs)
@commandWrap
def evaluationManager(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.evaluationManager(*args, **kwargs)
@commandWrap
def DuplicateFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateFace(*args, **kwargs)
@commandWrap
def sbs_GetWorkflow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetWorkflow(*args, **kwargs)
@commandWrap
def artSetPaintCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artSetPaintCtx(*args, **kwargs)
@commandWrap
def igConvertToLogical(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.igConvertToLogical(*args, **kwargs)
@commandWrap
def PublishConnectionsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishConnectionsOptions(*args, **kwargs)
@commandWrap
def PolygonBooleanIntersectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonBooleanIntersectionOptions(*args, **kwargs)
@commandWrap
def cacheFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cacheFile(*args, **kwargs)
@commandWrap
def LookAtSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LookAtSelection(*args, **kwargs)
@commandWrap
def setKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setKeyCtx(*args, **kwargs)
@commandWrap
def InTangentLinear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InTangentLinear(*args, **kwargs)
@commandWrap
def editMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.editMetadata(*args, **kwargs)
@commandWrap
def NodeEditorToggleZoomIn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleZoomIn(*args, **kwargs)
@commandWrap
def FBXExportIncludeChildren(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportIncludeChildren(*args, **kwargs)
@commandWrap
def SetVertexNormal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetVertexNormal(*args, **kwargs)
@commandWrap
def ShowMeshCloneTargetToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshCloneTargetToolOptions(*args, **kwargs)
@commandWrap
def polySplitCtx2(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySplitCtx2(*args, **kwargs)
@commandWrap
def IntersectSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IntersectSurfaces(*args, **kwargs)
@commandWrap
def ShowCameraManipulators(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowCameraManipulators(*args, **kwargs)
@commandWrap
def sbs_SetBakeFormat(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_SetBakeFormat(*args, **kwargs)
@commandWrap
def GpuCacheExportAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GpuCacheExportAll(*args, **kwargs)
@commandWrap
def InTangentAuto(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InTangentAuto(*args, **kwargs)
@commandWrap
def dR_convertSelectionToEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_convertSelectionToEdge(*args, **kwargs)
@commandWrap
def LoopBrushAnimation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LoopBrushAnimation(*args, **kwargs)
@commandWrap
def ToggleRotationPivots(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleRotationPivots(*args, **kwargs)
@commandWrap
def MoveRight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveRight(*args, **kwargs)
@commandWrap
def MirrorPolygonGeometryOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorPolygonGeometryOptions(*args, **kwargs)
@commandWrap
def UVNormalBasedProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVNormalBasedProjection(*args, **kwargs)
@commandWrap
def UntemplateObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UntemplateObject(*args, **kwargs)
@commandWrap
def CreateWrapOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateWrapOptions(*args, **kwargs)
@commandWrap
def GraphEditorFrameAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorFrameAll(*args, **kwargs)
@commandWrap
def filter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.filter(*args, **kwargs)
@commandWrap
def ShowSmoothSkinInfluences(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowSmoothSkinInfluences(*args, **kwargs)
@commandWrap
def SelectUVShell(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVShell(*args, **kwargs)
@commandWrap
def hikBodyPart(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikBodyPart(*args, **kwargs)
@commandWrap
def ParticleFillOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParticleFillOptions(*args, **kwargs)
@commandWrap
def ResetWeightsToDefault(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetWeightsToDefault(*args, **kwargs)
@commandWrap
def UVPlanarProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVPlanarProjection(*args, **kwargs)
@commandWrap
def furPointOnMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.furPointOnMesh(*args, **kwargs)
@commandWrap
def SelectAllPolygonGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllPolygonGeometry(*args, **kwargs)
@commandWrap
def dR_showOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_showOptions(*args, **kwargs)
@commandWrap
def xgmSelectBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSelectBrushToolCmd(*args, **kwargs)
@commandWrap
def FrontPerspViewLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FrontPerspViewLayout(*args, **kwargs)
@commandWrap
def TogglePaintOnPaintableObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePaintOnPaintableObjects(*args, **kwargs)
@commandWrap
def SetMeshBulgeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshBulgeTool(*args, **kwargs)
@commandWrap
def ToggleTextureBorderEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleTextureBorderEdges(*args, **kwargs)
@commandWrap
def ShowNonlinears(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowNonlinears(*args, **kwargs)
@commandWrap
def SelectToolMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectToolMarkingMenu(*args, **kwargs)
@commandWrap
def ToggleSelectionHandles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSelectionHandles(*args, **kwargs)
@commandWrap
def ShowMeshBulgeToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshBulgeToolOptions(*args, **kwargs)
@commandWrap
def mouldSrf(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mouldSrf(*args, **kwargs)
@commandWrap
def ApplySettingsToSelectedStroke(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ApplySettingsToSelectedStroke(*args, **kwargs)
@commandWrap
def MatchTransform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MatchTransform(*args, **kwargs)
@commandWrap
def DeleteRigidBodies(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteRigidBodies(*args, **kwargs)
@commandWrap
def FlipUVsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FlipUVsOptions(*args, **kwargs)
@commandWrap
def polyColorSetCmdWrapper(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyColorSetCmdWrapper(*args, **kwargs)
@commandWrap
def ToggleTimeSlider(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleTimeSlider(*args, **kwargs)
@commandWrap
def RemoveBifrostFoamMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostFoamMask(*args, **kwargs)
@commandWrap
def PrelightPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PrelightPolygon(*args, **kwargs)
@commandWrap
def TransplantHairOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransplantHairOptions(*args, **kwargs)
@commandWrap
def lightlink(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lightlink(*args, **kwargs)
@commandWrap
def getRenderDependencies(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getRenderDependencies(*args, **kwargs)
@commandWrap
def StitchTogether(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StitchTogether(*args, **kwargs)
@commandWrap
def psdChannelOutliner(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.psdChannelOutliner(*args, **kwargs)
@commandWrap
def polyDisc(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyDisc(*args, **kwargs)
@commandWrap
def selectionConnection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectionConnection(*args, **kwargs)
@commandWrap
def geometryMergeCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryMergeCacheOpt(*args, **kwargs)
@commandWrap
def CreateConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateConstraint(*args, **kwargs)
@commandWrap
def NodeEditorShowAllCustomAttrs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorShowAllCustomAttrs(*args, **kwargs)
@commandWrap
def HypershadeCreateTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCreateTab(*args, **kwargs)
@commandWrap
def PublishRootTransform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishRootTransform(*args, **kwargs)
@commandWrap
def TimeEditorToggleTimeCursorPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorToggleTimeCursorPress(*args, **kwargs)
@commandWrap
def reloadImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reloadImage(*args, **kwargs)
@commandWrap
def polyMergeUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMergeUV(*args, **kwargs)
@commandWrap
def SplitMeshWithProjectedCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitMeshWithProjectedCurve(*args, **kwargs)
@commandWrap
def OutTangentFlat(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutTangentFlat(*args, **kwargs)
@commandWrap
def FBXGetTakeName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXGetTakeName(*args, **kwargs)
@commandWrap
def softModCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.softModCtx(*args, **kwargs)
@commandWrap
def viewLookAt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.viewLookAt(*args, **kwargs)
@commandWrap
def fluidReplaceFrames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidReplaceFrames(*args, **kwargs)
@commandWrap
def parentConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.parentConstraint(*args, **kwargs)
@commandWrap
def AirOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AirOptions(*args, **kwargs)
@commandWrap
def curveMoveEPCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveMoveEPCtx(*args, **kwargs)
@commandWrap
def SaveSceneAs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveSceneAs(*args, **kwargs)
@commandWrap
def ToggleViewportRenderer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleViewportRenderer(*args, **kwargs)
@commandWrap
def dR_selectPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectPress(*args, **kwargs)
@commandWrap
def NodeEditorGridToggleSnap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGridToggleSnap(*args, **kwargs)
@commandWrap
def NURBSSmoothnessRough(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessRough(*args, **kwargs)
@commandWrap
def illustratorCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.illustratorCurves(*args, **kwargs)
@commandWrap
def CreateCameraAimUpOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCameraAimUpOptions(*args, **kwargs)
@commandWrap
def Turbulence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Turbulence(*args, **kwargs)
@commandWrap
def polyVertexNormalCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyVertexNormalCtx(*args, **kwargs)
@commandWrap
def HypershadeToggleTransformDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleTransformDisplay(*args, **kwargs)
@commandWrap
def SendAsNewScene3dsMax(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendAsNewScene3dsMax(*args, **kwargs)
@commandWrap
def NParticleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NParticleTool(*args, **kwargs)
@commandWrap
def track(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.track(*args, **kwargs)
@commandWrap
def FBXImportSkeletonDefinitionsAs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportSkeletonDefinitionsAs(*args, **kwargs)
@commandWrap
def FloatSelectedPondObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FloatSelectedPondObjects(*args, **kwargs)
@commandWrap
def RemoveBifrostFoam(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostFoam(*args, **kwargs)
@commandWrap
def geometryCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryCacheOpt(*args, **kwargs)
@commandWrap
def SetCutSewUVTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetCutSewUVTool(*args, **kwargs)
@commandWrap
def FBXExportConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportConstraints(*args, **kwargs)
@commandWrap
def polyCheck(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCheck(*args, **kwargs)
@commandWrap
def SubstituteGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubstituteGeometry(*args, **kwargs)
@commandWrap
def AlignCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlignCurveOptions(*args, **kwargs)
@commandWrap
def evaluator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.evaluator(*args, **kwargs)
@commandWrap
def ShowLightManipulators(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowLightManipulators(*args, **kwargs)
@commandWrap
def artSelectCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artSelectCtx(*args, **kwargs)
@commandWrap
def FBXImportSetTake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportSetTake(*args, **kwargs)
@commandWrap
def HypershadeGridToggleVisibility(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGridToggleVisibility(*args, **kwargs)
@commandWrap
def PolyConvertToRingAndSplit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyConvertToRingAndSplit(*args, **kwargs)
@commandWrap
def ThreePointArcToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ThreePointArcToolOptions(*args, **kwargs)
@commandWrap
def FBXExportColladaTriangulate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportColladaTriangulate(*args, **kwargs)
@commandWrap
def WireDropoffLocatorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WireDropoffLocatorOptions(*args, **kwargs)
@commandWrap
def HypershadeConvertToFileTexture(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeConvertToFileTexture(*args, **kwargs)
@commandWrap
def PublishParentAnchor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishParentAnchor(*args, **kwargs)
@commandWrap
def BrushPresetBlend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetBlend(*args, **kwargs)
@commandWrap
def PolyCircularizeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyCircularizeOptions(*args, **kwargs)
@commandWrap
def PencilCurveToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PencilCurveToolOptions(*args, **kwargs)
@commandWrap
def FBXImportConvertUnitString(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportConvertUnitString(*args, **kwargs)
@commandWrap
def CreateFluidCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateFluidCache(*args, **kwargs)
@commandWrap
def stitchSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stitchSurface(*args, **kwargs)
@commandWrap
def surface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.surface(*args, **kwargs)
@commandWrap
def polyInstallAction(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyInstallAction(*args, **kwargs)
@commandWrap
def PolygonPasteOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonPasteOptions(*args, **kwargs)
@commandWrap
def SendToUnrealSetProject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendToUnrealSetProject(*args, **kwargs)
@commandWrap
def nonLinear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nonLinear(*args, **kwargs)
@commandWrap
def shot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shot(*args, **kwargs)
@commandWrap
def displaySurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displaySurface(*args, **kwargs)
@commandWrap
def SetMeshFoamyTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshFoamyTool(*args, **kwargs)
@commandWrap
def IncreaseManipulatorSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncreaseManipulatorSize(*args, **kwargs)
@commandWrap
def SymmetrizeUVBrushSizeOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SymmetrizeUVBrushSizeOn(*args, **kwargs)
@commandWrap
def XgmSetCutBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetCutBrushToolOption(*args, **kwargs)
@commandWrap
def HIKInitAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKInitAxis(*args, **kwargs)
@commandWrap
def CreateSpotLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSpotLight(*args, **kwargs)
@commandWrap
def ExportSkinWeightMaps(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportSkinWeightMaps(*args, **kwargs)
@commandWrap
def resampleFluid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.resampleFluid(*args, **kwargs)
@commandWrap
def polyCut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCut(*args, **kwargs)
@commandWrap
def nucleusDisplayTransformNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusDisplayTransformNodes(*args, **kwargs)
@commandWrap
def OneClickAcknowledgeCallback(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickAcknowledgeCallback(*args, **kwargs)
@commandWrap
def ikHandle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikHandle(*args, **kwargs)
@commandWrap
def HideClusters(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideClusters(*args, **kwargs)
@commandWrap
def dR_viewBottom(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewBottom(*args, **kwargs)
@commandWrap
def GeometryConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GeometryConstraint(*args, **kwargs)
@commandWrap
def PublishAttributesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishAttributesOptions(*args, **kwargs)
@commandWrap
def ExtendCurveOnSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendCurveOnSurface(*args, **kwargs)
@commandWrap
def createPolyPlatonicSolidCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyPlatonicSolidCtx(*args, **kwargs)
@commandWrap
def xgmModifierGuideOp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmModifierGuideOp(*args, **kwargs)
@commandWrap
def CreateSculptDeformer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSculptDeformer(*args, **kwargs)
@commandWrap
def CameraModeToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CameraModeToggle(*args, **kwargs)
@commandWrap
def CurveFillet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveFillet(*args, **kwargs)
@commandWrap
def DecreaseGammaFine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DecreaseGammaFine(*args, **kwargs)
@commandWrap
def myTestCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.myTestCmd(*args, **kwargs)
@commandWrap
def dR_tweakPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_tweakPress(*args, **kwargs)
@commandWrap
def SetBreakdownKeyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetBreakdownKeyOptions(*args, **kwargs)
@commandWrap
def TimeEditorExportSelectionOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorExportSelectionOpt(*args, **kwargs)
@commandWrap
def namespaceInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.namespaceInfo(*args, **kwargs)
@commandWrap
def ToggleWireframeInArtisan(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleWireframeInArtisan(*args, **kwargs)
@commandWrap
def SelectComponentToolMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectComponentToolMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def CreatePointLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePointLight(*args, **kwargs)
@commandWrap
def OneClickFetchRemoteCharacter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickFetchRemoteCharacter(*args, **kwargs)
@commandWrap
def CurlCurvesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurlCurvesOptions(*args, **kwargs)
@commandWrap
def CreateCameraAim(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCameraAim(*args, **kwargs)
@commandWrap
def BlindDataEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BlindDataEditor(*args, **kwargs)
@commandWrap
def sbs_GetEditionModeScale(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetEditionModeScale(*args, **kwargs)
@commandWrap
def OffsetSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetSurfacesOptions(*args, **kwargs)
@commandWrap
def resourceManager(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.resourceManager(*args, **kwargs)
@commandWrap
def artSetPaint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artSetPaint(*args, **kwargs)
@commandWrap
def dR_multiCutPointCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_multiCutPointCmd(*args, **kwargs)
@commandWrap
def SelectAllNURBSSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllNURBSSurfaces(*args, **kwargs)
@commandWrap
def CreatePolygonDisc(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonDisc(*args, **kwargs)
@commandWrap
def PanZoomTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PanZoomTool(*args, **kwargs)
@commandWrap
def ToggleMeshMaps(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMeshMaps(*args, **kwargs)
@commandWrap
def ToggleRangeSlider(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleRangeSlider(*args, **kwargs)
@commandWrap
def HypershadeAdditiveGraphingMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeAdditiveGraphingMode(*args, **kwargs)
@commandWrap
def polySphere(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySphere(*args, **kwargs)
@commandWrap
def PaintEffectsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsTool(*args, **kwargs)
@commandWrap
def polyCircularize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCircularize(*args, **kwargs)
@commandWrap
def DollyTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DollyTool(*args, **kwargs)
@commandWrap
def CreateNURBSPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSPlane(*args, **kwargs)
@commandWrap
def CreateParticleDiskCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateParticleDiskCache(*args, **kwargs)
@commandWrap
def ShowBaseWire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowBaseWire(*args, **kwargs)
@commandWrap
def xgmBakeGuideToUVSpace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmBakeGuideToUVSpace(*args, **kwargs)
@commandWrap
def polyCircularizeFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCircularizeFace(*args, **kwargs)
@commandWrap
def pointPosition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointPosition(*args, **kwargs)
@commandWrap
def flushThumbnailCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.flushThumbnailCache(*args, **kwargs)
@commandWrap
def MakeFluidCollideOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeFluidCollideOptions(*args, **kwargs)
@commandWrap
def fontAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fontAttributes(*args, **kwargs)
@commandWrap
def GraphSnapOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphSnapOptions(*args, **kwargs)
@commandWrap
def EnableFluids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableFluids(*args, **kwargs)
@commandWrap
def polyBevel3(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyBevel3(*args, **kwargs)
@commandWrap
def OneClickGetContactingAppName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickGetContactingAppName(*args, **kwargs)
@commandWrap
def dagPose(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dagPose(*args, **kwargs)
@commandWrap
def ScaleUVTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleUVTool(*args, **kwargs)
@commandWrap
def circle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.circle(*args, **kwargs)
@commandWrap
def assembly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.assembly(*args, **kwargs)
@commandWrap
def FBXImportSkins(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportSkins(*args, **kwargs)
@commandWrap
def createAttrPatterns(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createAttrPatterns(*args, **kwargs)
@commandWrap
def BakeDeformerTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeDeformerTool(*args, **kwargs)
@commandWrap
def SaveFluidStateAs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveFluidStateAs(*args, **kwargs)
@commandWrap
def FineLevelComponentDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FineLevelComponentDisplay(*args, **kwargs)
@commandWrap
def polyMoveFacetUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMoveFacetUV(*args, **kwargs)
@commandWrap
def FBXImportForcedFileAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportForcedFileAxis(*args, **kwargs)
@commandWrap
def SelectAllRigidBodies(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllRigidBodies(*args, **kwargs)
@commandWrap
def ExtractFaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtractFaceOptions(*args, **kwargs)
@commandWrap
def SelectAllMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def TangentsSpline(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsSpline(*args, **kwargs)
@commandWrap
def xgmExportToP3D(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmExportToP3D(*args, **kwargs)
@commandWrap
def OffsetEdgeLoopTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetEdgeLoopTool(*args, **kwargs)
@commandWrap
def HypershadeRemoveTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRemoveTab(*args, **kwargs)
@commandWrap
def PruneSculpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PruneSculpt(*args, **kwargs)
@commandWrap
def BendCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BendCurves(*args, **kwargs)
@commandWrap
def CreatePolygonSphere(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSphere(*args, **kwargs)
@commandWrap
def agFormatOut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.agFormatOut(*args, **kwargs)
@commandWrap
def PolyMergeVerticesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyMergeVerticesOptions(*args, **kwargs)
@commandWrap
def SubdivProxy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivProxy(*args, **kwargs)
@commandWrap
def transformLimits(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.transformLimits(*args, **kwargs)
@commandWrap
def SetMeshWaxTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshWaxTool(*args, **kwargs)
@commandWrap
def PolyEditEdgeFlowOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyEditEdgeFlowOptions(*args, **kwargs)
@commandWrap
def viewFit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.viewFit(*args, **kwargs)
@commandWrap
def AddInBetweenTargetShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddInBetweenTargetShape(*args, **kwargs)
@commandWrap
def MirrorCutPolygonGeometryOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorCutPolygonGeometryOptions(*args, **kwargs)
@commandWrap
def ShowAllComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowAllComponents(*args, **kwargs)
@commandWrap
def pasteKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pasteKey(*args, **kwargs)
@commandWrap
def TrackTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TrackTool(*args, **kwargs)
@commandWrap
def ClusterCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClusterCurve(*args, **kwargs)
@commandWrap
def FBXExportShowUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportShowUI(*args, **kwargs)
@commandWrap
def RenderPassSetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderPassSetEditor(*args, **kwargs)
@commandWrap
def HypershadeSelectTextures(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectTextures(*args, **kwargs)
@commandWrap
def PointConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PointConstraintOptions(*args, **kwargs)
@commandWrap
def AlignSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlignSurfaces(*args, **kwargs)
@commandWrap
def CreateDiskCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateDiskCache(*args, **kwargs)
@commandWrap
def SetMeshRelaxTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshRelaxTool(*args, **kwargs)
@commandWrap
def HideFollicles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideFollicles(*args, **kwargs)
@commandWrap
def ArtPaintAttrToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintAttrToolOptions(*args, **kwargs)
@commandWrap
def mtkShrinkWrap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mtkShrinkWrap(*args, **kwargs)
@commandWrap
def CreatePoseOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePoseOptions(*args, **kwargs)
@commandWrap
def sequenceManager(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sequenceManager(*args, **kwargs)
@commandWrap
def ChamferVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ChamferVertex(*args, **kwargs)
@commandWrap
def DeactivateGlobalScreenSliderModeMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeactivateGlobalScreenSliderModeMarkingMenu(*args, **kwargs)
@commandWrap
def renderGlobalsNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderGlobalsNode(*args, **kwargs)
@commandWrap
def psdConvSolidTxOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.psdConvSolidTxOptions(*args, **kwargs)
@commandWrap
def objectTypeUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.objectTypeUI(*args, **kwargs)
@commandWrap
def BreakTangents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BreakTangents(*args, **kwargs)
@commandWrap
def PanePop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PanePop(*args, **kwargs)
@commandWrap
def NodeEditorShapeMenuStateNoShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorShapeMenuStateNoShapes(*args, **kwargs)
@commandWrap
def ModifyUpperRadiusPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyUpperRadiusPress(*args, **kwargs)
@commandWrap
def sbs_GetEnumCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetEnumCount(*args, **kwargs)
@commandWrap
def parent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.parent(*args, **kwargs)
@commandWrap
def dgfilter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgfilter(*args, **kwargs)
@commandWrap
def ToggleHoleFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleHoleFaces(*args, **kwargs)
@commandWrap
def PickWalkDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkDown(*args, **kwargs)
@commandWrap
def AveragePolygonNormalsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AveragePolygonNormalsOptions(*args, **kwargs)
@commandWrap
def CreateVolumeSphere(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateVolumeSphere(*args, **kwargs)
@commandWrap
def PolyConvertToRingAndCollapse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyConvertToRingAndCollapse(*args, **kwargs)
@commandWrap
def nClothMergeCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothMergeCacheOpt(*args, **kwargs)
@commandWrap
def paramDimContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.paramDimContext(*args, **kwargs)
@commandWrap
def polyHelix(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyHelix(*args, **kwargs)
@commandWrap
def xgmSculptLayerInit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSculptLayerInit(*args, **kwargs)
@commandWrap
def ExtrudeEdgeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtrudeEdgeOptions(*args, **kwargs)
@commandWrap
def CreateAnnotateNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateAnnotateNode(*args, **kwargs)
@commandWrap
def HidePlanes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HidePlanes(*args, **kwargs)
@commandWrap
def SlideEdgeToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SlideEdgeToolOptions(*args, **kwargs)
@commandWrap
def NodeEditorSelectDownStream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorSelectDownStream(*args, **kwargs)
@commandWrap
def HypershadeToggleNodeSwatchSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleNodeSwatchSize(*args, **kwargs)
@commandWrap
def attachCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attachCurve(*args, **kwargs)
@commandWrap
def CreatePlatonicSolid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePlatonicSolid(*args, **kwargs)
@commandWrap
def fluidAppendOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidAppendOpt(*args, **kwargs)
@commandWrap
def VolumeAxisOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.VolumeAxisOptions(*args, **kwargs)
@commandWrap
def geometryExportCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryExportCacheOpt(*args, **kwargs)
@commandWrap
def displayRGBColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayRGBColor(*args, **kwargs)
@commandWrap
def keyframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframe(*args, **kwargs)
@commandWrap
def toolPropertyWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.toolPropertyWindow(*args, **kwargs)
@commandWrap
def PFXUVSetLinkingEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PFXUVSetLinkingEditor(*args, **kwargs)
@commandWrap
def expression(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.expression(*args, **kwargs)
@commandWrap
def PolyAssignSubdivHoleOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyAssignSubdivHoleOptions(*args, **kwargs)
@commandWrap
def PreloadReferenceEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreloadReferenceEditor(*args, **kwargs)
@commandWrap
def IKSplineHandleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IKSplineHandleTool(*args, **kwargs)
@commandWrap
def CurveSmoothnessMedium(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveSmoothnessMedium(*args, **kwargs)
@commandWrap
def dR_quadDrawTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_quadDrawTool(*args, **kwargs)
@commandWrap
def dgControl(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgControl(*args, **kwargs)
@commandWrap
def color(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.color(*args, **kwargs)
@commandWrap
def dR_hypergraphTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_hypergraphTGL(*args, **kwargs)
@commandWrap
def connectControl(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.connectControl(*args, **kwargs)
@commandWrap
def recordAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.recordAttr(*args, **kwargs)
@commandWrap
def HIKToggleReleasePinning(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKToggleReleasePinning(*args, **kwargs)
@commandWrap
def buildFurImages(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.buildFurImages(*args, **kwargs)
@commandWrap
def hwRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hwRender(*args, **kwargs)
@commandWrap
def DeleteAllLattices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllLattices(*args, **kwargs)
@commandWrap
def ShowMeshSmoothTargetToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshSmoothTargetToolOptions(*args, **kwargs)
@commandWrap
def GpuCacheRefreshAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GpuCacheRefreshAll(*args, **kwargs)
@commandWrap
def ProfilerToolShowSelectedRepetition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolShowSelectedRepetition(*args, **kwargs)
@commandWrap
def PaintGeomCacheToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintGeomCacheToolOptions(*args, **kwargs)
@commandWrap
def SelectPolygonToolMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectPolygonToolMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def mtkQuadDrawPoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mtkQuadDrawPoint(*args, **kwargs)
@commandWrap
def TimeEditorKeepTransitionsToggleRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorKeepTransitionsToggleRelease(*args, **kwargs)
@commandWrap
def polyRetopo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyRetopo(*args, **kwargs)
@commandWrap
def UnpinSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnpinSelection(*args, **kwargs)
@commandWrap
def FreeformFillet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FreeformFillet(*args, **kwargs)
@commandWrap
def CreateActiveRigidBodyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateActiveRigidBodyOptions(*args, **kwargs)
@commandWrap
def BevelPlusOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BevelPlusOptions(*args, **kwargs)
@commandWrap
def FBXExportSmoothingGroups(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportSmoothingGroups(*args, **kwargs)
@commandWrap
def skinPercent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.skinPercent(*args, **kwargs)
@commandWrap
def Shatter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Shatter(*args, **kwargs)
@commandWrap
def emitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.emitter(*args, **kwargs)
@commandWrap
def EnterEditModePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnterEditModePress(*args, **kwargs)
@commandWrap
def HypershadeRefreshFileListing(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRefreshFileListing(*args, **kwargs)
@commandWrap
def fileInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fileInfo(*args, **kwargs)
@commandWrap
def Create2DContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create2DContainerOptions(*args, **kwargs)
@commandWrap
def ilrTextureBakeCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrTextureBakeCmd(*args, **kwargs)
@commandWrap
def ToggleUIElements(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUIElements(*args, **kwargs)
@commandWrap
def dolly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dolly(*args, **kwargs)
@commandWrap
def pointCloudInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointCloudInfo(*args, **kwargs)
@commandWrap
def AttachSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachSurfaces(*args, **kwargs)
@commandWrap
def PaintReduceWeightsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintReduceWeightsToolOptions(*args, **kwargs)
@commandWrap
def PickWalkIn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkIn(*args, **kwargs)
@commandWrap
def dR_bevelPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_bevelPress(*args, **kwargs)
@commandWrap
def GrowPolygonSelectionRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GrowPolygonSelectionRegion(*args, **kwargs)
@commandWrap
def MakeFluidCollide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeFluidCollide(*args, **kwargs)
@commandWrap
def dR_viewGridTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewGridTGL(*args, **kwargs)
@commandWrap
def colorManagementConvert(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.colorManagementConvert(*args, **kwargs)
@commandWrap
def polySelectConstraintMonitor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySelectConstraintMonitor(*args, **kwargs)
@commandWrap
def GetToonExample(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetToonExample(*args, **kwargs)
@commandWrap
def dR_timeConfigTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_timeConfigTGL(*args, **kwargs)
@commandWrap
def OptimizeSceneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OptimizeSceneOptions(*args, **kwargs)
@commandWrap
def dR_selConstraintAngle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selConstraintAngle(*args, **kwargs)
@commandWrap
def sound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sound(*args, **kwargs)
@commandWrap
def PolyConvertToLoopAndDuplicate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyConvertToLoopAndDuplicate(*args, **kwargs)
@commandWrap
def connectionInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.connectionInfo(*args, **kwargs)
@commandWrap
def dR_movePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_movePress(*args, **kwargs)
@commandWrap
def xgmFindAttachment(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmFindAttachment(*args, **kwargs)
@commandWrap
def xgmParticleRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmParticleRender(*args, **kwargs)
@commandWrap
def CreateCreaseSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCreaseSet(*args, **kwargs)
@commandWrap
def AlembicReplace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicReplace(*args, **kwargs)
@commandWrap
def whatsNewHighlight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.whatsNewHighlight(*args, **kwargs)
@commandWrap
def TimeEditorKeepTransitionsTogglePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorKeepTransitionsTogglePress(*args, **kwargs)
@commandWrap
def dataStructure(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dataStructure(*args, **kwargs)
@commandWrap
def DeleteAllCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllCameras(*args, **kwargs)
@commandWrap
def profiler(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.profiler(*args, **kwargs)
@commandWrap
def dR_selectModeHybrid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectModeHybrid(*args, **kwargs)
@commandWrap
def HypergraphWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypergraphWindow(*args, **kwargs)
@commandWrap
def LightningOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LightningOptions(*args, **kwargs)
@commandWrap
def u3dAutoSeam(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.u3dAutoSeam(*args, **kwargs)
@commandWrap
def ShowMeshScrapeToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshScrapeToolOptions(*args, **kwargs)
@commandWrap
def HideManipulators(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideManipulators(*args, **kwargs)
@commandWrap
def SetProject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetProject(*args, **kwargs)
@commandWrap
def texLatticeDeformContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texLatticeDeformContext(*args, **kwargs)
@commandWrap
def RepeatLast(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RepeatLast(*args, **kwargs)
@commandWrap
def CreateBifrostAero(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateBifrostAero(*args, **kwargs)
@commandWrap
def HairUVSetLinkingEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HairUVSetLinkingEditor(*args, **kwargs)
@commandWrap
def assignCommand(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.assignCommand(*args, **kwargs)
@commandWrap
def FillHole(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FillHole(*args, **kwargs)
@commandWrap
def ConvertSelectionToShellBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToShellBorder(*args, **kwargs)
@commandWrap
def LayoutUVOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LayoutUVOptions(*args, **kwargs)
@commandWrap
def cluster(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cluster(*args, **kwargs)
@commandWrap
def RemoveMaterialSoloing(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveMaterialSoloing(*args, **kwargs)
@commandWrap
def CreateNURBSPlaneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSPlaneOptions(*args, **kwargs)
@commandWrap
def DetachCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachCurveOptions(*args, **kwargs)
@commandWrap
def texSculptCacheContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texSculptCacheContext(*args, **kwargs)
@commandWrap
def ChamferVertexOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ChamferVertexOptions(*args, **kwargs)
@commandWrap
def ModifyLowerRadiusRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyLowerRadiusRelease(*args, **kwargs)
@commandWrap
def RelaxUVShell(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RelaxUVShell(*args, **kwargs)
@commandWrap
def TimeDraggerToolActivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeDraggerToolActivate(*args, **kwargs)
@commandWrap
def xgmWidthBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmWidthBrushContext(*args, **kwargs)
@commandWrap
def subdivCrease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdivCrease(*args, **kwargs)
@commandWrap
def TimeEditorCreateGroupFromSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateGroupFromSelection(*args, **kwargs)
@commandWrap
def AddBifrostAccelerator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostAccelerator(*args, **kwargs)
@commandWrap
def HypershadeShowConnectedAttrs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShowConnectedAttrs(*args, **kwargs)
@commandWrap
def propMove(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.propMove(*args, **kwargs)
@commandWrap
def u3dLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.u3dLayout(*args, **kwargs)
@commandWrap
def ThreeTopSplitViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ThreeTopSplitViewArrangement(*args, **kwargs)
@commandWrap
def fluidReplaceCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidReplaceCacheOpt(*args, **kwargs)
@commandWrap
def LoopBrushAnimationOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LoopBrushAnimationOptions(*args, **kwargs)
@commandWrap
def ShowRenderingUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowRenderingUI(*args, **kwargs)
@commandWrap
def ActivateGlobalScreenSlider(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ActivateGlobalScreenSlider(*args, **kwargs)
@commandWrap
def ShowAllEditedComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowAllEditedComponents(*args, **kwargs)
@commandWrap
def HidePolygonSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HidePolygonSurfaces(*args, **kwargs)
@commandWrap
def CreateEmptyUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateEmptyUVSet(*args, **kwargs)
@commandWrap
def modelCurrentTimeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.modelCurrentTimeCtx(*args, **kwargs)
@commandWrap
def AddKeyToolDeactivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddKeyToolDeactivate(*args, **kwargs)
@commandWrap
def DetachSkeletonJoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachSkeletonJoints(*args, **kwargs)
@commandWrap
def xgmSplineApplyRenderOverride(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplineApplyRenderOverride(*args, **kwargs)
@commandWrap
def texSmoothContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texSmoothContext(*args, **kwargs)
@commandWrap
def dR_objectXrayTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_objectXrayTGL(*args, **kwargs)
@commandWrap
def TogglePolyDisplayEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyDisplayEdges(*args, **kwargs)
@commandWrap
def disconnectJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.disconnectJoint(*args, **kwargs)
@commandWrap
def DeleteExpressionsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteExpressionsOptions(*args, **kwargs)
@commandWrap
def polyClipboard(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyClipboard(*args, **kwargs)
@commandWrap
def moduleDetectionLogic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.moduleDetectionLogic(*args, **kwargs)
@commandWrap
def RenderLayerEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderLayerEditorWindow(*args, **kwargs)
@commandWrap
def QualityDisplayMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.QualityDisplayMarkingMenu(*args, **kwargs)
@commandWrap
def OffsetCurveOnSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetCurveOnSurfaceOptions(*args, **kwargs)
@commandWrap
def HideStrokeControlCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideStrokeControlCurves(*args, **kwargs)
@commandWrap
def HoldCurrentKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HoldCurrentKeys(*args, **kwargs)
@commandWrap
def nodeGrapher(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nodeGrapher(*args, **kwargs)
@commandWrap
def TwoStackedViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TwoStackedViewArrangement(*args, **kwargs)
@commandWrap
def AddPondDynamicLocatorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPondDynamicLocatorOptions(*args, **kwargs)
@commandWrap
def CustomPolygonDisplayOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CustomPolygonDisplayOptions(*args, **kwargs)
@commandWrap
def CreateWakeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateWakeOptions(*args, **kwargs)
@commandWrap
def dR_lockSelTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_lockSelTGL(*args, **kwargs)
@commandWrap
def ShowNParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowNParticles(*args, **kwargs)
@commandWrap
def Snap2PointsTo2Points(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Snap2PointsTo2Points(*args, **kwargs)
@commandWrap
def dynamicLoad(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynamicLoad(*args, **kwargs)
@commandWrap
def HideHotbox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideHotbox(*args, **kwargs)
@commandWrap
def SelectAllAssets(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllAssets(*args, **kwargs)
@commandWrap
def TranslateToolMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TranslateToolMarkingMenu(*args, **kwargs)
@commandWrap
def HypershadeDisplayAsMediumSwatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayAsMediumSwatches(*args, **kwargs)
@commandWrap
def CreateCameraAimUp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCameraAimUp(*args, **kwargs)
@commandWrap
def TimeEditorCopyClips(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCopyClips(*args, **kwargs)
@commandWrap
def drawExtrudeFacetCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.drawExtrudeFacetCtx(*args, **kwargs)
@commandWrap
def dR_rotatePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_rotatePress(*args, **kwargs)
@commandWrap
def shotRipple(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shotRipple(*args, **kwargs)
@commandWrap
def ShowBoundingBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowBoundingBox(*args, **kwargs)
@commandWrap
def timeEditorClipOffset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorClipOffset(*args, **kwargs)
@commandWrap
def SaveHIKCharacterDefinition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveHIKCharacterDefinition(*args, **kwargs)
@commandWrap
def fltSwitch(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fltSwitch(*args, **kwargs)
@commandWrap
def runTimeCommand(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.runTimeCommand(*args, **kwargs)
@commandWrap
def upAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.upAxis(*args, **kwargs)
@commandWrap
def HypershadeFrameAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeFrameAll(*args, **kwargs)
@commandWrap
def AddCombinationTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddCombinationTarget(*args, **kwargs)
@commandWrap
def XgmSplineCacheDisableSelectedCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheDisableSelectedCache(*args, **kwargs)
@commandWrap
def HIKCharacterControlsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKCharacterControlsTool(*args, **kwargs)
@commandWrap
def ScaleCurvatureOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleCurvatureOptions(*args, **kwargs)
@commandWrap
def ImportSkinWeightMaps(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ImportSkinWeightMaps(*args, **kwargs)
@commandWrap
def layeredTexturePort(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.layeredTexturePort(*args, **kwargs)
@commandWrap
def cutKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cutKey(*args, **kwargs)
@commandWrap
def polyExtrudeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyExtrudeEdge(*args, **kwargs)
@commandWrap
def HypershadeSelectShadingGroupsAndMaterials(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectShadingGroupsAndMaterials(*args, **kwargs)
@commandWrap
def CreateNURBSCircle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSCircle(*args, **kwargs)
@commandWrap
def sortCaseInsensitive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sortCaseInsensitive(*args, **kwargs)
@commandWrap
def NodeEditorPinSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPinSelected(*args, **kwargs)
@commandWrap
def dx11Shader(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dx11Shader(*args, **kwargs)
@commandWrap
def ThreeLeftSplitViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ThreeLeftSplitViewArrangement(*args, **kwargs)
@commandWrap
def CreateNURBSCylinderOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSCylinderOptions(*args, **kwargs)
@commandWrap
def CreatePolygonPrism(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPrism(*args, **kwargs)
@commandWrap
def ResetWireOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetWireOptions(*args, **kwargs)
@commandWrap
def MergeMultipleEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeMultipleEdges(*args, **kwargs)
@commandWrap
def GroupOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GroupOptions(*args, **kwargs)
@commandWrap
def dR_coordSpaceObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_coordSpaceObject(*args, **kwargs)
@commandWrap
def DeleteAllShadingGroupsAndMaterials(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllShadingGroupsAndMaterials(*args, **kwargs)
@commandWrap
def CollapseSubdivSurfaceHierarchy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CollapseSubdivSurfaceHierarchy(*args, **kwargs)
@commandWrap
def ShowFur(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowFur(*args, **kwargs)
@commandWrap
def deleteAttrPattern(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deleteAttrPattern(*args, **kwargs)
@commandWrap
def ScaleConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleConstraint(*args, **kwargs)
@commandWrap
def XgmSetPlaceBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetPlaceBrushTool(*args, **kwargs)
@commandWrap
def ZoomTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ZoomTool(*args, **kwargs)
@commandWrap
def dR_activeHandleYZ(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_activeHandleYZ(*args, **kwargs)
@commandWrap
def directionalLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.directionalLight(*args, **kwargs)
@commandWrap
def CreateCameraFromView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCameraFromView(*args, **kwargs)
@commandWrap
def mirrorJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mirrorJoint(*args, **kwargs)
@commandWrap
def ParentConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParentConstraint(*args, **kwargs)
@commandWrap
def renderSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSettings(*args, **kwargs)
@commandWrap
def DisableFluids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableFluids(*args, **kwargs)
@commandWrap
def CreateNURBSCylinder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSCylinder(*args, **kwargs)
@commandWrap
def RenameCurrentColorSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenameCurrentColorSet(*args, **kwargs)
@commandWrap
def ToggleScalePivots(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleScalePivots(*args, **kwargs)
@commandWrap
def ExportDeformerWeightsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportDeformerWeightsOptions(*args, **kwargs)
@commandWrap
def ToggleVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleVertices(*args, **kwargs)
@commandWrap
def UVOrientShells(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVOrientShells(*args, **kwargs)
@commandWrap
def HypershadeCloseAllTabs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCloseAllTabs(*args, **kwargs)
@commandWrap
def CreateBifrostLiquid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateBifrostLiquid(*args, **kwargs)
@commandWrap
def UseSelectedEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UseSelectedEmitter(*args, **kwargs)
@commandWrap
def PreInfinityOscillate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreInfinityOscillate(*args, **kwargs)
@commandWrap
def grid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.grid(*args, **kwargs)
@commandWrap
def offsetCurveOnSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.offsetCurveOnSurface(*args, **kwargs)
@commandWrap
def DisableConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableConstraints(*args, **kwargs)
@commandWrap
def EnableIKSolvers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableIKSolvers(*args, **kwargs)
@commandWrap
def ProfilerToolCategoryView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolCategoryView(*args, **kwargs)
@commandWrap
def sbs_GetChannelsNamesFromSubstanceNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetChannelsNamesFromSubstanceNode(*args, **kwargs)
@commandWrap
def dR_activeHandleXZ(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_activeHandleXZ(*args, **kwargs)
@commandWrap
def particle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.particle(*args, **kwargs)
@commandWrap
def CreateLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateLocator(*args, **kwargs)
@commandWrap
def CreateBindingSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateBindingSet(*args, **kwargs)
@commandWrap
def FlowPathObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FlowPathObject(*args, **kwargs)
@commandWrap
def meshRemapContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.meshRemapContext(*args, **kwargs)
@commandWrap
def HypershadeGraphDownstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphDownstream(*args, **kwargs)
@commandWrap
def AttachToPath(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachToPath(*args, **kwargs)
@commandWrap
def DeleteSurfaceFlow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteSurfaceFlow(*args, **kwargs)
@commandWrap
def IncreaseExposureFine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncreaseExposureFine(*args, **kwargs)
@commandWrap
def GraphEditorEnableCurveSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorEnableCurveSelection(*args, **kwargs)
@commandWrap
def PoleVectorConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PoleVectorConstraint(*args, **kwargs)
@commandWrap
def xgmGroomTransfer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGroomTransfer(*args, **kwargs)
@commandWrap
def SelectFacePath(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectFacePath(*args, **kwargs)
@commandWrap
def ComponentEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ComponentEditor(*args, **kwargs)
@commandWrap
def GeometryToBoundingBoxOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GeometryToBoundingBoxOptions(*args, **kwargs)
@commandWrap
def U3DBrushPressureOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.U3DBrushPressureOn(*args, **kwargs)
@commandWrap
def NodeEditorShowAllAttrs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorShowAllAttrs(*args, **kwargs)
@commandWrap
def PresetBlendingWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PresetBlendingWindow(*args, **kwargs)
@commandWrap
def ShrinkLoopPolygonSelectionRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShrinkLoopPolygonSelectionRegion(*args, **kwargs)
@commandWrap
def ilrUVSACmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrUVSACmd(*args, **kwargs)
@commandWrap
def SelectAllNRigids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllNRigids(*args, **kwargs)
@commandWrap
def AssumePreferredAngle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssumePreferredAngle(*args, **kwargs)
@commandWrap
def editRenderLayerAdjustment(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.editRenderLayerAdjustment(*args, **kwargs)
@commandWrap
def spaceLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.spaceLocator(*args, **kwargs)
@commandWrap
def SelectCurveCVsLast(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectCurveCVsLast(*args, **kwargs)
@commandWrap
def HypershadeRenderPerspLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRenderPerspLayout(*args, **kwargs)
@commandWrap
def DisplayLayerEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayLayerEditorWindow(*args, **kwargs)
@commandWrap
def PolygonCollapseEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonCollapseEdges(*args, **kwargs)
@commandWrap
def polyUnite(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUnite(*args, **kwargs)
@commandWrap
def SubdivSmoothnessRough(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessRough(*args, **kwargs)
@commandWrap
def polySoftEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySoftEdge(*args, **kwargs)
@commandWrap
def NodeEditorGraphUpDownstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphUpDownstream(*args, **kwargs)
@commandWrap
def CreatePolygonSuperEllipseOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSuperEllipseOptions(*args, **kwargs)
@commandWrap
def ProductInformation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProductInformation(*args, **kwargs)
@commandWrap
def ReverseSurfaceDirectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReverseSurfaceDirectionOptions(*args, **kwargs)
@commandWrap
def xgmSculptLayerMerge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSculptLayerMerge(*args, **kwargs)
@commandWrap
def Birail2(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Birail2(*args, **kwargs)
@commandWrap
def Birail3(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Birail3(*args, **kwargs)
@commandWrap
def Birail1(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Birail1(*args, **kwargs)
@commandWrap
def FBXExportInstances(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportInstances(*args, **kwargs)
@commandWrap
def SequenceEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SequenceEditor(*args, **kwargs)
@commandWrap
def HIKPinRotate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKPinRotate(*args, **kwargs)
@commandWrap
def dR_gridSnapRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_gridSnapRelease(*args, **kwargs)
@commandWrap
def UVStraightenOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVStraightenOptions(*args, **kwargs)
@commandWrap
def SelectVertexFaceMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectVertexFaceMask(*args, **kwargs)
@commandWrap
def notifyPostUndo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.notifyPostUndo(*args, **kwargs)
@commandWrap
def PaintReduceWeightsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintReduceWeightsTool(*args, **kwargs)
@commandWrap
def polyMoveFacet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMoveFacet(*args, **kwargs)
@commandWrap
def ReducePolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReducePolygon(*args, **kwargs)
@commandWrap
def SplitUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitUV(*args, **kwargs)
@commandWrap
def BlendShapeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BlendShapeEditor(*args, **kwargs)
@commandWrap
def dR_customPivotToolRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_customPivotToolRelease(*args, **kwargs)
@commandWrap
def DuplicateNURBSPatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateNURBSPatches(*args, **kwargs)
@commandWrap
def BrushPresetBlendShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetBlendShape(*args, **kwargs)
@commandWrap
def posePanel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.posePanel(*args, **kwargs)
@commandWrap
def boxDollyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.boxDollyCtx(*args, **kwargs)
@commandWrap
def ToggleSymmetryDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSymmetryDisplay(*args, **kwargs)
@commandWrap
def SetCurrentColorSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetCurrentColorSet(*args, **kwargs)
@commandWrap
def AddOceanDynamicLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddOceanDynamicLocator(*args, **kwargs)
@commandWrap
def BrushPresetBlendShadingOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetBlendShadingOff(*args, **kwargs)
@commandWrap
def adskAssetLibrary(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.adskAssetLibrary(*args, **kwargs)
@commandWrap
def PaintCacheToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintCacheToolOptions(*args, **kwargs)
@commandWrap
def HypershadeCreateNewTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCreateNewTab(*args, **kwargs)
@commandWrap
def debug(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.debug(*args, **kwargs)
@commandWrap
def polySplitVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySplitVertex(*args, **kwargs)
@commandWrap
def dR_visorTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_visorTGL(*args, **kwargs)
@commandWrap
def CreatePolygonPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPlane(*args, **kwargs)
@commandWrap
def viewPlace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.viewPlace(*args, **kwargs)
@commandWrap
def AutoProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AutoProjection(*args, **kwargs)
@commandWrap
def CurveFlow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveFlow(*args, **kwargs)
@commandWrap
def PrefixHierarchyNames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PrefixHierarchyNames(*args, **kwargs)
@commandWrap
def MirrorJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorJoint(*args, **kwargs)
@commandWrap
def xgmCombBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCombBrushToolCmd(*args, **kwargs)
@commandWrap
def SetKeyScale(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKeyScale(*args, **kwargs)
@commandWrap
def XgmSplinePresetImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplinePresetImport(*args, **kwargs)
@commandWrap
def sbs_AffectTheseAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_AffectTheseAttributes(*args, **kwargs)
@commandWrap
def cameraView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cameraView(*args, **kwargs)
@commandWrap
def RotateToolMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateToolMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def xgmGuideContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGuideContext(*args, **kwargs)
@commandWrap
def NonWeightedTangents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NonWeightedTangents(*args, **kwargs)
@commandWrap
def shadingNetworkCompare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shadingNetworkCompare(*args, **kwargs)
@commandWrap
def FBXResetExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXResetExport(*args, **kwargs)
@commandWrap
def dR_setExtendLoop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_setExtendLoop(*args, **kwargs)
@commandWrap
def ShowSurfaceCVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowSurfaceCVs(*args, **kwargs)
@commandWrap
def dR_symmetryFlip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_symmetryFlip(*args, **kwargs)
@commandWrap
def ProjectCurveOnSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProjectCurveOnSurface(*args, **kwargs)
@commandWrap
def EnableTimeChangeUndoConsolidation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableTimeChangeUndoConsolidation(*args, **kwargs)
@commandWrap
def RotateUVTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateUVTool(*args, **kwargs)
@commandWrap
def SymmetrizeUVUpdateCommand(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SymmetrizeUVUpdateCommand(*args, **kwargs)
@commandWrap
def OutlinerToggleIgnoreHidden(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleIgnoreHidden(*args, **kwargs)
@commandWrap
def MirrorSkinWeightsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorSkinWeightsOptions(*args, **kwargs)
@commandWrap
def dR_selectAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectAll(*args, **kwargs)
@commandWrap
def dR_selConstraintEdgeLoop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selConstraintEdgeLoop(*args, **kwargs)
@commandWrap
def HypershadeIncreaseTraversalDepth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeIncreaseTraversalDepth(*args, **kwargs)
@commandWrap
def eval(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.eval(*args, **kwargs)
@commandWrap
def exactWorldBoundingBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.exactWorldBoundingBox(*args, **kwargs)
@commandWrap
def NodeEditorShowCustomAttrs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorShowCustomAttrs(*args, **kwargs)
@commandWrap
def dR_selConstraintBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selConstraintBorder(*args, **kwargs)
@commandWrap
def DeleteStaticChannels(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteStaticChannels(*args, **kwargs)
@commandWrap
def UVStackSimilarShellsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVStackSimilarShellsOptions(*args, **kwargs)
@commandWrap
def TruncateHairCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TruncateHairCache(*args, **kwargs)
@commandWrap
def Duplicate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Duplicate(*args, **kwargs)
@commandWrap
def FBXExportCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportCameras(*args, **kwargs)
@commandWrap
def NodeEditorCreateNodePopup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCreateNodePopup(*args, **kwargs)
@commandWrap
def FBXExportSkeletonDefinitions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportSkeletonDefinitions(*args, **kwargs)
@commandWrap
def SetKeyRotate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKeyRotate(*args, **kwargs)
@commandWrap
def ExtrudeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtrudeOptions(*args, **kwargs)
@commandWrap
def ToggleSceneTimecode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSceneTimecode(*args, **kwargs)
@commandWrap
def ActivateViewport20(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ActivateViewport20(*args, **kwargs)
@commandWrap
def AttachSubdivSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachSubdivSurface(*args, **kwargs)
@commandWrap
def ToggleCreaseVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCreaseVertices(*args, **kwargs)
@commandWrap
def dR_multiCutRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_multiCutRelease(*args, **kwargs)
@commandWrap
def ConvertToFrozen(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertToFrozen(*args, **kwargs)
@commandWrap
def PerspGraphLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PerspGraphLayout(*args, **kwargs)
@commandWrap
def selectContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectContext(*args, **kwargs)
@commandWrap
def DeleteSurfaceFlowOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteSurfaceFlowOptions(*args, **kwargs)
@commandWrap
def polyMergeEdgeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMergeEdgeCtx(*args, **kwargs)
@commandWrap
def NodeEditorGraphAllShapesExceptShading(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphAllShapesExceptShading(*args, **kwargs)
@commandWrap
def SubdividePolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdividePolygonOptions(*args, **kwargs)
@commandWrap
def geometryAppendCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryAppendCacheOpt(*args, **kwargs)
@commandWrap
def WaveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WaveOptions(*args, **kwargs)
@commandWrap
def HypershadeOpenCreateWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenCreateWindow(*args, **kwargs)
@commandWrap
def FBXExportCacheFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportCacheFile(*args, **kwargs)
@commandWrap
def referenceQuery(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.referenceQuery(*args, **kwargs)
@commandWrap
def FBXExportAudio(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportAudio(*args, **kwargs)
@commandWrap
def RerootSkeleton(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RerootSkeleton(*args, **kwargs)
@commandWrap
def singleProfileBirailSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.singleProfileBirailSurface(*args, **kwargs)
@commandWrap
def ViewAlongAxisNegativeY(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewAlongAxisNegativeY(*args, **kwargs)
@commandWrap
def NodeEditorRenderSwatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorRenderSwatches(*args, **kwargs)
@commandWrap
def particleExists(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.particleExists(*args, **kwargs)
@commandWrap
def SetMeshFlattenTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshFlattenTool(*args, **kwargs)
@commandWrap
def ShowManipulatorTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowManipulatorTool(*args, **kwargs)
@commandWrap
def HideAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideAll(*args, **kwargs)
@commandWrap
def MoveNearestPickedKeyToolDeactivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveNearestPickedKeyToolDeactivate(*args, **kwargs)
@commandWrap
def AddBifrostFoamMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostFoamMask(*args, **kwargs)
@commandWrap
def objectCenter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.objectCenter(*args, **kwargs)
@commandWrap
def NodeEditorAutoSizeNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorAutoSizeNodes(*args, **kwargs)
@commandWrap
def NodeEditorCloseActiveTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCloseActiveTab(*args, **kwargs)
@commandWrap
def CreatePolygonSuperEllipse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSuperEllipse(*args, **kwargs)
@commandWrap
def TimeEditorDeleteClips(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorDeleteClips(*args, **kwargs)
@commandWrap
def ToggleStatusLine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleStatusLine(*args, **kwargs)
@commandWrap
def MakePondBoatsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakePondBoatsOptions(*args, **kwargs)
@commandWrap
def ToggleUseDefaultMaterial(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUseDefaultMaterial(*args, **kwargs)
@commandWrap
def FBXExportInputConnections(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportInputConnections(*args, **kwargs)
@commandWrap
def cacheFileMerge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cacheFileMerge(*args, **kwargs)
@commandWrap
def closeCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.closeCurve(*args, **kwargs)
@commandWrap
def setDynamic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setDynamic(*args, **kwargs)
@commandWrap
def AddAnimationOffsetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddAnimationOffsetOptions(*args, **kwargs)
@commandWrap
def CreateOceanOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateOceanOptions(*args, **kwargs)
@commandWrap
def EmitFluidFromObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EmitFluidFromObject(*args, **kwargs)
@commandWrap
def ViewSequence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewSequence(*args, **kwargs)
@commandWrap
def animLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.animLayer(*args, **kwargs)
@commandWrap
def HypershadeSelectBakeSets(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectBakeSets(*args, **kwargs)
@commandWrap
def attachFluidCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attachFluidCache(*args, **kwargs)
@commandWrap
def planarSrf(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.planarSrf(*args, **kwargs)
@commandWrap
def defineVirtualDevice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.defineVirtualDevice(*args, **kwargs)
@commandWrap
def projectionManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.projectionManip(*args, **kwargs)
@commandWrap
def evalContinue(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.evalContinue(*args, **kwargs)
@commandWrap
def IncrementAndSave(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncrementAndSave(*args, **kwargs)
@commandWrap
def SculptSurfacesToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptSurfacesToolOptions(*args, **kwargs)
@commandWrap
def dR_selConstraintUVEdgeLoop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selConstraintUVEdgeLoop(*args, **kwargs)
@commandWrap
def furSubdArea(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.furSubdArea(*args, **kwargs)
@commandWrap
def dR_bevelTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_bevelTool(*args, **kwargs)
@commandWrap
def FBXImportSetLockedAttribute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportSetLockedAttribute(*args, **kwargs)
@commandWrap
def HypershadeShapeMenuStateNoShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShapeMenuStateNoShapes(*args, **kwargs)
@commandWrap
def CutSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutSelected(*args, **kwargs)
@commandWrap
def NodeEditorGraphUpstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphUpstream(*args, **kwargs)
@commandWrap
def ShowCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowCameras(*args, **kwargs)
@commandWrap
def ToggleTangentDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleTangentDisplay(*args, **kwargs)
@commandWrap
def dbcount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dbcount(*args, **kwargs)
@commandWrap
def PolyExtrudeEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrudeEdges(*args, **kwargs)
@commandWrap
def RandomizeFollicles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RandomizeFollicles(*args, **kwargs)
@commandWrap
def polyToCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyToCurve(*args, **kwargs)
@commandWrap
def hotkeyEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hotkeyEditor(*args, **kwargs)
@commandWrap
def file(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.file(*args, **kwargs)
@commandWrap
def polyRemesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyRemesh(*args, **kwargs)
@commandWrap
def snapshotBeadContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.snapshotBeadContext(*args, **kwargs)
@commandWrap
def AffectSelectedObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AffectSelectedObject(*args, **kwargs)
@commandWrap
def QuadrangulateOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.QuadrangulateOptions(*args, **kwargs)
@commandWrap
def xgmSmoothBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSmoothBrushToolCmd(*args, **kwargs)
@commandWrap
def ConnectionEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConnectionEditor(*args, **kwargs)
@commandWrap
def poseInterpolator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.poseInterpolator(*args, **kwargs)
@commandWrap
def lockNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lockNode(*args, **kwargs)
@commandWrap
def TogglePolygonFaceCenters(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolygonFaceCenters(*args, **kwargs)
@commandWrap
def UnpublishParentAnchor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnpublishParentAnchor(*args, **kwargs)
@commandWrap
def PickWalkDownSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkDownSelect(*args, **kwargs)
@commandWrap
def dR_slideEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_slideEdge(*args, **kwargs)
@commandWrap
def recordDevice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.recordDevice(*args, **kwargs)
@commandWrap
def ilrPointCloudCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrPointCloudCmd(*args, **kwargs)
@commandWrap
def MakeBrushSpring(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeBrushSpring(*args, **kwargs)
@commandWrap
def furCompareFileTime(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.furCompareFileTime(*args, **kwargs)
@commandWrap
def EditMembershipTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EditMembershipTool(*args, **kwargs)
@commandWrap
def MatchScaling(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MatchScaling(*args, **kwargs)
@commandWrap
def Art3dPaintToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Art3dPaintToolOptions(*args, **kwargs)
@commandWrap
def ToggleCreaseEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCreaseEdges(*args, **kwargs)
@commandWrap
def insertKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.insertKeyCtx(*args, **kwargs)
@commandWrap
def FBXExportTriangulate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportTriangulate(*args, **kwargs)
@commandWrap
def Delete(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Delete(*args, **kwargs)
@commandWrap
def RadialOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RadialOptions(*args, **kwargs)
@commandWrap
def AlembicHelp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicHelp(*args, **kwargs)
@commandWrap
def UpdateCurrentSceneMotionBuilder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UpdateCurrentSceneMotionBuilder(*args, **kwargs)
@commandWrap
def ptexBake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ptexBake(*args, **kwargs)
@commandWrap
def fcheck(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fcheck(*args, **kwargs)
@commandWrap
def HIKGetRemoteCharacterList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKGetRemoteCharacterList(*args, **kwargs)
@commandWrap
def BatchRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BatchRender(*args, **kwargs)
@commandWrap
def SelectContiguousEdgesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectContiguousEdgesOptions(*args, **kwargs)
@commandWrap
def SculptMeshDeactivateBrushSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptMeshDeactivateBrushSize(*args, **kwargs)
@commandWrap
def CreateSubCharacterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubCharacterOptions(*args, **kwargs)
@commandWrap
def SaveCurrentLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveCurrentLayout(*args, **kwargs)
@commandWrap
def currentCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.currentCtx(*args, **kwargs)
@commandWrap
def smoothCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.smoothCurve(*args, **kwargs)
@commandWrap
def HypershadeDuplicateWithoutNetwork(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDuplicateWithoutNetwork(*args, **kwargs)
@commandWrap
def texSmudgeUVContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texSmudgeUVContext(*args, **kwargs)
@commandWrap
def PoseInterpolatorNewGroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PoseInterpolatorNewGroup(*args, **kwargs)
@commandWrap
def dR_disableTexturesTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_disableTexturesTGL(*args, **kwargs)
@commandWrap
def curve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curve(*args, **kwargs)
@commandWrap
def TimeEditorExportSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorExportSelection(*args, **kwargs)
@commandWrap
def SplitEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitEdge(*args, **kwargs)
@commandWrap
def geometryMergeCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryMergeCache(*args, **kwargs)
@commandWrap
def AddToContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddToContainer(*args, **kwargs)
@commandWrap
def dollyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dollyCtx(*args, **kwargs)
@commandWrap
def DisplayShaded(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayShaded(*args, **kwargs)
@commandWrap
def FloodSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FloodSurfaces(*args, **kwargs)
@commandWrap
def buildKeyframeMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.buildKeyframeMenu(*args, **kwargs)
@commandWrap
def PostInfinityConstant(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PostInfinityConstant(*args, **kwargs)
@commandWrap
def glRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.glRender(*args, **kwargs)
@commandWrap
def dR_viewTop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewTop(*args, **kwargs)
@commandWrap
def ResetProperty2State(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetProperty2State(*args, **kwargs)
@commandWrap
def UVEditorToggleTextureBorderDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVEditorToggleTextureBorderDisplay(*args, **kwargs)
@commandWrap
def HypershadeGraphRearrange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphRearrange(*args, **kwargs)
@commandWrap
def DeleteAllNonLinearDeformers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllNonLinearDeformers(*args, **kwargs)
@commandWrap
def CreateOceanWake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateOceanWake(*args, **kwargs)
@commandWrap
def SavePreferences(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SavePreferences(*args, **kwargs)
@commandWrap
def CreatePolygonHelixOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonHelixOptions(*args, **kwargs)
@commandWrap
def RemoveWrapInfluence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveWrapInfluence(*args, **kwargs)
@commandWrap
def PickWalkLeft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkLeft(*args, **kwargs)
@commandWrap
def MakeCurvesDynamic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeCurvesDynamic(*args, **kwargs)
@commandWrap
def UntrimSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UntrimSurfaces(*args, **kwargs)
@commandWrap
def SelectAllSculptObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllSculptObjects(*args, **kwargs)
@commandWrap
def CreateParticleDiskCacheOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateParticleDiskCacheOptions(*args, **kwargs)
@commandWrap
def SelectCurveCVsFirst(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectCurveCVsFirst(*args, **kwargs)
@commandWrap
def ChannelControlEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ChannelControlEditor(*args, **kwargs)
@commandWrap
def PartialCreaseSubdivSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PartialCreaseSubdivSurface(*args, **kwargs)
@commandWrap
def ConvertToKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertToKey(*args, **kwargs)
@commandWrap
def SelectAllIKHandles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllIKHandles(*args, **kwargs)
@commandWrap
def deleteHistoryAheadOfGeomCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deleteHistoryAheadOfGeomCache(*args, **kwargs)
@commandWrap
def ResetWire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetWire(*args, **kwargs)
@commandWrap
def pointConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointConstraint(*args, **kwargs)
@commandWrap
def dR_quadDrawClearDots(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_quadDrawClearDots(*args, **kwargs)
@commandWrap
def SculptMeshFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptMeshFrame(*args, **kwargs)
@commandWrap
def geometryCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryCache(*args, **kwargs)
@commandWrap
def CreateDagContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateDagContainerOptions(*args, **kwargs)
@commandWrap
def testPassContribution(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.testPassContribution(*args, **kwargs)
@commandWrap
def xgmGroomConvert(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGroomConvert(*args, **kwargs)
@commandWrap
def showShadingGroupAttrEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.showShadingGroupAttrEditor(*args, **kwargs)
@commandWrap
def CreateNodeWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNodeWindow(*args, **kwargs)
@commandWrap
def HideUIElements(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideUIElements(*args, **kwargs)
@commandWrap
def PaintEffectsWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsWindow(*args, **kwargs)
@commandWrap
def createMeshFromPoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createMeshFromPoints(*args, **kwargs)
@commandWrap
def FourViewLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FourViewLayout(*args, **kwargs)
@commandWrap
def RemoveBifrostKillplane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostKillplane(*args, **kwargs)
@commandWrap
def UVEditorFrameSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVEditorFrameSelected(*args, **kwargs)
@commandWrap
def HypershadeTransferAttributeValues(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeTransferAttributeValues(*args, **kwargs)
@commandWrap
def CreateLatticeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateLatticeOptions(*args, **kwargs)
@commandWrap
def Unfold3DContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Unfold3DContext(*args, **kwargs)
@commandWrap
def DetachSkinOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachSkinOptions(*args, **kwargs)
@commandWrap
def XgmSetClumpBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetClumpBrushToolOption(*args, **kwargs)
@commandWrap
def GraphCopy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphCopy(*args, **kwargs)
@commandWrap
def GetHIKChildCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKChildCount(*args, **kwargs)
@commandWrap
def XgmSetClumpBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetClumpBrushTool(*args, **kwargs)
@commandWrap
def OneClickGetState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickGetState(*args, **kwargs)
@commandWrap
def dR_mtkPanelTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_mtkPanelTGL(*args, **kwargs)
@commandWrap
def OutlinerToggleAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleAttributes(*args, **kwargs)
@commandWrap
def EditCharacterAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EditCharacterAttributes(*args, **kwargs)
@commandWrap
def SimplifyCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SimplifyCurveOptions(*args, **kwargs)
@commandWrap
def PolySpinEdgeBackward(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolySpinEdgeBackward(*args, **kwargs)
@commandWrap
def XgmSplineCacheImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheImport(*args, **kwargs)
@commandWrap
def condition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.condition(*args, **kwargs)
@commandWrap
def blendShapeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blendShapeEditor(*args, **kwargs)
@commandWrap
def sbs_GetSubstanceBuildVersion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetSubstanceBuildVersion(*args, **kwargs)
@commandWrap
def SelectAllParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllParticles(*args, **kwargs)
@commandWrap
def polyNormal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyNormal(*args, **kwargs)
@commandWrap
def polyAverageNormal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyAverageNormal(*args, **kwargs)
@commandWrap
def MirrorSkinWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorSkinWeights(*args, **kwargs)
@commandWrap
def xgmPromoteRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPromoteRender(*args, **kwargs)
@commandWrap
def SetKeyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKeyOptions(*args, **kwargs)
@commandWrap
def RemoveBifrostEmissionRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostEmissionRegion(*args, **kwargs)
@commandWrap
def ToggleMaterialLoadingDetailsVisibility(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMaterialLoadingDetailsVisibility(*args, **kwargs)
@commandWrap
def AutoPaintMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AutoPaintMarkingMenu(*args, **kwargs)
@commandWrap
def FBXExportBakeResampleAnimation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportBakeResampleAnimation(*args, **kwargs)
@commandWrap
def GpuCacheImportOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GpuCacheImportOptions(*args, **kwargs)
@commandWrap
def PositionAlongCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PositionAlongCurve(*args, **kwargs)
@commandWrap
def movOut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.movOut(*args, **kwargs)
@commandWrap
def Export(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Export(*args, **kwargs)
@commandWrap
def blendShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blendShape(*args, **kwargs)
@commandWrap
def ScaleConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleConstraintOptions(*args, **kwargs)
@commandWrap
def artPuttyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artPuttyCtx(*args, **kwargs)
@commandWrap
def HypershadeDeleteAllTextures(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteAllTextures(*args, **kwargs)
@commandWrap
def NURBSToPolygons(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSToPolygons(*args, **kwargs)
@commandWrap
def containerProxy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.containerProxy(*args, **kwargs)
@commandWrap
def ParentConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParentConstraintOptions(*args, **kwargs)
@commandWrap
def xgmLengthBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmLengthBrushToolCmd(*args, **kwargs)
@commandWrap
def timeEditorClipLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorClipLayer(*args, **kwargs)
@commandWrap
def SnapToGridPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToGridPress(*args, **kwargs)
@commandWrap
def ResetTransformationsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetTransformationsOptions(*args, **kwargs)
@commandWrap
def cacheAppend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cacheAppend(*args, **kwargs)
@commandWrap
def latticeDeformKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.latticeDeformKeyCtx(*args, **kwargs)
@commandWrap
def ExportOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportOptions(*args, **kwargs)
@commandWrap
def HypershadeGridToggleSnap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGridToggleSnap(*args, **kwargs)
@commandWrap
def GetHIKEffectorCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetHIKEffectorCount(*args, **kwargs)
@commandWrap
def interactionStyle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.interactionStyle(*args, **kwargs)
@commandWrap
def filterCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.filterCurve(*args, **kwargs)
@commandWrap
def reroot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reroot(*args, **kwargs)
@commandWrap
def FBXGetTakeCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXGetTakeCount(*args, **kwargs)
@commandWrap
def polySelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySelect(*args, **kwargs)
@commandWrap
def setParent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setParent(*args, **kwargs)
@commandWrap
def polyIterOnPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyIterOnPoly(*args, **kwargs)
@commandWrap
def ClearCurrentCharacterList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClearCurrentCharacterList(*args, **kwargs)
@commandWrap
def ubercam(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ubercam(*args, **kwargs)
@commandWrap
def NodeEditorToggleConsistentNodeNameSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleConsistentNodeNameSize(*args, **kwargs)
@commandWrap
def HypershadeOutlinerPerspLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOutlinerPerspLayout(*args, **kwargs)
@commandWrap
def polySlideEdgeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySlideEdgeCtx(*args, **kwargs)
@commandWrap
def ImportAnimOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ImportAnimOptions(*args, **kwargs)
@commandWrap
def FBXExportConvert2Tif(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportConvert2Tif(*args, **kwargs)
@commandWrap
def OutlinerExpandAllItems(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerExpandAllItems(*args, **kwargs)
@commandWrap
def intersect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.intersect(*args, **kwargs)
@commandWrap
def DeleteStaticChannelsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteStaticChannelsOptions(*args, **kwargs)
@commandWrap
def AddTargetShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddTargetShapeOptions(*args, **kwargs)
@commandWrap
def shapeCompare(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shapeCompare(*args, **kwargs)
@commandWrap
def HypershadeSelectLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectLights(*args, **kwargs)
@commandWrap
def snapshotModifyKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.snapshotModifyKeyCtx(*args, **kwargs)
@commandWrap
def HypershadeConnectSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeConnectSelected(*args, **kwargs)
@commandWrap
def nodeType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nodeType(*args, **kwargs)
@commandWrap
def FBXExportSkins(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportSkins(*args, **kwargs)
@commandWrap
def HypershadePickWalkRight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePickWalkRight(*args, **kwargs)
@commandWrap
def canCreateManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.canCreateManip(*args, **kwargs)
@commandWrap
def UnfoldPackUVs3DInEmptyTile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnfoldPackUVs3DInEmptyTile(*args, **kwargs)
@commandWrap
def SnapToGrid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToGrid(*args, **kwargs)
@commandWrap
def PolySelectToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolySelectToolOptions(*args, **kwargs)
@commandWrap
def ShowAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowAll(*args, **kwargs)
@commandWrap
def SurfaceBooleanSubtractToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceBooleanSubtractToolOptions(*args, **kwargs)
@commandWrap
def SetMeshSculptTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshSculptTool(*args, **kwargs)
@commandWrap
def nClothDeleteCacheFrames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothDeleteCacheFrames(*args, **kwargs)
@commandWrap
def SetNClothStartFromMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetNClothStartFromMesh(*args, **kwargs)
@commandWrap
def RemoveBifrostAccelerator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostAccelerator(*args, **kwargs)
@commandWrap
def PolyMergeVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyMergeVertices(*args, **kwargs)
@commandWrap
def AveragePolygonNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AveragePolygonNormals(*args, **kwargs)
@commandWrap
def ContentBrowserWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ContentBrowserWindow(*args, **kwargs)
@commandWrap
def HypershadeSelectUpStream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectUpStream(*args, **kwargs)
@commandWrap
def xgmGuideRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGuideRender(*args, **kwargs)
@commandWrap
def subdDisplayMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdDisplayMode(*args, **kwargs)
@commandWrap
def SelectMaskToolMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectMaskToolMarkingMenu(*args, **kwargs)
@commandWrap
def freeFormFillet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.freeFormFillet(*args, **kwargs)
@commandWrap
def polyCollapseFacet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCollapseFacet(*args, **kwargs)
@commandWrap
def CopyVertexSkinWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyVertexSkinWeights(*args, **kwargs)
@commandWrap
def GlobalStitchOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GlobalStitchOptions(*args, **kwargs)
@commandWrap
def xgmClumpBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmClumpBrushContext(*args, **kwargs)
@commandWrap
def spBirailCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.spBirailCtx(*args, **kwargs)
@commandWrap
def polySlideEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySlideEdge(*args, **kwargs)
@commandWrap
def FBXExportReferencedContainersContent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportReferencedContainersContent(*args, **kwargs)
@commandWrap
def sbs_SetEditionModeScale(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_SetEditionModeScale(*args, **kwargs)
@commandWrap
def MoveLeft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveLeft(*args, **kwargs)
@commandWrap
def rename(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rename(*args, **kwargs)
@commandWrap
def TogglePolyDisplaySoftEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyDisplaySoftEdges(*args, **kwargs)
@commandWrap
def dynCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynCache(*args, **kwargs)
@commandWrap
def SelectHierarchy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectHierarchy(*args, **kwargs)
@commandWrap
def getMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getMetadata(*args, **kwargs)
@commandWrap
def manipPivot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipPivot(*args, **kwargs)
@commandWrap
def renderPassRegistry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderPassRegistry(*args, **kwargs)
@commandWrap
def MakePressureCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakePressureCurve(*args, **kwargs)
@commandWrap
def CycleIKHandleStickyState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CycleIKHandleStickyState(*args, **kwargs)
@commandWrap
def PruneSmallWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PruneSmallWeights(*args, **kwargs)
@commandWrap
def MarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MarkingMenuPopDown(*args, **kwargs)
@commandWrap
def ConvertInstanceToObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertInstanceToObject(*args, **kwargs)
@commandWrap
def xgmAddGuide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmAddGuide(*args, **kwargs)
@commandWrap
def boxZoomCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.boxZoomCtx(*args, **kwargs)
@commandWrap
def CreatePolygonTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonTool(*args, **kwargs)
@commandWrap
def AddPondDynamicLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPondDynamicLocator(*args, **kwargs)
@commandWrap
def ilrIBLCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrIBLCmd(*args, **kwargs)
@commandWrap
def MoveSkinJointsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveSkinJointsToolOptions(*args, **kwargs)
@commandWrap
def NewScene(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NewScene(*args, **kwargs)
@commandWrap
def RemoveBindingSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBindingSet(*args, **kwargs)
@commandWrap
def MakePressureCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakePressureCurveOptions(*args, **kwargs)
@commandWrap
def CreateSubdivSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivSurfaceOptions(*args, **kwargs)
@commandWrap
def ShowAnimationUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowAnimationUI(*args, **kwargs)
@commandWrap
def HypershadeSelectMaterialsFromObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectMaterialsFromObjects(*args, **kwargs)
@commandWrap
def PolygonSoftenHarden(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonSoftenHarden(*args, **kwargs)
@commandWrap
def reverseCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reverseCurve(*args, **kwargs)
@commandWrap
def arubaNurbsToPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.arubaNurbsToPoly(*args, **kwargs)
@commandWrap
def ProjectWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProjectWindow(*args, **kwargs)
@commandWrap
def ShowWrapInfluences(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowWrapInfluences(*args, **kwargs)
@commandWrap
def rampWidget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rampWidget(*args, **kwargs)
@commandWrap
def NodeEditorIncreaseTraversalDepth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorIncreaseTraversalDepth(*args, **kwargs)
@commandWrap
def HypershadeGraphUpstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphUpstream(*args, **kwargs)
@commandWrap
def coarsenSubdivSelectionList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.coarsenSubdivSelectionList(*args, **kwargs)
@commandWrap
def SetFullBodyIKKeysBodyPart(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFullBodyIKKeysBodyPart(*args, **kwargs)
@commandWrap
def SymmetrizeUVBrushSizeOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SymmetrizeUVBrushSizeOff(*args, **kwargs)
@commandWrap
def AddBifrostMotionField(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostMotionField(*args, **kwargs)
@commandWrap
def dgInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgInfo(*args, **kwargs)
@commandWrap
def ParticleInstancer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParticleInstancer(*args, **kwargs)
@commandWrap
def UVStackSimilarShells(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVStackSimilarShells(*args, **kwargs)
@commandWrap
def ModifyDisplacementPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyDisplacementPress(*args, **kwargs)
@commandWrap
def itemFilterAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.itemFilterAttr(*args, **kwargs)
@commandWrap
def OutlinerToggleOrganizeByLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleOrganizeByLayer(*args, **kwargs)
@commandWrap
def caddyManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.caddyManip(*args, **kwargs)
@commandWrap
def moveVertexAlongDirection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.moveVertexAlongDirection(*args, **kwargs)
@commandWrap
def sbs_GetBakeFormat(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetBakeFormat(*args, **kwargs)
@commandWrap
def polyEvaluate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyEvaluate(*args, **kwargs)
@commandWrap
def polySelectEditCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySelectEditCtx(*args, **kwargs)
@commandWrap
def sbs_GetPackageFullPathNameFromSubstanceNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetPackageFullPathNameFromSubstanceNode(*args, **kwargs)
@commandWrap
def polySetToFaceNormal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySetToFaceNormal(*args, **kwargs)
@commandWrap
def deltaMush(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deltaMush(*args, **kwargs)
@commandWrap
def HideJoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideJoints(*args, **kwargs)
@commandWrap
def CreateSpringOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSpringOptions(*args, **kwargs)
@commandWrap
def CreateFlexorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateFlexorWindow(*args, **kwargs)
@commandWrap
def RemoveBifrostCollider(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostCollider(*args, **kwargs)
@commandWrap
def saveInitialState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.saveInitialState(*args, **kwargs)
@commandWrap
def dR_setRelaxAffectsBorders(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_setRelaxAffectsBorders(*args, **kwargs)
@commandWrap
def ResetReflectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetReflectionOptions(*args, **kwargs)
@commandWrap
def launch(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.launch(*args, **kwargs)
@commandWrap
def xgmDataQueryHelperForTest(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmDataQueryHelperForTest(*args, **kwargs)
@commandWrap
def RotateToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateToolOptions(*args, **kwargs)
@commandWrap
def ModifyOpacityRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyOpacityRelease(*args, **kwargs)
@commandWrap
def clearDynStartState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clearDynStartState(*args, **kwargs)
@commandWrap
def paramDimension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.paramDimension(*args, **kwargs)
@commandWrap
def applyTake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.applyTake(*args, **kwargs)
@commandWrap
def MoveRotateScaleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveRotateScaleTool(*args, **kwargs)
@commandWrap
def TextureViewWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TextureViewWindow(*args, **kwargs)
@commandWrap
def FitBSpline(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FitBSpline(*args, **kwargs)
@commandWrap
def SubdivToNURBS(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivToNURBS(*args, **kwargs)
@commandWrap
def dR_hypershadeTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_hypershadeTGL(*args, **kwargs)
@commandWrap
def dR_gridSnapPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_gridSnapPress(*args, **kwargs)
@commandWrap
def muMessageQuery(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.muMessageQuery(*args, **kwargs)
@commandWrap
def FBXExportApplyConstantKeyReducer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportApplyConstantKeyReducer(*args, **kwargs)
@commandWrap
def nurbsPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsPlane(*args, **kwargs)
@commandWrap
def PreInfinityConstant(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreInfinityConstant(*args, **kwargs)
@commandWrap
def RigidBindSkin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RigidBindSkin(*args, **kwargs)
@commandWrap
def AbortCurrentTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AbortCurrentTool(*args, **kwargs)
@commandWrap
def collision(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.collision(*args, **kwargs)
@commandWrap
def TexSewDeactivateBrushSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSewDeactivateBrushSize(*args, **kwargs)
@commandWrap
def makePaintable(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.makePaintable(*args, **kwargs)
@commandWrap
def RemoveLatticeTweaks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveLatticeTweaks(*args, **kwargs)
@commandWrap
def FBXImportShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportShapes(*args, **kwargs)
@commandWrap
def polyMultiLayoutUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMultiLayoutUV(*args, **kwargs)
@commandWrap
def HypershadePublishConnections(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePublishConnections(*args, **kwargs)
@commandWrap
def showHelp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.showHelp(*args, **kwargs)
@commandWrap
def polySelectSp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySelectSp(*args, **kwargs)
@commandWrap
def AssignTemplateOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignTemplateOptions(*args, **kwargs)
@commandWrap
def ViewAlongAxisX(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewAlongAxisX(*args, **kwargs)
@commandWrap
def ViewAlongAxisZ(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewAlongAxisZ(*args, **kwargs)
@commandWrap
def ToggleHelpLine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleHelpLine(*args, **kwargs)
@commandWrap
def UntrimSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UntrimSurfacesOptions(*args, **kwargs)
@commandWrap
def ATOMTemplateOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ATOMTemplateOptions(*args, **kwargs)
@commandWrap
def WhatsNewHighlightingOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WhatsNewHighlightingOff(*args, **kwargs)
@commandWrap
def PaintCacheTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintCacheTool(*args, **kwargs)
@commandWrap
def ToggleBackfaceGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleBackfaceGeometry(*args, **kwargs)
@commandWrap
def NodeEditorGraphNoShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphNoShapes(*args, **kwargs)
@commandWrap
def xgmMoveDescription(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmMoveDescription(*args, **kwargs)
@commandWrap
def CreatePolygonPlaneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPlaneOptions(*args, **kwargs)
@commandWrap
def subdAutoProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdAutoProjection(*args, **kwargs)
@commandWrap
def AddPfxToHairSystem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPfxToHairSystem(*args, **kwargs)
@commandWrap
def dynPref(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynPref(*args, **kwargs)
@commandWrap
def AddSelectionAsInBetweenTargetShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddSelectionAsInBetweenTargetShape(*args, **kwargs)
@commandWrap
def waitCursor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.waitCursor(*args, **kwargs)
@commandWrap
def FBXExportUpAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportUpAxis(*args, **kwargs)
@commandWrap
def ToggleUVEditorUVStatisticsHUDOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVEditorUVStatisticsHUDOptions(*args, **kwargs)
@commandWrap
def hwRenderLoad(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hwRenderLoad(*args, **kwargs)
@commandWrap
def RemoveBifrostAdaptiveMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostAdaptiveMesh(*args, **kwargs)
@commandWrap
def SubdivToNURBSOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivToNURBSOptions(*args, **kwargs)
@commandWrap
def PerspRelationshipEditorLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PerspRelationshipEditorLayout(*args, **kwargs)
@commandWrap
def UnfoldUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnfoldUV(*args, **kwargs)
@commandWrap
def plane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.plane(*args, **kwargs)
@commandWrap
def DeleteCurrentColorSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteCurrentColorSet(*args, **kwargs)
@commandWrap
def UpdateCurrentScene3dsMax(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UpdateCurrentScene3dsMax(*args, **kwargs)
@commandWrap
def shotTrack(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shotTrack(*args, **kwargs)
@commandWrap
def CreateTextureDeformer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateTextureDeformer(*args, **kwargs)
@commandWrap
def choice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.choice(*args, **kwargs)
@commandWrap
def OutlinerToggleReferenceMembers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleReferenceMembers(*args, **kwargs)
@commandWrap
def SendToUnityAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendToUnityAll(*args, **kwargs)
@commandWrap
def MovePolygonComponent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MovePolygonComponent(*args, **kwargs)
@commandWrap
def EnableSelectedIKHandles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableSelectedIKHandles(*args, **kwargs)
@commandWrap
def AbcExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AbcExport(*args, **kwargs)
@commandWrap
def polyFlipUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyFlipUV(*args, **kwargs)
@commandWrap
def ToggleFaceIDs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFaceIDs(*args, **kwargs)
@commandWrap
def BatchBakeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BatchBakeOptions(*args, **kwargs)
@commandWrap
def createPolyPipeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyPipeCtx(*args, **kwargs)
@commandWrap
def SoftModTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SoftModTool(*args, **kwargs)
@commandWrap
def AddSelectionAsCombinationTargetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddSelectionAsCombinationTargetOptions(*args, **kwargs)
@commandWrap
def GravityOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GravityOptions(*args, **kwargs)
@commandWrap
def AddDynamicBuoy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddDynamicBuoy(*args, **kwargs)
@commandWrap
def Extrude(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Extrude(*args, **kwargs)
@commandWrap
def FBXExportQuaternion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportQuaternion(*args, **kwargs)
@commandWrap
def SetStrokeControlCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetStrokeControlCurves(*args, **kwargs)
@commandWrap
def dR_vertUnlockAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_vertUnlockAll(*args, **kwargs)
@commandWrap
def meshReorderContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.meshReorderContext(*args, **kwargs)
@commandWrap
def GraphCut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphCut(*args, **kwargs)
@commandWrap
def panZoomCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.panZoomCtx(*args, **kwargs)
@commandWrap
def moveKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.moveKeyCtx(*args, **kwargs)
@commandWrap
def TimeEditorFrameAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorFrameAll(*args, **kwargs)
@commandWrap
def RemoveShrinkWrapInnerObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveShrinkWrapInnerObject(*args, **kwargs)
@commandWrap
def OutTangentSpline(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutTangentSpline(*args, **kwargs)
@commandWrap
def help(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.help(*args, **kwargs)
@commandWrap
def polyToSubdiv(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyToSubdiv(*args, **kwargs)
@commandWrap
def enableDevice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.enableDevice(*args, **kwargs)
@commandWrap
def PolygonCollapse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonCollapse(*args, **kwargs)
@commandWrap
def assignInputDevice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.assignInputDevice(*args, **kwargs)
@commandWrap
def ShowSelectedObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowSelectedObjects(*args, **kwargs)
@commandWrap
def undoInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.undoInfo(*args, **kwargs)
@commandWrap
def bakeResults(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bakeResults(*args, **kwargs)
@commandWrap
def ModifyConstraintAxisOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyConstraintAxisOptions(*args, **kwargs)
@commandWrap
def OutlinerRevealSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerRevealSelected(*args, **kwargs)
@commandWrap
def ilrDisplacementToPolyCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrDisplacementToPolyCmd(*args, **kwargs)
@commandWrap
def xgmGuideGeom(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGuideGeom(*args, **kwargs)
@commandWrap
def modelingToolkitSuperCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.modelingToolkitSuperCtx(*args, **kwargs)
@commandWrap
def ArtPaintBlendShapeWeightsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintBlendShapeWeightsTool(*args, **kwargs)
@commandWrap
def SelectContainerContents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectContainerContents(*args, **kwargs)
@commandWrap
def ClosestPointOnOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClosestPointOnOptions(*args, **kwargs)
@commandWrap
def timeEditorClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorClip(*args, **kwargs)
@commandWrap
def xgmWrapXGen(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmWrapXGen(*args, **kwargs)
@commandWrap
def MirrorCutPolygonGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorCutPolygonGeometry(*args, **kwargs)
@commandWrap
def SelectPolygonToolMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectPolygonToolMarkingMenu(*args, **kwargs)
@commandWrap
def render(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.render(*args, **kwargs)
@commandWrap
def HypershadeShowCustomAttrs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShowCustomAttrs(*args, **kwargs)
@commandWrap
def reproInstancer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reproInstancer(*args, **kwargs)
@commandWrap
def CreatePondOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePondOptions(*args, **kwargs)
@commandWrap
def xpmPicker(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xpmPicker(*args, **kwargs)
@commandWrap
def manipComponentPivot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipComponentPivot(*args, **kwargs)
@commandWrap
def GraphCopyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphCopyOptions(*args, **kwargs)
@commandWrap
def ReverseCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReverseCurveOptions(*args, **kwargs)
@commandWrap
def batchRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.batchRender(*args, **kwargs)
@commandWrap
def CharacterMapper(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CharacterMapper(*args, **kwargs)
@commandWrap
def Art3dPaintTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Art3dPaintTool(*args, **kwargs)
@commandWrap
def SetMeshGrabUVTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshGrabUVTool(*args, **kwargs)
@commandWrap
def NodeEditorGraphAllShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphAllShapes(*args, **kwargs)
@commandWrap
def resetTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.resetTool(*args, **kwargs)
@commandWrap
def subdCleanTopology(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdCleanTopology(*args, **kwargs)
@commandWrap
def convertSolidTx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.convertSolidTx(*args, **kwargs)
@commandWrap
def StraightenCurvesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StraightenCurvesOptions(*args, **kwargs)
@commandWrap
def FlipUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FlipUVs(*args, **kwargs)
@commandWrap
def PickWalkRightSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkRightSelect(*args, **kwargs)
@commandWrap
def AlignUVOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlignUVOptions(*args, **kwargs)
@commandWrap
def AddPondBoatLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPondBoatLocator(*args, **kwargs)
@commandWrap
def UnmirrorSmoothProxyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnmirrorSmoothProxyOptions(*args, **kwargs)
@commandWrap
def apfEntityNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.apfEntityNode(*args, **kwargs)
@commandWrap
def CVHardnessOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CVHardnessOptions(*args, **kwargs)
@commandWrap
def TransformPolygonComponent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransformPolygonComponent(*args, **kwargs)
@commandWrap
def HypershadeCreatePSDFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCreatePSDFile(*args, **kwargs)
@commandWrap
def UnlockCurveLength(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnlockCurveLength(*args, **kwargs)
@commandWrap
def Lightning(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Lightning(*args, **kwargs)
@commandWrap
def AddEdgeDivisions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddEdgeDivisions(*args, **kwargs)
@commandWrap
def directConnectPath(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.directConnectPath(*args, **kwargs)
@commandWrap
def XgmSplineCacheDelete(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheDelete(*args, **kwargs)
@commandWrap
def HypershadeRenameActiveTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRenameActiveTab(*args, **kwargs)
@commandWrap
def playblast(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.playblast(*args, **kwargs)
@commandWrap
def NodeEditorHighlightConnectionsOnNodeSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorHighlightConnectionsOnNodeSelection(*args, **kwargs)
@commandWrap
def hilite(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hilite(*args, **kwargs)
@commandWrap
def ogsdebug(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ogsdebug(*args, **kwargs)
@commandWrap
def xgmLengthBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmLengthBrushContext(*args, **kwargs)
@commandWrap
def containerView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.containerView(*args, **kwargs)
@commandWrap
def SnapToCurvePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToCurvePress(*args, **kwargs)
@commandWrap
def cMuscleWeightSave(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleWeightSave(*args, **kwargs)
@commandWrap
def SelectAllLattices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllLattices(*args, **kwargs)
@commandWrap
def TexSculptActivateBrushStrength(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSculptActivateBrushStrength(*args, **kwargs)
@commandWrap
def Newton(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Newton(*args, **kwargs)
@commandWrap
def polySuperShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySuperShape(*args, **kwargs)
@commandWrap
def refresh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.refresh(*args, **kwargs)
@commandWrap
def RetimeKeysToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RetimeKeysToolOptions(*args, **kwargs)
@commandWrap
def radial(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.radial(*args, **kwargs)
@commandWrap
def dR_selConstraintElement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selConstraintElement(*args, **kwargs)
@commandWrap
def U3DBrushPressureOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.U3DBrushPressureOff(*args, **kwargs)
@commandWrap
def NodeEditorConnectionStyleStraight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorConnectionStyleStraight(*args, **kwargs)
@commandWrap
def RenderViewNextImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderViewNextImage(*args, **kwargs)
@commandWrap
def TimeEditorSetKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorSetKey(*args, **kwargs)
@commandWrap
def IncreaseExposureCoarse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncreaseExposureCoarse(*args, **kwargs)
@commandWrap
def openMayaPref(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.openMayaPref(*args, **kwargs)
@commandWrap
def renderInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderInfo(*args, **kwargs)
@commandWrap
def DeleteAllIKHandles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllIKHandles(*args, **kwargs)
@commandWrap
def CutPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutPolygon(*args, **kwargs)
@commandWrap
def XgmSetDensityBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetDensityBrushToolOption(*args, **kwargs)
@commandWrap
def ShowManipulators(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowManipulators(*args, **kwargs)
@commandWrap
def selectKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectKeyCtx(*args, **kwargs)
@commandWrap
def TranslateToolMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TranslateToolMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def CPMeldoIt__1703324687(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CPMeldoIt__1703324687(*args, **kwargs)
@commandWrap
def dR_connectRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_connectRelease(*args, **kwargs)
@commandWrap
def OutTangentPlateau(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutTangentPlateau(*args, **kwargs)
@commandWrap
def FBXExportAnimationOnly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportAnimationOnly(*args, **kwargs)
@commandWrap
def bakeClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bakeClip(*args, **kwargs)
@commandWrap
def MirrorSubdivSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorSubdivSurfaceOptions(*args, **kwargs)
@commandWrap
def event(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.event(*args, **kwargs)
@commandWrap
def UnpublishAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnpublishAttributes(*args, **kwargs)
@commandWrap
def hikCharacterToolWidget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikCharacterToolWidget(*args, **kwargs)
@commandWrap
def CreateConstructionPlaneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateConstructionPlaneOptions(*args, **kwargs)
@commandWrap
def HideIntermediateObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideIntermediateObjects(*args, **kwargs)
@commandWrap
def copyDeformerWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.copyDeformerWeights(*args, **kwargs)
@commandWrap
def rebuildSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rebuildSurface(*args, **kwargs)
@commandWrap
def XgmSplineCacheImportOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheImportOptions(*args, **kwargs)
@commandWrap
def OutTangentFixed(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutTangentFixed(*args, **kwargs)
@commandWrap
def HypershadeSelectObjectsWithMaterials(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSelectObjectsWithMaterials(*args, **kwargs)
@commandWrap
def characterizationToolUICmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.characterizationToolUICmd(*args, **kwargs)
@commandWrap
def polyCBoolOp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCBoolOp(*args, **kwargs)
@commandWrap
def FBXExportDeleteOriginalTakeOnSplitAnimation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportDeleteOriginalTakeOnSplitAnimation(*args, **kwargs)
@commandWrap
def polyColorPerVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyColorPerVertex(*args, **kwargs)
@commandWrap
def AddDivisionsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddDivisionsOptions(*args, **kwargs)
@commandWrap
def Revolve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Revolve(*args, **kwargs)
@commandWrap
def sbs_SetWorkflow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_SetWorkflow(*args, **kwargs)
@commandWrap
def AttributeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttributeEditor(*args, **kwargs)
@commandWrap
def dR_setRelaxAffectsAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_setRelaxAffectsAll(*args, **kwargs)
@commandWrap
def showHidden(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.showHidden(*args, **kwargs)
@commandWrap
def displaySmoothness(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displaySmoothness(*args, **kwargs)
@commandWrap
def dagCommandWrapper(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dagCommandWrapper(*args, **kwargs)
@commandWrap
def polyReduce(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyReduce(*args, **kwargs)
@commandWrap
def RenderViewWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderViewWindow(*args, **kwargs)
@commandWrap
def EmptyAnimLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EmptyAnimLayer(*args, **kwargs)
@commandWrap
def PoleVectorConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PoleVectorConstraintOptions(*args, **kwargs)
@commandWrap
def renameUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renameUI(*args, **kwargs)
@commandWrap
def AnimationSnapshot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AnimationSnapshot(*args, **kwargs)
@commandWrap
def xgmSplineSetCurrentDescription(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplineSetCurrentDescription(*args, **kwargs)
@commandWrap
def HIKBodyPartMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKBodyPartMode(*args, **kwargs)
@commandWrap
def ToggleUVIsolateViewSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVIsolateViewSelected(*args, **kwargs)
@commandWrap
def DuplicateWithTransform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateWithTransform(*args, **kwargs)
@commandWrap
def AttachSelectedAsSourceField(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachSelectedAsSourceField(*args, **kwargs)
@commandWrap
def polySeparate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySeparate(*args, **kwargs)
@commandWrap
def ToggleChannelsLayers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleChannelsLayers(*args, **kwargs)
@commandWrap
def AddHolderOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddHolderOptions(*args, **kwargs)
@commandWrap
def NEmitFromObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NEmitFromObject(*args, **kwargs)
@commandWrap
def XgmSetLengthBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetLengthBrushTool(*args, **kwargs)
@commandWrap
def SetMeshScrapeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshScrapeTool(*args, **kwargs)
@commandWrap
def nucleusDisplayMaterialNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusDisplayMaterialNodes(*args, **kwargs)
@commandWrap
def FBXExportUseTmpFilePeripheral(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportUseTmpFilePeripheral(*args, **kwargs)
@commandWrap
def PolyMerge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyMerge(*args, **kwargs)
@commandWrap
def rigidBody(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rigidBody(*args, **kwargs)
@commandWrap
def ExtendFluidOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendFluidOptions(*args, **kwargs)
@commandWrap
def MakeBrushSpringOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeBrushSpringOptions(*args, **kwargs)
@commandWrap
def selectKeyframeRegionCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectKeyframeRegionCtx(*args, **kwargs)
@commandWrap
def deleteExtension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deleteExtension(*args, **kwargs)
@commandWrap
def AnimationSnapshotOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AnimationSnapshotOptions(*args, **kwargs)
@commandWrap
def setRenderPassType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setRenderPassType(*args, **kwargs)
@commandWrap
def geometryConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryConstraint(*args, **kwargs)
@commandWrap
def StitchSurfacePoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StitchSurfacePoints(*args, **kwargs)
@commandWrap
def AppendToHairCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AppendToHairCache(*args, **kwargs)
@commandWrap
def NodeEditorToggleNodeTitleMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleNodeTitleMode(*args, **kwargs)
@commandWrap
def SetMeshFillTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshFillTool(*args, **kwargs)
@commandWrap
def PolyEditEdgeFlow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyEditEdgeFlow(*args, **kwargs)
@commandWrap
def PaintEffectsToPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsToPoly(*args, **kwargs)
@commandWrap
def instancer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.instancer(*args, **kwargs)
@commandWrap
def renderSetupHighlight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetupHighlight(*args, **kwargs)
@commandWrap
def openGLExtension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.openGLExtension(*args, **kwargs)
@commandWrap
def SubdivSmoothnessMediumOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessMediumOptions(*args, **kwargs)
@commandWrap
def roundConstantRadius(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.roundConstantRadius(*args, **kwargs)
@commandWrap
def LoftOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LoftOptions(*args, **kwargs)
@commandWrap
def u3dUnfold(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.u3dUnfold(*args, **kwargs)
@commandWrap
def TurbulenceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TurbulenceOptions(*args, **kwargs)
@commandWrap
def AddAttribute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddAttribute(*args, **kwargs)
@commandWrap
def PlayblastOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PlayblastOptions(*args, **kwargs)
@commandWrap
def BakeChannel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeChannel(*args, **kwargs)
@commandWrap
def texManipContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texManipContext(*args, **kwargs)
@commandWrap
def xgmDensityComp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmDensityComp(*args, **kwargs)
@commandWrap
def createNurbsPlaneCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsPlaneCtx(*args, **kwargs)
@commandWrap
def HypershadeImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeImport(*args, **kwargs)
@commandWrap
def truncateHairCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.truncateHairCache(*args, **kwargs)
@commandWrap
def arcLenDimContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.arcLenDimContext(*args, **kwargs)
@commandWrap
def ilrRenderWindowCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrRenderWindowCmd(*args, **kwargs)
@commandWrap
def FloatSelectedObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FloatSelectedObjects(*args, **kwargs)
@commandWrap
def TimeEditorFrameSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorFrameSelected(*args, **kwargs)
@commandWrap
def InsertIsoparms(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertIsoparms(*args, **kwargs)
@commandWrap
def FBXImportLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportLights(*args, **kwargs)
@commandWrap
def dR_meshAlphaTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_meshAlphaTGL(*args, **kwargs)
@commandWrap
def nodeCast(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nodeCast(*args, **kwargs)
@commandWrap
def DuplicateCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateCurveOptions(*args, **kwargs)
@commandWrap
def selectPriority(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectPriority(*args, **kwargs)
@commandWrap
def saveImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.saveImage(*args, **kwargs)
@commandWrap
def dgmodified(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgmodified(*args, **kwargs)
@commandWrap
def HypershadePickWalkUp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePickWalkUp(*args, **kwargs)
@commandWrap
def SelectCVsMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectCVsMask(*args, **kwargs)
@commandWrap
def NodeEditorSetTraversalDepthZero(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorSetTraversalDepthZero(*args, **kwargs)
@commandWrap
def relationship(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.relationship(*args, **kwargs)
@commandWrap
def pfxstrokes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pfxstrokes(*args, **kwargs)
@commandWrap
def launchImageEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.launchImageEditor(*args, **kwargs)
@commandWrap
def BridgeEdgeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BridgeEdgeOptions(*args, **kwargs)
@commandWrap
def PolyExtrudeVerticesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrudeVerticesOptions(*args, **kwargs)
@commandWrap
def SelectAllFurs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllFurs(*args, **kwargs)
@commandWrap
def detachDeviceAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.detachDeviceAttr(*args, **kwargs)
@commandWrap
def AddShrinkWrapSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddShrinkWrapSurfaces(*args, **kwargs)
@commandWrap
def DeleteAllLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllLights(*args, **kwargs)
@commandWrap
def CreateSubdivSphere(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivSphere(*args, **kwargs)
@commandWrap
def PruneLattice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PruneLattice(*args, **kwargs)
@commandWrap
def XgmSetPartBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetPartBrushToolOption(*args, **kwargs)
@commandWrap
def xform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xform(*args, **kwargs)
@commandWrap
def polySpinEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySpinEdge(*args, **kwargs)
@commandWrap
def XgmSetLengthBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetLengthBrushToolOption(*args, **kwargs)
@commandWrap
def HideNonlinears(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideNonlinears(*args, **kwargs)
@commandWrap
def PolygonNormalEditTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonNormalEditTool(*args, **kwargs)
@commandWrap
def AutoPaintMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AutoPaintMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def subdivDisplaySmoothness(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdivDisplaySmoothness(*args, **kwargs)
@commandWrap
def TexSculptUnpinAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSculptUnpinAll(*args, **kwargs)
@commandWrap
def SelectContiguousEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectContiguousEdges(*args, **kwargs)
@commandWrap
def InTangentClamped(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InTangentClamped(*args, **kwargs)
@commandWrap
def curveCVCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveCVCtx(*args, **kwargs)
@commandWrap
def hitTest(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hitTest(*args, **kwargs)
@commandWrap
def setEditCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setEditCtx(*args, **kwargs)
@commandWrap
def TimeEditorCutClips(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCutClips(*args, **kwargs)
@commandWrap
def BrushPresetReplaceShadingOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetReplaceShadingOff(*args, **kwargs)
@commandWrap
def ExportProxyContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportProxyContainerOptions(*args, **kwargs)
@commandWrap
def SetFocusToNumericInputLine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFocusToNumericInputLine(*args, **kwargs)
@commandWrap
def XgCreateDescriptionEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgCreateDescriptionEditor(*args, **kwargs)
@commandWrap
def dR_objectBackfaceTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_objectBackfaceTGL(*args, **kwargs)
@commandWrap
def OptimzeUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OptimzeUVs(*args, **kwargs)
@commandWrap
def STRSTweakModeToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.STRSTweakModeToggle(*args, **kwargs)
@commandWrap
def Bevel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Bevel(*args, **kwargs)
@commandWrap
def CreateTextOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateTextOptions(*args, **kwargs)
@commandWrap
def TesselateSubdivSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TesselateSubdivSurfaceOptions(*args, **kwargs)
@commandWrap
def PruneSmallWeightsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PruneSmallWeightsOptions(*args, **kwargs)
@commandWrap
def HypergraphHierarchyWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypergraphHierarchyWindow(*args, **kwargs)
@commandWrap
def polyAppendFacetCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyAppendFacetCtx(*args, **kwargs)
@commandWrap
def draggerContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.draggerContext(*args, **kwargs)
@commandWrap
def EditFluidResolution(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EditFluidResolution(*args, **kwargs)
@commandWrap
def dR_convertSelectionToVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_convertSelectionToVertex(*args, **kwargs)
@commandWrap
def ShowMeshFreezeToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshFreezeToolOptions(*args, **kwargs)
@commandWrap
def ShowMeshFlattenToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshFlattenToolOptions(*args, **kwargs)
@commandWrap
def NodeEditorGraphAddSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphAddSelected(*args, **kwargs)
@commandWrap
def ShowUIElements(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowUIElements(*args, **kwargs)
@commandWrap
def nucleusDisplayDynamicConstraintNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusDisplayDynamicConstraintNodes(*args, **kwargs)
@commandWrap
def ModifyStampDepthRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyStampDepthRelease(*args, **kwargs)
@commandWrap
def DeleteEntireHairSystem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteEntireHairSystem(*args, **kwargs)
@commandWrap
def OffsetEdgeLoopToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetEdgeLoopToolOptions(*args, **kwargs)
@commandWrap
def DisableIKSolvers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableIKSolvers(*args, **kwargs)
@commandWrap
def ScaleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleTool(*args, **kwargs)
@commandWrap
def sculptTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sculptTarget(*args, **kwargs)
@commandWrap
def DisplayWireframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayWireframe(*args, **kwargs)
@commandWrap
def ConvertSelectionToUVShellBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToUVShellBorder(*args, **kwargs)
@commandWrap
def NodeEditorLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorLayout(*args, **kwargs)
@commandWrap
def MinimizeApplication(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MinimizeApplication(*args, **kwargs)
@commandWrap
def timeCode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeCode(*args, **kwargs)
@commandWrap
def ToggleSurfaceOrigin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSurfaceOrigin(*args, **kwargs)
@commandWrap
def psdTextureFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.psdTextureFile(*args, **kwargs)
@commandWrap
def PolyMergeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyMergeOptions(*args, **kwargs)
@commandWrap
def ShowPlanes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowPlanes(*args, **kwargs)
@commandWrap
def play(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.play(*args, **kwargs)
@commandWrap
def UnitizeUVsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnitizeUVsOptions(*args, **kwargs)
@commandWrap
def polyBridgeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyBridgeEdge(*args, **kwargs)
@commandWrap
def polyCanBridgeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCanBridgeEdge(*args, **kwargs)
@commandWrap
def UVGatherShells(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVGatherShells(*args, **kwargs)
@commandWrap
def NodeEditorToggleShowNamespace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleShowNamespace(*args, **kwargs)
@commandWrap
def nClothDeleteCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothDeleteCacheOpt(*args, **kwargs)
@commandWrap
def AssignBrushToHairSystem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignBrushToHairSystem(*args, **kwargs)
@commandWrap
def dR_cycleCustomCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_cycleCustomCameras(*args, **kwargs)
@commandWrap
def iGroom(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.iGroom(*args, **kwargs)
@commandWrap
def hasMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hasMetadata(*args, **kwargs)
@commandWrap
def AddBifrostFoam(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostFoam(*args, **kwargs)
@commandWrap
def NodeEditorPickWalkDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorPickWalkDown(*args, **kwargs)
@commandWrap
def scriptJob(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scriptJob(*args, **kwargs)
@commandWrap
def XgmSetDirectionBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetDirectionBrushTool(*args, **kwargs)
@commandWrap
def HypershadeDeleteAllLights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteAllLights(*args, **kwargs)
@commandWrap
def viewClipPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.viewClipPlane(*args, **kwargs)
@commandWrap
def UpdateCurrentSceneMudbox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UpdateCurrentSceneMudbox(*args, **kwargs)
@commandWrap
def FBXImportAxisConversionEnable(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportAxisConversionEnable(*args, **kwargs)
@commandWrap
def HideDeformingGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideDeformingGeometry(*args, **kwargs)
@commandWrap
def DetachSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachSurfaces(*args, **kwargs)
@commandWrap
def blindDataType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blindDataType(*args, **kwargs)
@commandWrap
def FilletBlendToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FilletBlendToolOptions(*args, **kwargs)
@commandWrap
def torus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.torus(*args, **kwargs)
@commandWrap
def InsertKnot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertKnot(*args, **kwargs)
@commandWrap
def artBaseCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artBaseCtx(*args, **kwargs)
@commandWrap
def MakeCollideHair(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeCollideHair(*args, **kwargs)
@commandWrap
def RevolveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RevolveOptions(*args, **kwargs)
@commandWrap
def paintPointsCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.paintPointsCmd(*args, **kwargs)
@commandWrap
def xgmExportSplineDataInternal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmExportSplineDataInternal(*args, **kwargs)
@commandWrap
def DeactivateGlobalScreenSlider(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeactivateGlobalScreenSlider(*args, **kwargs)
@commandWrap
def doBlur(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.doBlur(*args, **kwargs)
@commandWrap
def PlanarOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PlanarOptions(*args, **kwargs)
@commandWrap
def blend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blend(*args, **kwargs)
@commandWrap
def GoToBindPose(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoToBindPose(*args, **kwargs)
@commandWrap
def normalConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.normalConstraint(*args, **kwargs)
@commandWrap
def RelaxInitialStateOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RelaxInitialStateOptions(*args, **kwargs)
@commandWrap
def TimeEditorClipRazor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipRazor(*args, **kwargs)
@commandWrap
def applyMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.applyMetadata(*args, **kwargs)
@commandWrap
def HypershadePickWalkDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePickWalkDown(*args, **kwargs)
@commandWrap
def HideHairSystems(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideHairSystems(*args, **kwargs)
@commandWrap
def PlayblastWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PlayblastWindow(*args, **kwargs)
@commandWrap
def HideKinematics(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideKinematics(*args, **kwargs)
@commandWrap
def ShowIKHandles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowIKHandles(*args, **kwargs)
@commandWrap
def ShowMeshRelaxToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshRelaxToolOptions(*args, **kwargs)
@commandWrap
def PublishAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishAttributes(*args, **kwargs)
@commandWrap
def HypershadeDeleteAllShadingGroupsAndMaterials(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteAllShadingGroupsAndMaterials(*args, **kwargs)
@commandWrap
def autoSave(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.autoSave(*args, **kwargs)
@commandWrap
def ToggleToolMessage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleToolMessage(*args, **kwargs)
@commandWrap
def ToolSettingsWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToolSettingsWindow(*args, **kwargs)
@commandWrap
def polySelectConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySelectConstraint(*args, **kwargs)
@commandWrap
def CreateSubdivCylinder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivCylinder(*args, **kwargs)
@commandWrap
def TimeEditorCreateClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateClip(*args, **kwargs)
@commandWrap
def SubdCutUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdCutUVs(*args, **kwargs)
@commandWrap
def dR_objectHideTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_objectHideTGL(*args, **kwargs)
@commandWrap
def RemoveBifrostEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostEmitter(*args, **kwargs)
@commandWrap
def HideStrokes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideStrokes(*args, **kwargs)
@commandWrap
def BakeCustomPivot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeCustomPivot(*args, **kwargs)
@commandWrap
def polyEditUVShell(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyEditUVShell(*args, **kwargs)
@commandWrap
def HypershadeHideAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeHideAttributes(*args, **kwargs)
@commandWrap
def HideCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideCameras(*args, **kwargs)
@commandWrap
def FBXImportGenerateLog(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportGenerateLog(*args, **kwargs)
@commandWrap
def CreateDiskCacheOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateDiskCacheOptions(*args, **kwargs)
@commandWrap
def PasteKeysOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PasteKeysOptions(*args, **kwargs)
@commandWrap
def SendAsNewSceneMotionBuilder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendAsNewSceneMotionBuilder(*args, **kwargs)
@commandWrap
def IKSplineHandleToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IKSplineHandleToolOptions(*args, **kwargs)
@commandWrap
def XgmSplineCacheDeleteOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheDeleteOptions(*args, **kwargs)
@commandWrap
def diskCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.diskCache(*args, **kwargs)
@commandWrap
def TagAsController(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TagAsController(*args, **kwargs)
@commandWrap
def PruneCluster(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PruneCluster(*args, **kwargs)
@commandWrap
def SendToUnrealSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendToUnrealSelection(*args, **kwargs)
@commandWrap
def dynParticleCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynParticleCtx(*args, **kwargs)
@commandWrap
def AbcBulletExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AbcBulletExport(*args, **kwargs)
@commandWrap
def ilrVertexBakeCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrVertexBakeCmd(*args, **kwargs)
@commandWrap
def CutKeysOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutKeysOptions(*args, **kwargs)
@commandWrap
def polyMapSew(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMapSew(*args, **kwargs)
@commandWrap
def SurfaceEditingTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceEditingTool(*args, **kwargs)
@commandWrap
def ClearBifrostInitialState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClearBifrostInitialState(*args, **kwargs)
@commandWrap
def dR_symmetryTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_symmetryTGL(*args, **kwargs)
@commandWrap
def detachSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.detachSurface(*args, **kwargs)
@commandWrap
def getDefaultBrush(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getDefaultBrush(*args, **kwargs)
@commandWrap
def HypershadeOpenBinsWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenBinsWindow(*args, **kwargs)
@commandWrap
def TransferAttributeValues(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransferAttributeValues(*args, **kwargs)
@commandWrap
def DeleteHairCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteHairCache(*args, **kwargs)
@commandWrap
def truncateFluidCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.truncateFluidCache(*args, **kwargs)
@commandWrap
def ToggleHikDetails(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleHikDetails(*args, **kwargs)
@commandWrap
def UpdateBindingSetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UpdateBindingSetOptions(*args, **kwargs)
@commandWrap
def nClothMergeCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothMergeCache(*args, **kwargs)
@commandWrap
def SelectUVBorderComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVBorderComponents(*args, **kwargs)
@commandWrap
def NormalConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NormalConstraintOptions(*args, **kwargs)
@commandWrap
def AddPondSurfaceLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPondSurfaceLocator(*args, **kwargs)
@commandWrap
def RemoveWireOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveWireOptions(*args, **kwargs)
@commandWrap
def sbs_GetEngine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetEngine(*args, **kwargs)
@commandWrap
def Help(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Help(*args, **kwargs)
@commandWrap
def ConnectComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConnectComponents(*args, **kwargs)
@commandWrap
def blendTwoAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blendTwoAttr(*args, **kwargs)
@commandWrap
def HypershadeAddOnNodeCreate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeAddOnNodeCreate(*args, **kwargs)
@commandWrap
def CreateAreaLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateAreaLight(*args, **kwargs)
@commandWrap
def offsetSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.offsetSurface(*args, **kwargs)
@commandWrap
def PolySpinEdgeForward(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolySpinEdgeForward(*args, **kwargs)
@commandWrap
def LevelOfDetailUngroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LevelOfDetailUngroup(*args, **kwargs)
@commandWrap
def ToggleLatticeShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleLatticeShape(*args, **kwargs)
@commandWrap
def BakeSimulation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeSimulation(*args, **kwargs)
@commandWrap
def SmoothSkinWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothSkinWeights(*args, **kwargs)
@commandWrap
def IKHandleToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IKHandleToolOptions(*args, **kwargs)
@commandWrap
def unknownPlugin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.unknownPlugin(*args, **kwargs)
@commandWrap
def HIKSetBodyPartKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKSetBodyPartKey(*args, **kwargs)
@commandWrap
def InsertKeysToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertKeysToolOptions(*args, **kwargs)
@commandWrap
def MoveUp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveUp(*args, **kwargs)
@commandWrap
def ConformPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConformPolygon(*args, **kwargs)
@commandWrap
def polyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyOptions(*args, **kwargs)
@commandWrap
def SplitEdgeRingTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitEdgeRingTool(*args, **kwargs)
@commandWrap
def TransformNoSelectOnTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransformNoSelectOnTool(*args, **kwargs)
@commandWrap
def MergeVertexToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeVertexToolOptions(*args, **kwargs)
@commandWrap
def Create2DContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create2DContainer(*args, **kwargs)
@commandWrap
def HIKLiveConnectionTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKLiveConnectionTool(*args, **kwargs)
@commandWrap
def AimConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AimConstraintOptions(*args, **kwargs)
@commandWrap
def polyChipOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyChipOff(*args, **kwargs)
@commandWrap
def DisplayShadedAndTextured(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayShadedAndTextured(*args, **kwargs)
@commandWrap
def polySphericalProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySphericalProjection(*args, **kwargs)
@commandWrap
def ConvertSelectionToVertexPerimeter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToVertexPerimeter(*args, **kwargs)
@commandWrap
def polySubdivideEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySubdivideEdge(*args, **kwargs)
@commandWrap
def InTangentFixed(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InTangentFixed(*args, **kwargs)
@commandWrap
def mouldMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mouldMesh(*args, **kwargs)
@commandWrap
def SelectVertexMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectVertexMask(*args, **kwargs)
@commandWrap
def createLayeredPsdFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createLayeredPsdFile(*args, **kwargs)
@commandWrap
def xgmNoiseBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmNoiseBrushToolCmd(*args, **kwargs)
@commandWrap
def NodeEditorSelectUpStream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorSelectUpStream(*args, **kwargs)
@commandWrap
def CenterViewOfSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CenterViewOfSelection(*args, **kwargs)
@commandWrap
def setDynStartState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setDynStartState(*args, **kwargs)
@commandWrap
def sculptMeshCacheCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sculptMeshCacheCtx(*args, **kwargs)
@commandWrap
def untangleUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.untangleUV(*args, **kwargs)
@commandWrap
def HyperGraphPanelUndoViewChange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HyperGraphPanelUndoViewChange(*args, **kwargs)
@commandWrap
def UVEditorUnpinAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVEditorUnpinAll(*args, **kwargs)
@commandWrap
def subdiv(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdiv(*args, **kwargs)
@commandWrap
def renderQualityNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderQualityNode(*args, **kwargs)
@commandWrap
def GraphEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditor(*args, **kwargs)
@commandWrap
def dgstats(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgstats(*args, **kwargs)
@commandWrap
def SelectTextureReferenceObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectTextureReferenceObject(*args, **kwargs)
@commandWrap
def ShowKinematics(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowKinematics(*args, **kwargs)
@commandWrap
def FBXExportInAscii(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportInAscii(*args, **kwargs)
@commandWrap
def HypershadeDeleteAllBakeSets(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteAllBakeSets(*args, **kwargs)
@commandWrap
def dR_bevelRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_bevelRelease(*args, **kwargs)
@commandWrap
def HypershadeDisplayInterestingShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayInterestingShapes(*args, **kwargs)
@commandWrap
def NodeEditorGridToggleCrosshairOnEdgeDragging(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGridToggleCrosshairOnEdgeDragging(*args, **kwargs)
@commandWrap
def GraphCutOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphCutOptions(*args, **kwargs)
@commandWrap
def selectKeyframe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectKeyframe(*args, **kwargs)
@commandWrap
def DistributeUVsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DistributeUVsOptions(*args, **kwargs)
@commandWrap
def ToggleMainMenubar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMainMenubar(*args, **kwargs)
@commandWrap
def NodeEditorToggleNodeSwatchSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleNodeSwatchSize(*args, **kwargs)
@commandWrap
def TexSculptDeactivateBrushSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSculptDeactivateBrushSize(*args, **kwargs)
@commandWrap
def ModifyDisplacementRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyDisplacementRelease(*args, **kwargs)
@commandWrap
def ShowLattices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowLattices(*args, **kwargs)
@commandWrap
def FBXExportColladaSingleMatrix(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportColladaSingleMatrix(*args, **kwargs)
@commandWrap
def SnapToPointPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToPointPress(*args, **kwargs)
@commandWrap
def paintEffectsDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.paintEffectsDisplay(*args, **kwargs)
@commandWrap
def SelectUVBackFacingComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVBackFacingComponents(*args, **kwargs)
@commandWrap
def SculptSubdivsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptSubdivsTool(*args, **kwargs)
@commandWrap
def RemoveBifrostField(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostField(*args, **kwargs)
@commandWrap
def dR_meshOffsetTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_meshOffsetTGL(*args, **kwargs)
@commandWrap
def UnlockNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnlockNormals(*args, **kwargs)
@commandWrap
def ToggleShowResults(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleShowResults(*args, **kwargs)
@commandWrap
def LayoutUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LayoutUV(*args, **kwargs)
@commandWrap
def renderSetupSwitchVisibleRenderLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetupSwitchVisibleRenderLayer(*args, **kwargs)
@commandWrap
def BevelPolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BevelPolygonOptions(*args, **kwargs)
@commandWrap
def makeIdentity(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.makeIdentity(*args, **kwargs)
@commandWrap
def HypershadeDeleteUnusedNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteUnusedNodes(*args, **kwargs)
@commandWrap
def XgmSetSmoothBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetSmoothBrushToolOption(*args, **kwargs)
@commandWrap
def EditPolygonType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EditPolygonType(*args, **kwargs)
@commandWrap
def dR_viewPersp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewPersp(*args, **kwargs)
@commandWrap
def cMuscleSimulate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleSimulate(*args, **kwargs)
@commandWrap
def DisplaySmoothShaded(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplaySmoothShaded(*args, **kwargs)
@commandWrap
def dynPaintEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynPaintEditor(*args, **kwargs)
@commandWrap
def CreateSubdivTorus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivTorus(*args, **kwargs)
@commandWrap
def MapUVBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MapUVBorder(*args, **kwargs)
@commandWrap
def AddBifrostKillField(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostKillField(*args, **kwargs)
@commandWrap
def currentUnit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.currentUnit(*args, **kwargs)
@commandWrap
def FBXExportShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportShapes(*args, **kwargs)
@commandWrap
def HypershadeSortByName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSortByName(*args, **kwargs)
@commandWrap
def stereoRigManager(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stereoRigManager(*args, **kwargs)
@commandWrap
def HighQualityDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HighQualityDisplay(*args, **kwargs)
@commandWrap
def dR_coordSpaceWorld(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_coordSpaceWorld(*args, **kwargs)
@commandWrap
def HypershadeDisplayAsList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayAsList(*args, **kwargs)
@commandWrap
def ikSystem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikSystem(*args, **kwargs)
@commandWrap
def PolyCircularize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyCircularize(*args, **kwargs)
@commandWrap
def GeometryToBoundingBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GeometryToBoundingBox(*args, **kwargs)
@commandWrap
def CustomNURBSSmoothnessOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CustomNURBSSmoothnessOptions(*args, **kwargs)
@commandWrap
def OneClickDispatch(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickDispatch(*args, **kwargs)
@commandWrap
def SelectAllSubdivGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllSubdivGeometry(*args, **kwargs)
@commandWrap
def ToggleReflection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleReflection(*args, **kwargs)
@commandWrap
def DistributeUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DistributeUVs(*args, **kwargs)
@commandWrap
def keyingGroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyingGroup(*args, **kwargs)
@commandWrap
def MoveDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveDown(*args, **kwargs)
@commandWrap
def RemoveFromContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveFromContainer(*args, **kwargs)
@commandWrap
def HypershadeRemoveAsset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRemoveAsset(*args, **kwargs)
@commandWrap
def applyAttrPattern(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.applyAttrPattern(*args, **kwargs)
@commandWrap
def ShowRiggingUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowRiggingUI(*args, **kwargs)
@commandWrap
def SewUVs3D(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SewUVs3D(*args, **kwargs)
@commandWrap
def bakePartialHistory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bakePartialHistory(*args, **kwargs)
@commandWrap
def SaveBrushPreset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveBrushPreset(*args, **kwargs)
@commandWrap
def FBXClose(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXClose(*args, **kwargs)
@commandWrap
def NextFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NextFrame(*args, **kwargs)
@commandWrap
def scaleKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scaleKeyCtx(*args, **kwargs)
@commandWrap
def HIKCycleMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKCycleMode(*args, **kwargs)
@commandWrap
def PolygonBooleanUnion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonBooleanUnion(*args, **kwargs)
@commandWrap
def XgmSetGrabBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetGrabBrushToolOption(*args, **kwargs)
@commandWrap
def artAttrPaintVertexCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artAttrPaintVertexCtx(*args, **kwargs)
@commandWrap
def DeleteAllMotionPaths(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllMotionPaths(*args, **kwargs)
@commandWrap
def dR_scaleTweakTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_scaleTweakTool(*args, **kwargs)
@commandWrap
def SmoothBindSkinOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothBindSkinOptions(*args, **kwargs)
@commandWrap
def polyMoveVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMoveVertex(*args, **kwargs)
@commandWrap
def xgmSetActive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSetActive(*args, **kwargs)
@commandWrap
def SubdivSmoothnessRoughOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessRoughOptions(*args, **kwargs)
@commandWrap
def SoftModDeformer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SoftModDeformer(*args, **kwargs)
@commandWrap
def TimeEditorClipLoopToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipLoopToggle(*args, **kwargs)
@commandWrap
def srtContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.srtContext(*args, **kwargs)
@commandWrap
def orientConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.orientConstraint(*args, **kwargs)
@commandWrap
def SetTimecode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetTimecode(*args, **kwargs)
@commandWrap
def textureDeformer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.textureDeformer(*args, **kwargs)
@commandWrap
def geoUtils(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geoUtils(*args, **kwargs)
@commandWrap
def bifrost(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bifrost(*args, **kwargs)
@commandWrap
def ImportDeformerWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ImportDeformerWeights(*args, **kwargs)
@commandWrap
def InsertJointTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertJointTool(*args, **kwargs)
@commandWrap
def FlowPathObjectOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FlowPathObjectOptions(*args, **kwargs)
@commandWrap
def viewHeadOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.viewHeadOn(*args, **kwargs)
@commandWrap
def mrMapVisualizer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mrMapVisualizer(*args, **kwargs)
@commandWrap
def SetMeshAmplifyTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshAmplifyTool(*args, **kwargs)
@commandWrap
def sbs_GoToMarketPlace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GoToMarketPlace(*args, **kwargs)
@commandWrap
def DeleteAllFurs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllFurs(*args, **kwargs)
@commandWrap
def VertexNormalEditTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.VertexNormalEditTool(*args, **kwargs)
@commandWrap
def HideIKHandles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideIKHandles(*args, **kwargs)
@commandWrap
def SelectHullsMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectHullsMask(*args, **kwargs)
@commandWrap
def renderWindowSelectContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderWindowSelectContext(*args, **kwargs)
@commandWrap
def dR_showAbout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_showAbout(*args, **kwargs)
@commandWrap
def addDynamicAttribute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.addDynamicAttribute(*args, **kwargs)
@commandWrap
def error(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.error(*args, **kwargs)
@commandWrap
def WireDropoffLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WireDropoffLocator(*args, **kwargs)
@commandWrap
def setDynamicsInitialState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setDynamicsInitialState(*args, **kwargs)
@commandWrap
def HypershadeConvertPSDToFileTexture(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeConvertPSDToFileTexture(*args, **kwargs)
@commandWrap
def ResetTransformations(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetTransformations(*args, **kwargs)
@commandWrap
def DeleteAllImagePlanes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllImagePlanes(*args, **kwargs)
@commandWrap
def CurveFlowOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveFlowOptions(*args, **kwargs)
@commandWrap
def DopeSheetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DopeSheetEditor(*args, **kwargs)
@commandWrap
def GridUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GridUV(*args, **kwargs)
@commandWrap
def displayCull(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayCull(*args, **kwargs)
@commandWrap
def xgmMakeGuideDynamic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmMakeGuideDynamic(*args, **kwargs)
@commandWrap
def CVHardness(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CVHardness(*args, **kwargs)
@commandWrap
def CreatePolygonTorusOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonTorusOptions(*args, **kwargs)
@commandWrap
def xgmCreateSplineDescription(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCreateSplineDescription(*args, **kwargs)
@commandWrap
def TimeEditorCreateOverrideLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreateOverrideLayer(*args, **kwargs)
@commandWrap
def RenderLayerRelationshipEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderLayerRelationshipEditor(*args, **kwargs)
@commandWrap
def dR_modePoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_modePoly(*args, **kwargs)
@commandWrap
def NURBSSmoothnessMedium(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessMedium(*args, **kwargs)
@commandWrap
def polyForceUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyForceUV(*args, **kwargs)
@commandWrap
def SelectEdgeLoop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectEdgeLoop(*args, **kwargs)
@commandWrap
def PlaybackBackward(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PlaybackBackward(*args, **kwargs)
@commandWrap
def cMuscleRayIntersect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleRayIntersect(*args, **kwargs)
@commandWrap
def XgmSetWidthBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetWidthBrushToolOption(*args, **kwargs)
@commandWrap
def polyPyramid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPyramid(*args, **kwargs)
@commandWrap
def PolyExtrudeFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrudeFaces(*args, **kwargs)
@commandWrap
def alignCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.alignCtx(*args, **kwargs)
@commandWrap
def paint3d(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.paint3d(*args, **kwargs)
@commandWrap
def FBXImportCameras(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportCameras(*args, **kwargs)
@commandWrap
def geometryDeleteCacheFramesOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryDeleteCacheFramesOpt(*args, **kwargs)
@commandWrap
def GetProperty2StateAttrNameFromHIKEffectorId(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetProperty2StateAttrNameFromHIKEffectorId(*args, **kwargs)
@commandWrap
def RemoveSubdivProxyMirrorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveSubdivProxyMirrorOptions(*args, **kwargs)
@commandWrap
def ToggleFocalLength(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFocalLength(*args, **kwargs)
@commandWrap
def HypershadeRevertToDefaultTabs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRevertToDefaultTabs(*args, **kwargs)
@commandWrap
def greaseRenderPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.greaseRenderPlane(*args, **kwargs)
@commandWrap
def polyCutUVCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCutUVCtx(*args, **kwargs)
@commandWrap
def HideLattices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideLattices(*args, **kwargs)
@commandWrap
def extrude(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.extrude(*args, **kwargs)
@commandWrap
def CreateMotionTrail(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateMotionTrail(*args, **kwargs)
@commandWrap
def nucleusGetnParticleExample(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusGetnParticleExample(*args, **kwargs)
@commandWrap
def CreatePolygonSoccerBall(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonSoccerBall(*args, **kwargs)
@commandWrap
def convertUnit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.convertUnit(*args, **kwargs)
@commandWrap
def GLSLShader(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GLSLShader(*args, **kwargs)
@commandWrap
def SetKeyTranslate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetKeyTranslate(*args, **kwargs)
@commandWrap
def CreateSpring(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSpring(*args, **kwargs)
@commandWrap
def PaintOnPaintableObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintOnPaintableObjects(*args, **kwargs)
@commandWrap
def camera(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.camera(*args, **kwargs)
@commandWrap
def HypershadeCloseActiveTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeCloseActiveTab(*args, **kwargs)
@commandWrap
def createPolyPyramidCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyPyramidCtx(*args, **kwargs)
@commandWrap
def nexTRSContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexTRSContext(*args, **kwargs)
@commandWrap
def BrushAnimationMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushAnimationMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def SnapToPixel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToPixel(*args, **kwargs)
@commandWrap
def dR_connectTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_connectTool(*args, **kwargs)
@commandWrap
def IncreaseGammaFine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IncreaseGammaFine(*args, **kwargs)
@commandWrap
def ToggleFkIk(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFkIk(*args, **kwargs)
@commandWrap
def FBXExportSplitAnimationIntoTakes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportSplitAnimationIntoTakes(*args, **kwargs)
@commandWrap
def sampleImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sampleImage(*args, **kwargs)
@commandWrap
def ctxCompletion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ctxCompletion(*args, **kwargs)
@commandWrap
def dR_increaseManipSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_increaseManipSize(*args, **kwargs)
@commandWrap
def OutlinerCollapseAllItems(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerCollapseAllItems(*args, **kwargs)
@commandWrap
def TensionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TensionOptions(*args, **kwargs)
@commandWrap
def isDirty(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.isDirty(*args, **kwargs)
@commandWrap
def StraightenUVBorderOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StraightenUVBorderOptions(*args, **kwargs)
@commandWrap
def createNurbsCircleCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsCircleCtx(*args, **kwargs)
@commandWrap
def PaintEffectsMeshQuality(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsMeshQuality(*args, **kwargs)
@commandWrap
def UniversalManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UniversalManip(*args, **kwargs)
@commandWrap
def FBXImportAudio(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportAudio(*args, **kwargs)
@commandWrap
def soloMaterial(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.soloMaterial(*args, **kwargs)
@commandWrap
def CollapseSubdivSurfaceHierarchyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CollapseSubdivSurfaceHierarchyOptions(*args, **kwargs)
@commandWrap
def ToggleCompIDs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCompIDs(*args, **kwargs)
@commandWrap
def SetMeshMaskTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshMaskTool(*args, **kwargs)
@commandWrap
def setKeyframeBlendshapeTargetWts(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setKeyframeBlendshapeTargetWts(*args, **kwargs)
@commandWrap
def CurlCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurlCurves(*args, **kwargs)
@commandWrap
def SubdivSmoothnessFine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessFine(*args, **kwargs)
@commandWrap
def softSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.softSelect(*args, **kwargs)
@commandWrap
def polyBlendColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyBlendColor(*args, **kwargs)
@commandWrap
def fluidDeleteCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidDeleteCacheOpt(*args, **kwargs)
@commandWrap
def TimeEditorCreatePoseClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorCreatePoseClip(*args, **kwargs)
@commandWrap
def SetFullBodyIKKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFullBodyIKKeys(*args, **kwargs)
@commandWrap
def AlembicExportSelectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicExportSelectionOptions(*args, **kwargs)
@commandWrap
def DeleteEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteEdge(*args, **kwargs)
@commandWrap
def ShowMeshKnifeToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshKnifeToolOptions(*args, **kwargs)
@commandWrap
def effector(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.effector(*args, **kwargs)
@commandWrap
def dR_slideSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_slideSurface(*args, **kwargs)
@commandWrap
def devicePanel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.devicePanel(*args, **kwargs)
@commandWrap
def SelectAllBrushes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllBrushes(*args, **kwargs)
@commandWrap
def StitchTogetherOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StitchTogetherOptions(*args, **kwargs)
@commandWrap
def dR_mtkToolTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_mtkToolTGL(*args, **kwargs)
@commandWrap
def CVCurveToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CVCurveToolOptions(*args, **kwargs)
@commandWrap
def ExtractSubdivSurfaceVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtractSubdivSurfaceVertices(*args, **kwargs)
@commandWrap
def PaintOnViewPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintOnViewPlane(*args, **kwargs)
@commandWrap
def nSoft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nSoft(*args, **kwargs)
@commandWrap
def polySelectCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySelectCtx(*args, **kwargs)
@commandWrap
def dR_activeHandleZ(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_activeHandleZ(*args, **kwargs)
@commandWrap
def dR_activeHandleY(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_activeHandleY(*args, **kwargs)
@commandWrap
def dR_activeHandleX(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_activeHandleX(*args, **kwargs)
@commandWrap
def BendCurvesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BendCurvesOptions(*args, **kwargs)
@commandWrap
def AlignCameraToPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlignCameraToPolygon(*args, **kwargs)
@commandWrap
def LatticeDeformKeysTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LatticeDeformKeysTool(*args, **kwargs)
@commandWrap
def timeEditorAnimSource(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorAnimSource(*args, **kwargs)
@commandWrap
def HypershadeToggleAttrFilter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleAttrFilter(*args, **kwargs)
@commandWrap
def FBXExportTangents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportTangents(*args, **kwargs)
@commandWrap
def CurveFilletOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveFilletOptions(*args, **kwargs)
@commandWrap
def particleRenderInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.particleRenderInfo(*args, **kwargs)
@commandWrap
def cMuscleAbout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleAbout(*args, **kwargs)
@commandWrap
def sbs_GetGlobalTextureHeight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetGlobalTextureHeight(*args, **kwargs)
@commandWrap
def createPolyConeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyConeCtx(*args, **kwargs)
@commandWrap
def PostInfinityCycle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PostInfinityCycle(*args, **kwargs)
@commandWrap
def ChangeNormalSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ChangeNormalSize(*args, **kwargs)
@commandWrap
def polyOutput(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyOutput(*args, **kwargs)
@commandWrap
def disable(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.disable(*args, **kwargs)
@commandWrap
def FireOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FireOptions(*args, **kwargs)
@commandWrap
def TimeEditorGhostTrackToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorGhostTrackToggle(*args, **kwargs)
@commandWrap
def format(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.format(*args, **kwargs)
@commandWrap
def swatchRefresh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.swatchRefresh(*args, **kwargs)
@commandWrap
def PickWalkUp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkUp(*args, **kwargs)
@commandWrap
def CreateSubdivCone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivCone(*args, **kwargs)
@commandWrap
def attributeName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attributeName(*args, **kwargs)
@commandWrap
def OptimzeUVsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OptimzeUVsOptions(*args, **kwargs)
@commandWrap
def Air(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Air(*args, **kwargs)
@commandWrap
def ToggleKeepWireCulling(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleKeepWireCulling(*args, **kwargs)
@commandWrap
def CreateBezierCurveToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateBezierCurveToolOptions(*args, **kwargs)
@commandWrap
def texSculptCacheSync(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texSculptCacheSync(*args, **kwargs)
@commandWrap
def CreateExpressionClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateExpressionClip(*args, **kwargs)
@commandWrap
def AddBoatLocatorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBoatLocatorOptions(*args, **kwargs)
@commandWrap
def groupParts(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.groupParts(*args, **kwargs)
@commandWrap
def xgmBrushManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmBrushManip(*args, **kwargs)
@commandWrap
def SelectTimeWarp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectTimeWarp(*args, **kwargs)
@commandWrap
def TexSculptActivateBrushSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TexSculptActivateBrushSize(*args, **kwargs)
@commandWrap
def HypershadeAutoSizeNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeAutoSizeNodes(*args, **kwargs)
@commandWrap
def dR_scalePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_scalePress(*args, **kwargs)
@commandWrap
def CreateNURBSTorusOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSTorusOptions(*args, **kwargs)
@commandWrap
def preferredRenderer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.preferredRenderer(*args, **kwargs)
@commandWrap
def xgmCutBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCutBrushToolCmd(*args, **kwargs)
@commandWrap
def SetFullBodyIKKeysKeyToPin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFullBodyIKKeysKeyToPin(*args, **kwargs)
@commandWrap
def DeleteTimeWarp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteTimeWarp(*args, **kwargs)
@commandWrap
def MergeUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeUV(*args, **kwargs)
@commandWrap
def buildBookmarkMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.buildBookmarkMenu(*args, **kwargs)
@commandWrap
def affectedNet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.affectedNet(*args, **kwargs)
@commandWrap
def dynPaintCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynPaintCtx(*args, **kwargs)
@commandWrap
def SymmetrizeUVOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SymmetrizeUVOptions(*args, **kwargs)
@commandWrap
def SinglePerspectiveViewLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SinglePerspectiveViewLayout(*args, **kwargs)
@commandWrap
def ExtrudeVertexOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtrudeVertexOptions(*args, **kwargs)
@commandWrap
def AddKeysTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddKeysTool(*args, **kwargs)
@commandWrap
def SubdivSmoothnessHullOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessHullOptions(*args, **kwargs)
@commandWrap
def EmitFromObjectOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EmitFromObjectOptions(*args, **kwargs)
@commandWrap
def HypershadeShowDirectoriesOnly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShowDirectoriesOnly(*args, **kwargs)
@commandWrap
def AddSelectionAsTargetShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddSelectionAsTargetShapeOptions(*args, **kwargs)
@commandWrap
def createNurbsTorusCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsTorusCtx(*args, **kwargs)
@commandWrap
def hikCustomRigToolWidget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikCustomRigToolWidget(*args, **kwargs)
@commandWrap
def TwistOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TwistOptions(*args, **kwargs)
@commandWrap
def MoveUVTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveUVTool(*args, **kwargs)
@commandWrap
def ConvertToBreakdown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertToBreakdown(*args, **kwargs)
@commandWrap
def DisableMemoryCaching(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableMemoryCaching(*args, **kwargs)
@commandWrap
def spring(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.spring(*args, **kwargs)
@commandWrap
def PolyMergeEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyMergeEdges(*args, **kwargs)
@commandWrap
def propModCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.propModCtx(*args, **kwargs)
@commandWrap
def marker(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.marker(*args, **kwargs)
@commandWrap
def TogglePanelMenubar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePanelMenubar(*args, **kwargs)
@commandWrap
def SmoothProxy(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothProxy(*args, **kwargs)
@commandWrap
def loadModule(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.loadModule(*args, **kwargs)
@commandWrap
def InitialFluidStatesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InitialFluidStatesOptions(*args, **kwargs)
@commandWrap
def NodeEditorGraphRemoveUnselected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphRemoveUnselected(*args, **kwargs)
@commandWrap
def polyEditUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyEditUV(*args, **kwargs)
@commandWrap
def PaintRandom(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintRandom(*args, **kwargs)
@commandWrap
def ReversePolygonNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReversePolygonNormals(*args, **kwargs)
@commandWrap
def xgmBakeGuideVertices(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmBakeGuideVertices(*args, **kwargs)
@commandWrap
def ToggleCameraNames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCameraNames(*args, **kwargs)
@commandWrap
def scale(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scale(*args, **kwargs)
@commandWrap
def Redo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Redo(*args, **kwargs)
@commandWrap
def xgmDirectionBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmDirectionBrushToolCmd(*args, **kwargs)
@commandWrap
def CreateShrinkWrapOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateShrinkWrapOptions(*args, **kwargs)
@commandWrap
def affects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.affects(*args, **kwargs)
@commandWrap
def LODGenerateMeshes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LODGenerateMeshes(*args, **kwargs)
@commandWrap
def softModContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.softModContext(*args, **kwargs)
@commandWrap
def graphDollyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.graphDollyCtx(*args, **kwargs)
@commandWrap
def inheritTransform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.inheritTransform(*args, **kwargs)
@commandWrap
def toggleAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.toggleAxis(*args, **kwargs)
@commandWrap
def dropoffLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dropoffLocator(*args, **kwargs)
@commandWrap
def DeleteAllRigidConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllRigidConstraints(*args, **kwargs)
@commandWrap
def CreateBezierCurveTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateBezierCurveTool(*args, **kwargs)
@commandWrap
def SetPreferredAngleOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetPreferredAngleOptions(*args, **kwargs)
@commandWrap
def evalDeferred(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.evalDeferred(*args, **kwargs)
@commandWrap
def nucleusDisplayTextureNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusDisplayTextureNodes(*args, **kwargs)
@commandWrap
def nurbsSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsSelect(*args, **kwargs)
@commandWrap
def geometryDeleteCacheFrames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryDeleteCacheFrames(*args, **kwargs)
@commandWrap
def SelectPreviousObjects3dsMax(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectPreviousObjects3dsMax(*args, **kwargs)
@commandWrap
def SelectAllNCloths(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllNCloths(*args, **kwargs)
@commandWrap
def xgmWidthBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmWidthBrushToolCmd(*args, **kwargs)
@commandWrap
def furClosestFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.furClosestFace(*args, **kwargs)
@commandWrap
def NodeEditorConnectNodeOnCreation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorConnectNodeOnCreation(*args, **kwargs)
@commandWrap
def GetFluidExample(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetFluidExample(*args, **kwargs)
@commandWrap
def SetActiveKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetActiveKey(*args, **kwargs)
@commandWrap
def SetInitialState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetInitialState(*args, **kwargs)
@commandWrap
def PaintGrid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintGrid(*args, **kwargs)
@commandWrap
def SelectAllGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllGeometry(*args, **kwargs)
@commandWrap
def CreateNURBSCircleOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSCircleOptions(*args, **kwargs)
@commandWrap
def WrinkleToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WrinkleToolOptions(*args, **kwargs)
@commandWrap
def bulletAlignRigidBody(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bulletAlignRigidBody(*args, **kwargs)
@commandWrap
def insertKnotSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.insertKnotSurface(*args, **kwargs)
@commandWrap
def dR_multiCutTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_multiCutTool(*args, **kwargs)
@commandWrap
def ToggleProxyDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleProxyDisplay(*args, **kwargs)
@commandWrap
def MergeUVOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeUVOptions(*args, **kwargs)
@commandWrap
def NCreateEmitterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NCreateEmitterOptions(*args, **kwargs)
@commandWrap
def WeightedTangents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WeightedTangents(*args, **kwargs)
@commandWrap
def ParentBaseWire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParentBaseWire(*args, **kwargs)
@commandWrap
def PolygonCopyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonCopyOptions(*args, **kwargs)
@commandWrap
def xgmPlaceBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPlaceBrushToolCmd(*args, **kwargs)
@commandWrap
def PaintSetMembershipToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintSetMembershipToolOptions(*args, **kwargs)
@commandWrap
def filterStudioImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.filterStudioImport(*args, **kwargs)
@commandWrap
def CreateNURBSSquareOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSSquareOptions(*args, **kwargs)
@commandWrap
def dynGlobals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynGlobals(*args, **kwargs)
@commandWrap
def PickWalkStopAtTransform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkStopAtTransform(*args, **kwargs)
@commandWrap
def dR_softSelDistanceTypeVolume(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_softSelDistanceTypeVolume(*args, **kwargs)
@commandWrap
def SelectEdgeMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectEdgeMask(*args, **kwargs)
@commandWrap
def artSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artSelect(*args, **kwargs)
@commandWrap
def texMoveContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texMoveContext(*args, **kwargs)
@commandWrap
def SubdivSurfacePolygonProxyMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSurfacePolygonProxyMode(*args, **kwargs)
@commandWrap
def XgmSplineCacheDeleteNodesAhead(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheDeleteNodesAhead(*args, **kwargs)
@commandWrap
def manipRotateLimitsCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipRotateLimitsCtx(*args, **kwargs)
@commandWrap
def ogsRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ogsRender(*args, **kwargs)
@commandWrap
def ResolveInterpenetration(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResolveInterpenetration(*args, **kwargs)
@commandWrap
def PickWalkOut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkOut(*args, **kwargs)
@commandWrap
def PreviousGreasePencilFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreviousGreasePencilFrame(*args, **kwargs)
@commandWrap
def polyTriangulate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyTriangulate(*args, **kwargs)
@commandWrap
def polyPoke(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPoke(*args, **kwargs)
@commandWrap
def ModifyUVVectorPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyUVVectorPress(*args, **kwargs)
@commandWrap
def FBXExportUseSceneName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportUseSceneName(*args, **kwargs)
@commandWrap
def ProfilerToolHideSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolHideSelected(*args, **kwargs)
@commandWrap
def rigidSolver(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rigidSolver(*args, **kwargs)
@commandWrap
def SmoothBindSkin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothBindSkin(*args, **kwargs)
@commandWrap
def ResetLattice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetLattice(*args, **kwargs)
@commandWrap
def AssignTemplate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignTemplate(*args, **kwargs)
@commandWrap
def dR_pointSnapPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_pointSnapPress(*args, **kwargs)
@commandWrap
def SurfaceBooleanIntersectTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceBooleanIntersectTool(*args, **kwargs)
@commandWrap
def curveAddPtCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveAddPtCtx(*args, **kwargs)
@commandWrap
def CloseFrontWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CloseFrontWindow(*args, **kwargs)
@commandWrap
def CreateCameraOnly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCameraOnly(*args, **kwargs)
@commandWrap
def nClothCreate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothCreate(*args, **kwargs)
@commandWrap
def XgmSplinePresetExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplinePresetExport(*args, **kwargs)
@commandWrap
def ToggleChannelBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleChannelBox(*args, **kwargs)
@commandWrap
def SelectAllClusters(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllClusters(*args, **kwargs)
@commandWrap
def FBXUIShowOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXUIShowOptions(*args, **kwargs)
@commandWrap
def BreakRigidBodyConnection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BreakRigidBodyConnection(*args, **kwargs)
@commandWrap
def CreateShot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateShot(*args, **kwargs)
@commandWrap
def ExpandSelectedComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExpandSelectedComponents(*args, **kwargs)
@commandWrap
def PolyCreaseToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyCreaseToolOptions(*args, **kwargs)
@commandWrap
def Drag(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Drag(*args, **kwargs)
@commandWrap
def dR_extrudePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_extrudePress(*args, **kwargs)
@commandWrap
def ExtrudeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtrudeEdge(*args, **kwargs)
@commandWrap
def CreateNURBSSphere(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSSphere(*args, **kwargs)
@commandWrap
def MakeBoats(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeBoats(*args, **kwargs)
@commandWrap
def TransplantHair(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransplantHair(*args, **kwargs)
@commandWrap
def dagObjectHit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dagObjectHit(*args, **kwargs)
@commandWrap
def AddSelectionAsInBetweenTargetShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddSelectionAsInBetweenTargetShapeOptions(*args, **kwargs)
@commandWrap
def psdEditTextureFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.psdEditTextureFile(*args, **kwargs)
@commandWrap
def ShowStrokeControlCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowStrokeControlCurves(*args, **kwargs)
@commandWrap
def MergeMultipleEdgesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeMultipleEdgesOptions(*args, **kwargs)
@commandWrap
def LatticeUVToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LatticeUVToolOptions(*args, **kwargs)
@commandWrap
def CreateOceanWakeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateOceanWakeOptions(*args, **kwargs)
@commandWrap
def RotateToolMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateToolMarkingMenu(*args, **kwargs)
@commandWrap
def OneClickSetCallback(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickSetCallback(*args, **kwargs)
@commandWrap
def subgraph(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subgraph(*args, **kwargs)
@commandWrap
def artAttrSkinPaint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artAttrSkinPaint(*args, **kwargs)
@commandWrap
def bezierAnchorPreset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bezierAnchorPreset(*args, **kwargs)
@commandWrap
def HypershadeOpenOutlinerWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenOutlinerWindow(*args, **kwargs)
@commandWrap
def CreateCreaseSetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCreaseSetOptions(*args, **kwargs)
@commandWrap
def flexor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.flexor(*args, **kwargs)
@commandWrap
def NodeEditorToggleZoomOut(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleZoomOut(*args, **kwargs)
@commandWrap
def dR_contextChanged(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_contextChanged(*args, **kwargs)
@commandWrap
def NodeEditorShapeMenuStateAllExceptShadingGroupMembers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorShapeMenuStateAllExceptShadingGroupMembers(*args, **kwargs)
@commandWrap
def PolygonApplyColorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonApplyColorOptions(*args, **kwargs)
@commandWrap
def texWinToolCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texWinToolCtx(*args, **kwargs)
@commandWrap
def CreatePolygonPyramid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPyramid(*args, **kwargs)
@commandWrap
def xgmCurveToGuide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCurveToGuide(*args, **kwargs)
@commandWrap
def shadingLightRelCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shadingLightRelCtx(*args, **kwargs)
@commandWrap
def bevel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bevel(*args, **kwargs)
@commandWrap
def HypershadeOpenPropertyEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenPropertyEditorWindow(*args, **kwargs)
@commandWrap
def selectMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selectMode(*args, **kwargs)
@commandWrap
def MakePondMotorBoatsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakePondMotorBoatsOptions(*args, **kwargs)
@commandWrap
def SquareSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SquareSurfaceOptions(*args, **kwargs)
@commandWrap
def xgmDirectionBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmDirectionBrushContext(*args, **kwargs)
@commandWrap
def TwoPointArcToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TwoPointArcToolOptions(*args, **kwargs)
@commandWrap
def textureWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.textureWindow(*args, **kwargs)
@commandWrap
def SmoothSkinWeightsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothSkinWeightsOptions(*args, **kwargs)
@commandWrap
def reorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reorder(*args, **kwargs)
@commandWrap
def RemoveFromCharacterSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveFromCharacterSet(*args, **kwargs)
@commandWrap
def polyTorus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyTorus(*args, **kwargs)
@commandWrap
def HypershadeRefreshSelectedSwatchesOnDisk(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRefreshSelectedSwatchesOnDisk(*args, **kwargs)
@commandWrap
def TangentsLinear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsLinear(*args, **kwargs)
@commandWrap
def SmoothingDisplayToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothingDisplayToggle(*args, **kwargs)
@commandWrap
def deviceEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deviceEditor(*args, **kwargs)
@commandWrap
def TimeEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorWindow(*args, **kwargs)
@commandWrap
def CreateExpressionClipOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateExpressionClipOptions(*args, **kwargs)
@commandWrap
def SewUVsWithoutHotkey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SewUVsWithoutHotkey(*args, **kwargs)
@commandWrap
def SelectComponentToolMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectComponentToolMarkingMenu(*args, **kwargs)
@commandWrap
def BifMeshImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BifMeshImport(*args, **kwargs)
@commandWrap
def RebuildSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RebuildSurfacesOptions(*args, **kwargs)
@commandWrap
def dR_selectModeTweakMarquee(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectModeTweakMarquee(*args, **kwargs)
@commandWrap
def PaintVertexColorToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintVertexColorToolOptions(*args, **kwargs)
@commandWrap
def MakeHoleToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeHoleToolOptions(*args, **kwargs)
@commandWrap
def warning(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.warning(*args, **kwargs)
@commandWrap
def skinBindCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.skinBindCtx(*args, **kwargs)
@commandWrap
def keyframeRegionSetKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionSetKeyCtx(*args, **kwargs)
@commandWrap
def FireworksOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FireworksOptions(*args, **kwargs)
@commandWrap
def TimeEditorToggleSoloSelectedTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorToggleSoloSelectedTracks(*args, **kwargs)
@commandWrap
def rampColorPort(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rampColorPort(*args, **kwargs)
@commandWrap
def TogglePolyUVsCreateShader(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyUVsCreateShader(*args, **kwargs)
@commandWrap
def clipEditorCurrentTimeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clipEditorCurrentTimeCtx(*args, **kwargs)
@commandWrap
def LayoutUVAlongOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LayoutUVAlongOptions(*args, **kwargs)
@commandWrap
def DeleteAllJoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllJoints(*args, **kwargs)
@commandWrap
def DeleteChannelsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteChannelsOptions(*args, **kwargs)
@commandWrap
def fluidMergeCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidMergeCacheOpt(*args, **kwargs)
@commandWrap
def CreateBlendShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateBlendShapeOptions(*args, **kwargs)
@commandWrap
def isDescendentPulling(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.isDescendentPulling(*args, **kwargs)
@commandWrap
def keyframeRegionInsertKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionInsertKeyCtx(*args, **kwargs)
@commandWrap
def SendToUnitySetProject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendToUnitySetProject(*args, **kwargs)
@commandWrap
def MergeVertexTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeVertexTool(*args, **kwargs)
@commandWrap
def MoveSkinJointsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveSkinJointsTool(*args, **kwargs)
@commandWrap
def fitBspline(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fitBspline(*args, **kwargs)
@commandWrap
def ReverseSurfaceDirection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReverseSurfaceDirection(*args, **kwargs)
@commandWrap
def MoveInfluence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveInfluence(*args, **kwargs)
@commandWrap
def SnapToMeshCenter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToMeshCenter(*args, **kwargs)
@commandWrap
def deviceManager(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deviceManager(*args, **kwargs)
@commandWrap
def CreatePolygonPlatonic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPlatonic(*args, **kwargs)
@commandWrap
def sbs_GetAllInputsFromSubstanceNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetAllInputsFromSubstanceNode(*args, **kwargs)
@commandWrap
def xgmRebuildSplineDescription(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmRebuildSplineDescription(*args, **kwargs)
@commandWrap
def InteractivePlayback(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InteractivePlayback(*args, **kwargs)
@commandWrap
def XgmSetCombBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetCombBrushToolOption(*args, **kwargs)
@commandWrap
def keyframeStats(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeStats(*args, **kwargs)
@commandWrap
def FBXImportProtectDrivenKeys(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportProtectDrivenKeys(*args, **kwargs)
@commandWrap
def NURBSSmoothnessHull(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessHull(*args, **kwargs)
@commandWrap
def HypershadeShapeMenuStateAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShapeMenuStateAll(*args, **kwargs)
@commandWrap
def RemoveShrinkWrapTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveShrinkWrapTarget(*args, **kwargs)
@commandWrap
def AverageVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AverageVertex(*args, **kwargs)
@commandWrap
def ProfilerToolShowAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolShowAll(*args, **kwargs)
@commandWrap
def expressionEditorListen(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.expressionEditorListen(*args, **kwargs)
@commandWrap
def HypershadeToggleZoomIn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleZoomIn(*args, **kwargs)
@commandWrap
def currentTimeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.currentTimeCtx(*args, **kwargs)
@commandWrap
def adskAsset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.adskAsset(*args, **kwargs)
@commandWrap
def NodeEditorGraphRemoveUpstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphRemoveUpstream(*args, **kwargs)
@commandWrap
def wrinkle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.wrinkle(*args, **kwargs)
@commandWrap
def MoveNearestPickedKeyToolActivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveNearestPickedKeyToolActivate(*args, **kwargs)
@commandWrap
def InteractiveSplitTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InteractiveSplitTool(*args, **kwargs)
@commandWrap
def ConvertSelectionToShell(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToShell(*args, **kwargs)
@commandWrap
def sceneUIReplacement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sceneUIReplacement(*args, **kwargs)
@commandWrap
def polyBevel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyBevel(*args, **kwargs)
@commandWrap
def dbfootprint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dbfootprint(*args, **kwargs)
@commandWrap
def FBXExportBakeComplexAnimation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportBakeComplexAnimation(*args, **kwargs)
@commandWrap
def dgcontrol(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgcontrol(*args, **kwargs)
@commandWrap
def xgmSetAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSetAttr(*args, **kwargs)
@commandWrap
def orbit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.orbit(*args, **kwargs)
@commandWrap
def renderSetupPostApply(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetupPostApply(*args, **kwargs)
@commandWrap
def defineDataServer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.defineDataServer(*args, **kwargs)
@commandWrap
def cMuscleQuery(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleQuery(*args, **kwargs)
@commandWrap
def MergeVerticesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeVerticesOptions(*args, **kwargs)
@commandWrap
def ShowDynamicsUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowDynamicsUI(*args, **kwargs)
@commandWrap
def FrameSelectedWithoutChildrenInAllViews(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FrameSelectedWithoutChildrenInAllViews(*args, **kwargs)
@commandWrap
def NURBSToPolygonsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSToPolygonsOptions(*args, **kwargs)
@commandWrap
def InsertIsoparmsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertIsoparmsOptions(*args, **kwargs)
@commandWrap
def polyGear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyGear(*args, **kwargs)
@commandWrap
def requires(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.requires(*args, **kwargs)
@commandWrap
def attachSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attachSurface(*args, **kwargs)
@commandWrap
def FBXImportMergeBackNullPivots(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportMergeBackNullPivots(*args, **kwargs)
@commandWrap
def SelectEdgeRingSp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectEdgeRingSp(*args, **kwargs)
@commandWrap
def dgdebug(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dgdebug(*args, **kwargs)
@commandWrap
def FBXImportUnlockNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportUnlockNormals(*args, **kwargs)
@commandWrap
def geometryExportCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryExportCache(*args, **kwargs)
@commandWrap
def detachCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.detachCurve(*args, **kwargs)
@commandWrap
def polyMergeFacetCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMergeFacetCtx(*args, **kwargs)
@commandWrap
def ParticleCollisionEvents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParticleCollisionEvents(*args, **kwargs)
@commandWrap
def stitchSurfaceCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stitchSurfaceCtx(*args, **kwargs)
@commandWrap
def toggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.toggle(*args, **kwargs)
@commandWrap
def HypershadeGraphUpDownstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphUpDownstream(*args, **kwargs)
@commandWrap
def volumeAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.volumeAxis(*args, **kwargs)
@commandWrap
def dR_customPivotToolPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_customPivotToolPress(*args, **kwargs)
@commandWrap
def itemFilterRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.itemFilterRender(*args, **kwargs)
@commandWrap
def SoftModToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SoftModToolOptions(*args, **kwargs)
@commandWrap
def HypershadeShapeMenuStateAllExceptShadingGroupMembers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShapeMenuStateAllExceptShadingGroupMembers(*args, **kwargs)
@commandWrap
def DragOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DragOptions(*args, **kwargs)
@commandWrap
def ScaleToolMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleToolMarkingMenu(*args, **kwargs)
@commandWrap
def DeleteAllChannels(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllChannels(*args, **kwargs)
@commandWrap
def Parent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Parent(*args, **kwargs)
@commandWrap
def PaintEffectsGlobalSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsGlobalSettings(*args, **kwargs)
@commandWrap
def BevelPlus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BevelPlus(*args, **kwargs)
@commandWrap
def HypershadeDisplayAsExtraLargeSwatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayAsExtraLargeSwatches(*args, **kwargs)
@commandWrap
def GPUBuiltInDeformerControl(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GPUBuiltInDeformerControl(*args, **kwargs)
@commandWrap
def PolygonClearClipboardOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonClearClipboardOptions(*args, **kwargs)
@commandWrap
def getFileList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getFileList(*args, **kwargs)
@commandWrap
def ShowAllPolyComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowAllPolyComponents(*args, **kwargs)
@commandWrap
def polyPrimitiveMisc(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPrimitiveMisc(*args, **kwargs)
@commandWrap
def HypershadeDeleteDuplicateShadingNetworks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteDuplicateShadingNetworks(*args, **kwargs)
@commandWrap
def polyCone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCone(*args, **kwargs)
@commandWrap
def OutTangentClamped(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutTangentClamped(*args, **kwargs)
@commandWrap
def RemoveSubdivProxyMirror(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveSubdivProxyMirror(*args, **kwargs)
@commandWrap
def polySplitEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySplitEdge(*args, **kwargs)
@commandWrap
def jointDisplayScale(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.jointDisplayScale(*args, **kwargs)
@commandWrap
def FluidEmitterOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FluidEmitterOptions(*args, **kwargs)
@commandWrap
def ToggleSoftEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSoftEdges(*args, **kwargs)
@commandWrap
def regionSelectKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.regionSelectKeyCtx(*args, **kwargs)
@commandWrap
def querySubdiv(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.querySubdiv(*args, **kwargs)
@commandWrap
def DefaultQualityDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DefaultQualityDisplay(*args, **kwargs)
@commandWrap
def SelectAllMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllMarkingMenu(*args, **kwargs)
@commandWrap
def XgGroomingVis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgGroomingVis(*args, **kwargs)
@commandWrap
def NodeEditorRenameActiveTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorRenameActiveTab(*args, **kwargs)
@commandWrap
def XgmSplineCacheExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheExport(*args, **kwargs)
@commandWrap
def FBXExportSmoothMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportSmoothMesh(*args, **kwargs)
@commandWrap
def OrientJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OrientJoint(*args, **kwargs)
@commandWrap
def rollCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rollCtx(*args, **kwargs)
@commandWrap
def SnapToPointRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToPointRelease(*args, **kwargs)
@commandWrap
def SetMeshEraseTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshEraseTool(*args, **kwargs)
@commandWrap
def SquareSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SquareSurface(*args, **kwargs)
@commandWrap
def dR_overlayAppendMeshTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_overlayAppendMeshTGL(*args, **kwargs)
@commandWrap
def PreInfinityCycle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreInfinityCycle(*args, **kwargs)
@commandWrap
def PaintSetMembershipTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintSetMembershipTool(*args, **kwargs)
@commandWrap
def SetMeshFreezeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshFreezeTool(*args, **kwargs)
@commandWrap
def ModifyLowerRadiusPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyLowerRadiusPress(*args, **kwargs)
@commandWrap
def dR_bridgePress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_bridgePress(*args, **kwargs)
@commandWrap
def getModulePath(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getModulePath(*args, **kwargs)
@commandWrap
def Create2DContainerEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create2DContainerEmitter(*args, **kwargs)
@commandWrap
def Unfold3DuvUpdateCommand(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Unfold3DuvUpdateCommand(*args, **kwargs)
@commandWrap
def CoarseLevelComponentDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CoarseLevelComponentDisplay(*args, **kwargs)
@commandWrap
def RotateUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateUVs(*args, **kwargs)
@commandWrap
def createPolyPrismCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyPrismCtx(*args, **kwargs)
@commandWrap
def CreateLattice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateLattice(*args, **kwargs)
@commandWrap
def BothProxySubdivDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BothProxySubdivDisplay(*args, **kwargs)
@commandWrap
def subdCollapse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdCollapse(*args, **kwargs)
@commandWrap
def GetOceanPondExample(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GetOceanPondExample(*args, **kwargs)
@commandWrap
def keyframeRegionScaleKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionScaleKeyCtx(*args, **kwargs)
@commandWrap
def UVAutomaticProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVAutomaticProjectionOptions(*args, **kwargs)
@commandWrap
def OutlinerUnhide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerUnhide(*args, **kwargs)
@commandWrap
def HypershadeSaveSwatchesToDisk(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSaveSwatchesToDisk(*args, **kwargs)
@commandWrap
def ViewImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ViewImage(*args, **kwargs)
@commandWrap
def ConvertSelectionToContainedEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToContainedEdges(*args, **kwargs)
@commandWrap
def HypergraphDecreaseDepth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypergraphDecreaseDepth(*args, **kwargs)
@commandWrap
def HypershadeShowAllAttrs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeShowAllAttrs(*args, **kwargs)
@commandWrap
def DeleteAllDynamicConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllDynamicConstraints(*args, **kwargs)
@commandWrap
def blendCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.blendCtx(*args, **kwargs)
@commandWrap
def xgmPreview(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPreview(*args, **kwargs)
@commandWrap
def NURBSSmoothnessHullOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessHullOptions(*args, **kwargs)
@commandWrap
def HypershadeFrameSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeFrameSelected(*args, **kwargs)
@commandWrap
def makeSingleSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.makeSingleSurface(*args, **kwargs)
@commandWrap
def BridgeEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BridgeEdge(*args, **kwargs)
@commandWrap
def LatticeDeformKeysToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LatticeDeformKeysToolOptions(*args, **kwargs)
@commandWrap
def ArtPaintSkinWeightsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintSkinWeightsTool(*args, **kwargs)
@commandWrap
def CreateUVShellAlongBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateUVShellAlongBorder(*args, **kwargs)
@commandWrap
def CreateMotionTrailOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateMotionTrailOptions(*args, **kwargs)
@commandWrap
def SelectAllImagePlanes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllImagePlanes(*args, **kwargs)
@commandWrap
def stackTrace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stackTrace(*args, **kwargs)
@commandWrap
def HypershadeOpenModelEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenModelEditorWindow(*args, **kwargs)
@commandWrap
def SurfaceBooleanUnionTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceBooleanUnionTool(*args, **kwargs)
@commandWrap
def AttachSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachSurfacesOptions(*args, **kwargs)
@commandWrap
def dR_renderGlobalsTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_renderGlobalsTGL(*args, **kwargs)
@commandWrap
def Squash(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Squash(*args, **kwargs)
@commandWrap
def DecreaseGammaCoarse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DecreaseGammaCoarse(*args, **kwargs)
@commandWrap
def CreateBlendShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateBlendShape(*args, **kwargs)
@commandWrap
def SubdivSurfaceHierarchyMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSurfaceHierarchyMode(*args, **kwargs)
@commandWrap
def CopyUVsToUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyUVsToUVSet(*args, **kwargs)
@commandWrap
def nexCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexCtx(*args, **kwargs)
@commandWrap
def SelectAllFluids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllFluids(*args, **kwargs)
@commandWrap
def SelectMeshUVShell(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectMeshUVShell(*args, **kwargs)
@commandWrap
def refineSubdivSelectionList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.refineSubdivSelectionList(*args, **kwargs)
@commandWrap
def CreateImagePlaneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateImagePlaneOptions(*args, **kwargs)
@commandWrap
def DuplicateEdgesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateEdgesOptions(*args, **kwargs)
@commandWrap
def dR_paintPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_paintPress(*args, **kwargs)
@commandWrap
def poseEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.poseEditor(*args, **kwargs)
@commandWrap
def EnableGlobalStitch(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableGlobalStitch(*args, **kwargs)
@commandWrap
def polyExtrudeFacet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyExtrudeFacet(*args, **kwargs)
@commandWrap
def polyCube(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCube(*args, **kwargs)
@commandWrap
def DisableSelectedIKHandles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableSelectedIKHandles(*args, **kwargs)
@commandWrap
def SaveSceneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveSceneOptions(*args, **kwargs)
@commandWrap
def StraightenCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StraightenCurves(*args, **kwargs)
@commandWrap
def Create3DContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Create3DContainerOptions(*args, **kwargs)
@commandWrap
def NextGreasePencilFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NextGreasePencilFrame(*args, **kwargs)
@commandWrap
def dR_selectModeMarquee(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectModeMarquee(*args, **kwargs)
@commandWrap
def xgmPolyToGuide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPolyToGuide(*args, **kwargs)
@commandWrap
def XgmSplineCacheReplaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheReplaceOptions(*args, **kwargs)
@commandWrap
def BreakTangent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BreakTangent(*args, **kwargs)
@commandWrap
def NodeEditorShowConnectedAttrs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorShowConnectedAttrs(*args, **kwargs)
@commandWrap
def InTangentFlat(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InTangentFlat(*args, **kwargs)
@commandWrap
def typeManipContextCommand(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.typeManipContextCommand(*args, **kwargs)
@commandWrap
def MirrorPolygonGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorPolygonGeometry(*args, **kwargs)
@commandWrap
def dR_quadDrawPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_quadDrawPress(*args, **kwargs)
@commandWrap
def TextureCentricUVLinkingEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TextureCentricUVLinkingEditor(*args, **kwargs)
@commandWrap
def ExportOfflineFileFromRefEdOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportOfflineFileFromRefEdOptions(*args, **kwargs)
@commandWrap
def WalkTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WalkTool(*args, **kwargs)
@commandWrap
def layeredShaderPort(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.layeredShaderPort(*args, **kwargs)
@commandWrap
def DuplicateSpecial(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateSpecial(*args, **kwargs)
@commandWrap
def CopyUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyUVs(*args, **kwargs)
@commandWrap
def AddBifrostEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostEmitter(*args, **kwargs)
@commandWrap
def FluidGradients(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FluidGradients(*args, **kwargs)
@commandWrap
def CreateShotOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateShotOptions(*args, **kwargs)
@commandWrap
def FBXExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExport(*args, **kwargs)
@commandWrap
def SaveSceneAsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SaveSceneAsOptions(*args, **kwargs)
@commandWrap
def OutlinerDoHide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerDoHide(*args, **kwargs)
@commandWrap
def sbs_GetEnumValue(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetEnumValue(*args, **kwargs)
@commandWrap
def ShowMeshEraseToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshEraseToolOptions(*args, **kwargs)
@commandWrap
def XgmSplineCacheCreate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheCreate(*args, **kwargs)
@commandWrap
def ikSpringSolverRestPose(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikSpringSolverRestPose(*args, **kwargs)
@commandWrap
def TangentsFixed(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangentsFixed(*args, **kwargs)
@commandWrap
def nurbsToPolygonsPref(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsToPolygonsPref(*args, **kwargs)
@commandWrap
def CreateNURBSTorus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSTorus(*args, **kwargs)
@commandWrap
def timeEditorBakeClips(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorBakeClips(*args, **kwargs)
@commandWrap
def redo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.redo(*args, **kwargs)
@commandWrap
def OutlinerToggleAutoExpandLayers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleAutoExpandLayers(*args, **kwargs)
@commandWrap
def fluidEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidEmitter(*args, **kwargs)
@commandWrap
def objectType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.objectType(*args, **kwargs)
@commandWrap
def geometryAppendCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryAppendCache(*args, **kwargs)
@commandWrap
def SimplifyStrokePathCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SimplifyStrokePathCurves(*args, **kwargs)
@commandWrap
def writeTake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.writeTake(*args, **kwargs)
@commandWrap
def attachDeviceAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attachDeviceAttr(*args, **kwargs)
@commandWrap
def hikGlobals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikGlobals(*args, **kwargs)
@commandWrap
def BakeNonDefHistory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeNonDefHistory(*args, **kwargs)
@commandWrap
def ModelingPanelRedoViewChange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModelingPanelRedoViewChange(*args, **kwargs)
@commandWrap
def LoadHIKCharacterState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LoadHIKCharacterState(*args, **kwargs)
@commandWrap
def binMembership(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.binMembership(*args, **kwargs)
@commandWrap
def saveToolSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.saveToolSettings(*args, **kwargs)
@commandWrap
def pointOnSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointOnSurface(*args, **kwargs)
@commandWrap
def duplicate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.duplicate(*args, **kwargs)
@commandWrap
def dynWireCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynWireCtx(*args, **kwargs)
@commandWrap
def polyUVStackSimilarShellsCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUVStackSimilarShellsCmd(*args, **kwargs)
@commandWrap
def getClassification(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getClassification(*args, **kwargs)
@commandWrap
def ShowPolygonSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowPolygonSurfaces(*args, **kwargs)
@commandWrap
def InsertKeyToolActivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertKeyToolActivate(*args, **kwargs)
@commandWrap
def duplicateCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.duplicateCurve(*args, **kwargs)
@commandWrap
def UnfoldUVOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnfoldUVOptions(*args, **kwargs)
@commandWrap
def PasteUVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PasteUVs(*args, **kwargs)
@commandWrap
def FBXImportSetMayaFrameRate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportSetMayaFrameRate(*args, **kwargs)
@commandWrap
def UVCameraBasedProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVCameraBasedProjection(*args, **kwargs)
@commandWrap
def reorderContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reorderContainer(*args, **kwargs)
@commandWrap
def CreatePlatonicSolidOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePlatonicSolidOptions(*args, **kwargs)
@commandWrap
def EvaluationToolkit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EvaluationToolkit(*args, **kwargs)
@commandWrap
def SetRigidBodyCollision(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetRigidBodyCollision(*args, **kwargs)
@commandWrap
def CreateText(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateText(*args, **kwargs)
@commandWrap
def dR_softSelStickyPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_softSelStickyPress(*args, **kwargs)
@commandWrap
def GoToMinFrame(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoToMinFrame(*args, **kwargs)
@commandWrap
def renderSetupLegacyLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderSetupLegacyLayer(*args, **kwargs)
@commandWrap
def ToggleVertexNormalDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleVertexNormalDisplay(*args, **kwargs)
@commandWrap
def bezierCurveToNurbs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bezierCurveToNurbs(*args, **kwargs)
@commandWrap
def mirrorShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mirrorShape(*args, **kwargs)
@commandWrap
def assignViewportFactories(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.assignViewportFactories(*args, **kwargs)
@commandWrap
def CopySelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopySelected(*args, **kwargs)
@commandWrap
def ConvertSelectionToEdgePerimeter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToEdgePerimeter(*args, **kwargs)
@commandWrap
def dbtrace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dbtrace(*args, **kwargs)
@commandWrap
def polyMergeVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMergeVertex(*args, **kwargs)
@commandWrap
def PixelMoveLeft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PixelMoveLeft(*args, **kwargs)
@commandWrap
def ContentBrowserLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ContentBrowserLayout(*args, **kwargs)
@commandWrap
def viewCamera(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.viewCamera(*args, **kwargs)
@commandWrap
def FBXPopSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXPopSettings(*args, **kwargs)
@commandWrap
def CreateSubCharacter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubCharacter(*args, **kwargs)
@commandWrap
def GoToPreviousDrivenKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoToPreviousDrivenKey(*args, **kwargs)
@commandWrap
def HypershadeGraphRemoveUnselected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphRemoveUnselected(*args, **kwargs)
@commandWrap
def CreateNURBSCube(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSCube(*args, **kwargs)
@commandWrap
def CreateSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSet(*args, **kwargs)
@commandWrap
def SquashOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SquashOptions(*args, **kwargs)
@commandWrap
def SetMeshCloneTargetTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshCloneTargetTool(*args, **kwargs)
@commandWrap
def nexConnectCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexConnectCtx(*args, **kwargs)
@commandWrap
def polySubdivideFacet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySubdivideFacet(*args, **kwargs)
@commandWrap
def mateCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mateCtx(*args, **kwargs)
@commandWrap
def ToggleCustomNURBSComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCustomNURBSComponents(*args, **kwargs)
@commandWrap
def DeleteAllContainers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllContainers(*args, **kwargs)
@commandWrap
def ShowJoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowJoints(*args, **kwargs)
@commandWrap
def DecreaseManipulatorSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DecreaseManipulatorSize(*args, **kwargs)
@commandWrap
def uiTemplate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.uiTemplate(*args, **kwargs)
@commandWrap
def GraphPaste(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphPaste(*args, **kwargs)
@commandWrap
def nClothAppendOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothAppendOpt(*args, **kwargs)
@commandWrap
def PolySelectTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolySelectTool(*args, **kwargs)
@commandWrap
def LongPolygonNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LongPolygonNormals(*args, **kwargs)
@commandWrap
def ShareColorInstances(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShareColorInstances(*args, **kwargs)
@commandWrap
def UVCylindricProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVCylindricProjection(*args, **kwargs)
@commandWrap
def ToggleSurfaceFaceCenters(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSurfaceFaceCenters(*args, **kwargs)
@commandWrap
def AssignNewMaterial(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignNewMaterial(*args, **kwargs)
@commandWrap
def boneLattice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.boneLattice(*args, **kwargs)
@commandWrap
def dR_showHelp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_showHelp(*args, **kwargs)
@commandWrap
def fluidDeleteCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidDeleteCache(*args, **kwargs)
@commandWrap
def BatchBake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BatchBake(*args, **kwargs)
@commandWrap
def NormalConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NormalConstraint(*args, **kwargs)
@commandWrap
def CloudImportExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CloudImportExport(*args, **kwargs)
@commandWrap
def dR_selectModeRaycast(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectModeRaycast(*args, **kwargs)
@commandWrap
def CreateQuickSelectSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateQuickSelectSet(*args, **kwargs)
@commandWrap
def GraphEditorValueLinesToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorValueLinesToggle(*args, **kwargs)
@commandWrap
def nurbsToPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsToPoly(*args, **kwargs)
@commandWrap
def ExtendCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendCurveOptions(*args, **kwargs)
@commandWrap
def namespace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.namespace(*args, **kwargs)
@commandWrap
def ProjectCurveOnMesh(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProjectCurveOnMesh(*args, **kwargs)
@commandWrap
def Wave(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Wave(*args, **kwargs)
@commandWrap
def DeleteAllSounds(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllSounds(*args, **kwargs)
@commandWrap
def ShowSculptObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowSculptObjects(*args, **kwargs)
@commandWrap
def polyCylinder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCylinder(*args, **kwargs)
@commandWrap
def InTangentPlateau(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InTangentPlateau(*args, **kwargs)
@commandWrap
def RelaxUVShellOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RelaxUVShellOptions(*args, **kwargs)
@commandWrap
def geometryReplaceCacheFrames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryReplaceCacheFrames(*args, **kwargs)
@commandWrap
def PluginManager(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PluginManager(*args, **kwargs)
@commandWrap
def SplitPolygonToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitPolygonToolOptions(*args, **kwargs)
@commandWrap
def OneClickSetupMotionBuilderCharacterStream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OneClickSetupMotionBuilderCharacterStream(*args, **kwargs)
@commandWrap
def tension(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.tension(*args, **kwargs)
@commandWrap
def select(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.select(*args, **kwargs)
@commandWrap
def CreateConstructionPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateConstructionPlane(*args, **kwargs)
@commandWrap
def CreateNSoftBodyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNSoftBodyOptions(*args, **kwargs)
@commandWrap
def displayColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayColor(*args, **kwargs)
@commandWrap
def attributeInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.attributeInfo(*args, **kwargs)
@commandWrap
def ToggleUVEditorIsolateSelectHUD(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVEditorIsolateSelectHUD(*args, **kwargs)
@commandWrap
def ToggleSelectDetails(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSelectDetails(*args, **kwargs)
@commandWrap
def DetachSkeleton(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachSkeleton(*args, **kwargs)
@commandWrap
def Triangulate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Triangulate(*args, **kwargs)
@commandWrap
def prepareRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.prepareRender(*args, **kwargs)
@commandWrap
def RemoveBlendShapeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBlendShapeOptions(*args, **kwargs)
@commandWrap
def SoloMaterial(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SoloMaterial(*args, **kwargs)
@commandWrap
def dR_autoWeldTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_autoWeldTGL(*args, **kwargs)
@commandWrap
def clipSchedule(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clipSchedule(*args, **kwargs)
@commandWrap
def ToggleOppositeFlagOfSelectedShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleOppositeFlagOfSelectedShapes(*args, **kwargs)
@commandWrap
def xgmDensityBrushToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmDensityBrushToolCmd(*args, **kwargs)
@commandWrap
def renderLayerMembers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderLayerMembers(*args, **kwargs)
@commandWrap
def PublishParentAnchorOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishParentAnchorOptions(*args, **kwargs)
@commandWrap
def DisplayUVShaded(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayUVShaded(*args, **kwargs)
@commandWrap
def cMuscleWeightMirror(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleWeightMirror(*args, **kwargs)
@commandWrap
def UniformOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UniformOptions(*args, **kwargs)
@commandWrap
def timeEditorComposition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditorComposition(*args, **kwargs)
@commandWrap
def nurbsCurveRebuildPref(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsCurveRebuildPref(*args, **kwargs)
@commandWrap
def ShowBatchRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowBatchRender(*args, **kwargs)
@commandWrap
def panZoom(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.panZoom(*args, **kwargs)
@commandWrap
def fluidCacheInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidCacheInfo(*args, **kwargs)
@commandWrap
def HypershadeExpandAsset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeExpandAsset(*args, **kwargs)
@commandWrap
def FBXGetTakeLocalTimeSpan(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXGetTakeLocalTimeSpan(*args, **kwargs)
@commandWrap
def snapKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.snapKey(*args, **kwargs)
@commandWrap
def CreatePolygonHelix(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonHelix(*args, **kwargs)
@commandWrap
def stereoCameraView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.stereoCameraView(*args, **kwargs)
@commandWrap
def HypershadeGraphMaterialsOnSelectedObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphMaterialsOnSelectedObjects(*args, **kwargs)
@commandWrap
def cMuscleBindSticky(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleBindSticky(*args, **kwargs)
@commandWrap
def WhatsNewHighlightingOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WhatsNewHighlightingOn(*args, **kwargs)
@commandWrap
def LockCamera(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LockCamera(*args, **kwargs)
@commandWrap
def HideDynamicConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideDynamicConstraints(*args, **kwargs)
@commandWrap
def SendToUnitySelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendToUnitySelection(*args, **kwargs)
@commandWrap
def mute(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mute(*args, **kwargs)
@commandWrap
def TimeEditorDeleteSelectedTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorDeleteSelectedTracks(*args, **kwargs)
@commandWrap
def SubdivSmoothnessFineOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessFineOptions(*args, **kwargs)
@commandWrap
def move(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.move(*args, **kwargs)
@commandWrap
def ToggleUVShellBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVShellBorder(*args, **kwargs)
@commandWrap
def FullCreaseSubdivSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FullCreaseSubdivSurface(*args, **kwargs)
@commandWrap
def CreateJiggleDeformer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateJiggleDeformer(*args, **kwargs)
@commandWrap
def XgmSetGrabBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetGrabBrushTool(*args, **kwargs)
@commandWrap
def SetAsCombinationTargetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetAsCombinationTargetOptions(*args, **kwargs)
@commandWrap
def sbs_EditSubstance(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_EditSubstance(*args, **kwargs)
@commandWrap
def RedoPreviousRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RedoPreviousRender(*args, **kwargs)
@commandWrap
def InsertEdgeLoopTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertEdgeLoopTool(*args, **kwargs)
@commandWrap
def createSubdivRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createSubdivRegion(*args, **kwargs)
@commandWrap
def sbs_AffectedByAllInputs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_AffectedByAllInputs(*args, **kwargs)
@commandWrap
def setXformManip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setXformManip(*args, **kwargs)
@commandWrap
def MakePondMotorBoats(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakePondMotorBoats(*args, **kwargs)
@commandWrap
def EditTexture(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EditTexture(*args, **kwargs)
@commandWrap
def SelectEdgeRing(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectEdgeRing(*args, **kwargs)
@commandWrap
def MergeToCenter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeToCenter(*args, **kwargs)
@commandWrap
def polyUVSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUVSet(*args, **kwargs)
@commandWrap
def HideNParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideNParticles(*args, **kwargs)
@commandWrap
def HypershadeOpenMaterialViewerWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenMaterialViewerWindow(*args, **kwargs)
@commandWrap
def ShowMeshSmoothToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshSmoothToolOptions(*args, **kwargs)
@commandWrap
def xgmSelectBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSelectBrushContext(*args, **kwargs)
@commandWrap
def spotLightPreviewPort(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.spotLightPreviewPort(*args, **kwargs)
@commandWrap
def ToggleMeshPoints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMeshPoints(*args, **kwargs)
@commandWrap
def HypershadeToggleNodeTitleMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleNodeTitleMode(*args, **kwargs)
@commandWrap
def CopyUVsToUVSetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyUVsToUVSetOptions(*args, **kwargs)
@commandWrap
def SplitVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitVertex(*args, **kwargs)
@commandWrap
def addDynamic(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.addDynamic(*args, **kwargs)
@commandWrap
def RenderGlobalsWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderGlobalsWindow(*args, **kwargs)
@commandWrap
def texTweakUVContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texTweakUVContext(*args, **kwargs)
@commandWrap
def ls(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ls(*args, **kwargs)
@commandWrap
def Sine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Sine(*args, **kwargs)
@commandWrap
def RedoViewChange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RedoViewChange(*args, **kwargs)
@commandWrap
def RebuildCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RebuildCurve(*args, **kwargs)
@commandWrap
def CustomNURBSSmoothness(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CustomNURBSSmoothness(*args, **kwargs)
@commandWrap
def sbs_SetAutoBake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_SetAutoBake(*args, **kwargs)
@commandWrap
def CreateTextureReferenceObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateTextureReferenceObject(*args, **kwargs)
@commandWrap
def FluidGradientsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FluidGradientsOptions(*args, **kwargs)
@commandWrap
def SelectSurfacePointsMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectSurfacePointsMask(*args, **kwargs)
@commandWrap
def python(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.python(*args, **kwargs)
@commandWrap
def createPolyCubeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyCubeCtx(*args, **kwargs)
@commandWrap
def FBXImportShowUI(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportShowUI(*args, **kwargs)
@commandWrap
def ShowSubdivSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowSubdivSurfaces(*args, **kwargs)
@commandWrap
def ikfkDisplayMethod(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikfkDisplayMethod(*args, **kwargs)
@commandWrap
def ShowMeshFoamyToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshFoamyToolOptions(*args, **kwargs)
@commandWrap
def transferAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.transferAttributes(*args, **kwargs)
@commandWrap
def bufferCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bufferCurve(*args, **kwargs)
@commandWrap
def SwapBufferCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SwapBufferCurve(*args, **kwargs)
@commandWrap
def ToggleMeshEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleMeshEdges(*args, **kwargs)
@commandWrap
def UnghostObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnghostObject(*args, **kwargs)
@commandWrap
def TangetConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangetConstraint(*args, **kwargs)
@commandWrap
def KeyframeTangentMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.KeyframeTangentMarkingMenu(*args, **kwargs)
@commandWrap
def ParticleTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParticleTool(*args, **kwargs)
@commandWrap
def geometryReplaceCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryReplaceCache(*args, **kwargs)
@commandWrap
def keyframeRegionMoveKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionMoveKeyCtx(*args, **kwargs)
@commandWrap
def UVCameraBasedProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVCameraBasedProjectionOptions(*args, **kwargs)
@commandWrap
def CommandShell(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CommandShell(*args, **kwargs)
@commandWrap
def geomBind(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geomBind(*args, **kwargs)
@commandWrap
def HypershadeTestTexture(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeTestTexture(*args, **kwargs)
@commandWrap
def sceneEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sceneEditor(*args, **kwargs)
@commandWrap
def TimeEditorExplodeGroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorExplodeGroup(*args, **kwargs)
@commandWrap
def FloatSelectedObjectsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FloatSelectedObjectsOptions(*args, **kwargs)
@commandWrap
def PostInfinityOscillate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PostInfinityOscillate(*args, **kwargs)
@commandWrap
def scriptNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.scriptNode(*args, **kwargs)
@commandWrap
def debugVar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.debugVar(*args, **kwargs)
@commandWrap
def dR_defLightTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_defLightTGL(*args, **kwargs)
@commandWrap
def OpenCloseSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OpenCloseSurfacesOptions(*args, **kwargs)
@commandWrap
def wireContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.wireContext(*args, **kwargs)
@commandWrap
def OutlinerToggleReferenceNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleReferenceNodes(*args, **kwargs)
@commandWrap
def xgmPatchInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPatchInfo(*args, **kwargs)
@commandWrap
def NodeEditorTransforms(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorTransforms(*args, **kwargs)
@commandWrap
def SelectAllHairSystem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllHairSystem(*args, **kwargs)
@commandWrap
def aaf2fcp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.aaf2fcp(*args, **kwargs)
@commandWrap
def HypershadeMoveTabDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeMoveTabDown(*args, **kwargs)
@commandWrap
def displayString(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayString(*args, **kwargs)
@commandWrap
def dR_nexTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_nexTool(*args, **kwargs)
@commandWrap
def HypershadeOpenGraphEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeOpenGraphEditorWindow(*args, **kwargs)
@commandWrap
def AlembicExportAllOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicExportAllOptions(*args, **kwargs)
@commandWrap
def ShowFluids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowFluids(*args, **kwargs)
@commandWrap
def displayPref(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayPref(*args, **kwargs)
@commandWrap
def fileDialog2(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fileDialog2(*args, **kwargs)
@commandWrap
def SetToFaceNormalsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetToFaceNormalsOptions(*args, **kwargs)
@commandWrap
def ToggleParticleCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleParticleCount(*args, **kwargs)
@commandWrap
def PaintRandomOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintRandomOptions(*args, **kwargs)
@commandWrap
def GraphPasteOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphPasteOptions(*args, **kwargs)
@commandWrap
def license(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.license(*args, **kwargs)
@commandWrap
def HypershadeDisplayAllShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayAllShapes(*args, **kwargs)
@commandWrap
def polySuperCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySuperCtx(*args, **kwargs)
@commandWrap
def MirrorDeformerWeightsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MirrorDeformerWeightsOptions(*args, **kwargs)
@commandWrap
def AddAnimationOffset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddAnimationOffset(*args, **kwargs)
@commandWrap
def PolyExtrudeFacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrudeFacesOptions(*args, **kwargs)
@commandWrap
def HypershadePickWalkLeft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadePickWalkLeft(*args, **kwargs)
@commandWrap
def TransferVertexOrder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransferVertexOrder(*args, **kwargs)
@commandWrap
def FreezeTransformations(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FreezeTransformations(*args, **kwargs)
@commandWrap
def CleanupPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CleanupPolygon(*args, **kwargs)
@commandWrap
def NodeEditorGraphRemoveDownstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphRemoveDownstream(*args, **kwargs)
@commandWrap
def pointLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointLight(*args, **kwargs)
@commandWrap
def walkCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.walkCtx(*args, **kwargs)
@commandWrap
def ConvertSelectionToFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToFaces(*args, **kwargs)
@commandWrap
def FBXExportGenerateLog(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportGenerateLog(*args, **kwargs)
@commandWrap
def showMetadata(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.showMetadata(*args, **kwargs)
@commandWrap
def hardware(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hardware(*args, **kwargs)
@commandWrap
def GlobalDiskCacheControl(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GlobalDiskCacheControl(*args, **kwargs)
@commandWrap
def displayLevelOfDetail(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayLevelOfDetail(*args, **kwargs)
@commandWrap
def IPROptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.IPROptions(*args, **kwargs)
@commandWrap
def RemoveFromContainerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveFromContainerOptions(*args, **kwargs)
@commandWrap
def HypershadeReduceTraversalDepth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeReduceTraversalDepth(*args, **kwargs)
@commandWrap
def HypershadeRenderTextureRange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRenderTextureRange(*args, **kwargs)
@commandWrap
def ArchiveScene(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArchiveScene(*args, **kwargs)
@commandWrap
def movieCompressor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.movieCompressor(*args, **kwargs)
@commandWrap
def cMuscleWeight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleWeight(*args, **kwargs)
@commandWrap
def dR_modeVert(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_modeVert(*args, **kwargs)
@commandWrap
def ToggleAnimationDetails(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleAnimationDetails(*args, **kwargs)
@commandWrap
def offsetCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.offsetCurve(*args, **kwargs)
@commandWrap
def xgmSmoothBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSmoothBrushContext(*args, **kwargs)
@commandWrap
def dR_testCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_testCmd(*args, **kwargs)
@commandWrap
def NEmitFromObjectOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NEmitFromObjectOptions(*args, **kwargs)
@commandWrap
def xgmCutBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmCutBrushContext(*args, **kwargs)
@commandWrap
def MakeShadowLinks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeShadowLinks(*args, **kwargs)
@commandWrap
def FloatSelectedPondObjectsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FloatSelectedPondObjectsOptions(*args, **kwargs)
@commandWrap
def insertKnotCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.insertKnotCurve(*args, **kwargs)
@commandWrap
def PolygonSoftenEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonSoftenEdge(*args, **kwargs)
@commandWrap
def OutlinerCollapseAllSelectedItems(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerCollapseAllSelectedItems(*args, **kwargs)
@commandWrap
def CreateSubdivPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivPlane(*args, **kwargs)
@commandWrap
def u3dOptimize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.u3dOptimize(*args, **kwargs)
@commandWrap
def CreateGhostOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateGhostOptions(*args, **kwargs)
@commandWrap
def cmdFileOutput(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cmdFileOutput(*args, **kwargs)
@commandWrap
def GraphEditorNeverDisplayTangents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorNeverDisplayTangents(*args, **kwargs)
@commandWrap
def nurbsCurveToBezier(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsCurveToBezier(*args, **kwargs)
@commandWrap
def furNurbsArea(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.furNurbsArea(*args, **kwargs)
@commandWrap
def DeleteAllParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllParticles(*args, **kwargs)
@commandWrap
def dR_coordSpaceCustom(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_coordSpaceCustom(*args, **kwargs)
@commandWrap
def CreatePolygonCube(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonCube(*args, **kwargs)
@commandWrap
def UVUnstackShells(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVUnstackShells(*args, **kwargs)
@commandWrap
def setInfinity(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setInfinity(*args, **kwargs)
@commandWrap
def connectAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.connectAttr(*args, **kwargs)
@commandWrap
def timer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timer(*args, **kwargs)
@commandWrap
def dR_conform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_conform(*args, **kwargs)
@commandWrap
def dR_loadRecentFile2(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_loadRecentFile2(*args, **kwargs)
@commandWrap
def SculptReferenceVectorMarkingMenuRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptReferenceVectorMarkingMenuRelease(*args, **kwargs)
@commandWrap
def sbs_GetAutoBake(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetAutoBake(*args, **kwargs)
@commandWrap
def createNurbsCubeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsCubeCtx(*args, **kwargs)
@commandWrap
def hikGetEffectorIdFromName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hikGetEffectorIdFromName(*args, **kwargs)
@commandWrap
def HideControllers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideControllers(*args, **kwargs)
@commandWrap
def dR_selectInvert(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_selectInvert(*args, **kwargs)
@commandWrap
def prependListItem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.prependListItem(*args, **kwargs)
@commandWrap
def cameraSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cameraSet(*args, **kwargs)
@commandWrap
def EditOversamplingForCacheSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EditOversamplingForCacheSettings(*args, **kwargs)
@commandWrap
def unapplyOverride(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.unapplyOverride(*args, **kwargs)
@commandWrap
def EnableRigidBodies(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableRigidBodies(*args, **kwargs)
@commandWrap
def pickWalk(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pickWalk(*args, **kwargs)
@commandWrap
def HypershadeMoveTabRight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeMoveTabRight(*args, **kwargs)
@commandWrap
def BakeAllNonDefHistory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeAllNonDefHistory(*args, **kwargs)
@commandWrap
def SetBreakdownKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetBreakdownKey(*args, **kwargs)
@commandWrap
def dR_softSelDistanceTypeObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_softSelDistanceTypeObject(*args, **kwargs)
@commandWrap
def FBXExportFinestSubdivLevel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportFinestSubdivLevel(*args, **kwargs)
@commandWrap
def ShowDeformingGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowDeformingGeometry(*args, **kwargs)
@commandWrap
def artUserPaintCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artUserPaintCtx(*args, **kwargs)
@commandWrap
def FBXExportBakeComplexStart(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportBakeComplexStart(*args, **kwargs)
@commandWrap
def PrevSkinPaintMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PrevSkinPaintMode(*args, **kwargs)
@commandWrap
def polyExtrudeVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyExtrudeVertex(*args, **kwargs)
@commandWrap
def dR_convertSelectionToUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_convertSelectionToUV(*args, **kwargs)
@commandWrap
def dR_symmetrize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_symmetrize(*args, **kwargs)
@commandWrap
def PerspGraphHypergraphLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PerspGraphHypergraphLayout(*args, **kwargs)
@commandWrap
def DuplicateEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DuplicateEdges(*args, **kwargs)
@commandWrap
def shapeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shapeEditor(*args, **kwargs)
@commandWrap
def reference(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.reference(*args, **kwargs)
@commandWrap
def gameExporter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.gameExporter(*args, **kwargs)
@commandWrap
def Fireworks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Fireworks(*args, **kwargs)
@commandWrap
def ParticleToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParticleToolOptions(*args, **kwargs)
@commandWrap
def ClearCurrentContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClearCurrentContainer(*args, **kwargs)
@commandWrap
def AssignOfflineFileFromRefEdOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AssignOfflineFileFromRefEdOptions(*args, **kwargs)
@commandWrap
def Snap3PointsTo3Points(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Snap3PointsTo3Points(*args, **kwargs)
@commandWrap
def paintPointsContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.paintPointsContext(*args, **kwargs)
@commandWrap
def SelectAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAll(*args, **kwargs)
@commandWrap
def SculptMeshActivateBrushSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptMeshActivateBrushSize(*args, **kwargs)
@commandWrap
def PolygonClearClipboard(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonClearClipboard(*args, **kwargs)
@commandWrap
def commandLogging(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.commandLogging(*args, **kwargs)
@commandWrap
def geometryDeleteCacheOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.geometryDeleteCacheOpt(*args, **kwargs)
@commandWrap
def agFormatIn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.agFormatIn(*args, **kwargs)
@commandWrap
def ShotPlaylistEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShotPlaylistEditor(*args, **kwargs)
@commandWrap
def SetFullBodyIKKeysAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFullBodyIKKeysAll(*args, **kwargs)
@commandWrap
def ConnectJointOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConnectJointOptions(*args, **kwargs)
@commandWrap
def Planar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Planar(*args, **kwargs)
@commandWrap
def ogs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ogs(*args, **kwargs)
@commandWrap
def SelectNextIntermediatObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectNextIntermediatObject(*args, **kwargs)
@commandWrap
def MergeEdgeToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MergeEdgeToolOptions(*args, **kwargs)
@commandWrap
def ShowMeshPinchToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshPinchToolOptions(*args, **kwargs)
@commandWrap
def nexMultiCutContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexMultiCutContext(*args, **kwargs)
@commandWrap
def CreatePolygonConeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonConeOptions(*args, **kwargs)
@commandWrap
def ToggleVisibilityAndKeepSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleVisibilityAndKeepSelection(*args, **kwargs)
@commandWrap
def PokePolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PokePolygon(*args, **kwargs)
@commandWrap
def closeSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.closeSurface(*args, **kwargs)
@commandWrap
def ImportDeformerWeightsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ImportDeformerWeightsOptions(*args, **kwargs)
@commandWrap
def XgmSetPartBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetPartBrushTool(*args, **kwargs)
@commandWrap
def pushPinning(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pushPinning(*args, **kwargs)
@commandWrap
def CreatePassiveRigidBody(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePassiveRigidBody(*args, **kwargs)
@commandWrap
def EnableNCloths(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableNCloths(*args, **kwargs)
@commandWrap
def GoToNextDrivenKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoToNextDrivenKey(*args, **kwargs)
@commandWrap
def manipScaleLimitsCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipScaleLimitsCtx(*args, **kwargs)
@commandWrap
def polyMoveUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMoveUV(*args, **kwargs)
@commandWrap
def GpuCacheExportSelectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GpuCacheExportSelectionOptions(*args, **kwargs)
@commandWrap
def PolyDisplayReset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyDisplayReset(*args, **kwargs)
@commandWrap
def ResetTemplateBrush(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResetTemplateBrush(*args, **kwargs)
@commandWrap
def SmokeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmokeOptions(*args, **kwargs)
@commandWrap
def polyNormalPerVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyNormalPerVertex(*args, **kwargs)
@commandWrap
def threadCount(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.threadCount(*args, **kwargs)
@commandWrap
def CurveSmoothnessFine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveSmoothnessFine(*args, **kwargs)
@commandWrap
def dR_softSelToolTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_softSelToolTGL(*args, **kwargs)
@commandWrap
def ShowMeshSprayToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowMeshSprayToolOptions(*args, **kwargs)
@commandWrap
def FBXExportFileVersion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportFileVersion(*args, **kwargs)
@commandWrap
def PreviousViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PreviousViewArrangement(*args, **kwargs)
@commandWrap
def DeleteKeysOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteKeysOptions(*args, **kwargs)
@commandWrap
def SelectSharedUVInstances(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectSharedUVInstances(*args, **kwargs)
@commandWrap
def AddWire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddWire(*args, **kwargs)
@commandWrap
def SelectEdgeLoopSp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectEdgeLoopSp(*args, **kwargs)
@commandWrap
def ObjectCentricLightLinkingEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ObjectCentricLightLinkingEditor(*args, **kwargs)
@commandWrap
def xgmSplineCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSplineCache(*args, **kwargs)
@commandWrap
def isTrue(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.isTrue(*args, **kwargs)
@commandWrap
def DecreaseExposureFine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DecreaseExposureFine(*args, **kwargs)
@commandWrap
def curveSketchCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveSketchCtx(*args, **kwargs)
@commandWrap
def MakeLightLinks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeLightLinks(*args, **kwargs)
@commandWrap
def FBXImportFillTimeline(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportFillTimeline(*args, **kwargs)
@commandWrap
def EnableNParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableNParticles(*args, **kwargs)
@commandWrap
def PaintGeomCacheTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintGeomCacheTool(*args, **kwargs)
@commandWrap
def userCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.userCtx(*args, **kwargs)
@commandWrap
def createPolyPlaneCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyPlaneCtx(*args, **kwargs)
@commandWrap
def RecentCommandsWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RecentCommandsWindow(*args, **kwargs)
@commandWrap
def webView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.webView(*args, **kwargs)
@commandWrap
def DeleteAllNCloths(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllNCloths(*args, **kwargs)
@commandWrap
def GoToDefaultView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GoToDefaultView(*args, **kwargs)
@commandWrap
def CreateImagePlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateImagePlane(*args, **kwargs)
@commandWrap
def SubdivSurfaceMatchTopology(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSurfaceMatchTopology(*args, **kwargs)
@commandWrap
def ctxData(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ctxData(*args, **kwargs)
@commandWrap
def HIKUiControl(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKUiControl(*args, **kwargs)
@commandWrap
def jointCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.jointCtx(*args, **kwargs)
@commandWrap
def gravity(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.gravity(*args, **kwargs)
@commandWrap
def CreatePolygonType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonType(*args, **kwargs)
@commandWrap
def CurveSmoothnessCoarse(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CurveSmoothnessCoarse(*args, **kwargs)
@commandWrap
def dR_scaleRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_scaleRelease(*args, **kwargs)
@commandWrap
def editImportedStatus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.editImportedStatus(*args, **kwargs)
@commandWrap
def HideNURBSSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideNURBSSurfaces(*args, **kwargs)
@commandWrap
def dR_softSelDistanceTypeSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_softSelDistanceTypeSurface(*args, **kwargs)
@commandWrap
def xgmNullRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmNullRender(*args, **kwargs)
@commandWrap
def igBrush(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.igBrush(*args, **kwargs)
@commandWrap
def retimeHelper(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.retimeHelper(*args, **kwargs)
@commandWrap
def xgmRebuildCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmRebuildCurve(*args, **kwargs)
@commandWrap
def FluidEmitter(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FluidEmitter(*args, **kwargs)
@commandWrap
def OutlinerToggleSetMembers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleSetMembers(*args, **kwargs)
@commandWrap
def EnableSnapshots(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EnableSnapshots(*args, **kwargs)
@commandWrap
def unloadPlugin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.unloadPlugin(*args, **kwargs)
@commandWrap
def AddWireOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddWireOptions(*args, **kwargs)
@commandWrap
def ProportionalModificationTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProportionalModificationTool(*args, **kwargs)
@commandWrap
def cMuscleCompIndex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleCompIndex(*args, **kwargs)
@commandWrap
def keyframeRegionDirectKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionDirectKeyCtx(*args, **kwargs)
@commandWrap
def ThreePointArcTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ThreePointArcTool(*args, **kwargs)
@commandWrap
def UniversalManipOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UniversalManipOptions(*args, **kwargs)
@commandWrap
def SetReFormTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetReFormTool(*args, **kwargs)
@commandWrap
def xgmGrabBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGrabBrushContext(*args, **kwargs)
@commandWrap
def Radial(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Radial(*args, **kwargs)
@commandWrap
def CreateSubdivSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSubdivSurface(*args, **kwargs)
@commandWrap
def subdMirror(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdMirror(*args, **kwargs)
@commandWrap
def HypershadeDisplayNoShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayNoShapes(*args, **kwargs)
@commandWrap
def keyframeRegionDollyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionDollyCtx(*args, **kwargs)
@commandWrap
def SculptPolygonsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptPolygonsToolOptions(*args, **kwargs)
@commandWrap
def ModifyUpperRadiusRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyUpperRadiusRelease(*args, **kwargs)
@commandWrap
def ConvertSelectionToContainedFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToContainedFaces(*args, **kwargs)
@commandWrap
def TimeEditorFramePlaybackRange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorFramePlaybackRange(*args, **kwargs)
@commandWrap
def snapshot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.snapshot(*args, **kwargs)
@commandWrap
def Bend(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Bend(*args, **kwargs)
@commandWrap
def workspace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.workspace(*args, **kwargs)
@commandWrap
def SetMeshSmearTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshSmearTool(*args, **kwargs)
@commandWrap
def SelectBrushNames(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectBrushNames(*args, **kwargs)
@commandWrap
def constrain(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.constrain(*args, **kwargs)
@commandWrap
def xgmDraRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmDraRender(*args, **kwargs)
@commandWrap
def setToolTo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setToolTo(*args, **kwargs)
@commandWrap
def TimeEditorPasteClips(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorPasteClips(*args, **kwargs)
@commandWrap
def orbitCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.orbitCtx(*args, **kwargs)
@commandWrap
def DeleteMemoryCaching(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteMemoryCaching(*args, **kwargs)
@commandWrap
def profilerTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.profilerTool(*args, **kwargs)
@commandWrap
def extendCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.extendCurve(*args, **kwargs)
@commandWrap
def isFromReferencedFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.isFromReferencedFile(*args, **kwargs)
@commandWrap
def Goal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Goal(*args, **kwargs)
@commandWrap
def substituteGeometry(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.substituteGeometry(*args, **kwargs)
@commandWrap
def WarpImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WarpImage(*args, **kwargs)
@commandWrap
def GrowLoopPolygonSelectionRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GrowLoopPolygonSelectionRegion(*args, **kwargs)
@commandWrap
def FBXExportAxisConversionMethod(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportAxisConversionMethod(*args, **kwargs)
@commandWrap
def xgmGuideSculptToolCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGuideSculptToolCmd(*args, **kwargs)
@commandWrap
def ToggleUVDistortion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVDistortion(*args, **kwargs)
@commandWrap
def UVEditorFrameAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVEditorFrameAll(*args, **kwargs)
@commandWrap
def AddTargetShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddTargetShape(*args, **kwargs)
@commandWrap
def DetachEdgeComponent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachEdgeComponent(*args, **kwargs)
@commandWrap
def NodeEditorGraphRemoveSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphRemoveSelected(*args, **kwargs)
@commandWrap
def FBXExportConvertUnitString(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportConvertUnitString(*args, **kwargs)
@commandWrap
def manipRotateContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipRotateContext(*args, **kwargs)
@commandWrap
def NodeEditorExtendToShapes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorExtendToShapes(*args, **kwargs)
@commandWrap
def MakeCollide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeCollide(*args, **kwargs)
@commandWrap
def adskRepresentation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.adskRepresentation(*args, **kwargs)
@commandWrap
def RetimeKeysTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RetimeKeysTool(*args, **kwargs)
@commandWrap
def subdPlanarProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdPlanarProjection(*args, **kwargs)
@commandWrap
def MarkingMenuPreferencesWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MarkingMenuPreferencesWindow(*args, **kwargs)
@commandWrap
def xgmUISelectionSync(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmUISelectionSync(*args, **kwargs)
@commandWrap
def DisplayShadingMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayShadingMarkingMenu(*args, **kwargs)
@commandWrap
def ConvertSelectionToUVEdgeLoop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConvertSelectionToUVEdgeLoop(*args, **kwargs)
@commandWrap
def SelectLightsIlluminatingObject(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectLightsIlluminatingObject(*args, **kwargs)
@commandWrap
def ShowDynamicConstraints(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowDynamicConstraints(*args, **kwargs)
@commandWrap
def xgmFreezeBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmFreezeBrushContext(*args, **kwargs)
@commandWrap
def BendOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BendOptions(*args, **kwargs)
@commandWrap
def sculptMeshCacheChangeCloneSource(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sculptMeshCacheChangeCloneSource(*args, **kwargs)
@commandWrap
def NodeEditorToggleNodeSelectedPins(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleNodeSelectedPins(*args, **kwargs)
@commandWrap
def NURBSSmoothnessRoughOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessRoughOptions(*args, **kwargs)
@commandWrap
def ExportProxyContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExportProxyContainer(*args, **kwargs)
@commandWrap
def FBXImportResamplingRateSource(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportResamplingRateSource(*args, **kwargs)
@commandWrap
def melInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.melInfo(*args, **kwargs)
@commandWrap
def exportEdits(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.exportEdits(*args, **kwargs)
@commandWrap
def Undo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Undo(*args, **kwargs)
@commandWrap
def PolyRemoveAllCrease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyRemoveAllCrease(*args, **kwargs)
@commandWrap
def DeleteVertex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteVertex(*args, **kwargs)
@commandWrap
def trimCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.trimCtx(*args, **kwargs)
@commandWrap
def graphTrackCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.graphTrackCtx(*args, **kwargs)
@commandWrap
def StitchEdgesTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.StitchEdgesTool(*args, **kwargs)
@commandWrap
def ShelfPreferencesWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShelfPreferencesWindow(*args, **kwargs)
@commandWrap
def CutPolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutPolygonOptions(*args, **kwargs)
@commandWrap
def FBXImportConvertDeformingNullsToJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportConvertDeformingNullsToJoint(*args, **kwargs)
@commandWrap
def createNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNode(*args, **kwargs)
@commandWrap
def flushUndo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.flushUndo(*args, **kwargs)
@commandWrap
def setDefaultShadingGroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setDefaultShadingGroup(*args, **kwargs)
@commandWrap
def CreatePolygonPipe(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPipe(*args, **kwargs)
@commandWrap
def toolDropped(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.toolDropped(*args, **kwargs)
@commandWrap
def polyCollapseTweaks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCollapseTweaks(*args, **kwargs)
@commandWrap
def testPa(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.testPa(*args, **kwargs)
@commandWrap
def CreateSpotLightOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSpotLightOptions(*args, **kwargs)
@commandWrap
def clearShear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clearShear(*args, **kwargs)
@commandWrap
def joint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.joint(*args, **kwargs)
@commandWrap
def LayoutUVRectangle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LayoutUVRectangle(*args, **kwargs)
@commandWrap
def revolve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.revolve(*args, **kwargs)
@commandWrap
def SelectUVBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUVBorder(*args, **kwargs)
@commandWrap
def CopyKeysOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CopyKeysOptions(*args, **kwargs)
@commandWrap
def texCutContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texCutContext(*args, **kwargs)
@commandWrap
def dynExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynExport(*args, **kwargs)
@commandWrap
def spotLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.spotLight(*args, **kwargs)
@commandWrap
def subdTransferUVsToCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdTransferUVsToCache(*args, **kwargs)
@commandWrap
def untrim(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.untrim(*args, **kwargs)
@commandWrap
def Unparent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Unparent(*args, **kwargs)
@commandWrap
def CreatePolygonTorus(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonTorus(*args, **kwargs)
@commandWrap
def UnfoldPackUVs3DInCurrentTile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnfoldPackUVs3DInCurrentTile(*args, **kwargs)
@commandWrap
def ScaleToolWithSnapMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleToolWithSnapMarkingMenu(*args, **kwargs)
@commandWrap
def dR_extrudeRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_extrudeRelease(*args, **kwargs)
@commandWrap
def WhatsNewStartupDialogOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WhatsNewStartupDialogOff(*args, **kwargs)
@commandWrap
def CreateReference(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateReference(*args, **kwargs)
@commandWrap
def NodeEditorDiveIntoCompound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorDiveIntoCompound(*args, **kwargs)
@commandWrap
def SlideEdgeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SlideEdgeTool(*args, **kwargs)
@commandWrap
def nexQuadDrawCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexQuadDrawCtx(*args, **kwargs)
@commandWrap
def CreatePolygonPrismOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPrismOptions(*args, **kwargs)
@commandWrap
def dynTestData(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dynTestData(*args, **kwargs)
@commandWrap
def AddBifrostCollider(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBifrostCollider(*args, **kwargs)
@commandWrap
def NodeEditorConnectionStyleBezier(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorConnectionStyleBezier(*args, **kwargs)
@commandWrap
def SmoothProxyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothProxyOptions(*args, **kwargs)
@commandWrap
def CreateCurveFromPolyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCurveFromPolyOptions(*args, **kwargs)
@commandWrap
def PointOnPolyConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PointOnPolyConstraint(*args, **kwargs)
@commandWrap
def resolutionNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.resolutionNode(*args, **kwargs)
@commandWrap
def deformerWeights(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deformerWeights(*args, **kwargs)
@commandWrap
def HypershadeToggleCrosshairOnEdgeDragging(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleCrosshairOnEdgeDragging(*args, **kwargs)
@commandWrap
def MatchRotation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MatchRotation(*args, **kwargs)
@commandWrap
def FBXExportBakeComplexEnd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportBakeComplexEnd(*args, **kwargs)
@commandWrap
def ParameterTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParameterTool(*args, **kwargs)
@commandWrap
def nodeIconButton(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nodeIconButton(*args, **kwargs)
@commandWrap
def PaintEffectsToCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsToCurve(*args, **kwargs)
@commandWrap
def ikHandleCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikHandleCtx(*args, **kwargs)
@commandWrap
def HypershadeDeleteSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteSelected(*args, **kwargs)
@commandWrap
def SplitMeshWithProjectedCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SplitMeshWithProjectedCurveOptions(*args, **kwargs)
@commandWrap
def Ungroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Ungroup(*args, **kwargs)
@commandWrap
def AddHolder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddHolder(*args, **kwargs)
@commandWrap
def XgExpressionEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgExpressionEditor(*args, **kwargs)
@commandWrap
def Twist(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Twist(*args, **kwargs)
@commandWrap
def CenterPivot(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CenterPivot(*args, **kwargs)
@commandWrap
def wire(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.wire(*args, **kwargs)
@commandWrap
def DeleteAllClips(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllClips(*args, **kwargs)
@commandWrap
def HypershadeRenderTextureRangeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRenderTextureRangeOptions(*args, **kwargs)
@commandWrap
def NURBSSmoothnessFine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessFine(*args, **kwargs)
@commandWrap
def NodeEditorConnectionStyleSShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorConnectionStyleSShape(*args, **kwargs)
@commandWrap
def ReducePolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReducePolygonOptions(*args, **kwargs)
@commandWrap
def boundary(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.boundary(*args, **kwargs)
@commandWrap
def rampWidgetAttrless(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.rampWidgetAttrless(*args, **kwargs)
@commandWrap
def DisableParticles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableParticles(*args, **kwargs)
@commandWrap
def OutlinerToggleIgnoreUseColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OutlinerToggleIgnoreUseColor(*args, **kwargs)
@commandWrap
def OpenVisorForMeshes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OpenVisorForMeshes(*args, **kwargs)
@commandWrap
def UpdateEraseSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UpdateEraseSurface(*args, **kwargs)
@commandWrap
def AddPointsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddPointsTool(*args, **kwargs)
@commandWrap
def removeJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.removeJoint(*args, **kwargs)
@commandWrap
def ArtPaintSkinWeightsToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ArtPaintSkinWeightsToolOptions(*args, **kwargs)
@commandWrap
def TimeEditorImportAnimation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorImportAnimation(*args, **kwargs)
@commandWrap
def TimeDraggerToolDeactivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeDraggerToolDeactivate(*args, **kwargs)
@commandWrap
def nClothRemove(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothRemove(*args, **kwargs)
@commandWrap
def polyCreaseCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCreaseCtx(*args, **kwargs)
@commandWrap
def NodeEditorExplodeCompound(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorExplodeCompound(*args, **kwargs)
@commandWrap
def volumeBind(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.volumeBind(*args, **kwargs)
@commandWrap
def HideLightManipulators(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideLightManipulators(*args, **kwargs)
@commandWrap
def dR_setExtendBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_setExtendBorder(*args, **kwargs)
@commandWrap
def PerPointEmissionRates(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PerPointEmissionRates(*args, **kwargs)
@commandWrap
def SnapKeysOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapKeysOptions(*args, **kwargs)
@commandWrap
def Smoke(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Smoke(*args, **kwargs)
@commandWrap
def CreateGhost(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateGhost(*args, **kwargs)
@commandWrap
def displayStats(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayStats(*args, **kwargs)
@commandWrap
def LowQualityDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LowQualityDisplay(*args, **kwargs)
@commandWrap
def CreateIllustratorCurvesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateIllustratorCurvesOptions(*args, **kwargs)
@commandWrap
def HypershadeToggleUseAssetsAndPublishedAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleUseAssetsAndPublishedAttributes(*args, **kwargs)
@commandWrap
def UVSetEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVSetEditor(*args, **kwargs)
@commandWrap
def unassignInputDevice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.unassignInputDevice(*args, **kwargs)
@commandWrap
def BrushPresetBlendShading(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BrushPresetBlendShading(*args, **kwargs)
@commandWrap
def XgmSetDensityBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetDensityBrushTool(*args, **kwargs)
@commandWrap
def mouldSubdiv(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.mouldSubdiv(*args, **kwargs)
@commandWrap
def removeListItem(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.removeListItem(*args, **kwargs)
@commandWrap
def loadFluid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.loadFluid(*args, **kwargs)
@commandWrap
def ExtendCurveOnSurfaceOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendCurveOnSurfaceOptions(*args, **kwargs)
@commandWrap
def renderWindowEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderWindowEditor(*args, **kwargs)
@commandWrap
def AddFaceDivisions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddFaceDivisions(*args, **kwargs)
@commandWrap
def SubdivSmoothnessHull(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessHull(*args, **kwargs)
@commandWrap
def SnapToPoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToPoint(*args, **kwargs)
@commandWrap
def DetachComponent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachComponent(*args, **kwargs)
@commandWrap
def DisableSnapshots(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableSnapshots(*args, **kwargs)
@commandWrap
def TimeEditorFrameCenterView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorFrameCenterView(*args, **kwargs)
@commandWrap
def FBXLoadMBExportPresetFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXLoadMBExportPresetFile(*args, **kwargs)
@commandWrap
def SelectAllStrokes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllStrokes(*args, **kwargs)
@commandWrap
def polyDuplicateAndConnect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyDuplicateAndConnect(*args, **kwargs)
@commandWrap
def timeWarp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeWarp(*args, **kwargs)
@commandWrap
def FitBSplineOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FitBSplineOptions(*args, **kwargs)
@commandWrap
def ReassignBoneLatticeJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ReassignBoneLatticeJoint(*args, **kwargs)
@commandWrap
def xgmPointRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPointRender(*args, **kwargs)
@commandWrap
def symmetrizeUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.symmetrizeUV(*args, **kwargs)
@commandWrap
def AddCombinationTargetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddCombinationTargetOptions(*args, **kwargs)
@commandWrap
def artAttrSkinPaintCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artAttrSkinPaintCtx(*args, **kwargs)
@commandWrap
def ModifyConstraintAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ModifyConstraintAxis(*args, **kwargs)
@commandWrap
def Boundary(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Boundary(*args, **kwargs)
@commandWrap
def HypergraphDGWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypergraphDGWindow(*args, **kwargs)
@commandWrap
def dR_setExtendEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_setExtendEdge(*args, **kwargs)
@commandWrap
def RemoveConstraintTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveConstraintTarget(*args, **kwargs)
@commandWrap
def quit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.quit(*args, **kwargs)
@commandWrap
def LevelOfDetailGroupOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LevelOfDetailGroupOptions(*args, **kwargs)
@commandWrap
def ClearPaintEffectsView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClearPaintEffectsView(*args, **kwargs)
@commandWrap
def nurbsCube(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsCube(*args, **kwargs)
@commandWrap
def ToggleDisplayGradient(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleDisplayGradient(*args, **kwargs)
@commandWrap
def ScriptPaintTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScriptPaintTool(*args, **kwargs)
@commandWrap
def HypershadeEditTexture(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeEditTexture(*args, **kwargs)
@commandWrap
def DetachCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DetachCurve(*args, **kwargs)
@commandWrap
def DeleteAllExpressions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllExpressions(*args, **kwargs)
@commandWrap
def PaintEffectsToCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsToCurveOptions(*args, **kwargs)
@commandWrap
def polyContourProjection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyContourProjection(*args, **kwargs)
@commandWrap
def MovePolygonComponentOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MovePolygonComponentOptions(*args, **kwargs)
@commandWrap
def ClearInitialState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ClearInitialState(*args, **kwargs)
@commandWrap
def AddBlendShape(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddBlendShape(*args, **kwargs)
@commandWrap
def ToggleFullScreenMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleFullScreenMode(*args, **kwargs)
@commandWrap
def uvLink(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.uvLink(*args, **kwargs)
@commandWrap
def addIK2BsolverCallbacks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.addIK2BsolverCallbacks(*args, **kwargs)
@commandWrap
def polyConnectComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyConnectComponents(*args, **kwargs)
@commandWrap
def ungroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ungroup(*args, **kwargs)
@commandWrap
def XgmSetNoiseBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetNoiseBrushToolOption(*args, **kwargs)
@commandWrap
def createNurbsSquareCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsSquareCtx(*args, **kwargs)
@commandWrap
def Birail2Options(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Birail2Options(*args, **kwargs)
@commandWrap
def UVIsolateLoadSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVIsolateLoadSet(*args, **kwargs)
@commandWrap
def polyStraightenUVBorder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyStraightenUVBorder(*args, **kwargs)
@commandWrap
def movIn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.movIn(*args, **kwargs)
@commandWrap
def SelectMaskToolMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectMaskToolMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def UVCylindricProjectionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVCylindricProjectionOptions(*args, **kwargs)
@commandWrap
def CreateNURBSConeOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSConeOptions(*args, **kwargs)
@commandWrap
def artAttrSkinPaintCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artAttrSkinPaintCmd(*args, **kwargs)
@commandWrap
def BakeSpringAnimationOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BakeSpringAnimationOptions(*args, **kwargs)
@commandWrap
def WhatsNewStartupDialogOn(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WhatsNewStartupDialogOn(*args, **kwargs)
@commandWrap
def NodeEditorSetTraversalDepthUnlim(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorSetTraversalDepthUnlim(*args, **kwargs)
@commandWrap
def ScriptEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScriptEditor(*args, **kwargs)
@commandWrap
def NodeEditorWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorWindow(*args, **kwargs)
@commandWrap
def GameExporterWnd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GameExporterWnd(*args, **kwargs)
@commandWrap
def controller(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.controller(*args, **kwargs)
@commandWrap
def SubdivSmoothnessMedium(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSmoothnessMedium(*args, **kwargs)
@commandWrap
def SurfaceEditingToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceEditingToolOptions(*args, **kwargs)
@commandWrap
def HypershadeConvertPSDToLayeredTexture(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeConvertPSDToLayeredTexture(*args, **kwargs)
@commandWrap
def OffsetCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetCurveOptions(*args, **kwargs)
@commandWrap
def GraphSnap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphSnap(*args, **kwargs)
@commandWrap
def SelectUnmappedFaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectUnmappedFaces(*args, **kwargs)
@commandWrap
def SymmetrizeUVContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SymmetrizeUVContext(*args, **kwargs)
@commandWrap
def nucleusGetEffectsAsset(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusGetEffectsAsset(*args, **kwargs)
@commandWrap
def dR_outlinerTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_outlinerTGL(*args, **kwargs)
@commandWrap
def PolyCreaseTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyCreaseTool(*args, **kwargs)
@commandWrap
def DeleteAllRigidBodies(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllRigidBodies(*args, **kwargs)
@commandWrap
def SelectObjectsShadowedByLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectObjectsShadowedByLight(*args, **kwargs)
@commandWrap
def dR_targetWeldTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_targetWeldTool(*args, **kwargs)
@commandWrap
def ShadingGroupAttributeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShadingGroupAttributeEditor(*args, **kwargs)
@commandWrap
def XgmSetWidthBrushTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetWidthBrushTool(*args, **kwargs)
@commandWrap
def align(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.align(*args, **kwargs)
@commandWrap
def PickWalkUpSelect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickWalkUpSelect(*args, **kwargs)
@commandWrap
def checkDefaultRenderGlobals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.checkDefaultRenderGlobals(*args, **kwargs)
@commandWrap
def HideUnselectedObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideUnselectedObjects(*args, **kwargs)
@commandWrap
def GreasePencilTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GreasePencilTool(*args, **kwargs)
@commandWrap
def wrinkleContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.wrinkleContext(*args, **kwargs)
@commandWrap
def MediumPolygonNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MediumPolygonNormals(*args, **kwargs)
@commandWrap
def CreatePolygonToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonToolOptions(*args, **kwargs)
@commandWrap
def ctxEditMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ctxEditMode(*args, **kwargs)
@commandWrap
def TimeEditorToggleSnapToClipRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorToggleSnapToClipRelease(*args, **kwargs)
@commandWrap
def arclen(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.arclen(*args, **kwargs)
@commandWrap
def OptimizeScene(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OptimizeScene(*args, **kwargs)
@commandWrap
def DeleteMotionPaths(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteMotionPaths(*args, **kwargs)
@commandWrap
def polyUniteSkinned(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUniteSkinned(*args, **kwargs)
@commandWrap
def polyMapDel(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyMapDel(*args, **kwargs)
@commandWrap
def SelectPointsMask(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectPointsMask(*args, **kwargs)
@commandWrap
def TimeEditorClipScaleToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipScaleToggle(*args, **kwargs)
@commandWrap
def polyOptUvs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyOptUvs(*args, **kwargs)
@commandWrap
def fileBrowserDialog(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fileBrowserDialog(*args, **kwargs)
@commandWrap
def CommandWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CommandWindow(*args, **kwargs)
@commandWrap
def Uniform(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Uniform(*args, **kwargs)
@commandWrap
def ScaleKeysOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleKeysOptions(*args, **kwargs)
@commandWrap
def FBXImportCacheFile(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportCacheFile(*args, **kwargs)
@commandWrap
def HideSubdivSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideSubdivSurfaces(*args, **kwargs)
@commandWrap
def UnparentOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnparentOptions(*args, **kwargs)
@commandWrap
def SmoothHairCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothHairCurves(*args, **kwargs)
@commandWrap
def distanceDimContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.distanceDimContext(*args, **kwargs)
@commandWrap
def BevelOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BevelOptions(*args, **kwargs)
@commandWrap
def UVEditorInvertPin(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVEditorInvertPin(*args, **kwargs)
@commandWrap
def polyUVRectangle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUVRectangle(*args, **kwargs)
@commandWrap
def keyframeRegionTrackCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionTrackCtx(*args, **kwargs)
@commandWrap
def PaintEffectsToNurbsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintEffectsToNurbsOptions(*args, **kwargs)
@commandWrap
def CreateEmptyGroup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateEmptyGroup(*args, **kwargs)
@commandWrap
def CreatePolygonGear(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonGear(*args, **kwargs)
@commandWrap
def OpenSceneOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OpenSceneOptions(*args, **kwargs)
@commandWrap
def dR_curveSnapRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_curveSnapRelease(*args, **kwargs)
@commandWrap
def FBXImportMode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportMode(*args, **kwargs)
@commandWrap
def bulletConvexDecomposition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bulletConvexDecomposition(*args, **kwargs)
@commandWrap
def FBXGetTakeReferenceTimeSpan(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXGetTakeReferenceTimeSpan(*args, **kwargs)
@commandWrap
def nexOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nexOpt(*args, **kwargs)
@commandWrap
def polyCacheMonitor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyCacheMonitor(*args, **kwargs)
@commandWrap
def VolumeAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.VolumeAxis(*args, **kwargs)
@commandWrap
def RotateToolWithSnapMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateToolWithSnapMarkingMenu(*args, **kwargs)
@commandWrap
def DisplayLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayLight(*args, **kwargs)
@commandWrap
def TogglePolyDisplayLimitToSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePolyDisplayLimitToSelected(*args, **kwargs)
@commandWrap
def HypershadeToggleShowNamespace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeToggleShowNamespace(*args, **kwargs)
@commandWrap
def CreateNSoftBody(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNSoftBody(*args, **kwargs)
@commandWrap
def AnimationTurntableOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AnimationTurntableOptions(*args, **kwargs)
@commandWrap
def BaseLevelComponentDisplay(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.BaseLevelComponentDisplay(*args, **kwargs)
@commandWrap
def RemoveShrinkWrapSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveShrinkWrapSurfaces(*args, **kwargs)
@commandWrap
def dR_viewRight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewRight(*args, **kwargs)
@commandWrap
def OpenCloseSurfaces(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OpenCloseSurfaces(*args, **kwargs)
@commandWrap
def SubdivSurfaceCleanTopology(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SubdivSurfaceCleanTopology(*args, **kwargs)
@commandWrap
def AlembicExportAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicExportAll(*args, **kwargs)
@commandWrap
def SetRigidBodyInterpenetration(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetRigidBodyInterpenetration(*args, **kwargs)
@commandWrap
def dR_multiCutPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_multiCutPress(*args, **kwargs)
@commandWrap
def TimeEditorClipTrimToggle(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorClipTrimToggle(*args, **kwargs)
@commandWrap
def SelectAllInput(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllInput(*args, **kwargs)
@commandWrap
def RenderViewPrevImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderViewPrevImage(*args, **kwargs)
@commandWrap
def dR_viewFront(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewFront(*args, **kwargs)
@commandWrap
def DeletePolyElements(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeletePolyElements(*args, **kwargs)
@commandWrap
def furMeshArea(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.furMeshArea(*args, **kwargs)
@commandWrap
def InTangentSpline(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InTangentSpline(*args, **kwargs)
@commandWrap
def GraphEditorDisplayValues(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorDisplayValues(*args, **kwargs)
@commandWrap
def exclusiveLightCheckBox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.exclusiveLightCheckBox(*args, **kwargs)
@commandWrap
def SmoothPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothPolygon(*args, **kwargs)
@commandWrap
def ToggleCVs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCVs(*args, **kwargs)
@commandWrap
def FBXExportEmbeddedTextures(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportEmbeddedTextures(*args, **kwargs)
@commandWrap
def polyDuplicateEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyDuplicateEdge(*args, **kwargs)
@commandWrap
def HypershadeDeleteNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDeleteNodes(*args, **kwargs)
@commandWrap
def directKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.directKeyCtx(*args, **kwargs)
@commandWrap
def setNClothStartState(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.setNClothStartState(*args, **kwargs)
@commandWrap
def TrimToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TrimToolOptions(*args, **kwargs)
@commandWrap
def SetMeshKnifeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshKnifeTool(*args, **kwargs)
@commandWrap
def ToggleColorFeedback(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleColorFeedback(*args, **kwargs)
@commandWrap
def xgmPlaceBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPlaceBrushContext(*args, **kwargs)
@commandWrap
def ToggleSubdDetails(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleSubdDetails(*args, **kwargs)
@commandWrap
def TimeEditorSoloSelectedTracks(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TimeEditorSoloSelectedTracks(*args, **kwargs)
@commandWrap
def fluidReplaceCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.fluidReplaceCache(*args, **kwargs)
@commandWrap
def debugNamespace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.debugNamespace(*args, **kwargs)
@commandWrap
def CreateActiveRigidBody(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateActiveRigidBody(*args, **kwargs)
@commandWrap
def ToggleHulls(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleHulls(*args, **kwargs)
@commandWrap
def AttachToPathOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachToPathOptions(*args, **kwargs)
@commandWrap
def sets(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sets(*args, **kwargs)
@commandWrap
def JointTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.JointTool(*args, **kwargs)
@commandWrap
def MakeMotorBoats(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeMotorBoats(*args, **kwargs)
@commandWrap
def Quadrangulate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Quadrangulate(*args, **kwargs)
@commandWrap
def sbs_SetEngine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_SetEngine(*args, **kwargs)
@commandWrap
def DeleteAllStrokes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllStrokes(*args, **kwargs)
@commandWrap
def DeleteAllHistory(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllHistory(*args, **kwargs)
@commandWrap
def baseTemplate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.baseTemplate(*args, **kwargs)
@commandWrap
def ShortPolygonNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShortPolygonNormals(*args, **kwargs)
@commandWrap
def NodeEditorToggleUseAssetsAndPublishedAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleUseAssetsAndPublishedAttributes(*args, **kwargs)
@commandWrap
def CreatePointLightOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePointLightOptions(*args, **kwargs)
@commandWrap
def createPolyCylinderCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createPolyCylinderCtx(*args, **kwargs)
@commandWrap
def adskAssetList(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.adskAssetList(*args, **kwargs)
@commandWrap
def tumbleCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.tumbleCtx(*args, **kwargs)
@commandWrap
def keyframeOutliner(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeOutliner(*args, **kwargs)
@commandWrap
def getAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getAttr(*args, **kwargs)
@commandWrap
def PolyRemoveCrease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyRemoveCrease(*args, **kwargs)
@commandWrap
def hardenPointCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hardenPointCurve(*args, **kwargs)
@commandWrap
def AbcImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AbcImport(*args, **kwargs)
@commandWrap
def LODGenerateMeshesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LODGenerateMeshesOptions(*args, **kwargs)
@commandWrap
def selLoadSettings(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.selLoadSettings(*args, **kwargs)
@commandWrap
def subdToPoly(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdToPoly(*args, **kwargs)
@commandWrap
def ProfilerTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerTool(*args, **kwargs)
@commandWrap
def nucleusDisplayOtherNodes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nucleusDisplayOtherNodes(*args, **kwargs)
@commandWrap
def convertIffToPsd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.convertIffToPsd(*args, **kwargs)
@commandWrap
def bifMeshExport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bifMeshExport(*args, **kwargs)
@commandWrap
def meshRemap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.meshRemap(*args, **kwargs)
@commandWrap
def dR_activeHandleXY(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_activeHandleXY(*args, **kwargs)
@commandWrap
def ikHandleDisplayScale(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikHandleDisplayScale(*args, **kwargs)
@commandWrap
def ToggleCharacterControls(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCharacterControls(*args, **kwargs)
@commandWrap
def lattice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.lattice(*args, **kwargs)
@commandWrap
def pointCurveConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pointCurveConstraint(*args, **kwargs)
@commandWrap
def nClothDeleteHistoryOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothDeleteHistoryOpt(*args, **kwargs)
@commandWrap
def jointCluster(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.jointCluster(*args, **kwargs)
@commandWrap
def moduleInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.moduleInfo(*args, **kwargs)
@commandWrap
def ShowStrokePathCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowStrokePathCurves(*args, **kwargs)
@commandWrap
def NextViewArrangement(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NextViewArrangement(*args, **kwargs)
@commandWrap
def ToggleCommandLine(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleCommandLine(*args, **kwargs)
@commandWrap
def polyFlipEdge(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyFlipEdge(*args, **kwargs)
@commandWrap
def ToggleVertIDs(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleVertIDs(*args, **kwargs)
@commandWrap
def DisplacementToPolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplacementToPolygon(*args, **kwargs)
@commandWrap
def UVStraighten(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVStraighten(*args, **kwargs)
@commandWrap
def RemoveBifrostGuide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveBifrostGuide(*args, **kwargs)
@commandWrap
def filePathEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.filePathEditor(*args, **kwargs)
@commandWrap
def DisableExpressions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableExpressions(*args, **kwargs)
@commandWrap
def TanimLayer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TanimLayer(*args, **kwargs)
@commandWrap
def SendAsNewSceneMudbox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SendAsNewSceneMudbox(*args, **kwargs)
@commandWrap
def sbs_SetGlobalTextureWidth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_SetGlobalTextureWidth(*args, **kwargs)
@commandWrap
def ShapeEditorSelectNone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShapeEditorSelectNone(*args, **kwargs)
@commandWrap
def AlembicExportSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicExportSelection(*args, **kwargs)
@commandWrap
def polyPlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPlane(*args, **kwargs)
@commandWrap
def xgmDensityBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmDensityBrushContext(*args, **kwargs)
@commandWrap
def texturePlacementContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texturePlacementContext(*args, **kwargs)
@commandWrap
def turbulence(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.turbulence(*args, **kwargs)
@commandWrap
def dR_multiCutSlicePointCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_multiCutSlicePointCmd(*args, **kwargs)
@commandWrap
def CustomNURBSComponentsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CustomNURBSComponentsOptions(*args, **kwargs)
@commandWrap
def HypershadeSortByType(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSortByType(*args, **kwargs)
@commandWrap
def SculptMeshActivateBrushStrength(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptMeshActivateBrushStrength(*args, **kwargs)
@commandWrap
def sbs_GetGlobalTextureWidth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetGlobalTextureWidth(*args, **kwargs)
@commandWrap
def deleteAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deleteAttr(*args, **kwargs)
@commandWrap
def SelectCurveCVsAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectCurveCVsAll(*args, **kwargs)
@commandWrap
def SelectPolygonSelectionBoundary(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectPolygonSelectionBoundary(*args, **kwargs)
@commandWrap
def polyRetopoCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyRetopoCtx(*args, **kwargs)
@commandWrap
def dR_modeUV(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_modeUV(*args, **kwargs)
@commandWrap
def PublishChildAnchor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PublishChildAnchor(*args, **kwargs)
@commandWrap
def renderLayerPostProcess(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderLayerPostProcess(*args, **kwargs)
@commandWrap
def polyPrimitive(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPrimitive(*args, **kwargs)
@commandWrap
def displayAffected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.displayAffected(*args, **kwargs)
@commandWrap
def textCurves(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.textCurves(*args, **kwargs)
@commandWrap
def textureLassoContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.textureLassoContext(*args, **kwargs)
@commandWrap
def vortex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.vortex(*args, **kwargs)
@commandWrap
def TransformPolygonComponentOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransformPolygonComponentOptions(*args, **kwargs)
@commandWrap
def HypershadeGraphRemoveDownstream(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeGraphRemoveDownstream(*args, **kwargs)
@commandWrap
def ikSolver(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ikSolver(*args, **kwargs)
@commandWrap
def CreateDirectionalLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateDirectionalLight(*args, **kwargs)
@commandWrap
def soft(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.soft(*args, **kwargs)
@commandWrap
def cgfxShader(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cgfxShader(*args, **kwargs)
@commandWrap
def SnapToCurveRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToCurveRelease(*args, **kwargs)
@commandWrap
def Quit(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Quit(*args, **kwargs)
@commandWrap
def SetMaxInfluences(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMaxInfluences(*args, **kwargs)
@commandWrap
def dR_moveRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_moveRelease(*args, **kwargs)
@commandWrap
def createCurveWarp(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createCurveWarp(*args, **kwargs)
@commandWrap
def tumble(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.tumble(*args, **kwargs)
@commandWrap
def clip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.clip(*args, **kwargs)
@commandWrap
def NodeEditorToggleLockUnlock(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleLockUnlock(*args, **kwargs)
@commandWrap
def dR_softSelStickyRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_softSelStickyRelease(*args, **kwargs)
@commandWrap
def ShrinkPolygonSelectionRegion(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShrinkPolygonSelectionRegion(*args, **kwargs)
@commandWrap
def SculptGeometryToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SculptGeometryToolOptions(*args, **kwargs)
@commandWrap
def AlembicOpen(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicOpen(*args, **kwargs)
@commandWrap
def CreatePassiveRigidBodyOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePassiveRigidBodyOptions(*args, **kwargs)
@commandWrap
def bezierInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bezierInfo(*args, **kwargs)
@commandWrap
def dR_customPivotTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_customPivotTool(*args, **kwargs)
@commandWrap
def AppendToPolygonTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AppendToPolygonTool(*args, **kwargs)
@commandWrap
def DisableRigidBodies(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableRigidBodies(*args, **kwargs)
@commandWrap
def CreateNURBSCone(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateNURBSCone(*args, **kwargs)
@commandWrap
def LoadHIKCharacterDefinition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LoadHIKCharacterDefinition(*args, **kwargs)
@commandWrap
def RenderTextureRange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderTextureRange(*args, **kwargs)
@commandWrap
def insertListItemBefore(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.insertListItemBefore(*args, **kwargs)
@commandWrap
def NodeEditorGraphRearrange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorGraphRearrange(*args, **kwargs)
@commandWrap
def MoveIKtoFK(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MoveIKtoFK(*args, **kwargs)
@commandWrap
def GamePipeline(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GamePipeline(*args, **kwargs)
@commandWrap
def CreatePolygonCylinder(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonCylinder(*args, **kwargs)
@commandWrap
def SetMeshPinchTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshPinchTool(*args, **kwargs)
@commandWrap
def NodeEditorAddIterationStatePorts(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorAddIterationStatePorts(*args, **kwargs)
@commandWrap
def timeEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.timeEditor(*args, **kwargs)
@commandWrap
def ParticleInstancerOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParticleInstancerOptions(*args, **kwargs)
@commandWrap
def PerformanceSettingsWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PerformanceSettingsWindow(*args, **kwargs)
@commandWrap
def smoothTangentSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.smoothTangentSurface(*args, **kwargs)
@commandWrap
def SetFullBodyIKKeysSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFullBodyIKKeysSelected(*args, **kwargs)
@commandWrap
def UnpublishNode(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnpublishNode(*args, **kwargs)
@commandWrap
def XgmSplineCacheCreateOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineCacheCreateOptions(*args, **kwargs)
@commandWrap
def xgmNop(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmNop(*args, **kwargs)
@commandWrap
def insertJointCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.insertJointCtx(*args, **kwargs)
@commandWrap
def HypershadeRestoreLastClosedTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRestoreLastClosedTab(*args, **kwargs)
@commandWrap
def HIKSetFullBodyKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HIKSetFullBodyKey(*args, **kwargs)
@commandWrap
def PolyBrushMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyBrushMarkingMenu(*args, **kwargs)
@commandWrap
def baseView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.baseView(*args, **kwargs)
@commandWrap
def ProjectTangentOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProjectTangentOptions(*args, **kwargs)
@commandWrap
def CompleteCurrentTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CompleteCurrentTool(*args, **kwargs)
@commandWrap
def NodeEditorSetSmallNodeSwatchSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorSetSmallNodeSwatchSize(*args, **kwargs)
@commandWrap
def PolygonPaste(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonPaste(*args, **kwargs)
@commandWrap
def nurbsToSubdivPref(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsToSubdivPref(*args, **kwargs)
@commandWrap
def audioTrack(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.audioTrack(*args, **kwargs)
@commandWrap
def journal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.journal(*args, **kwargs)
@commandWrap
def colorManagementFileRules(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.colorManagementFileRules(*args, **kwargs)
@commandWrap
def polySmooth(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polySmooth(*args, **kwargs)
@commandWrap
def CircularFillet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CircularFillet(*args, **kwargs)
@commandWrap
def FrameSelectedWithoutChildren(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FrameSelectedWithoutChildren(*args, **kwargs)
@commandWrap
def getModifiers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getModifiers(*args, **kwargs)
@commandWrap
def texRotateContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.texRotateContext(*args, **kwargs)
@commandWrap
def GpuCacheImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GpuCacheImport(*args, **kwargs)
@commandWrap
def SetShrinkWrapTarget(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetShrinkWrapTarget(*args, **kwargs)
@commandWrap
def artFluidAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artFluidAttr(*args, **kwargs)
@commandWrap
def XgmSetFreezeBrushToolOption(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSetFreezeBrushToolOption(*args, **kwargs)
@commandWrap
def AlignSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlignSurfacesOptions(*args, **kwargs)
@commandWrap
def dR_decreaseManipSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_decreaseManipSize(*args, **kwargs)
@commandWrap
def SetToFaceNormals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetToFaceNormals(*args, **kwargs)
@commandWrap
def DeleteAllNRigids(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllNRigids(*args, **kwargs)
@commandWrap
def about(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.about(*args, **kwargs)
@commandWrap
def curveEPCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.curveEPCtx(*args, **kwargs)
@commandWrap
def pluginInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.pluginInfo(*args, **kwargs)
@commandWrap
def GraphEditorFrameCenterView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorFrameCenterView(*args, **kwargs)
@commandWrap
def dR_coordSpaceLocal(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_coordSpaceLocal(*args, **kwargs)
@commandWrap
def cleanPerFaceAssignment(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cleanPerFaceAssignment(*args, **kwargs)
@commandWrap
def createNurbsSphereCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsSphereCtx(*args, **kwargs)
@commandWrap
def RenderDiagnostics(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderDiagnostics(*args, **kwargs)
@commandWrap
def HypershadeWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeWindow(*args, **kwargs)
@commandWrap
def HypershadeSetLargeNodeSwatchSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSetLargeNodeSwatchSize(*args, **kwargs)
@commandWrap
def RoundToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RoundToolOptions(*args, **kwargs)
@commandWrap
def ResolveInterpenetrationOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ResolveInterpenetrationOptions(*args, **kwargs)
@commandWrap
def WedgePolygon(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.WedgePolygon(*args, **kwargs)
@commandWrap
def AttachCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AttachCurveOptions(*args, **kwargs)
@commandWrap
def getInputDeviceRange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getInputDeviceRange(*args, **kwargs)
@commandWrap
def colorIndex(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.colorIndex(*args, **kwargs)
@commandWrap
def NURBSSmoothnessMediumOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NURBSSmoothnessMediumOptions(*args, **kwargs)
@commandWrap
def ExtendSurfacesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtendSurfacesOptions(*args, **kwargs)
@commandWrap
def CreatePolygonPlatonicOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePolygonPlatonicOptions(*args, **kwargs)
@commandWrap
def HideSculptObjects(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideSculptObjects(*args, **kwargs)
@commandWrap
def TangetConstraintOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TangetConstraintOptions(*args, **kwargs)
@commandWrap
def sbs_SetGlobalTextureHeight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_SetGlobalTextureHeight(*args, **kwargs)
@commandWrap
def ToggleUVTextureImage(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleUVTextureImage(*args, **kwargs)
@commandWrap
def SetMeshImprintTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshImprintTool(*args, **kwargs)
@commandWrap
def createNurbsConeCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.createNurbsConeCtx(*args, **kwargs)
@commandWrap
def TransferAttributes(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TransferAttributes(*args, **kwargs)
@commandWrap
def renderer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderer(*args, **kwargs)
@commandWrap
def CreateSetOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateSetOptions(*args, **kwargs)
@commandWrap
def DisableAll(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisableAll(*args, **kwargs)
@commandWrap
def ToggleIKAllowRotation(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleIKAllowRotation(*args, **kwargs)
@commandWrap
def MakeMotionField(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeMotionField(*args, **kwargs)
@commandWrap
def cMuscleRelaxSetup(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleRelaxSetup(*args, **kwargs)
@commandWrap
def SelectAllOutput(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectAllOutput(*args, **kwargs)
@commandWrap
def PerspTextureLayout(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PerspTextureLayout(*args, **kwargs)
@commandWrap
def xgmGeoRender(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmGeoRender(*args, **kwargs)
@commandWrap
def LatticeUVTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.LatticeUVTool(*args, **kwargs)
@commandWrap
def HypershadeDuplicateWithConnections(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDuplicateWithConnections(*args, **kwargs)
@commandWrap
def shadingGeometryRelCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.shadingGeometryRelCtx(*args, **kwargs)
@commandWrap
def EPCurveTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.EPCurveTool(*args, **kwargs)
@commandWrap
def PaintFluidsTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PaintFluidsTool(*args, **kwargs)
@commandWrap
def ProjectCurveOnMeshOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProjectCurveOnMeshOptions(*args, **kwargs)
@commandWrap
def artFluidAttrCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artFluidAttrCtx(*args, **kwargs)
@commandWrap
def AddOceanSurfaceLocator(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddOceanSurfaceLocator(*args, **kwargs)
@commandWrap
def xgmSyncPatchVisibility(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmSyncPatchVisibility(*args, **kwargs)
@commandWrap
def CreaseProxyEdgeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreaseProxyEdgeTool(*args, **kwargs)
@commandWrap
def nClothDeleteCacheFramesOpt(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothDeleteCacheFramesOpt(*args, **kwargs)
@commandWrap
def STRSTweakModeOff(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.STRSTweakModeOff(*args, **kwargs)
@commandWrap
def CoarsenSelectedComponents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CoarsenSelectedComponents(*args, **kwargs)
@commandWrap
def TogglePanZoomRelease(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TogglePanZoomRelease(*args, **kwargs)
@commandWrap
def renameAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renameAttr(*args, **kwargs)
@commandWrap
def CreateAmbientLightOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateAmbientLightOptions(*args, **kwargs)
@commandWrap
def TranslateToolWithSnapMarkingMenu(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TranslateToolWithSnapMarkingMenu(*args, **kwargs)
@commandWrap
def deleteNclothCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.deleteNclothCache(*args, **kwargs)
@commandWrap
def SelectBorderEdgeTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SelectBorderEdgeTool(*args, **kwargs)
@commandWrap
def HideSmoothSkinInfluences(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HideSmoothSkinInfluences(*args, **kwargs)
@commandWrap
def HypershadeSetSmallNodeSwatchSize(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeSetSmallNodeSwatchSize(*args, **kwargs)
@commandWrap
def SurfaceBooleanIntersectToolOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SurfaceBooleanIntersectToolOptions(*args, **kwargs)
@commandWrap
def FBXImportMergeAnimationLayers(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportMergeAnimationLayers(*args, **kwargs)
@commandWrap
def ProfilerToolHideSelectedRepetition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ProfilerToolHideSelectedRepetition(*args, **kwargs)
@commandWrap
def cMuscleCache(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.cMuscleCache(*args, **kwargs)
@commandWrap
def TesselateSubdivSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.TesselateSubdivSurface(*args, **kwargs)
@commandWrap
def nClothMakeCollide(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nClothMakeCollide(*args, **kwargs)
@commandWrap
def printStudio(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.printStudio(*args, **kwargs)
@commandWrap
def imagePlane(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.imagePlane(*args, **kwargs)
@commandWrap
def DeleteAllWires(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DeleteAllWires(*args, **kwargs)
@commandWrap
def ScaleCurvature(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ScaleCurvature(*args, **kwargs)
@commandWrap
def MakeUVInstanceCurrent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.MakeUVInstanceCurrent(*args, **kwargs)
@commandWrap
def ToggleOriginAxis(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleOriginAxis(*args, **kwargs)
@commandWrap
def FBXExportHardEdges(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXExportHardEdges(*args, **kwargs)
@commandWrap
def alignCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.alignCurve(*args, **kwargs)
@commandWrap
def editRenderLayerGlobals(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.editRenderLayerGlobals(*args, **kwargs)
@commandWrap
def SnapToMeshCenterPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SnapToMeshCenterPress(*args, **kwargs)
@commandWrap
def xgmClumpMap(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmClumpMap(*args, **kwargs)
@commandWrap
def GraphEditorFrameSelected(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorFrameSelected(*args, **kwargs)
@commandWrap
def RemoveJoint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RemoveJoint(*args, **kwargs)
@commandWrap
def DisplayShadingMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayShadingMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def ParentBaseWireOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ParentBaseWireOptions(*args, **kwargs)
@commandWrap
def AlembicImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AlembicImport(*args, **kwargs)
@commandWrap
def PickColorActivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PickColorActivate(*args, **kwargs)
@commandWrap
def ilrGetFileLayersCmd(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ilrGetFileLayersCmd(*args, **kwargs)
@commandWrap
def artAttr(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.artAttr(*args, **kwargs)
@commandWrap
def CreatePartitionOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreatePartitionOptions(*args, **kwargs)
@commandWrap
def CreateDagContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateDagContainer(*args, **kwargs)
@commandWrap
def OffsetCurveOnSurface(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OffsetCurveOnSurface(*args, **kwargs)
@commandWrap
def SetPassiveKey(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetPassiveKey(*args, **kwargs)
@commandWrap
def NodeEditorToggleSyncedSelection(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorToggleSyncedSelection(*args, **kwargs)
@commandWrap
def ShowFollicles(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowFollicles(*args, **kwargs)
@commandWrap
def jointLattice(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.jointLattice(*args, **kwargs)
@commandWrap
def SetFullBodyIKKeysOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetFullBodyIKKeysOptions(*args, **kwargs)
@commandWrap
def FilletBlendTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FilletBlendTool(*args, **kwargs)
@commandWrap
def PolyAssignSubdivHole(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyAssignSubdivHole(*args, **kwargs)
@commandWrap
def NodeEditorCreateTab(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.NodeEditorCreateTab(*args, **kwargs)
@commandWrap
def dR_viewLightsTGL(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_viewLightsTGL(*args, **kwargs)
@commandWrap
def CreateUVsBasedOnCameraOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateUVsBasedOnCameraOptions(*args, **kwargs)
@commandWrap
def ExtractSubdivSurfaceVerticesOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ExtractSubdivSurfaceVerticesOptions(*args, **kwargs)
@commandWrap
def XgmSplineGeometryConvert(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.XgmSplineGeometryConvert(*args, **kwargs)
@commandWrap
def dR_extrudeBevelPress(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_extrudeBevelPress(*args, **kwargs)
@commandWrap
def Snap3PointsTo3PointsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.Snap3PointsTo3PointsOptions(*args, **kwargs)
@commandWrap
def InsertKeyToolDeactivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.InsertKeyToolDeactivate(*args, **kwargs)
@commandWrap
def polyUVStackSimilarShells(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyUVStackSimilarShells(*args, **kwargs)
@commandWrap
def HypershadeDisplayAsIcons(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeDisplayAsIcons(*args, **kwargs)
@commandWrap
def manipOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.manipOptions(*args, **kwargs)
@commandWrap
def dR_convertSelectionToFace(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_convertSelectionToFace(*args, **kwargs)
@commandWrap
def polyPrism(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyPrism(*args, **kwargs)
@commandWrap
def AddKeyToolActivate(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddKeyToolActivate(*args, **kwargs)
@commandWrap
def RaiseApplicationWindows(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RaiseApplicationWindows(*args, **kwargs)
@commandWrap
def DisplayViewport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.DisplayViewport(*args, **kwargs)
@commandWrap
def GpuCacheExportAllOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GpuCacheExportAllOptions(*args, **kwargs)
@commandWrap
def SetMeshSprayTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SetMeshSprayTool(*args, **kwargs)
@commandWrap
def SmoothCurve(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.SmoothCurve(*args, **kwargs)
@commandWrap
def getLastError(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.getLastError(*args, **kwargs)
@commandWrap
def RenderIntoNewWindow(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RenderIntoNewWindow(*args, **kwargs)
@commandWrap
def CleanupPolygonOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CleanupPolygonOptions(*args, **kwargs)
@commandWrap
def containerBind(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.containerBind(*args, **kwargs)
@commandWrap
def polyTransfer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.polyTransfer(*args, **kwargs)
@commandWrap
def percent(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.percent(*args, **kwargs)
@commandWrap
def UVSnapTogether(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UVSnapTogether(*args, **kwargs)
@commandWrap
def xgmPartBrushContext(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.xgmPartBrushContext(*args, **kwargs)
@commandWrap
def contextInfo(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.contextInfo(*args, **kwargs)
@commandWrap
def CutCurveOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CutCurveOptions(*args, **kwargs)
@commandWrap
def FBXImportAutoAxisEnable(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.FBXImportAutoAxisEnable(*args, **kwargs)
@commandWrap
def HypershadeRefreshSelectedSwatches(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.HypershadeRefreshSelectedSwatches(*args, **kwargs)
@commandWrap
def RotateTool(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.RotateTool(*args, **kwargs)
@commandWrap
def saveFluid(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.saveFluid(*args, **kwargs)
@commandWrap
def animCurveEditor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.animCurveEditor(*args, **kwargs)
@commandWrap
def ToggleEvaluationManagerVisibility(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ToggleEvaluationManagerVisibility(*args, **kwargs)
@commandWrap
def ConnectComponentsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ConnectComponentsOptions(*args, **kwargs)
@commandWrap
def PixelMoveDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PixelMoveDown(*args, **kwargs)
@commandWrap
def renderPartition(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.renderPartition(*args, **kwargs)
@commandWrap
def optionVar(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.optionVar(*args, **kwargs)
@commandWrap
def ambientLight(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ambientLight(*args, **kwargs)
@commandWrap
def ShowResultsOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.ShowResultsOptions(*args, **kwargs)
@commandWrap
def bakeDeformer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bakeDeformer(*args, **kwargs)
@commandWrap
def CreateFluidCacheOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateFluidCacheOptions(*args, **kwargs)
@commandWrap
def subdDuplicateAndConnect(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.subdDuplicateAndConnect(*args, **kwargs)
@commandWrap
def PolyExtrude(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolyExtrude(*args, **kwargs)
@commandWrap
def CreateCameraAimOptions(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateCameraAimOptions(*args, **kwargs)
@commandWrap
def OrientConstraint(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.OrientConstraint(*args, **kwargs)
@commandWrap
def AddToCurrentSceneMudbox(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddToCurrentSceneMudbox(*args, **kwargs)
@commandWrap
def GraphEditorFramePlaybackRange(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.GraphEditorFramePlaybackRange(*args, **kwargs)
@commandWrap
def hotkeyMapSet(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.hotkeyMapSet(*args, **kwargs)
@commandWrap
def PolygonApplyColor(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.PolygonApplyColor(*args, **kwargs)
@commandWrap
def AutobindContainer(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AutobindContainer(*args, **kwargs)
@commandWrap
def keyframeRegionSelectKeyCtx(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.keyframeRegionSelectKeyCtx(*args, **kwargs)
@commandWrap
def nurbsToSubdiv(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.nurbsToSubdiv(*args, **kwargs)
@commandWrap
def UIModeMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UIModeMarkingMenuPopDown(*args, **kwargs)
@commandWrap
def CreateConstraintClip(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.CreateConstraintClip(*args, **kwargs)
@commandWrap
def dR_createCameraFromView(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.dR_createCameraFromView(*args, **kwargs)
@commandWrap
def sbs_GetEnumName(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.sbs_GetEnumName(*args, **kwargs)
@commandWrap
def AddInbetween(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.AddInbetween(*args, **kwargs)
@commandWrap
def bifMeshImport(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.bifMeshImport(*args, **kwargs)
@commandWrap
def UnifyTangents(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.UnifyTangents(*args, **kwargs)
@commandWrap
def KeyframeTangentMarkingMenuPopDown(*args, **kwargs):
    u""":rtype: list|str|DagNode|AttrObject|ArrayAttrObject|Components1Base"""
    return cmds.KeyframeTangentMarkingMenuPopDown(*args, **kwargs)
@commandWrap
@listWrap
def listInputDevices(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listInputDevices(*args, **kwargs)
@commandWrap
@listWrap
def listAttr(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listAttr(*args, **kwargs)
@commandWrap
@listWrap
def listDeviceAttachments(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listDeviceAttachments(*args, **kwargs)
@commandWrap
@listWrap
def listConnections(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listConnections(*args, **kwargs)
@commandWrap
@listWrap
def listCameras(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listCameras(*args, **kwargs)
@commandWrap
@listWrap
def listRelatives(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listRelatives(*args, **kwargs)
@commandWrap
@listWrap
def listInputDeviceButtons(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listInputDeviceButtons(*args, **kwargs)
@commandWrap
@listWrap
def listInputDeviceAxes(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listInputDeviceAxes(*args, **kwargs)
@commandWrap
@listWrap
def listSets(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listSets(*args, **kwargs)
@commandWrap
@listWrap
def listAnimatable(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listAnimatable(*args, **kwargs)
@commandWrap
@listWrap
def listAttrPatterns(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listAttrPatterns(*args, **kwargs)
@commandWrap
@listWrap
def listNodeTypes(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listNodeTypes(*args, **kwargs)
@commandWrap
@listWrap
def listNodesWithIncorrectNames(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listNodesWithIncorrectNames(*args, **kwargs)
@commandWrap
@listWrap
def listHistory(*args, **kwargs):
    u""":rtype: list"""
    return cmds.listHistory(*args, **kwargs)
@uiCommandWrap
def saveShelf(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.saveShelf(*args, **kwargs)
@uiCommandWrap
def saveAllShelves(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.saveAllShelves(*args, **kwargs)
@uiCommandWrap
def hyperGraph(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hyperGraph(*args, **kwargs)
@uiCommandWrap
def gradientControlNoAttr(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.gradientControlNoAttr(*args, **kwargs)
@uiCommandWrap
def menuBarLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.menuBarLayout(*args, **kwargs)
@uiCommandWrap
def text(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.text(*args, **kwargs)
@uiCommandWrap
def soundControl(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.soundControl(*args, **kwargs)
@uiCommandWrap
def channelBox(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.channelBox(*args, **kwargs)
@uiCommandWrap
def flowLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.flowLayout(*args, **kwargs)
@uiCommandWrap
def toggleWindowVisibility(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.toggleWindowVisibility(*args, **kwargs)
@uiCommandWrap
def webBrowserPrefs(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.webBrowserPrefs(*args, **kwargs)
@uiCommandWrap
def menuEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.menuEditor(*args, **kwargs)
@uiCommandWrap
def thumbnailCaptureComponent(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.thumbnailCaptureComponent(*args, **kwargs)
@uiCommandWrap
def iconTextStaticLabel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.iconTextStaticLabel(*args, **kwargs)
@uiCommandWrap
def shelfButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.shelfButton(*args, **kwargs)
@uiCommandWrap
def disableIncorrectNameWarning(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.disableIncorrectNameWarning(*args, **kwargs)
@uiCommandWrap
def layout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.layout(*args, **kwargs)
@uiCommandWrap
def saveViewportSettings(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.saveViewportSettings(*args, **kwargs)
@uiCommandWrap
def menu(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.menu(*args, **kwargs)
@uiCommandWrap
def hotBox(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hotBox(*args, **kwargs)
@uiCommandWrap
def componentBox(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.componentBox(*args, **kwargs)
@uiCommandWrap
def rowColumnLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.rowColumnLayout(*args, **kwargs)
@uiCommandWrap
def iconTextRadioCollection(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.iconTextRadioCollection(*args, **kwargs)
@uiCommandWrap
def window(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.window(*args, **kwargs)
@uiCommandWrap
def iconTextRadioButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.iconTextRadioButton(*args, **kwargs)
@uiCommandWrap
def hotkeyCheck(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hotkeyCheck(*args, **kwargs)
@uiCommandWrap
def confirmDialog(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.confirmDialog(*args, **kwargs)
@uiCommandWrap
def attrNavigationControlGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attrNavigationControlGrp(*args, **kwargs)
@uiCommandWrap
def rangeControl(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.rangeControl(*args, **kwargs)
@uiCommandWrap
def gradientControl(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.gradientControl(*args, **kwargs)
@uiCommandWrap
def helpLine(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.helpLine(*args, **kwargs)
@uiCommandWrap
def setNodeTypeFlag(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.setNodeTypeFlag(*args, **kwargs)
@uiCommandWrap
def layerButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.layerButton(*args, **kwargs)
@uiCommandWrap
def callbacks(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.callbacks(*args, **kwargs)
@uiCommandWrap
def scriptEditorInfo(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.scriptEditorInfo(*args, **kwargs)
@uiCommandWrap
def layoutDialog(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.layoutDialog(*args, **kwargs)
@uiCommandWrap
def floatFieldGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.floatFieldGrp(*args, **kwargs)
@uiCommandWrap
def button(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.button(*args, **kwargs)
@uiCommandWrap
def floatField(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.floatField(*args, **kwargs)
@uiCommandWrap
def palettePort(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.palettePort(*args, **kwargs)
@uiCommandWrap
def webBrowser(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.webBrowser(*args, **kwargs)
@uiCommandWrap
def scrollLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.scrollLayout(*args, **kwargs)
@uiCommandWrap
def gridLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.gridLayout(*args, **kwargs)
@uiCommandWrap
def intFieldGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.intFieldGrp(*args, **kwargs)
@uiCommandWrap
def textField(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.textField(*args, **kwargs)
@uiCommandWrap
def formLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.formLayout(*args, **kwargs)
@uiCommandWrap
def toolCollection(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.toolCollection(*args, **kwargs)
@uiCommandWrap
def iconTextCheckBox(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.iconTextCheckBox(*args, **kwargs)
@uiCommandWrap
def textScrollList(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.textScrollList(*args, **kwargs)
@uiCommandWrap
def floatScrollBar(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.floatScrollBar(*args, **kwargs)
@uiCommandWrap
def workspaceControlState(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.workspaceControlState(*args, **kwargs)
@uiCommandWrap
def spreadSheetEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.spreadSheetEditor(*args, **kwargs)
@uiCommandWrap
def textManip(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.textManip(*args, **kwargs)
@uiCommandWrap
def createEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.createEditor(*args, **kwargs)
@uiCommandWrap
def paneLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.paneLayout(*args, **kwargs)
@uiCommandWrap
def checkBoxGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.checkBoxGrp(*args, **kwargs)
@uiCommandWrap
def symbolButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.symbolButton(*args, **kwargs)
@uiCommandWrap
def nodeEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.nodeEditor(*args, **kwargs)
@uiCommandWrap
def canvas(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.canvas(*args, **kwargs)
@uiCommandWrap
def intScrollBar(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.intScrollBar(*args, **kwargs)
@uiCommandWrap
def floatSlider(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.floatSlider(*args, **kwargs)
@uiCommandWrap
def hudButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hudButton(*args, **kwargs)
@uiCommandWrap
def treeLister(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.treeLister(*args, **kwargs)
@uiCommandWrap
def scriptedPanelType(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.scriptedPanelType(*args, **kwargs)
@uiCommandWrap
def overrideModifier(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.overrideModifier(*args, **kwargs)
@uiCommandWrap
def messageLine(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.messageLine(*args, **kwargs)
@uiCommandWrap
def optionMenu(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.optionMenu(*args, **kwargs)
@uiCommandWrap
def menuSetPref(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.menuSetPref(*args, **kwargs)
@uiCommandWrap
def textFieldGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.textFieldGrp(*args, **kwargs)
@uiCommandWrap
def cmdShell(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.cmdShell(*args, **kwargs)
@uiCommandWrap
def setStartupMessage(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.setStartupMessage(*args, **kwargs)
@uiCommandWrap
def timeControl(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.timeControl(*args, **kwargs)
@uiCommandWrap
def progressBar(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.progressBar(*args, **kwargs)
@uiCommandWrap
def intField(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.intField(*args, **kwargs)
@uiCommandWrap
def multiTouch(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.multiTouch(*args, **kwargs)
@uiCommandWrap
def grabColor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.grabColor(*args, **kwargs)
@uiCommandWrap
def menuItem(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.menuItem(*args, **kwargs)
@uiCommandWrap
def windowPref(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.windowPref(*args, **kwargs)
@uiCommandWrap
def scriptTable(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.scriptTable(*args, **kwargs)
@uiCommandWrap
def panel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.panel(*args, **kwargs)
@uiCommandWrap
def fontDialog(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.fontDialog(*args, **kwargs)
@uiCommandWrap
def cmdScrollFieldExecuter(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.cmdScrollFieldExecuter(*args, **kwargs)
@uiCommandWrap
def attrFieldGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attrFieldGrp(*args, **kwargs)
@uiCommandWrap
def scriptedPanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.scriptedPanel(*args, **kwargs)
@uiCommandWrap
def separator(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.separator(*args, **kwargs)
@uiCommandWrap
def canCreateCaddyManip(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.canCreateCaddyManip(*args, **kwargs)
@uiCommandWrap
def timePort(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.timePort(*args, **kwargs)
@uiCommandWrap
def progressWindow(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.progressWindow(*args, **kwargs)
@uiCommandWrap
def timeField(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.timeField(*args, **kwargs)
@uiCommandWrap
def hyperPanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hyperPanel(*args, **kwargs)
@uiCommandWrap
def nameCommand(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.nameCommand(*args, **kwargs)
@uiCommandWrap
def falloffCurveAttr(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.falloffCurveAttr(*args, **kwargs)
@uiCommandWrap
def attributeMenu(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attributeMenu(*args, **kwargs)
@uiCommandWrap
def minimizeApp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.minimizeApp(*args, **kwargs)
@uiCommandWrap
def loadUI(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.loadUI(*args, **kwargs)
@uiCommandWrap
def refreshEditorTemplates(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.refreshEditorTemplates(*args, **kwargs)
@uiCommandWrap
def image(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.image(*args, **kwargs)
@uiCommandWrap
def hotkeyCtx(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hotkeyCtx(*args, **kwargs)
@uiCommandWrap
def panelConfiguration(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.panelConfiguration(*args, **kwargs)
@uiCommandWrap
def annotate(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.annotate(*args, **kwargs)
@uiCommandWrap
def hotkey(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hotkey(*args, **kwargs)
@uiCommandWrap
def colorIndexSliderGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.colorIndexSliderGrp(*args, **kwargs)
@uiCommandWrap
def iconTextScrollList(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.iconTextScrollList(*args, **kwargs)
@uiCommandWrap
def rowLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.rowLayout(*args, **kwargs)
@uiCommandWrap
def defaultNavigation(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.defaultNavigation(*args, **kwargs)
@uiCommandWrap
def contentBrowser(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.contentBrowser(*args, **kwargs)
@uiCommandWrap
def tabLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.tabLayout(*args, **kwargs)
@uiCommandWrap
def scrollField(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.scrollField(*args, **kwargs)
@uiCommandWrap
def hyperShade(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hyperShade(*args, **kwargs)
@uiCommandWrap
def nodeOutliner(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.nodeOutliner(*args, **kwargs)
@uiCommandWrap
def outlinerEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.outlinerEditor(*args, **kwargs)
@uiCommandWrap
def commandLine(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.commandLine(*args, **kwargs)
@uiCommandWrap
def radioButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.radioButton(*args, **kwargs)
@uiCommandWrap
def promptDialog(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.promptDialog(*args, **kwargs)
@uiCommandWrap
def editor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.editor(*args, **kwargs)
@uiCommandWrap
def showSelectionInTitle(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.showSelectionInTitle(*args, **kwargs)
@uiCommandWrap
def inViewMessage(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.inViewMessage(*args, **kwargs)
@uiCommandWrap
def nodeTreeLister(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.nodeTreeLister(*args, **kwargs)
@uiCommandWrap
def treeView(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.treeView(*args, **kwargs)
@uiCommandWrap
def colorEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.colorEditor(*args, **kwargs)
@uiCommandWrap
def buttonManip(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.buttonManip(*args, **kwargs)
@uiCommandWrap
def attrFieldSliderGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attrFieldSliderGrp(*args, **kwargs)
@uiCommandWrap
def inViewEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.inViewEditor(*args, **kwargs)
@uiCommandWrap
def editorTemplate(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.editorTemplate(*args, **kwargs)
@uiCommandWrap
def shelfTabLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.shelfTabLayout(*args, **kwargs)
@uiCommandWrap
def attrEnumOptionMenuGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attrEnumOptionMenuGrp(*args, **kwargs)
@uiCommandWrap
def floatSliderButtonGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.floatSliderButtonGrp(*args, **kwargs)
@uiCommandWrap
def timeFieldGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.timeFieldGrp(*args, **kwargs)
@uiCommandWrap
def componentEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.componentEditor(*args, **kwargs)
@uiCommandWrap
def dockControl(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.dockControl(*args, **kwargs)
@uiCommandWrap
def mayaDpiSetting(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.mayaDpiSetting(*args, **kwargs)
@uiCommandWrap
def setFocus(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.setFocus(*args, **kwargs)
@uiCommandWrap
def headsUpDisplay(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.headsUpDisplay(*args, **kwargs)
@uiCommandWrap
def radioCollection(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.radioCollection(*args, **kwargs)
@uiCommandWrap
def setMenuMode(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.setMenuMode(*args, **kwargs)
@uiCommandWrap
def popupMenu(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.popupMenu(*args, **kwargs)
@uiCommandWrap
def attrControlGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attrControlGrp(*args, **kwargs)
@uiCommandWrap
def columnLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.columnLayout(*args, **kwargs)
@uiCommandWrap
def workspacePanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.workspacePanel(*args, **kwargs)
@uiCommandWrap
def workspaceControl(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.workspaceControl(*args, **kwargs)
@uiCommandWrap
def modelPanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.modelPanel(*args, **kwargs)
@uiCommandWrap
def falloffCurve(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.falloffCurve(*args, **kwargs)
@uiCommandWrap
def intSliderGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.intSliderGrp(*args, **kwargs)
@uiCommandWrap
def colorSliderButtonGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.colorSliderButtonGrp(*args, **kwargs)
@uiCommandWrap
def panelHistory(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.panelHistory(*args, **kwargs)
@uiCommandWrap
def control(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.control(*args, **kwargs)
@uiCommandWrap
def hudSlider(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hudSlider(*args, **kwargs)
@uiCommandWrap
def savePrefObjects(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.savePrefObjects(*args, **kwargs)
@uiCommandWrap
def swatchDisplayPort(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.swatchDisplayPort(*args, **kwargs)
@uiCommandWrap
def hotkeySet(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hotkeySet(*args, **kwargs)
@uiCommandWrap
def floatSliderGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.floatSliderGrp(*args, **kwargs)
@uiCommandWrap
def autoPlace(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.autoPlace(*args, **kwargs)
@uiCommandWrap
def attrColorSliderGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attrColorSliderGrp(*args, **kwargs)
@uiCommandWrap
def workspaceLayoutManager(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.workspaceLayoutManager(*args, **kwargs)
@uiCommandWrap
def colorInputWidgetGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.colorInputWidgetGrp(*args, **kwargs)
@uiCommandWrap
def outlinerPanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.outlinerPanel(*args, **kwargs)
@uiCommandWrap
def linearPrecision(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.linearPrecision(*args, **kwargs)
@uiCommandWrap
def floatSlider2(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.floatSlider2(*args, **kwargs)
@uiCommandWrap
def radioButtonGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.radioButtonGrp(*args, **kwargs)
@uiCommandWrap
def iconTextButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.iconTextButton(*args, **kwargs)
@uiCommandWrap
def hardwareRenderPanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hardwareRenderPanel(*args, **kwargs)
@uiCommandWrap
def savePrefs(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.savePrefs(*args, **kwargs)
@uiCommandWrap
def shelfLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.shelfLayout(*args, **kwargs)
@uiCommandWrap
def radioMenuItemCollection(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.radioMenuItemCollection(*args, **kwargs)
@uiCommandWrap
def headsUpMessage(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.headsUpMessage(*args, **kwargs)
@uiCommandWrap
def colorSliderGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.colorSliderGrp(*args, **kwargs)
@uiCommandWrap
def nameField(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.nameField(*args, **kwargs)
@uiCommandWrap
def viewManip(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.viewManip(*args, **kwargs)
@uiCommandWrap
def menuSet(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.menuSet(*args, **kwargs)
@uiCommandWrap
def artBuildPaintMenu(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.artBuildPaintMenu(*args, **kwargs)
@uiCommandWrap
def visor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.visor(*args, **kwargs)
@uiCommandWrap
def modelEditor(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.modelEditor(*args, **kwargs)
@uiCommandWrap
def picture(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.picture(*args, **kwargs)
@uiCommandWrap
def switchTable(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.switchTable(*args, **kwargs)
@uiCommandWrap
def textFieldButtonGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.textFieldButtonGrp(*args, **kwargs)
@uiCommandWrap
def getPanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.getPanel(*args, **kwargs)
@uiCommandWrap
def loadPrefObjects(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.loadPrefObjects(*args, **kwargs)
@uiCommandWrap
def optionMenuGrp(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.optionMenuGrp(*args, **kwargs)
@uiCommandWrap
def intSlider(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.intSlider(*args, **kwargs)
@uiCommandWrap
def scmh(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.scmh(*args, **kwargs)
@uiCommandWrap
def hotkeyEditorPanel(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hotkeyEditorPanel(*args, **kwargs)
@uiCommandWrap
def checkBox(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.checkBox(*args, **kwargs)
@uiCommandWrap
def toolButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.toolButton(*args, **kwargs)
@uiCommandWrap
def attrEnumOptionMenu(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.attrEnumOptionMenu(*args, **kwargs)
@uiCommandWrap
def saveMenu(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.saveMenu(*args, **kwargs)
@uiCommandWrap
def frameLayout(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.frameLayout(*args, **kwargs)
@uiCommandWrap
def symbolCheckBox(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.symbolCheckBox(*args, **kwargs)
@uiCommandWrap
def showWindow(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.showWindow(*args, **kwargs)
@uiCommandWrap
def hudSliderButton(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.hudSliderButton(*args, **kwargs)
@uiCommandWrap
def cmdScrollFieldReporter(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.cmdScrollFieldReporter(*args, **kwargs)
@uiCommandWrap
def toolBar(*args, **kwargs):
    u"""
    :rtype: UIObject
    """
    return cmds.toolBar(*args, **kwargs)

__all__ = ["insertListItem", "RenderSequence", "lookThru", "SurfaceFlow", "ClosestPointOn", "NodeEditorRestoreLastClosedTab", "pixelMove", "DeleteAllNRigids", "AddPondDynamicLocator", "pointCloudInfo", "RemoveWire", "PolyExtrudeVertices", "HypershadeGraphRearrange", "BevelPolygon", "IKHandleTool", "geometryReplaceCacheFramesOpt", "SubstituteGeometryOptions", "colorAtPoint", "blendCtx", "clearCache", "dR_viewLeft", "textureDeformer", "CreateHairOptions", "XgCreateIgSplineEditor", "polyDelVertex", "NodeEditorDeleteNodes", "OutlinerToggleTimeEditor", "pointLight", "XgPreview", "polyBoolOp", "SelectShortestEdgePathTool", "LightCentricLightLinkingEditor", "dR_gridAllTGL", "TogglePanZoomPress", "ToggleIKAllowRotation", "UVCameraBasedProjection", "xformConstraint", "copyKey", "dgtimer", "NodeEditorGraphDownstream", "ProfilerToolCpuView", "polyInfo", "ProfilerToolReset", "dR_selectModeDisableTweakMarquee", "QualityDisplayMarkingMenuPopDown", "dR_moveTweakTool", "floatSliderGrp", "ScaleKeys", "XgmSplineSelectReplaceBySelectedFaces", "PinSelection", "PerspGraphOutlinerLayout", "CreateIllustratorCurves", "UVPlanarProjectionOptions", "DoUnghost", "AddOceanPreviewPlane", "BreakLightLinks", "CreateContainerOptions", "CreateClusterOptions", "softSelectOptionsCtx", "ctxTraverse", "TangentsClamped", "dR_extrudeTool", "HypershadeRefreshAllSwatchesOnDisk", "deformerWeights", "dR_curveSnapPress", "dR_nexCmd", "PreInfinityCycleOffset", "polyPipe", "xgmBindPatches", "TogglePaintAtDepth", "CreatePond", "bevelPlus", "STRSTweakModeOff", "BatchRenderOptions", "adskAssetListUI", "tangentConstraint", "dispatchGenericCommand", "iconTextStaticLabel", "HypershadeReduceTraversalDepth", "HypershadeGraphClearGraph", "XgmSetSmoothBrushTool", "CreatePolygonSVG", "EnterEditModeRelease", "hide", "itemFilterType", "RandomizeFolliclesOptions", "suitePrefs", "OpenScene", "duplicate", "WarpImageOptions", "SelectSimilarOptions", "XgmSplineCacheReplace", "StitchEdgesToolOptions", "allNodeTypes", "dR_targetWeldPress", "GoalOptions", "nurbsUVSet", "NodeEditorRedockTornOffTab", "SelectAllLights", "CreateEmitter", "CombinePolygons", "dR_moveRelease", "AddKeysToolOptions", "duplicateSurface", "CreatePolygonCubeOptions", "IntersectCurve", "nClothDeleteHistory", "SewUVs", "SelectUVOverlappingComponentsPerObject", "undo", "TimeEditorUnmuteAllTracks", "WireDropoffLocator", "FBXResetImport", "GhostObject", "NodeEditorPickWalkUp", "AddDivisionsOptions", "colorInputWidgetGrp", "RemoveBlendShape", "ThreeBottomSplitViewArrangement", "attrFieldGrp", "NodeEditorGridToggleVisibility", "FullHotboxDisplay", "NextKey", "CreatePolygonCone", "BufferCurveSnapshot", "ProjectTangent", "curveOnSurface", "DeltaMush", "ConvertSelectionToVertices", "RoundTool", "iconTextCheckBox", "HideFluids", "ProjectCurveOnSurfaceOptions", "notifyPostRedo", "Group", "setInputDeviceMapping", "HypershadeDisplayNoShapes", "xgmGroomConvert", "renderPartition", "CreatePolygonUltraShape", "shapePanel", "DeleteChannels", "jointLattice", "PublishNode", "SelectAllImagePlanes", "NodeEditorReduceTraversalDepth", "ShowDeformers", "IPRRenderIntoNewWindow", "InteractiveBindSkinOptions", "LassoTool", "FlareOptions", "ParticleToolOptions", "particleInstancer", "ProfilerToolToggleRecording", "AttachCurve", "radioButton", "FilePathEditor", "adskSceneMetadataCmd", "addMetadata", "replaceCacheFrames", "BakeSpringAnimation", "MoveRotateScaleToolToggleSnapRelativeMode", "findDeformers", "SetFocusToCommandLine", "CreateGhostOptions", "ShapeEditorDuplicateTarget", "HypershadeMoveTabUp", "buttonManip", "ScriptPaintToolOptions", "PlaybackToggle", "dynSelectCtx", "DeleteAllControllers", "UnpublishRootTransform", "UVCentricUVLinkingEditor", "NewSceneOptions", "SurfaceBooleanUnionToolOptions", "nurbsCurveToBezier", "referenceEdit", "polyMirrorFace", "SubdivProxyOptions", "xgmSplinePreset", "OutlinerRenameSelectedItem", "dR_rotateRelease", "art3dPaintCtx", "DisableGlobalStitch", "PolygonHardenEdge", "perCameraVisibility", "setFocus", "CreateHairCache", "TranslateToolWithSnapMarkingMenuPopDown", "FourViewLayout", "CameraModeOrthographic", "NodeEditorConnectionStyleCorner", "ilrImportVertexColorsCmd", "curveBezierCtx", "DeleteAllClusters", "RemoveBrushSharing", "nucleusGetnClothExample", "TimeEditorRippleEditTogglePress", "sets", "ToggleLayerBar", "polyPinUV", "ShowNURBSCurves", "NodeEditorCopy", "ilrHwBakeVisualizerCmd", "NodeEditorToggleNodeTitleMode", "PaintOperationMarkingMenuPress", "SelectIsolate", "ConvertSelectionToUVBorder", "ConvertSelectionToContainedFaces", "DecreaseExposureCoarse", "NodeEditorCreateIterateCompound", "ApplySettingsToLastStroke", "RaiseMainWindow", "DetachVertexComponent", "CreateConstraintOptions", "dR_conform", "STRSTweakModeOn", "listInputDevices", "WrinkleTool", "ShowNRigids", "SculptMeshUnfreezeAll", "ShowHairSystems", "RigidBindSkinOptions", "HypershadeOpenBinsWindow", "polyColorDel", "CreatePolygonGearOptions", "SelectUVNonOverlappingComponentsPerObject", "DisplayIntermediateObjects", "ShowNCloths", "MergeVertices", "ConnectNodeToIKFK", "hikRigAlign", "hikManip", "polyCollapseEdge", "CreateSculptDeformerOptions", "CreatePolygonPyramidOptions", "GraphCopy", "TangentsFlat", "timeEditorTracks", "FlipTubeDirection", "AnimLayerRelationshipEditor", "hotkeyCtx", "dR_viewBack", "imageWindowEditor", "HypershadeDisplayAsList", "AddSelectionAsCombinationTarget", "CopySkinWeightsOptions", "CreateCurveFromPoly", "Vortex", "texScaleContext", "stringArrayIntersector", "ToggleShelf", "BakeSpringAnimationOptions", "CreateOcean", "SnapToCurve", "RotateToolMarkingMenuPopDown", "NonSacredTool", "transferShadingSets", "AddBifrostGuide", "ReversePolygonNormalsOptions", "DisableTimeChangeUndoConsolidation", "GraphEditorNormalizedView", "singleProfileBirailSurface", "stitchSurfacePoints", "PolyExtrudeFaces", "trackCtx", "ProfilerToolShowSelected", "NURBSSmoothnessFineOptions", "dR_activeHandleXYZ", "EnableParticles", "subdLayoutUV", "u3dTopoValid", "AssignHairConstraintOptions", "CustomPolygonDisplay", "loadPlugin", "PointOnPolyConstraintOptions", "OneClickAcknowledge", "CreateDirectionalLightOptions", "thumbnailCaptureComponent", "EnableAll", "nearestPointOnMesh", "CreateSubCharacter", "showManipCtx", "SurfaceFlowOptions", "vectorize", "OutlinerToggleAssignedMaterials", "CreatePolygonSphericalHarmonicsOptions", "applyTake", "DeleteAllNParticles", "TestTextureOptions", "HypershadeOpenBrowserWindow", "polyDelEdge", "SelectSimilar", "clipMatching", "GetProperty2StateAttrNameFromHIKEffectorId", "NormalizeUVsOptions", "condition", "makebot", "surfaceShaderList", "makeLive", "fluidDeleteCacheFrames", "dR_movePress", "TimeEditorClipScaleStart", "RepeatLastActionAtMousePosition", "AnimationSweep", "CutCurve", "matchTransform", "DeleteAttribute", "polySplitCtx", "snapTogetherCtx", "gradientControl", "FrameSelected", "TimeEditorSceneAuthoringToggle", "BakeNonDefHistoryOptions", "DecreaseCheckerDensity", "ChangeEdgeWidth", "ModifyPaintValuePress", "confirmDialog", "HypershadeGraphRemoveSelected", "BakeCustomPivotOptions", "AddBifrostCamera", "scaleKey", "nClothCacheOpt", "deleteAttr", "extrude", "addAttr", "WireTool", "setKeyCtx", "pathAnimation", "StraightenUVBorder", "createPolySphereCtx", "TogglePolyNonPlanarFaceDisplay", "CreateRigidBodySolver", "flagTest", "ShatterOptions", "MirrorSkinWeights", "ToggleVisibilityAndKeepSelectionOptions", "iterOnNurbs", "CreatePolygonSoccerBallOptions", "UVCreateSnapshot", "ShowAttributeEditorOrChannelBox", "CreateMotionTrail", "PaintEffectsToolOptions", "HardwareRenderBuffer", "LoadHIKPropertySetState", "ShowShadingGroupAttributeEditor", "readTake", "GraphEditorAbsoluteView", "HypershadePinSelected", "renderThumbnailUpdate", "ShowMeshImprintToolOptions", "CopySkinWeights", "CurveSmoothnessRough", "HIKFullBodyMode", "popListItem", "ToggleModelingToolkit", "containerTemplate", "TransferAttributeValuesOptions", "polyListComponentConversion", "HypershadeGraphAddSelected", "nClothReplaceFrames", "ToggleKeepHardEdgeCulling", "TransformNoSelectOffTool", "keyframeRegionCurrentTimeCtx", "TimeEditorClipTrimStart", "xgmSelectedPrims", "HypershadeMoveTabRight", "dR_vertSelectLocked", "SelectToolMarkingMenuPopDown", "dR_extrudeBevelRelease", "AddPondDynamicBuoy", "FBXExportReferencedAssetsContent", "SelectUVNonOverlappingComponents", "RegionKeysTool", "GpuCacheExportSelection", "ExportOfflineFileFromRefEd", "ToggleLatticePoints", "ToggleFaceMetadata", "OutTangentAuto", "scaleKeyCtx", "floatSlider", "SetVertexNormal", "xgmPartBrushToolCmd", "NodeEditorCreateCompound", "PolygonBooleanDifference", "ToggleBorderEdges", "CreateNURBSCubeOptions", "polyMergeFacet", "connectDynamic", "polyMergeEdge", "movieInfo", "ToggleAttributeEditor", "ToggleToolSettings", "ReattachSkeletonJoints", "nexTRSContext", "CharacterAnimationEditor", "EnableNucleuses", "ikSplineHandleCtx", "nurbsBoolean", "CreatePolyFromPreview", "CreateConstraintClipOptions", "SetBifrostInitialState", "dR_meshColorOverrideTGL", "editDisplayLayerMembers", "UngroupOptions", "PositionAlongCurve", "dR_connectTool", "invertShape", "NCreateEmitter", "ShowCameraManipulators", "scriptedPanel", "SmoothingLevelIncrease", "nClothMakeCollideOptions", "SelectUVMask", "ToggleXGenDisplayHUD", "copyFlexor", "InitialFluidStates", "xgmMelRender", "GraphEditorDisplayTangentActive", "SelectToggleMode", "isolateSelect", "xgmGuideGeom", "SculptGeometryTool", "HyperGraphPanelRedoViewChange", "BifMeshExport", "GridUVOptions", "UpdateReferenceSurface", "reorderDeformers", "NormalizeUVs", "Snap2PointsTo2PointsOptions", "ImportWorkspaceFiles", "SaveScene", "CreatePose", "ShowMarkers", "OutlinerExpandAllSelectedItems", "ConvertSelectionToUVPerimeter", "OutlinerToggleShapes", "MapUVBorderOptions", "MoveSewUVs", "polyAutoProjection", "PreviousFrame", "NodeEditorAddIterationStatePorts", "FBXPushSettings", "globalStitch", "ShowMeshSculptToolOptions", "TogglePolyDisplayHardEdgesColor", "dR_modeUV", "CharacterSetEditor", "DuplicateNURBSPatchesOptions", "ilrRenderCmd", "HypershadeOpenSpreadSheetWindow", "ReferenceEditor", "angleBetween", "NParticleToolOptions", "PrevSkinPaintMode", "RedoPreviousIPRRender", "VisualizeMetadataOptions", "getParticleAttr", "ShapeEditor", "ToggleMeshFaces", "ToggleCurrentContainerHud", "fontDialog", "GetFKIdFromEffectorId", "HypershadeSortByTime", "xgmSplineSelect", "texMoveUVShellContext", "attrEnumOptionMenuGrp", "GetHIKMatrixDecomposition", "layoutDialog", "nurbsEditUV", "ResetTransformations", "AssignHairConstraint", "ResampleCurve", "syncSculptCache", "PolygonSelectionConstraints", "ShapeEditorNewGroup", "dgdirty", "DeleteKeys", "DuplicateFaceOptions", "polyProjection", "paintPointsContext", "IncreaseGammaCoarse", "toggleDisplacement", "mayaDpiSetting", "HypershadeToggleNodeTitleMode", "ConvertSelectionToFacePerimeter", "AddToContainerOptions", "dR_objectTemplateTGL", "workspaceControl", "FreeformFilletOptions", "CreatePolygonSphericalHarmonics", "OpenCloseCurveOptions", "inViewEditor", "dR_objectEdgesOnlyTGL", "GraphEditorLockChannel", "UnitizeUVs", "shadingLightRelCtx", "SetInitialStateOptions", "NURBSTexturePlacementTool", "CreaseProxyEdgeToolOptions", "MakeBoatsOptions", "UndoViewChange", "UVPlanarProjection", "EPCurveToolOptions", "ToggleBackfaceCulling", "DisconnectJoint", "XgCreateDescription", "editDisplayLayerGlobals", "ToggleObjectDetails", "nClothMakeCollide", "PaintFluidsToolOptions", "PublishRootTransformOptions", "FBXProperties", "HypershadeConvertToFileTextureOptionBox", "editRenderLayerMembers", "ilrHwTextureCacheCmd", "setParticleAttr", "dR_showOptions", "ToggleShowBufferCurves", "menuItem", "xgmSelectBrushToolCmd", "ikSpringSolverCallbacks", "unknownNode", "SmoothingLevelDecrease", "scaleComponents", "translator", "simplify", "assignShaderToType", "ToggleFrameRate", "HideNRigids", "DetachSurfacesOptions", "HideCameraManipulators", "XgmSetCombBrushToolOption", "xgmPoints", "ShowMeshAmplifyToolOptions", "ParticleFill", "listCameras", "threePointArcCtx", "subdMapCut", "NodeEditorUnpinSelected", "TimeEditorAddToSoloSelectedTracks", "partition", "flow", "CreateReferenceOptions", "dgPerformance", "polyCreateFacet", "ToggleTextureBorderEdges", "xgmSetArchiveSize", "polyBlendColor", "polyWedgeFace", "ShowNonlinears", "ConformPolygonOptions", "encodeString", "hotkeySet", "InsertKnotOptions", "ImportOptions", "IntersectCurveOptions", "PickWalkUseController", "CreateCluster", "RemoveConstraintTargetOptions", "ConnectJoint", "RestoreUIElements", "circularFillet", "ubercam", "melProcSpreadsheet", "CycleBackgroundColor", "SelectAllRigidConstraints", "ImportDeformerWeightsOptions", "ikSystemInfo", "cMuscleQuery", "layout", "MirrorSubdivSurface", "DeleteAllImagePlanes", "window", "ModelingPanelUndoViewChange", "dR_rotateTweakTool", "buildSendToBackburnerDialog", "RebuildSurfaces", "AddPondBoatLocatorOptions", "xgmPresetSnapshotContext", "sbs_IsSubstanceRelocalized", "InteractiveBindSkin", "mayaDpiSettingAction", "NodeEditorPickWalkLeft", "shelfTabLayout", "SelectFacetMask", "SplitPolygonTool", "memoryDiag", "newton", "BakeSimulationOptions", "UnpublishChildAnchor", "ToggleParticleCount", "SendToUnrealAll", "ExportSelection", "AlembicImportOptions", "CreateVolumeCube", "GetHIKNode", "ToggleAutoSmooth", "NodeEditorToggleCreateNodePane", "TimeEditorCreateAdditiveLayer", "manipScaleLimitsCtx", "NextSkinPaintMode", "polyGeoSampler", "iprEngine", "subdToNurbs", "HideObjectGeometry", "formLayout", "polyIterOnPoly", "xgmClumpBrushToolCmd", "FreeTangentWeight", "HypershadeUpdatePSDNetworks", "AddFloorContactPlane", "renderSetupLocalOverride", "SelectAllFollicles", "dirmap", "fluidReplaceFramesOpt", "MakeMotorBoats", "DeleteAllPoses", "HypershadePublishConnections", "imfPlugins", "FlipTriangleEdge", "ToggleTimeSlider", "containerPublish", "ilrClearTextureCacheCmd", "polyNormalPerVertex", "HypershadeGraphRemoveUpstream", "dbmessage", "NURBSTexturePlacementToolOptions", "snapMode", "polySplitRing", "HideNCloths", "xgmNoiseBrushContext", "CVCurveToolOptions", "Tension", "HideTexturePlacements", "HIKSelectedMode", "HypershadeDisplayAsLargeSwatches", "XgmSplineSelectConvertToFreeze", "ExtractSubdivSurfaceVertices", "cmdScrollFieldReporter", "dR_softSelToolTGL", "evalEcho", "blendShapePanel", "dR_renderLastTGL", "tolerance", "HideStrokePathCurves", "HypershadeSetTraversalDepthZero", "SmoothTangent", "arcLengthDimension", "PasteSelected", "SelectNone", "clipEditor", "NodeEditorCopyConnectionsOnPaste", "falloffCurve", "ChangeVertexSize", "RotateUVsOptions", "XgmSetCombBrushTool", "SaveCurrentWorkspace", "unfold", "MakeLive", "HIKComputeReference", "PolyConvertToLoopAndDelete", "SelectAllTransforms", "ToggleEdgeMetadata", "dR_activeHandleZ", "ToggleContainerCentric", "ReplaceObjects", "CreateCharacterOptions", "SineOptions", "ExtendSurfaces", "dR_selConstraintEdgeRing", "cMuscleSplineBind", "PoseEditor", "dR_activeHandleX", "ToggleCurrentFrame", "multiTouch", "aimConstraint", "scrollLayout", "AddCurvesToHairSystem", "UncreaseSubdivSurface", "reverseSurface", "xgmUISelectionSync", "SymmetrizeSelection", "fluidAppend", "HideBoundingBox", "rehash", "ModifyUVVectorRelease", "ReattachSkeleton", "PaintGridOptions", "polyUVCoverage", "SetCurrentUVSet", "isConnected", "AppendToHairCache", "cmdShell", "polySewEdge", "setKeyPath", "ObjectCentricLightLinkingEditor", "timeEditorClipLayer", "polyQuad", "CreatePolygonSphereOptions", "attachCache", "preloadRefEd", "FBXImport", "xgmSplineCache", "DeformerSetEditor", "NodeEditorSelectConnected", "UVNormalBasedProjectionOptions", "cacheAppendOpt", "clip", "TangentsAuto", "ToggleCullingVertices", "FBXExportEmbeddedTextures", "ResetSoftSelectOptions", "dR_vertLockSelected", "UVSnapTogetherOptions", "AttachSubdivSurfaceOptions", "lassoContext", "XgmSetPartBrushTool", "BakeTopologyToTargets", "TimeEditorRippleEditToggleRelease", "ExpressionEditor", "ArtPaintAttrTool", "loft", "TimeEditorToggleSnapToClipPress", "SculptMeshActivateBrushStrength", "DeleteAllSculptObjects", "InsertKeyToolDeactivate", "HypershadeSelectUpStream", "greasePencil", "ReverseCurve", "DetachSkin", "meshReorder", "runup", "gradientControlNoAttr", "SelectTool", "OutTangentFlat", "sculpt", "CreateExpressionClipOptions", "DeleteKeysOptions", "PostInfinityOscillate", "clearNClothStartState", "NodeEditorHideAttributes", "polyEditEdgeFlow", "polyPlatonic", "selectedNodes", "OutTangentLinear", "hotkeyCheck", "PointOnCurveOptions", "ChangeNormalSize", "dR_cameraToPoly", "SetNormalAngle", "intSliderGrp", "roundCRCtx", "SurfaceBooleanSubtractTool", "OneClickMenuExecute", "cylinder", "MirrorDeformerWeights", "GetHIKEffectorName", "dR_selectSimilar", "subdEditUV", "polyCopyUV", "polyBevel", "characterize", "annotate", "DisplayUVWireframe", "linearPrecision", "softModCtx", "dR_connectRelease", "DuplicateSpecialOptions", "RotateToolWithSnapMarkingMenuPopDown", "ConvertSelectionToVertexFaces", "mouse", "webViewCmd", "evalNoSelectNotify", "dR_tweakRelease", "GlobalStitch", "shelfLayout", "PaintEffectPanelActivate", "HypergraphDGWindow", "copySkinWeights", "SetMeshRepeatTool", "dR_selectTool", "CycleThroughCameras", "DistributeShellsOptions", "SimplifyCurve", "viewManip", "SelectToolOptionsMarkingMenu", "AddBifrostChannelField", "XgBatchExportArchive", "ChannelControlEditor", "dR_loadRecentFile1", "MoveNormalTool", "dR_loadRecentFile3", "dR_loadRecentFile4", "setAttr", "dgeval", "createNurbsCylinderCtx", "keyframeRegionScaleKeyCtx", "polyTestPop", "bulletRigidSets", "ShareOneBrush", "floatField", "CameraModePerspective", "projectTangent", "UVContourStretchProjection", "PixelMoveUp", "ShowMeshWaxToolOptions", "SelectAllCameras", "NodeEditorShapeMenuStateAll", "nameCommand", "AssignOfflineFileOptions", "SubdivSurfaceMatchTopology", "pause", "ShowAllUI", "SetKeyPath", "texSculptCacheSync", "ExtrudeFaceOptions", "AddInfluenceOptions", "SelectMultiComponentMask", "FBXExportScaleFactor", "xgmSetGuideCVCount", "hudSliderButton", "dR_slideOff", "NodeEditorToggleAttrFilter", "AssignOfflineFile", "hyperGraph", "setFluidAttr", "xgmCache", "convertTessellation", "LockNormals", "hwReflectionMap", "XgmSplineCacheExportOptions", "SwapBlendShape", "LoadHIKEffectorSetState", "gravity", "dynWireCtx", "NodeEditorSetLargeNodeSwatchSize", "OutlinerToggleConnected", "greasePencilHelper", "PolyExtrudeEdgesOptions", "glRenderEditor", "loadUI", "HotkeyPreferencesWindow", "GraphDelete", "internalVar", "FBXGetTakeComment", "ExtendCurve", "SelectAllNURBSCurves", "TexSewActivateBrushSize", "GeometryConstraintOptions", "FBXExportBakeComplexStep", "XgmSplineCacheEnableSelectedCache", "FBXExportAxisConversionMethod", "getMetadata", "ShowLastHidden", "dragAttrContext", "findType", "CopyUVsToUVSet", "DuplicateCurve", "OutlinerToggleAttributes", "bezierAnchorState", "dR_connectPress", "helpLine", "CopyMeshAttributes", "NodeEditorAddOnNodeCreate", "DeleteHistory", "CreateCameraAimUpOptions", "HypershadeTestTextureOptions", "removeMultiInstance", "dR_alwaysOnTopTGL", "MakePressureCurve", "TimeEditorCreateAudioTracksAtEnd", "callbacks", "DisplayLight", "CreateCameraAimOptions", "Turbulence", "PasteKeys", "polyProjectCurve", "PaintEffectPanelDeactivate", "moveVertexAlongDirection", "XgmSetPlaceBrushToolOption", "XgGuideTool", "subdToBlind", "ShowMeshGrabToolOptions", "VortexOptions", "MergeEdgeTool", "PickWalkLeftSelect", "dR_viewJointsTGL", "XgmCreateInteractiveGroomSplines", "CoarserSubdivLevel", "TimeEditorFbxExportAll", "iconTextRadioCollection", "intFieldGrp", "PerspTextureLayout", "FBXLoadImportPresetFile", "TemplateObject", "JointToolOptions", "buildBookmarkMenu", "CombinePolygonsOptions", "polySplit", "sbs_GetSubstanceBuildVersion", "MakeMotorBoatsOptions", "CircularFilletOptions", "ToggleAutoActivateBodyPart", "affectedNet", "fluidDeleteCacheOpt", "polySetVertices", "OutlinerToggleDAGOnly", "NodeEditorConnectOnDrop", "nexQuadDrawContext", "polyWarpImage", "curveEditorCtx", "SelectAllJoints", "ExtractFace", "Loft", "xgmExportSplineDataInternal", "EnableDynamicConstraints", "CVCurveTool", "DeleteAllFluids", "nodePreset", "animDisplay", "CreatePolygonTool", "clipSchedulerOutliner", "BakeChannelOptions", "ExportSkinWeightMapsOptions", "ToggleOutliner", "cMuscleCompIndex", "nurbsSquare", "TimeEditorToggleTimeCursorRelease", "nClothCreateOptions", "HypershadePerspLayout", "TagAsControllerParent", "PreviousKey", "MoveSkinJointsToolOptions", "commandEcho", "UVSphericalProjection", "polyDelFacet", "ToggleTextureBorder", "SetVertexNormalOptions", "pointOnPolyConstraint", "RemoveInbetween", "RemoveBifrostFoam", "FBXGetTakeIndex", "SelectAllWires", "AddSelectionAsTargetShape", "PaintEffectsMeshQuality", "DistanceTool", "ToggleIsolateSelect", "polyCloseBorder", "timeEditorPanel", "MakeHoleTool", "FrameSelectedInAllViews", "ToggleCapsLockDisplay", "XgmSetDirectionBrushToolOption", "DeleteTextureReferenceObject", "HypershadeShowDirectoriesOnly", "attachGeometryCache", "ToggleEditPoints", "transferAttributes", "SelectAllNParticles", "SelectLinesMask", "SnapToGridPress", "AddBifrostKillplane", "SelectedAnimLayer", "SnapPointToPoint", "SmoothPolygonOptions", "CreateSoftBodyOptions", "UIModeMarkingMenu", "HideWrapInfluences", "ExtendFluid", "PlaybackForward", "hikCustomRigToolWidget", "TimeEditorClipTrimEnd", "toolHasOptions", "MatchPivots", "HypershadeMoveTabDown", "polyColorSet", "SetIKFKKeyframe", "falloffCurveAttr", "DeltaMushOptions", "dR_showHelp", "ShowObjectGeometry", "ShowFluids", "TwistOptions", "DecrementFluidCenter", "OpenCloseCurve", "xgmSplineBaseDensityScaleChangeCmd", "pointOnCurve", "CameraSetEditor", "RenderFlagsWindow", "SetPreferredAngle", "nClothReplaceFramesOpt", "U3DBrushSizeOff", "polyCreaseCtx", "CreateFluidCacheOptions", "SetShrinkWrapInnerObject", "UVAutomaticProjection", "editor", "RenderSetupWindow", "spring", "transformCompare", "InteractiveSplitToolOptions", "PreviousManipulatorHandle", "CopyKeys", "ShowMeshRepeatToolOptions", "SetFluidAttrFromCurveOptions", "CurveUtilitiesMarkingMenuPopDown", "CurveEditTool", "keyframeRegionDollyCtx", "BrushPresetBlendShapeOff", "polyColorBlindData", "RelaxInitialState", "SetKeyVertexColor", "CancelBatchRender", "SmoothCurveOptions", "dR_modeMulti", "HypershadeRevertSelectedSwatches", "dR_viewXrayTGL", "dR_selConstraintOff", "SoloLastOutput", "lightList", "distanceDimension", "CreateShrinkWrap", "checkBox", "SetMeshSmoothTool", "HypershadeGraphUpstream", "XgPreRendering", "ArtPaintSelectToolOptions", "SetAsCombinationTarget", "RefineSelectedComponents", "SelectAllDynamicConstraints", "FBXLoadExportPresetFile", "HypershadeDeleteAllUtilities", "AddToCurrentSceneMotionBuilder", "MirrorJointOptions", "EnterEditMode", "RenderOptions", "dR_setRelaxAffectsAuto", "artAttrTool", "PaintOperationMarkingMenuRelease", "emit", "delete", "trim", "loadModule", "ExportDeformerWeights", "graphSelectContext", "Create3DContainerEmitterOptions", "nClothReplaceCacheOpt", "NodeEditorGraphClearGraph", "polyMapSewMove", "polyCircularizeEdge", "BrushPresetReplaceShading", "NextManipulatorHandle", "InsertKeysTool", "UnmirrorSmoothProxy", "CreateSoftBody", "HypershadeOpenUVEditorWindow", "mpBirailCtx", "polyPlatonicSolid", "insertJoint", "ShareUVInstances", "changeSubdivComponentDisplayLevel", "SculptMeshDeactivateBrushStrength", "polySelectEditCtxDataCmd", "ProfilerToolThreadView", "LevelOfDetailGroup", "PostInfinityCycleOffset", "TimeEditorFramePlaybackRange", "ShowMeshGrabUVToolOptions", "PasteVertexSkinWeights", "artAttrCtx", "snapshot", "Create3DContainer", "roll", "createPolyPrismCtx", "TimeEditorClipScaleEnd", "pairBlend", "xgmCombBrushContext", "frameBufferName", "HypershadeEditPSDFile", "RebuildCurveOptions", "HideGeometry", "ToggleCameraNames", "SnapToGridRelease", "SelectBrushNames", "sysFile", "MatchTranslation", "MoveRotateScaleToolToggleSnapMode", "PlaybackStop", "ToggleEdgeIDs", "InsertEdgeLoopToolOptions", "IncreaseCheckerDensity", "combinationShape", "xgmPointsContext", "objExists", "currentTime", "xgmSplineGeometryConvert", "dpBirailCtx", "connectJoint", "shadingConnection", "hikRigSync", "stitchSurface", "Fire", "attributeQuery", "text", "nParticle", "fltLightPoints", "HypershadeCreateContainerOptions", "SculptPolygonsTool", "dgTimerSpreadsheet", "toolBar", "nexConnectCtx", "TimeEditorUnsoloAllTracks", "saveShelf", "CurveUtilitiesMarkingMenu", "ilrInternalVar", "SendToUnrealSetProject", "nodeOutliner", "createPolySoccerBallCtx", "scriptCtx", "ToggleViewCube", "fluidDeleteCacheFramesOpt", "ExportOfflineFileFromRefEdOptions", "AnimationTurntable", "VisorWindow", "inheritTransform", "manipMoveContext", "constructionHistory", "ConformPolygonNormals", "ScaleToolWithSnapMarkingMenuPopDown", "polyAppend", "CreateShrinkWrapOptions", "XgmSetSelectBrushToolOption", "CreatePolygonPipeOptions", "AddBifrostEmissionRegion", "polySuperShape", "crashInfoCmd", "furClosestFace", "disconnectAttr", "manipMoveLimitsCtx", "ArchiveSceneOptions", "DeviceEditor", "ToggleFaceNormalDisplay", "OutlinerToggleShowMuteInformation", "TimeEditorOpenContentBrowser", "toggleAxis", "HideFur", "CreateSpringOptions", "HypershadePinByDefault", "meshRemapContext", "dR_modeEdge", "TimeEditorCreateAudioClip", "NodeEditorCreateForEachCompound", "SetDrivenKeyOptions", "CreatePartition", "performanceOptions", "HIKSetSelectionKey", "IntersectSurfacesOptions", "DeleteAllRigidConstraints", "HIKInitAxis", "DoUnghostOptions", "TangentsStepped", "manipScaleContext", "DeleteConstraints", "ResampleCurveOptions", "ToggleNormals", "TimeEditorToggleMuteSelectedTracks", "ShadingGroupAttributeEditor", "nBase", "PreInfinityLinear", "ConvertSelectionToEdges", "listNodeTypes", "filterExpand", "nurbsSelect", "TemplateBrushSettings", "ReorderVertex", "ctxAbort", "TimeEditorMuteSelectedTracks", "colorManagementCatalog", "HideUnselectedObjects", "dR_setRelaxAffectsInterior", "NodeEditorExtendToShapes", "ResetReflectionOptions", "retimeKeyCtx", "CreateNURBSSphereOptions", "CreateNURBSSquare", "listAttr", "OutlinerToggleNamespace", "MakeCollide", "SetMeshGrabTool", "popPinning", "ToggleDisplacement", "ShowModelingUI", "xgmGuideSculptContext", "TogglePolyCount", "OneClickExecute", "bifSaveFrame", "HypershadeOpenRenderViewWindow", "curveRGBColor", "symbolButton", "PanelPreferencesWindow", "OneClickDisconnect", "view2dToolCtx", "BestPlaneTexturingTool", "xgmWidthBrushToolCmd", "SetFluidAttrFromCurve", "buildFurImages", "XgExportArchive", "uniform", "ViewAlongAxisNegativeZ", "ViewAlongAxisNegativeX", "HypershadeSelectConnected", "dgmodified", "Flare", "sbs_SetBakeFormat", "UVContourStretchProjectionOptions", "GeometryConstraint", "gpuCache", "DuplicateWithTransform", "pose", "AddToCharacterSet", "TwoPointArcTool", "WedgePolygonOptions", "setStartupMessage", "PrelightPolygonOptions", "HypershadeDuplicateShadingNetwork", "nurbsCopyUVSet", "UVSphericalProjectionOptions", "HIKPinTranslate", "AddFaceDivisionsOptions", "keyframeOutliner", "CreatePolygonDiscOptions", "CreateWrap", "GraphEditorStackedView", "dR_selectRelease", "listDeviceAttachments", "xgmFreezeBrushContext", "HypershadeTransferAttributeValuesOptions", "BrushPresetBlendOff", "targetWeldCtx", "PolygonBooleanIntersection", "polyHole", "SpreadSheetEditor", "NodeEditorToggleNodeSelectedPins", "FBXRead", "commandPort", "OutlinerToggleOrganizeByClip", "NURBSSmoothnessRoughOptions", "PublishConnections", "ToggleModelEditorBars", "RandomizeShellsOptions", "hotBox", "dR_pointSnapRelease", "ArtPaintBlendShapeWeightsToolOptions", "muMessageDelete", "PartitionEditor", "TimeEditorClipHoldToggle", "geometryReplaceCacheOpt", "SetMeshGrabUVTool", "CreatePolygonCylinderOptions", "panelConfiguration", "ArcLengthTool", "cycleCheck", "xgmDirectionBrushToolCmd", "SendAsNewScenePrintStudio", "ModifyOpacityPress", "Import", "dynExpression", "nClothCache", "ShapeEditorSelectNone", "AssignOfflineFileFromRefEd", "rotationInterpolation", "hyperShade", "bezierInfo", "changeSubdivRegion", "PolyRemoveAllCrease", "outlinerEditor", "ConvertSelectionToUVShell", "DeleteAllStaticChannels", "SetBreakdownKeyOptions", "createDisplayLayer", "TimeEditorExportSelectionOpt", "polyCylindricalProjection", "MoveToolOptions", "memory", "polyNormalizeUV", "appendListItem", "polyBlindData", "colorSliderButtonGrp", "PointConstraint", "GridOptions", "AddInBetweenTargetShapeOptions", "dR_bridgeTool", "AutoProjectionOptions", "PreInfinityConstant", "AddDivisions", "readPDC", "addPP", "FBXUICallBack", "OffsetSurfaces", "SelectPreviousObjectsMotionBuilder", "timeFieldGrp", "CreatePoseInterpolatorEditor", "NodeEditorConnectSelectedNodes", "ChangeUVSize", "disableIncorrectNameWarning", "CreateClip", "OrientJointOptions", "AttachBrushToCurves", "headsUpDisplay", "ShowMeshMaskToolOptions", "PolyBrushMarkingMenuPopDown", "RenameAttribute", "collision", "FourViewArrangement", "AddTimeWarp", "aliasAttr", "dR_bridgeRelease", "attrFieldSliderGrp", "PruneCluster", "NodeEditorAdditiveGraphingMode", "modelPanel", "HypershadeSetTraversalDepthUnlim", "PokePolygonOptions", "ctxEditMode", "HideDeformers", "SculptGeometryToolOptions", "deformer", "BrushAnimationMarkingMenu", "PinSelectionOptions", "SelectLightsShadowingObject", "SetKeyAnimated", "xgmPushOver", "dR_graphEditorTGL", "setDefaultShadingGroup", "OutlinerWindow", "FBXImportAutoAxisEnable", "stroke", "CreateEmptyUVSetOptions", "XgmCreateInteractiveGroomSplinesOption", "HypershadeDisplayAsSmallSwatches", "ReplaceObjectsOptions", "UndoCanvas", "ungroup", "rebuildCurve", "CreateVolumeCone", "instanceable", "xgmFileRender", "extendSurface", "resourceManager", "renderSetupSelect", "HypershadeSelectDownStream", "dR_modeObject", "ToggleLocalRotationAxes", "renderManip", "ToggleZoomInMode", "Birail1Options", "cMuscleWeightDefault", "LoopBrushAnimation", "HypershadeSortReverseOrder", "dR_safeFrameTGL", "nClothAppend", "setDrivenKeyframe", "geomToBBox", "SelectAllNURBSSurfaces", "getRenderTasks", "polyCrease", "MakePondBoats", "skinCluster", "EditFluidResolutionOptions", "LayoutUVAlong", "PanZoomTool", "PolygonBooleanDifferenceOptions", "bakeSimulation", "dynControl", "nexMultiCutCtx", "date", "AddOceanDynamicLocator", "TimeEditorCreatePoseClipOptions", "repeatLast", "displacementToPoly", "SelectToolOptionsMarkingMenuPopDown", "NodeEditorPaste", "ConvertSelectionToUVs", "SingleViewArrangement", "ToggleGrid", "AssumePreferredAngleOptions", "texSelectShortestPathCtx", "FBXImportUpAxis", "XgmSplineCacheDeleteNodesAhead", "HypershadeShowDirectoriesAndFiles", "PickWalkRight", "CreateCameraOnlyOptions", "HypershadeUnpinSelected", "subdMapSewMove", "ToggleUnsharedUVs", "hyperPanel", "HideMarkers", "WhatsNewHighlightingOff", "crashInfo", "polyCircularize", "greasePencilCtx", "dR_softSelDistanceTypeGlobal", "dynamicConstraintRemove", "HypershadeCreateAsset", "HypershadeSelectCamerasAndImagePlanes", "CutUVs", "AimConstraint", "DeleteAllConstraints", "TimeEditorUnmuteSelectedTracks", "PublishChildAnchorOptions", "poleVectorConstraint", "contentBrowser", "ShowStrokes", "ArtPaintSelectTool", "DeleteExpressions", "projectCurve", "polyClean", "CreateTextureDeformerOptions", "group", "dR_snapToBackfacesTGL", "SubdivSmoothnessHull", "melOptions", "ConnectToTime", "MakeCollideOptions", "SetShrinkWrapTarget", "DynamicRelationshipEditor", "ExtrudeVertex", "createPolyTorusCtx", "MatchUVs", "FBXExportUseSceneName", "ExportAnimOptions", "AutobindContainerOptions", "UpdateBindingSet", "ShowBaseWire", "ProfilerToolHideSelected", "FBXExportLights", "particleFill", "LastActionTool", "AddOceanDynamicLocatorOptions", "switchTable", "SetKey", "xgmPrimSelectionContext", "nClothReplaceCache", "setKeyframe", "iconTextButton", "nop", "TogglePolyDisplayHardEdges", "DeleteUVs", "GraphEditorAlwaysDisplayTangents", "FBXExportQuickSelectSetAsCache", "CreateClipOptions", "AddWrapInfluence", "modelEditor", "flushIdleQueue", "OffsetCurve", "ilrBatchRenderCmd", "AppendToHairCacheOptions", "animView", "UnfoldPackUVs3DInCurrentTile", "attrCompatibility", "ToggleIKSolvers", "HideSelectedObjects", "NodeEditorCreateDoWhileCompound", "shadingNode", "viewSet", "TimeEditorSetZeroKey", "alignSurface", "cacheFileCombine", "CreateEmitterOptions", "PolygonCopy", "lsThroughFilter", "ActivateGlobalScreenSliderModeMarkingMenu", "SetWorkingFrame", "textScrollList", "mayaPreviewRenderIntoNewWindow", "DeleteCurrentWorkspace", "FBXImportOCMerge", "PaintVertexColorTool", "CreateSetOptions", "scaleConstraint", "NodeEditorDiveIntoCompound", "replaceCacheFramesOpt", "CopyFlexor", "LockCurveLength", "radioButtonGrp", "SlideEdgeTool", "rangeControl", "polyQueryBlindData", "xgmFreezeBrushToolCmd", "LevelOfDetailGroupOptions", "bindSkin", "container", "SubdividePolygon", "dopeSheetEditor", "QuickRigEditor", "itemFilter", "PolygonBooleanUnionOptions", "TestTexture", "HypershadeDeleteAllCamerasAndImagePlanes", "SelectUVTool", "superCtx", "xgmInterpSetup", "DeleteUVsWithoutHotkey", "deleteGeometryCache", "PolyMergeEdgesOptions", "CreateJiggleOptions", "nameField", "polyAppendVertex", "ShowTexturePlacements", "hikGetNodeCount", "NodeEditorPublishCompound", "GoToWorkingFrame", "KeyBlendShapeTargetsWeight", "CreateUVsBasedOnCamera", "fluidVoxelInfo", "SmoothHairCurvesOptions", "NewtonOptions", "lsUI", "hikGetNodeIdFromName", "subdToPoly", "NodeEditorCloseAllTabs", "FBXProperty", "cmdScrollFieldExecuter", "SubstituteGeometry", "HypershadeSelectUtilities", "AssetEditor", "characterMap", "ExpandSelectedComponents", "FBXLoadMBImportPresetFile", "dR_edgedFacesTGL", "ToggleIKHandleSnap", "InvertSelection", "plane", "SymmetrizeUV", "TumbleTool", "textFieldButtonGrp", "RigidBodySolver", "FrameAll", "buildFurFiles", "psdExport", "SelectLightsIlluminatingObject", "evaluationManager", "DuplicateFace", "sbs_GetWorkflow", "artSetPaintCtx", "igConvertToLogical", "PublishConnectionsOptions", "PolygonBooleanIntersectionOptions", "cacheFile", "LookAtSelection", "XgmSplinePresetExport", "setUITemplate", "NodeEditorConnectionStyleBezier", "editMetadata", "defaultNavigation", "NodeEditorToggleZoomIn", "CustomNURBSSmoothnessOptions", "hikGetEffectorIdFromName", "addExtension", "ShowMeshCloneTargetToolOptions", "polySplitCtx2", "IntersectSurfaces", "SculptSubdivsToolOptions", "GpuCacheExportAll", "InTangentAuto", "dR_convertSelectionToEdge", "TimeEditorClipScaleToggle", "ToggleRotationPivots", "MoveRight", "HypershadeRemoveTab", "UVNormalBasedProjection", "UntemplateObject", "timerX", "GraphEditorFrameAll", "ShowSmoothSkinInfluences", "SelectUVShell", "MovePolygonComponent", "ParticleFillOptions", "ResetWeightsToDefault", "mrShaderManager", "furPointOnMesh", "SelectAllPolygonGeometry", "TwoSideBySideViewArrangement", "ToggleFastInteraction", "TogglePaintOnPaintableObjects", "FBXExportBakeComplexEnd", "HypershadePickWalkLeft", "RenderTextureRangeOptions", "CreateVolumeLightOptions", "SelectToolMarkingMenu", "TimeEditorDeleteSelectedTracks", "ToggleSelectionHandles", "ShowMeshBulgeToolOptions", "mouldSrf", "ApplySettingsToSelectedStroke", "BakeCustomPivot", "sequenceManager", "DeleteRigidBodies", "FBXLoadMBExportPresetFile", "FlipUVsOptions", "polyColorSetCmdWrapper", "TimeEditorClipResetTiming", "PrelightPolygon", "TransplantHairOptions", "lightlink", "getRenderDependencies", "SoftModTool", "psdChannelOutliner", "polyDisc", "selectionConnection", "geometryMergeCacheOpt", "CreateConstraint", "scmh", "ToggleReflection", "HypershadeCreateTab", "PublishRootTransform", "TimeEditorToggleTimeCursorPress", "polyMergeUV", "SplitMeshWithProjectedCurve", "FBXExportColladaFrameRate", "FBXGetTakeName", "MakeCurvesDynamicOptions", "fluidReplaceFrames", "parentConstraint", "AirOptions", "subgraph", "SaveSceneAs", "ToggleViewportRenderer", "ResolveInterpenetration", "NodeEditorGridToggleSnap", "AddHolder", "ColorPreferencesWindow", "AlignUV", "polyVertexNormalCtx", "nucleusDisplayMaterialNodes", "HypershadeToggleTransformDisplay", "HypershadeDeleteDuplicateShadingNetworks", "SendAsNewScene3dsMax", "NParticleTool", "track", "AddInfluence", "AssignTemplateOptions", "FloatSelectedPondObjects", "selectPref", "AddToCurrentScene3dsMax", "SetCutSewUVTool", "RemoveInfluence", "wire", "AlignCurveOptions", "evaluator", "PostInfinityLinear", "artSelectCtx", "FBXImportSetTake", "picture", "HypershadeGridToggleVisibility", "HypershadeRenderTextureRangeOptions", "ThreePointArcToolOptions", "FBXExportColladaTriangulate", "WireDropoffLocatorOptions", "PublishParentAnchor", "BrushPresetBlend", "PolyCircularizeOptions", "PencilCurveToolOptions", "FBXImportConvertUnitString", "CreateFluidCache", "toolButton", "findKeyframe", "PolygonPasteOptions", "CreateSubdivRegion", "nonLinear", "shot", "moveKeyCtx", "CreateDiskCache", "SymmetrizeUVBrushSizeOn", "XgmSetCutBrushToolOption", "PaintEffectsToNurbs", "CreateSpotLight", "ExportSkinWeightMaps", "toggleWindowVisibility", "polyCut", "nucleusDisplayTransformNodes", "OneClickAcknowledgeCallback", "HideClusters", "dR_viewBottom", "blend2", "mtkShrinkWrap", "ExtendCurveOnSurface", "ToggleUVDistortion", "xgmModifierGuideOp", "CreateSculptDeformer", "CameraModeToggle", "CreatePoseOptions", "DecreaseGammaFine", "myTestCmd", "dR_tweakPress", "EmitFluidFromObjectOptions", "air", "namespaceInfo", "ToggleWireframeInArtisan", "SelectComponentToolMarkingMenuPopDown", "CreatePointLight", "OneClickFetchRemoteCharacter", "CurlCurvesOptions", "CreateCameraAim", "BlindDataEditor", "sbs_GetEditionModeScale", "OffsetSurfacesOptions", "SnapPointToPointOptions", "artSetPaint", "dR_multiCutPointCmd", "createPolyHelixCtx", "CreatePolygonDisc", "surfaceSampler", "ToggleMeshMaps", "ToggleRangeSlider", "HypershadeAdditiveGraphingMode", "polySphere", "PaintEffectsTool", "EnableConstraints", "DollyTool", "CreateNURBSPlane", "boundary", "SelectPreviousObjectsMudbox", "xgmBakeGuideToUVSpace", "polyCircularizeFace", "pointPosition", "flushThumbnailCache", "MakeFluidCollideOptions", "fontAttributes", "GraphSnapOptions", "nurbsCube", "undoInfo", "polyBevel3", "OneClickGetContactingAppName", "dagPose", "ScaleUVTool", "FBXImportSkins", "createAttrPatterns", "BakeDeformerTool", "bakeResults", "textField", "bakePartialHistory", "FBXImportForcedFileAxis", "PanePop", "SelectAllMarkingMenuPopDown", "TangentsSpline", "xgmExportToP3D", "OffsetEdgeLoopTool", "MirrorPolygonGeometryOptions", "PruneSculpt", "BendCurves", "CreatePolygonSphere", "agFormatOut", "SubdivProxy", "SetMeshWaxTool", "PolyEditEdgeFlowOptions", "viewFit", "AddInBetweenTargetShape", "MirrorCutPolygonGeometryOptions", "ShowAllComponents", "pasteKey", "TrackTool", "ArtPaintBlendShapeWeightsTool", "FBXExportShowUI", "RenderPassSetEditor", "isDescendentPulling", "PointConstraintOptions", "AlignSurfaces", "removeJoint", "IncreaseManipulatorSize", "SetMeshRelaxTool", "HideFollicles", "ArtPaintAttrToolOptions", "PublishAttributesOptions", "CurveFillet", "uvSnapshot", "GraphSnap", "DeactivateGlobalScreenSliderModeMarkingMenu", "renderGlobalsNode", "ScaleKeysOptions", "objectTypeUI", "gridLayout", "ExtractFaceOptions", "NodeEditorShapeMenuStateNoShapes", "ModifyUpperRadiusPress", "PerPointEmissionRates", "sbs_GetEnumCount", "parent", "nodeEditor", "dgfilter", "BoundaryOptions", "PickWalkDown", "AveragePolygonNormalsOptions", "polyTorus", "paramDimContext", "polyHelix", "xgmSculptLayerInit", "ExtrudeEdgeOptions", "CreateAnnotateNode", "HidePlanes", "SlideEdgeToolOptions", "SelectAllInput", "NodeEditorSelectDownStream", "HypershadeToggleNodeSwatchSize", "attachCurve", "fluidAppendOpt", "VolumeAxisOptions", "geometryExportCacheOpt", "displayRGBColor", "keyframe", "toolPropertyWindow", "PFXUVSetLinkingEditor", "expression", "CreateHair", "PreloadReferenceEditor", "IKSplineHandleTool", "CurveSmoothnessMedium", "dR_quadDrawTool", "dgControl", "color", "dR_hypergraphTGL", "connectControl", "recordAttr", "HIKToggleReleasePinning", "hwRender", "defaultLightListCheckBox", "PolyCircularize", "GpuCacheRefreshAll", "ProfilerToolShowSelectedRepetition", "PaintGeomCacheToolOptions", "mtkQuadDrawPoint", "TimeEditorKeepTransitionsToggleRelease", "manipComponentPivot", "UnpinSelection", "FreeformFillet", "CreateActiveRigidBodyOptions", "CreateWake", "FBXExportSmoothingGroups", "skinPercent", "Shatter", "CreateIllustratorCurvesOptions", "EnterEditModePress", "HypershadeRefreshFileListing", "ConnectComponentsOptions", "fileInfo", "Create2DContainerOptions", "ilrTextureBakeCmd", "ShowLights", "CharacterMapper", "AttachSurfaces", "PaintReduceWeightsToolOptions", "PickWalkIn", "dR_bevelPress", "CreateWrapOptions", "GrowPolygonSelectionRegion", "MakeFluidCollide", "dR_viewGridTGL", "colorManagementConvert", "polySelectConstraintMonitor", "floatSliderButtonGrp", "GetToonExample", "jointDisplayScale", "OptimizeSceneOptions", "dR_selConstraintAngle", "componentBox", "sound", "PolyConvertToLoopAndDuplicate", "connectionInfo", "xgmFindAttachment", "insertJointCtx", "CreateCreaseSet", "AlembicReplace", "intField", "whatsNewHighlight", "dataStructure", "DeleteAllCameras", "profiler", "columnLayout", "dR_selectModeHybrid", "HypergraphWindow", "LightningOptions", "u3dAutoSeam", "ShowMeshScrapeToolOptions", "HideManipulators", "SetProject", "texLatticeDeformContext", "RepeatLast", "SetReFormTool", "CreateBifrostAero", "treeView", "assignCommand", "projectionContext", "ConvertSelectionToShellBorder", "LayoutUVOptions", "cluster", "squareSurface", "DetachCurveOptions", "texSculptCacheContext", "ChamferVertexOptions", "ModifyLowerRadiusRelease", "RandomizeShells", "xgmWidthBrushContext", "subdivCrease", "licenseCheck", "ShowMeshSmoothTargetToolOptions", "HypergraphIncreaseDepth", "propMove", "u3dLayout", "ThreeTopSplitViewArrangement", "fluidReplaceCacheOpt", "debug", "LoopBrushAnimationOptions", "CVHardnessOptions", "ActivateGlobalScreenSlider", "ShowAllEditedComponents", "HidePolygonSurfaces", "CreateEmptyUVSet", "modelCurrentTimeCtx", "menuSet", "AddPondSurfaceLocator", "AddKeyToolDeactivate", "DetachSkeletonJoints", "xgmSplineApplyRenderOverride", "texSmoothContext", "dR_objectXrayTGL", "TogglePolyDisplayEdges", "disconnectJoint", "DeleteExpressionsOptions", "polyClipboard", "moduleDetectionLogic", "RenderLayerEditorWindow", "QualityDisplayMarkingMenu", "OffsetCurveOnSurfaceOptions", "HideStrokeControlCurves", "HoldCurrentKeys", "nodeGrapher", "TwoStackedViewArrangement", "AddPondDynamicLocatorOptions", "CreateShot", "CustomPolygonDisplayOptions", "CreateWakeOptions", "TimeEditorCreateAnimTracksAtEnd", "ShowNParticles", "Snap2PointsTo2Points", "dynamicLoad", "DeleteAllJoints", "ConvertSelectionToShell", "TranslateToolMarkingMenu", "HypershadeDisplayAsMediumSwatches", "CreateCameraAimUp", "PolyAssignSubdivHoleOptions", "drawExtrudeFacetCtx", "dR_rotatePress", "shotRipple", "ShowBoundingBox", "frameLayout", "timeEditorClipOffset", "fltSwitch", "runTimeCommand", "upAxis", "HypershadeFrameAll", "AddCombinationTarget", "Birail3Options", "HIKCharacterControlsTool", "channelBox", "NodeEditorPinByDefault", "ImportSkinWeightMaps", "layeredTexturePort", "cutKey", "polyExtrudeEdge", "HypershadeSelectShadingGroupsAndMaterials", "CreateNURBSCircle", "sortCaseInsensitive", "NodeEditorHighlightConnectionsOnNodeSelection", "listRelatives", "ThreeLeftSplitViewArrangement", "CreateNURBSCylinderOptions", "CreatePolygonPrism", "ResetWireOptions", "keyframeRegionInsertKeyCtx", "dR_coordSpaceObject", "DeleteAllShadingGroupsAndMaterials", "CollapseSubdivSurfaceHierarchy", "AddSelectionAsTargetShapeOptions", "deleteAttrPattern", "GraphEditorDisableCurveSelection", "XgmSetPlaceBrushTool", "ZoomTool", "directionalLight", "artUserPaintCtx", "CreateCameraFromView", "mirrorJoint", "ParentConstraint", "colorSliderGrp", "renderSettings", "DisableFluids", "CreateNURBSCylinder", "MoveSkinJointsTool", "UVOrientShells", "HypershadeCloseAllTabs", "CreateBifrostLiquid", "UseSelectedEmitter", "PreInfinityOscillate", "grid", "offsetCurveOnSurface", "dbtrace", "floatFieldGrp", "expressionEditorListen", "xgmPointRender", "ProfilerToolCategoryView", "artBuildPaintMenu", "sbs_GetChannelsNamesFromSubstanceNode", "particle", "CreateLocator", "CreateBindingSet", "FlowPathObject", "wrinkleContext", "DeleteAllLattices", "AttachToPath", "IncreaseExposureFine", "GraphEditorEnableCurveSelection", "PoleVectorConstraint", "SetActiveKey", "SelectFacePath", "ComponentEditor", "GeometryToBoundingBoxOptions", "SnapToMeshCenterRelease", "PresetBlendingWindow", "ScaleToolMarkingMenu", "ilrUVSACmd", "SelectAllNRigids", "windowPref", "sbs_GetAllInputsFromSubstanceNode", "XgmSetClumpBrushTool", "skeletonEmbed", "xgmRebuildSplineDescription", "refresh", "DisplayLayerEditorWindow", "RemoveBifrostFoamMask", "polyUnite", "SubdivSmoothnessRough", "animCurveEditor", "NodeEditorGraphUpDownstream", "CreatePolygonSuperEllipseOptions", "ProductInformation", "ReverseSurfaceDirectionOptions", "xgmSculptLayerMerge", "Birail2", "Birail3", "Birail1", "FBXExportInstances", "SequenceEditor", "isFromReferencedFile", "HIKPinRotate", "nClothDeleteHistoryOpt", "dR_gridSnapRelease", "UVStraightenOptions", "RemoveFromContainerOptions", "notifyPostUndo", "PaintReduceWeightsTool", "polyMoveFacet", "getModulePath", "SplitUV", "BlendShapeEditor", "loadPrefObjects", "RemoveConstraintTarget", "DuplicateNURBSPatches", "assembly", "panelHistory", "posePanel", "boxDollyCtx", "SwapBlendShapeOptions", "SetCurrentColorSet", "BrushPresetBlendShadingOff", "PaintCacheToolOptions", "HypershadeCreateNewTab", "createPolyPlatonicSolidCtx", "ClearPaintEffectsView", "dR_visorTGL", "CreatePolygonPlane", "viewPlace", "AutoProjection", "SetKeyOptions", "PrefixHierarchyNames", "MirrorJoint", "xgmCombBrushToolCmd", "SetKeyScale", "dR_softSelDistanceTypeObject", "FBXImportHardEdges", "sbs_AffectTheseAttributes", "cameraView", "BevelPlusOptions", "xgmGuideContext", "NonWeightedTangents", "shadingNetworkCompare", "FBXResetExport", "dR_setExtendLoop", "ShowSurfaceCVs", "RotateTool", "dR_symmetryFlip", "ProjectCurveOnSurface", "EnableTimeChangeUndoConsolidation", "RotateUVTool", "SymmetrizeUVUpdateCommand", "NodeEditorPickWalkRight", "MirrorSkinWeightsOptions", "dR_selectAll", "DeleteAllExpressions", "HypershadeIncreaseTraversalDepth", "adskAsset", "exactWorldBoundingBox", "NodeEditorShowCustomAttrs", "dR_selConstraintBorder", "DeleteStaticChannels", "UVStackSimilarShellsOptions", "TruncateHairCache", "Duplicate", "polyContourProjection", "NodeEditorCreateNodePopup", "FBXExportSkeletonDefinitions", "SetKeyRotate", "ExtrudeOptions", "ActivateViewport20", "tabLayout", "AttachSubdivSurface", "ToggleCreaseVertices", "polyUVOverlap", "ConvertToFrozen", "PerspGraphLayout", "setMenuMode", "DeleteSurfaceFlowOptions", "polyMergeEdgeCtx", "NodeEditorGraphAllShapesExceptShading", "ResetProperty2State", "InteractiveSplitTool", "geometryAppendCacheOpt", "WaveOptions", "HypershadeOpenCreateWindow", "polyAverageVertex", "sceneUIReplacement", "ViewAlongAxisNegativeY", "NodeEditorRenderSwatches", "particleExists", "SetMeshFlattenTool", "ShowManipulatorTool", "HideAll", "MoveNearestPickedKeyToolDeactivate", "objectCenter", "dx11Shader", "NodeEditorCloseActiveTab", "CreatePolygonSuperEllipse", "TimeEditorDeleteClips", "dbfootprint", "MakePondBoatsOptions", "ToggleUseDefaultMaterial", "ToggleScalePivots", "cacheFileMerge", "closeCurve", "setDynamic", "AddAnimationOffsetOptions", "FBXExportBakeComplexAnimation", "EmitFluidFromObject", "ViewSequence", "animLayer", "HypershadeSelectBakeSets", "ToggleUIElements", "planarSrf", "curveIntersect", "projectionManip", "evalContinue", "volumeAxis", "IncrementAndSave", "SculptSurfacesToolOptions", "PickWalkUpSelect", "character", "dR_selConstraintUVEdgeLoop", "furSubdArea", "FrameAllInAllViews", "HypershadeGraphDownstream", "CutSelected", "NodeEditorGraphUpstream", "FBXImportScaleFactor", "ToggleVertices", "dbcount", "PolyExtrudeEdges", "RandomizeFollicles", "polyToCurve", "SelectMaskToolMarkingMenuPopDown", "hotkeyEditor", "file", "polyRemesh", "snapshotBeadContext", "AffectSelectedObject", "QuadrangulateOptions", "xgmSmoothBrushToolCmd", "ConnectionEditor", "poseInterpolator", "lockNode", "dgInfo", "UnpublishParentAnchor", "PickWalkDownSelect", "dR_slideEdge", "recordDevice", "ilrPointCloudCmd", "headsUpMessage", "MakeBrushSpring", "furCompareFileTime", "EditMembershipTool", "MatchScaling", "Art3dPaintToolOptions", "InTangentLinear", "insertKeyCtx", "FBXExportTriangulate", "keyframeRegionMoveKeyCtx", "Delete", "RadialOptions", "AlembicHelp", "PaintEffectsToPolyOptions", "UpdateCurrentSceneMotionBuilder", "render", "ptexBake", "showSelectionInTitle", "fcheck", "HIKGetRemoteCharacterList", "BatchRender", "optionMenuGrp", "SculptMeshDeactivateBrushSize", "CreateSubCharacterOptions", "SaveCurrentLayout", "currentCtx", "smoothCurve", "polyGear", "texSmudgeUVContext", "PoseInterpolatorNewGroup", "dR_disableTexturesTGL", "curve", "TimeEditorExportSelection", "SplitEdge", "geometryMergeCache", "AddToContainer", "extendCurve", "DisplayShaded", "XgmSplineCacheImportOptions", "buildKeyframeMenu", "SurfaceEditingToolOptions", "PostInfinityConstant", "renderSetupSwitchVisibleRenderLayer", "SnapToPoint", "HypershadeConvertPSDToLayeredTexture", "HairUVSetLinkingEditor", "saveAllShelves", "TexSculptDeactivateBrushStrength", "DistributeShells", "OffsetCurveOptions", "DeleteAllNonLinearDeformers", "SavePreferences", "CreatePolygonHelixOptions", "RemoveWrapInfluence", "PickWalkLeft", "MakeCurvesDynamic", "SelectAllSculptObjects", "CreateParticleDiskCacheOptions", "SelectCurveCVsFirst", "CreateVolumeSphere", "PartialCreaseSubdivSurface", "ConvertToKey", "SelectAllIKHandles", "deleteHistoryAheadOfGeomCache", "ResetWire", "pointConstraint", "dR_quadDrawClearDots", "SculptMeshFrame", "geometryCache", "CreateDagContainerOptions", "testPassContribution", "ToggleToolbox", "showShadingGroupAttrEditor", "createPtexUV", "HideUIElements", "PaintEffectsWindow", "createMeshFromPoints", "deleteUI", "RemoveBifrostKillplane", "UVEditorFrameSelected", "HypershadeTransferAttributeValues", "CreateLatticeOptions", "Unfold3DContext", "DetachSkinOptions", "XgmSetClumpBrushToolOption", "TrimTool", "GetHIKChildCount", "outlinerPanel", "AddBlendShapeOptions", "OneClickGetState", "dR_mtkPanelTGL", "SetMeshSmoothTargetTool", "EditCharacterAttributes", "ResetTemplateBrush", "SimplifyCurveOptions", "PolySpinEdgeBackward", "XgmSplineCacheImport", "AddDynamicBuoyOptions", "ExtrudeFace", "resolutionNode", "polyCutCtx", "SelectAllParticles", "polyNormal", "polyAverageNormal", "snapshotBeadCtx", "AttributeEditor", "RemoveBifrostEmissionRegion", "ToggleMaterialLoadingDetailsVisibility", "AutoPaintMarkingMenu", "overrideModifier", "FBXExportBakeResampleAnimation", "GpuCacheImportOptions", "PolygonApplyColorOptions", "TimeEditorCreateClipOptions", "movOut", "dynExport", "ScaleConstraintOptions", "artPuttyCtx", "HypershadeDeleteAllTextures", "NURBSToPolygons", "containerProxy", "FBXExportAudio", "xgmLengthBrushToolCmd", "polyMapDel", "OrientConstraintOptions", "ResetTransformationsOptions", "cacheAppend", "latticeDeformKeyCtx", "ExportOptions", "HypershadeGridToggleSnap", "GetHIKEffectorCount", "interactionStyle", "filterCurve", "reroot", "getLastError", "detachCurve", "shelfButton", "FBXGetTakeCount", "listNodesWithIncorrectNames", "polySelect", "setParent", "CutKeys", "ClearCurrentCharacterList", "ModifyStampDepthPress", "NodeEditorToggleConsistentNodeNameSize", "HypershadeOutlinerPerspLayout", "polySlideEdgeCtx", "ImportAnimOptions", "FBXExportConvert2Tif", "OutlinerExpandAllItems", "intersect", "DeleteStaticChannelsOptions", "SquashOptions", "createPolyPyramidCtx", "AddTargetShapeOptions", "shapeCompare", "polyPlanarProjection", "snapshotModifyKeyCtx", "HypershadeConnectSelected", "nodeType", "CreatePolygonToolOptions", "HypershadePickWalkRight", "canCreateManip", "UnfoldPackUVs3DInEmptyTile", "PolySelectToolOptions", "EnableGlobalStitch", "canvas", "ShowAll", "ShowMeshSmearToolOptions", "SetMeshSculptTool", "nClothDeleteCacheFrames", "SetNClothStartFromMesh", "RemoveBifrostAccelerator", "PolyMergeVertices", "nodeTreeLister", "ContentBrowserWindow", "polyMapCut", "xgmGuideRender", "subdDisplayMode", "SelectMaskToolMarkingMenu", "ReducePolygon", "CopyVertexSkinWeights", "GlobalStitchOptions", "xgmClumpBrushContext", "spBirailCtx", "polySlideEdge", "FillHole", "CreatePolygonTorus", "CloudImportExport", "FBXExportReferencedContainersContent", "sbs_SetEditionModeScale", "MoveLeft", "DeleteMotionPaths", "TogglePolyDisplaySoftEdges", "dynCache", "SelectHierarchy", "OneClickMotionBuilderSendToCurrentScene", "AnimationSnapshot", "renderPassRegistry", "CutUVs3D", "listConnections", "CycleIKHandleStickyState", "PruneSmallWeights", "paramLocator", "xgmAddGuide", "boxZoomCtx", "HideLights", "resampleFluid", "ilrIBLCmd", "muMessageAdd", "ReducePolygonOptions", "NewScene", "RemoveBindingSet", "MakePressureCurveOptions", "CreateSubdivSurfaceOptions", "ShowAnimationUI", "HypershadeSelectMaterialsFromObjects", "reverseCurve", "arubaNurbsToPoly", "ProjectWindow", "ShowWrapInfluences", "rampWidget", "NodeEditorIncreaseTraversalDepth", "NodeEditorBackToParent", "coarsenSubdivSelectionList", "FBXExportConvertUnitString", "SetFullBodyIKKeysBodyPart", "SymmetrizeUVBrushSizeOff", "AddBifrostMotionField", "TogglePolygonFaceCenters", "ParticleInstancer", "ModifyDisplacementPress", "itemFilterAttr", "AttachSelectedAsSourceField", "caddyManip", "TangentsPlateau", "sbs_GetBakeFormat", "polyEvaluate", "polySelectEditCtx", "CommandWindow", "polySetToFaceNormal", "deltaMush", "polySeparate", "XgmSetNoiseBrushTool", "hardware", "RemoveBifrostCollider", "saveInitialState", "HypergraphDecreaseDepth", "dR_setRelaxAffectsBorders", "U3DBrushSizeOn", "AddHolderOptions", "xgmDataQueryHelperForTest", "attrControlGrp", "ModifyOpacityRelease", "clearDynStartState", "RemoveMaterialSoloing", "subdListComponentConversion", "MoveRotateScaleTool", "TextureViewWindow", "FitBSpline", "FBXResamplingRate", "PaintRandomOptions", "dR_hypershadeTGL", "dR_gridSnapPress", "muMessageQuery", "ToggleDisplayGradient", "FBXExportApplyConstantKeyReducer", "ExportSelectionOptions", "polyLayoutUV", "AbortCurrentTool", "sphere", "TexSewDeactivateBrushSize", "makePaintable", "RemoveLatticeTweaks", "FBXImportShapes", "polyMultiLayoutUV", "filter", "showHelp", "polySelectSp", "ViewAlongAxisY", "goal", "ViewAlongAxisZ", "ToggleHelpLine", "timeEditorBakeClips", "ATOMTemplateOptions", "AppendToPolygonToolOptions", "ToggleBackfaceGeometry", "NodeEditorGraphNoShapes", "dR_mtkToolTGL", "subdAutoProjection", "HypershadeToggleZoomOut", "dynPref", "AddSelectionAsInBetweenTargetShape", "waitCursor", "ToggleUVEditorUVStatisticsHUDOptions", "hwRenderLoad", "RemoveBifrostAdaptiveMesh", "SubdivToNURBSOptions", "UnfoldUV", "ilrCreateSharedUVCmd", "DeleteCurrentColorSet", "UpdateCurrentScene3dsMax", "AddBifrostAccelerator", "CreateTextureDeformer", "choice", "OutlinerToggleReferenceMembers", "HypershadeShowConnectedAttrs", "hikBodyPart", "querySubdiv", "AbcExport", "polyFlipUV", "ToggleFaceIDs", "BatchBakeOptions", "createPolyPipeCtx", "SnapToGrid", "AddSelectionAsCombinationTargetOptions", "attrEnumOptionMenu", "GravityOptions", "viewLookAt", "Extrude", "FBXExportQuaternion", "SetStrokeControlCurves", "meshReorderContext", "GraphCut", "panZoomCtx", "displaySurface", "TimeEditorFrameAll", "RemoveShrinkWrapInnerObject", "OutTangentSpline", "help", "polyToSubdiv", "enableDevice", "PolygonCollapse", "assignInputDevice", "ShowSelectedObjects", "flowLayout", "EnableFluids", "SaveFluidStateAs", "ModifyConstraintAxisOptions", "OutlinerRevealSelected", "polyCollapseFacet", "modelingToolkitSuperCtx", "ClusterCurve", "SelectContainerContents", "ClosestPointOnOptions", "ikHandleDisplayScale", "timeEditorClip", "xgmWrapXGen", "polyConnectComponents", "MirrorCutPolygonGeometry", "SelectPolygonToolMarkingMenu", "FreezeTransformationsOptions", "saveViewportSettings", "HypershadeShowCustomAttrs", "reproInstancer", "CreatePondOptions", "xpmPicker", "polyRetopo", "GraphCopyOptions", "ReverseCurveOptions", "CreatePointLightOptions", "batchRender", "dolly", "Art3dPaintTool", "ParentOptions", "NodeEditorGraphAllShapes", "resetTool", "subdCleanTopology", "convertSolidTx", "FlipUVs", "PickWalkRightSelect", "AlignUVOptions", "polyCacheMonitor", "UnmirrorSmoothProxyOptions", "PolygonSoftenHardenOptions", "ShowRenderingUI", "HypershadeCreatePSDFile", "pluginDisplayFilter", "Lightning", "RotateToolWithSnapMarkingMenu", "directConnectPath", "HypershadeRenameActiveTab", "playblast", "NodeEditorPinSelected", "hilite", "ShowFur", "xgmLengthBrushContext", "containerView", "listInputDeviceAxes", "SnapToCurvePress", "cMuscleWeightSave", "SelectAllLattices", "TexSculptActivateBrushStrength", "Newton", "XgmSetCutBrushTool", "HypershadeRenderPerspLayout", "RetimeKeysToolOptions", "radial", "dR_selConstraintElement", "U3DBrushPressureOff", "NodeEditorConnectionStyleStraight", "RenderViewNextImage", "TimeEditorSetKey", "IncreaseExposureCoarse", "openMayaPref", "renderInfo", "DeleteAllIKHandles", "CutPolygon", "XgmSetDensityBrushToolOption", "selectKeyCtx", "TranslateToolMarkingMenuPopDown", "CPMeldoIt__1703324687", "CreateNURBSPlaneOptions", "OutTangentPlateau", "FBXExportAnimationOnly", "NamespaceEditor", "workspacePanel", "MirrorSubdivSurfaceOptions", "Quadrangulate", "event", "UnpublishAttributes", "OpenCloseSurfaces", "renderWindowEditor", "BreakShadowLinks", "dR_symmetrize", "copyDeformerWeights", "rebuildSurface", "FloodSurfaces", "OutTangentFixed", "HypershadeSelectObjectsWithMaterials", "AlembicExportAll", "listSets", "colorManagementPrefs", "polyColorPerVertex", "selectKey", "Revolve", "copyNode", "xgmPromoteRender", "dR_setRelaxAffectsAll", "displaySmoothness", "geometryCacheOpt", "SendToUnrealSelection", "polyReduce", "tumbleCtx", "RenderViewWindow", "EmptyAnimLayer", "DisplayUVShaded", "uvLink", "PoleVectorConstraintOptions", "renameUI", "manipPivot", "xgmSplineSetCurrentDescription", "ToggleUVIsolateViewSelected", "jointCluster", "ModifyPaintValueRelease", "OutlinerToggleOrganizeByLayer", "HideJoints", "ToggleChannelsLayers", "launch", "NEmitFromObject", "XgmSetLengthBrushTool", "SetMeshScrapeTool", "StraightenCurvesOptions", "FBXExportUseTmpFilePeripheral", "PolyMerge", "rigidBody", "canCreateCaddyManip", "timePort", "MakeBrushSpringOptions", "selectKeyframeRegionCtx", "furMeshArea", "deleteExtension", "AnimationSnapshotOptions", "arcLenDimContext", "renameAttr", "geometryConstraint", "attributeMenu", "RigidBindSkin", "StitchSurfacePoints", "PointOnCurve", "DeleteSurfaceFlow", "SetRigidBodyInterpenetration", "SetMeshFillTool", "fileBrowserDialog", "PolyEditEdgeFlow", "FBXImportConstraints", "instancer", "HideNURBSCurves", "openGLExtension", "SubdivSmoothnessMediumOptions", "roundConstantRadius", "LoftOptions", "exclusiveLightCheckBox", "TurbulenceOptions", "AddAttribute", "BakeChannel", "texManipContext", "xgmDensityComp", "createNurbsPlaneCtx", "HypershadeImport", "InsertIsoparms", "setRenderPassType", "ilrRenderWindowCmd", "promptDialog", "TimeEditorFrameSelected", "truncateHairCache", "FBXImportLights", "dR_meshAlphaTGL", "nodeCast", "UVSnapTogether", "polyDuplicateEdge", "ParentConstraintOptions", "saveImage", "ExportOfflineFileOptions", "HypershadePickWalkUp", "SelectCVsMask", "NodeEditorSetTraversalDepthZero", "relationship", "DeleteAllDynamicConstraints", "launchImageEditor", "BridgeEdgeOptions", "bakeClip", "HypershadeDeleteNodes", "detachDeviceAttr", "Gravity", "LockTangentWeight", "PruneLattice", "XgmSetPartBrushToolOption", "dR_selectPress", "polySpinEdge", "XgmSetLengthBrushToolOption", "HideNonlinears", "PolygonNormalEditTool", "PaintEffectsToPoly", "subdivDisplaySmoothness", "TexSculptUnpinAll", "SelectContiguousEdges", "InTangentClamped", "curveCVCtx", "hitTest", "setEditCtx", "AddBlendShape", "TimeEditorCutClips", "selectPriority", "ExportProxyContainerOptions", "SetFocusToNumericInputLine", "XgCreateDescriptionEditor", "hudSlider", "SaveHIKCharacterDefinition", "OptimzeUVs", "STRSTweakModeToggle", "Bevel", "xgmPlaceBrushContext", "TesselateSubdivSurfaceOptions", "timeEditorComposition", "PruneSmallWeightsOptions", "PaintCacheTool", "polyAppendFacetCtx", "draggerContext", "dR_convertSelectionToVertex", "TimeEditorCopyClips", "ShowMeshFreezeToolOptions", "ShowMeshFlattenToolOptions", "savePrefs", "NodeEditorGraphAddSelected", "ShowUIElements", "nucleusDisplayDynamicConstraintNodes", "ModifyStampDepthRelease", "DeleteEntireHairSystem", "OffsetEdgeLoopToolOptions", "DisableIKSolvers", "ScaleTool", "sculptTarget", "DisplayWireframe", "ConvertSelectionToUVShellBorder", "NodeEditorLayout", "MinimizeApplication", "timeCode", "ToggleSurfaceOrigin", "psdTextureFile", "PolyMergeOptions", "ShowPlanes", "play", "hotkeyEditorPanel", "getPanel", "polyBridgeEdge", "PolyExtrudeVerticesOptions", "UVGatherShells", "NodeEditorToggleShowNamespace", "CreateUVShellAlongBorder", "AssignBrushToHairSystem", "iGroom", "hasMetadata", "scriptJob", "AddShrinkWrapSurfaces", "HypershadeDeleteAllLights", "viewClipPlane", "UpdateCurrentSceneMudbox", "FBXImportAxisConversionEnable", "HideDeformingGeometry", "blindDataType", "ViewAlongAxisX", "torus", "artBaseCtx", "RevolveOptions", "HypershadeOpenModelEditorWindow", "ToggleHoleFaces", "DeactivateGlobalScreenSlider", "PlanarOptions", "blend", "GoToBindPose", "sbs_SetEngine", "RelaxInitialStateOptions", "TimeEditorClipRazor", "applyMetadata", "HypershadePickWalkDown", "HideHairSystems", "PlayblastWindow", "HideKinematics", "ShowIKHandles", "ShowMeshRelaxToolOptions", "PublishAttributes", "HypershadeDeleteAllShadingGroupsAndMaterials", "autoSave", "ToggleToolMessage", "ToolSettingsWindow", "polySelectConstraint", "CreateSubdivCylinder", "TimeEditorCreateClip", "SubdCutUVs", "dR_objectHideTGL", "LockContainer", "HideStrokes", "XgmSplineCacheDisableSelectedCache", "polyEditUVShell", "polyCone", "HypershadeHideAttributes", "ShortPolygonNormals", "FBXImportGenerateLog", "CreateDiskCacheOptions", "PasteKeysOptions", "ModelingPanelRedoViewChange", "IKSplineHandleToolOptions", "RenameCurrentColorSet", "TransplantHair", "diskCache", "TagAsController", "circle", "xform", "dynParticleCtx", "AbcBulletExport", "ilrVertexBakeCmd", "CutKeysOptions", "polyMapSew", "SurfaceEditingTool", "paintPointsCmd", "dR_symmetryTGL", "detachSurface", "filletCurve", "referenceQuery", "autoPlace", "TransferAttributeValues", "DeleteHairCache", "truncateFluidCache", "adskAssetList", "UpdateBindingSetOptions", "nClothMergeCache", "SelectUVBorderComponents", "SelectPolygonToolMarkingMenuPopDown", "LatticeUVToolOptions", "AutoPaintMarkingMenuPopDown", "ScaleCurvatureOptions", "sbs_GetEngine", "Help", "listAnimatable", "ConnectComponents", "blendTwoAttr", "HypershadeAddOnNodeCreate", "CreateHairCacheOptions", "offsetSurface", "getAttr", "PolySpinEdgeForward", "LevelOfDetailUngroup", "ToggleLatticeShape", "BakeSimulation", "SmoothSkinWeights", "AlembicExportSelection", "IKHandleToolOptions", "unknownPlugin", "ShowGeometry", "InsertKeysToolOptions", "MoveUp", "ConformPolygon", "polyOptions", "AbcImport", "CreateCharacter", "TransformNoSelectOnTool", "MergeVertexToolOptions", "Create2DContainer", "SymmetrizeUVOptions", "HIKLiveConnectionTool", "polyChipOff", "DisplayShadedAndTextured", "polySphericalProjection", "ConvertSelectionToVertexPerimeter", "polySubdivideEdge", "InTangentFixed", "mouldMesh", "SelectVertexMask", "createLayeredPsdFile", "xgmNoiseBrushToolCmd", "NodeEditorSelectUpStream", "intScrollBar", "setDynStartState", "MakeBoats", "sculptMeshCacheCtx", "untangleUV", "HyperGraphPanelUndoViewChange", "UVEditorUnpinAll", "progressWindow", "subdiv", "renderQualityNode", "GraphEditor", "SendToUnityAll", "dgstats", "SelectTextureReferenceObject", "ShowKinematics", "FBXExportInAscii", "AveragePolygonNormals", "dR_bevelRelease", "scriptTable", "HypershadeDisplayInterestingShapes", "NodeEditorGridToggleCrosshairOnEdgeDragging", "scriptedPanelType", "GraphCutOptions", "selectKeyframe", "DistributeUVsOptions", "ToggleMainMenubar", "NodeEditorToggleNodeSwatchSize", "TexSculptDeactivateBrushSize", "ModifyDisplacementRelease", "ShowLattices", "grabColor", "FBXExportColladaSingleMatrix", "SnapToPointPress", "paintEffectsDisplay", "RotateToolOptions", "SculptSubdivsTool", "dR_meshOffsetTGL", "UnlockNormals", "ToggleShowResults", "LayoutUV", "EditFluidResolution", "bifMeshExport", "makeIdentity", "HypershadeDeleteUnusedNodes", "XgmSetSmoothBrushToolOption", "EditPolygonType", "dR_viewPersp", "cMuscleSimulate", "separator", "CreateContainer", "ikHandle", "CreateSubdivTorus", "MapUVBorder", "ToggleAnimationDetails", "dR_setExtendEdge", "AddBifrostKillField", "currentUnit", "FBXExportShapes", "DisplaySmoothShaded", "stereoRigManager", "HighQualityDisplay", "dR_coordSpaceWorld", "CreateAmbientLight", "dR_objectBackfaceTGL", "RelaxUVShell", "reloadImage", "GeometryToBoundingBox", "HypershadeMoveTabLeft", "OneClickDispatch", "rowColumnLayout", "SelectAllSubdivGeometry", "SetToFaceNormals", "DistributeUVs", "keyingGroup", "MoveDown", "CreateNodeWindow", "xgmDirectionBrushContext", "HypershadeRemoveAsset", "xgmPolyToGuide", "ShowRiggingUI", "ScaleToolWithSnapMarkingMenu", "ScaleConstraint", "SaveBrushPreset", "FBXClose", "ConvertSelectionToEdgePerimeter", "NextFrame", "HIKCycleMode", "PolygonBooleanUnion", "XgmSetGrabBrushToolOption", "artAttrPaintVertexCtx", "GoToMaxFrame", "requires", "SmoothBindSkinOptions", "ConvertSelectionToContainedEdges", "polyMoveVertex", "xgmSetActive", "SubdivSmoothnessRoughOptions", "HypergraphHierarchyWindow", "TimeEditorClipLoopToggle", "srtContext", "orientConstraint", "SetTimecode", "XgmSetFreezeBrushTool", "geoUtils", "PolyConvertToRingAndCollapse", "ImportDeformerWeights", "FlowPathObjectOptions", "viewHeadOn", "mrMapVisualizer", "SetMeshAmplifyTool", "sbs_GoToMarketPlace", "VertexNormalEditTool", "typeManipContextCommand", "SelectHullsMask", "renderWindowSelectContext", "dR_showAbout", "addDynamicAttribute", "error", "ShowHotbox", "setDynamicsInitialState", "HypershadeConvertPSDToFileTexture", "LayerRelationshipEditor", "CurveFlowOptions", "savePrefObjects", "DopeSheetEditor", "displayCull", "xgmMakeGuideDynamic", "CVHardness", "spaceLocator", "xgmCreateSplineDescription", "TimeEditorCreateOverrideLayer", "RenderLayerRelationshipEditor", "dR_modePoly", "ilrDisplacementToPolyCmd", "SelectEdgeLoop", "PlaybackBackward", "hardwareRenderPanel", "cMuscleRayIntersect", "XgmSetWidthBrushToolOption", "polyPyramid", "PixelMoveRight", "alignCtx", "paint3d", "FBXImportCameras", "geometryDeleteCacheFramesOpt", "XgmSetSelectBrushTool", "RemoveSubdivProxyMirrorOptions", "ToggleFocalLength", "menuSetPref", "HypershadeRevertToDefaultTabs", "greaseRenderPlane", "HideLattices", "ogsdebug", "nucleusGetnParticleExample", "CreatePolygonSoccerBall", "convertUnit", "GLSLShader", "PaintOnPaintableObjects", "HypershadeCloseActiveTab", "ThreeRightSplitViewArrangement", "dR_DoCmd", "BrushAnimationMarkingMenuPopDown", "SnapToPixel", "TexSculptInvertPin", "IncreaseGammaFine", "ToggleFkIk", "PickColorDeactivate", "sampleImage", "OutlinerUnhide", "ctxCompletion", "intSlider", "iconTextRadioButton", "OutlinerCollapseAllItems", "TensionOptions", "layerButton", "SmoothingDisplayShowBoth", "layeredShaderPort", "createNurbsCircleCtx", "CreateSpring", "UniversalManip", "visor", "FBXImportAudio", "soloMaterial", "CreateAreaLightOptions", "ToggleCompIDs", "SetMeshMaskTool", "setKeyframeBlendshapeTargetWts", "CurlCurves", "SubdivSmoothnessFine", "softSelect", "UnlockContainer", "SelectUVFrontFacingComponents", "TimeEditorCreatePoseClip", "SetFullBodyIKKeys", "AlembicExportSelectionOptions", "DeleteEdge", "minimizeApp", "effector", "GpuCacheImport", "SmoothCurve", "devicePanel", "SelectAllBrushes", "StitchTogetherOptions", "MediumQualityDisplay", "FBXImportQuaternion", "PaintOnViewPlane", "XgmSplineCacheReplaceOptions", "nucleusGetEffectsAsset", "timeControl", "polySelectCtx", "fluidMergeCache", "dR_activeHandleY", "AddEdgeDivisionsOptions", "BendCurvesOptions", "AlignCameraToPolygon", "TogglePolygonFaceTriangles", "timeEditorAnimSource", "HypershadeToggleAttrFilter", "FBXExportTangents", "CurveFilletOptions", "particleRenderInfo", "cMuscleAbout", "distanceDimContext", "MoveNormalToolOptions", "PostInfinityCycle", "IncrementFluidCenter", "EnableNCloths", "disable", "FireOptions", "format", "swatchRefresh", "PickWalkUp", "CreateSubdivCone", "colorManagementFileRules", "attributeName", "OptimzeUVsOptions", "RetimeKeysTool", "Air", "ToggleKeepWireCulling", "CreateBezierCurveToolOptions", "EnableExpressions", "CreateExpressionClip", "AddBoatLocatorOptions", "groupParts", "CreateText", "xgmBrushManip", "SelectTimeWarp", "HypershadeAutoSizeNodes", "dR_scalePress", "ProfilerToolHideSelectedRepetition", "CreateNURBSTorusOptions", "rotate", "xgmCutBrushToolCmd", "SetFullBodyIKKeysKeyToPin", "DeleteTimeWarp", "MergeUV", "keyTangent", "MatchUVsOptions", "sbs_GetGraphsNamesFromSubstanceNode", "createCurveWarp", "SinglePerspectiveViewLayout", "ExtrudeVertexOptions", "SubdivSmoothnessHullOptions", "EmitFromObjectOptions", "GetHairExample", "SplitMeshWithProjectedCurveOptions", "createNurbsTorusCtx", "dbpeek", "GraphEditorValueLinesToggle", "PencilCurveTool", "MoveUVTool", "DisableMemoryCaching", "ToggleMultiColorFeedback", "selectType", "propModCtx", "curveEPCtx", "displayAffected", "XgmSplineCacheCreate", "marker", "FBXExportFinestSubdivLevel", "TogglePanelMenubar", "SmoothProxy", "ShowNURBSSurfaces", "CreateNURBSTorus", "NodeEditorGraphRemoveUnselected", "polyEditUV", "SetKeyTranslate", "FBXExportSplitAnimationIntoTakes", "ReversePolygonNormals", "xgmBakeGuideVertices", "RemoveWireOptions", "scale", "nexQuadDrawCtx", "AddBifrostFoam", "polyCreateFacetCtx", "affects", "LODGenerateMeshes", "softModContext", "dR_lockSelTGL", "graphDollyCtx", "CreateVolumeLight", "TransformPolygonComponentOptions", "polyCutUVCtx", "dropoffLocator", "polyCanBridgeEdge", "ToggleFaceNormals", "CreateBezierCurveTool", "SetPreferredAngleOptions", "evalDeferred", "messageLine", "CreatePolygonUltraShapeOptions", "geometryDeleteCacheFrames", "SelectPreviousObjects3dsMax", "SelectAllNCloths", "AddDynamicBuoy", "copyAttr", "subdMatchTopology", "NodeEditorConnectNodeOnCreation", "GetFluidExample", "SetInitialState", "PaintGrid", "SelectAllGeometry", "CreateNURBSCircleOptions", "WrinkleToolOptions", "bulletAlignRigidBody", "insertKnotSurface", "dR_multiCutTool", "deleteNclothCache", "MergeUVOptions", "dR_quadDrawRelease", "WeightedTangents", "ParentBaseWire", "PolygonCopyOptions", "xgmPlaceBrushToolCmd", "filterStudioImport", "CreateNURBSSquareOptions", "CutUVsWithoutHotkey", "PickWalkStopAtTransform", "dR_softSelDistanceTypeVolume", "SelectEdgeMask", "artSelect", "texMoveContext", "SubdivSurfacePolygonProxyMode", "AlignCurve", "manipRotateLimitsCtx", "ogsRender", "doBlur", "PickWalkOut", "PreviousGreasePencilFrame", "polyTriangulate", "dR_convertSelectionToUV", "ModifyUVVectorPress", "AnimationSweepOptions", "nucleusDisplayNComponentNodes", "playbackOptions", "preferredRenderer", "SmoothBindSkin", "ResetLattice", "colorIndexSliderGrp", "stackTrace", "SurfaceBooleanIntersectTool", "curveAddPtCtx", "CloseFrontWindow", "CreateCameraOnly", "artFluidAttr", "nClothCreate", "NodeEditorShowAllAttrs", "ToggleChannelBox", "SelectAllClusters", "FBXUIShowOptions", "XgmSetDirectionBrushTool", "BreakRigidBodyConnection", "ShowClusters", "bifrost", "PolyCreaseToolOptions", "Drag", "dR_extrudePress", "ExtrudeEdge", "CreateNURBSSphere", "CenterViewOfSelection", "camera", "dagObjectHit", "AddSelectionAsInBetweenTargetShapeOptions", "dR_slideSurface", "ShowStrokeControlCurves", "HypershadeWindow", "MergeMultipleEdgesOptions", "ShowControllers", "CreateOceanWakeOptions", "RotateToolMarkingMenu", "OneClickSetCallback", "curveMoveEPCtx", "artAttrSkinPaint", "editorTemplate", "HypershadeOpenOutlinerWindow", "CreateCreaseSetOptions", "Snap3PointsTo3Points", "flexor", "NodeEditorToggleZoomOut", "dollyCtx", "NodeEditorShapeMenuStateAllExceptShadingGroupMembers", "editRenderLayerAdjustment", "texWinToolCtx", "CreatePolygonPyramid", "xgmCurveToGuide", "ExtendFluidOptions", "bevel", "HypershadeOpenPropertyEditorWindow", "selectMode", "MakePondMotorBoatsOptions", "SquareSurfaceOptions", "SetMeshBulgeTool", "TwoPointArcToolOptions", "textureWindow", "SmoothSkinWeightsOptions", "reorder", "FilletBlendToolOptions", "nClothMergeCacheOpt", "HypershadeRefreshSelectedSwatchesOnDisk", "SmoothingDisplayToggle", "CleanupPolygonOptions", "TimeEditorWindow", "PaintEffectsPanel", "AlembicOpen", "SelectComponentToolMarkingMenu", "BifMeshImport", "PolygonCollapseEdges", "OptimizeScene", "reorderContainer", "MakeHoleToolOptions", "PolyExtrude", "shadingGeometryRelCtx", "warning", "attachFluidCache", "skinBindCtx", "keyframeRegionSetKeyCtx", "FireworksOptions", "componentEditor", "TimeEditorToggleSoloSelectedTracks", "rampColorPort", "TogglePolyUVsCreateShader", "clipEditorCurrentTimeCtx", "HideHotbox", "SmoothPolygon", "DeleteChannelsOptions", "textManip", "image", "CreateBlendShapeOptions", "polyCBoolOp", "GroupOptions", "SendToUnitySetProject", "MergeVertexTool", "ExportDeformerWeightsOptions", "fitBspline", "ReverseSurfaceDirection", "MoveInfluence", "SnapToMeshCenter", "U3DBrushPressureOn", "ShrinkLoopPolygonSelectionRegion", "AssumePreferredAngle", "SelectCurveCVsLast", "InteractivePlayback", "HIKBodyPartMode", "PaintRandom", "FBXImportProtectDrivenKeys", "NURBSSmoothnessHull", "HypershadeShapeMenuStateAll", "RemoveShrinkWrapTarget", "AverageVertex", "setInfinity", "ProfilerToolShowAll", "drag", "HypershadeToggleZoomIn", "currentTimeCtx", "eval", "NodeEditorGraphRemoveUpstream", "wrinkle", "MoveNearestPickedKeyToolActivate", "SubdividePolygonOptions", "DetachSurfaces", "RerootSkeleton", "GraphDeleteOptions", "ToggleStatusLine", "hudButton", "CreateOceanOptions", "dgcontrol", "xgmSetAttr", "orbit", "renderSetupPostApply", "defineDataServer", "PolygonSoftenHarden", "ShowDynamicsUI", "dockControl", "FrameSelectedWithoutChildrenInAllViews", "NURBSToPolygonsOptions", "InsertIsoparmsOptions", "HypershadeDuplicateWithoutNetwork", "dR_scaleTweakTool", "FBXImportMergeBackNullPivots", "deformerEvaluator", "dgdebug", "FBXImportUnlockNormals", "geometryExportCache", "ToggleUVEditorUVStatisticsHUD", "HypershadeOpenGraphEditorWindow", "RebuildSurfacesOptions", "ParticleCollisionEvents", "stitchSurfaceCtx", "CopySelected", "toggle", "HypershadeGraphUpDownstream", "menuEditor", "XgmSetNoiseBrushToolOption", "dR_timeConfigTGL", "Quit", "dR_customPivotToolPress", "itemFilterRender", "SoftModToolOptions", "HypershadeShapeMenuStateAllExceptShadingGroupMembers", "DragOptions", "HypershadeSelectLights", "polyMergeVertex", "Parent", "artFluidAttrCtx", "PaintEffectsGlobalSettings", "menuBarLayout", "BevelPlus", "HypershadeDisplayAsExtraLargeSwatches", "GPUBuiltInDeformerControl", "polyRetopoCtx", "PolygonClearClipboardOptions", "getFileList", "checkBoxGrp", "ShowAllPolyComponents", "polyPrimitiveMisc", "AddEdgeDivisions", "SubdivToNURBS", "OutTangentClamped", "RemoveSubdivProxyMirror", "polySplitEdge", "xgmMoveDescription", "FluidEmitterOptions", "ToggleSoftEdges", "regionSelectKeyCtx", "EnableSelectedIKHandles", "DefaultQualityDisplay", "scriptEditorInfo", "ContentBrowserLayout", "XgGroomingVis", "NodeEditorRenameActiveTab", "xgmNop", "FBXExportSmoothMesh", "OrientJoint", "rollCtx", "SnapToPointRelease", "SetMeshEraseTool", "SquareSurface", "dR_overlayAppendMeshTGL", "MatchTransform", "PaintSetMembershipTool", "SetMeshFreezeTool", "ModifyLowerRadiusPress", "dR_bridgePress", "HypershadeRestoreLastClosedTab", "button", "Create2DContainerEmitter", "Unfold3DuvUpdateCommand", "HIKSetFullBodyKey", "RotateUVs", "webBrowserPrefs", "webBrowser", "showHidden", "CreateLattice", "BothProxySubdivDisplay", "subdCollapse", "GetOceanPondExample", "toolCollection", "UVAutomaticProjectionOptions", "xgmSplineQuery", "popupMenu", "floatScrollBar", "ViewImage", "AddBifrostFoamMask", "nurbsPlane", "HypershadeShowAllAttrs", "GetHIKChildId", "createEditor", "ExportOfflineFile", "CreateNURBSCube", "xgmPreview", "NURBSSmoothnessHullOptions", "BrushPresetBlendShape", "makeSingleSurface", "BridgeEdge", "LatticeDeformKeysToolOptions", "ShowManipulators", "nClothDeleteCacheOpt", "CreateMotionTrailOptions", "shotTrack", "InsertKnot", "cone", "SurfaceBooleanUnionTool", "AttachSurfacesOptions", "dR_renderGlobalsTGL", "Squash", "DecreaseGammaCoarse", "CreateBlendShape", "SelectAllRigidBodies", "ToggleSymmetryDisplay", "nexCtx", "SelectAllFluids", "optionMenu", "refineSubdivSelectionList", "CreateImagePlaneOptions", "deviceManager", "DuplicateEdgesOptions", "dR_paintPress", "poseEditor", "dR_cycleCustomCameras", "polyExtrudeFacet", "polyCube", "DisableSelectedIKHandles", "RemoveBifrostEmitter", "SaveSceneOptions", "StraightenCurves", "Create3DContainerOptions", "NextGreasePencilFrame", "progressBar", "dR_selectModeMarquee", "applyAttrPattern", "MakeCollideHair", "BreakTangent", "SnapKeysOptions", "extendFluid", "InTangentFlat", "HideIKHandles", "MirrorPolygonGeometry", "dR_quadDrawPress", "TextureCentricUVLinkingEditor", "dR_contextChanged", "CreateConstructionPlaneOptions", "menu", "timeField", "WalkTool", "StraightenUVBorderOptions", "DuplicateSpecial", "CopyUVs", "AddBifrostEmitter", "FluidGradients", "CreateShotOptions", "paramDimension", "ShowMeshEraseToolOptions", "dR_paintRelease", "ikSpringSolverRestPose", "MovePolygonComponentOptions", "TangentsFixed", "redo", "nurbsToPolygonsPref", "InitialFluidStatesOptions", "nSoft", "GraphEditorUnlockChannel", "OutlinerToggleAutoExpandLayers", "freeFormFillet", "StitchTogether", "SurfaceBooleanIntersectToolOptions", "writeTake", "attachDeviceAttr", "hikGlobals", "BakeNonDefHistory", "SubdivSurfaceCleanTopology", "LoadHIKCharacterState", "binMembership", "pointOnSurface", "DeleteSelectedContainers", "XgmSplineCacheDeleteOptions", "polyUVStackSimilarShellsCmd", "getClassification", "InsertKeyToolActivate", "inViewMessage", "duplicateCurve", "panel", "nClothAppendOpt", "PasteUVs", "FBXImportSetMayaFrameRate", "dR_targetWeldRelease", "PaintVertexColorToolOptions", "CreatePlatonicSolidOptions", "EvaluationToolkit", "SetRigidBodyCollision", "dR_increaseManipSize", "dR_softSelStickyPress", "GoToMinFrame", "renderSetupLegacyLayer", "ToggleVertexNormalDisplay", "bezierCurveToNurbs", "assignViewportFactories", "LatticeDeformKeysTool", "autoKeyframe", "HypershadeOpenConnectWindow", "DeleteAllChannels", "SelectVertexFaceMask", "walkCtx", "SelectAllMarkingMenu", "viewCamera", "CreateQuickSelectSet", "FBXPopSettings", "SurfaceBooleanSubtractToolOptions", "GoToPreviousDrivenKey", "LongPolygonNormals", "MergeCharacterSet", "CreateSet", "polyCollapseTweaks", "SelectMeshUVShell", "dR_coordSpaceLocal", "attachSurface", "polySubdivideFacet", "mateCtx", "cleanPerFaceAssignment", "CreateNURBSConeOptions", "DeleteAllContainers", "control", "nurbsToPoly", "ShowJoints", "DecreaseManipulatorSize", "UVCylindricProjection", "GraphPaste", "UnfoldUVOptions", "ArtPaintSkinWeightsTool", "Birail2Options", "PolySelectTool", "HypershadeGraphRemoveUnselected", "ShareColorInstances", "uiTemplate", "ToggleSurfaceFaceCenters", "AssignNewMaterial", "dR_preferencesTGL", "renderSetupHighlight", "fluidDeleteCache", "BatchBake", "ClearBifrostInitialState", "NormalConstraint", "xgmGroomTransfer", "dR_selectModeRaycast", "radioMenuItemCollection", "SubdivSurfaceHierarchyMode", "NodeEditorShowAllCustomAttrs", "boneLattice", "ExtendCurveOptions", "namespace", "ProjectCurveOnMesh", "Wave", "DeleteAllSounds", "ToggleCreaseEdges", "polyCylinder", "InTangentPlateau", "getProcArguments", "geometryReplaceCacheFrames", "PluginManager", "getDefaultBrush", "OneClickSetupMotionBuilderCharacterStream", "tension", "select", "CreateConstructionPlane", "CreateNSoftBodyOptions", "displayColor", "nucleusDisplayTextureNodes", "ToggleUVEditorIsolateSelectHUD", "ToggleSelectDetails", "DetachSkeleton", "Triangulate", "prepareRender", "RemoveBlendShapeOptions", "SoloMaterial", "ToggleAutoFrame", "clipSchedule", "ToggleOppositeFlagOfSelectedShapes", "xgmDensityBrushToolCmd", "renderLayerMembers", "PolyMergeEdges", "HypershadeSelectTextures", "cMuscleWeightMirror", "OutlinerToggleIgnoreHidden", "HypershadeRenameTab", "nurbsCurveRebuildPref", "ShowBatchRender", "panZoom", "sbs_GetGlobalTextureHeight", "HypershadeExpandAsset", "palettePort", "snapKey", "CreatePolygonHelix", "showWindow", "stereoCameraView", "HypershadeGraphMaterialsOnSelectedObjects", "nexConnectContext", "WhatsNewHighlightingOn", "LockCamera", "HideDynamicConstraints", "ogs", "UniformOptions", "mute", "keyframeStats", "SubdivSmoothnessFineOptions", "FBXExportHardEdges", "move", "ToggleUVShellBorder", "FullCreaseSubdivSurface", "ShowLightManipulators", "XgmSetGrabBrushTool", "SetAsCombinationTargetOptions", "sbs_EditSubstance", "RedoPreviousRender", "InsertEdgeLoopTool", "sbs_GetEnumValue", "createSubdivRegion", "sbs_AffectedByAllInputs", "setXformManip", "MakePondMotorBoats", "EditTexture", "SelectEdgeRing", "nodeIconButton", "MergeToCenter", "polyUVSet", "HideNParticles", "HypershadeOpenMaterialViewerWindow", "ShowMeshSmoothToolOptions", "xgmSelectBrushContext", "ToggleMeshPoints", "NormalConstraintOptions", "CopyUVsToUVSetOptions", "SplitVertex", "addDynamic", "ShowSculptObjects", "EnableMemoryCaching", "ls", "Sine", "RedoViewChange", "RebuildCurve", "CustomNURBSSmoothness", "sbs_SetAutoBake", "CreateTextureReferenceObject", "FluidGradientsOptions", "SelectSurfacePointsMask", "python", "createPolyCubeCtx", "FBXImportShowUI", "ShowSubdivSurfaces", "ikfkDisplayMethod", "ShowMeshFoamyToolOptions", "RelaxUVShellOptions", "bufferCurve", "SwapBufferCurve", "ToggleMeshEdges", "UnghostObject", "align", "TangetConstraint", "KeyframeTangentMarkingMenu", "ParticleTool", "geometryReplaceCache", "PreInfinityCycle", "UVCameraBasedProjectionOptions", "CommandShell", "geomBind", "SplitPolygonToolOptions", "objectType", "RemoveFromCharacterSet", "TimeEditorExplodeGroup", "FloatSelectedObjectsOptions", "CreateOceanWake", "radioCollection", "scriptNode", "debugVar", "CreateAreaLight", "OpenCloseSurfacesOptions", "wireContext", "attrColorSliderGrp", "OutlinerToggleReferenceNodes", "xgmPatchInfo", "rowLayout", "SelectAllHairSystem", "aaf2fcp", "SetDrivenKey", "spreadSheetEditor", "displayString", "dR_nexTool", "MarkingMenuPopDown", "AlembicExportAllOptions", "XgmSplineCacheDelete", "displayPref", "fileDialog2", "SetToFaceNormalsOptions", "twoPointArcCtx", "GraphPasteOptions", "HypershadeDisplayAllShapes", "polySuperCtx", "MirrorDeformerWeightsOptions", "AddAnimationOffset", "PolyExtrudeFacesOptions", "doubleProfileBirailSurface", "TransferVertexOrder", "SelectAllOutput", "FreezeTransformations", "CleanupPolygon", "NodeEditorGraphRemoveDownstream", "SeparatePolygon", "PixelMoveLeft", "attributeInfo", "ConvertSelectionToFaces", "FBXExportGenerateLog", "GlobalDiskCacheControl", "displayLevelOfDetail", "IPROptions", "FBXExportIncludeChildren", "renderSetup", "HypershadeRenderTextureRange", "ArchiveScene", "movieCompressor", "cMuscleWeight", "dR_modeVert", "PruneWire", "cacheFileTrack", "xgmSmoothBrushContext", "dR_testCmd", "NEmitFromObjectOptions", "xgmCutBrushContext", "symmetricModelling", "FloatSelectedPondObjectsOptions", "insertKnotCurve", "PolygonSoftenEdge", "OutlinerCollapseAllSelectedItems", "HideUnselectedCVs", "WireToolOptions", "dR_multiCutRelease", "listAttrPatterns", "cmdFileOutput", "GraphEditorNeverDisplayTangents", "UntrimSurfaces", "furNurbsArea", "DeleteAllParticles", "dR_coordSpaceCustom", "CreatePolygonCube", "UVUnstackShells", "xgmParticleRender", "connectAttr", "timer", "SplitEdgeRingToolOptions", "dR_loadRecentFile2", "SculptReferenceVectorMarkingMenuRelease", "sbs_GetAutoBake", "createNurbsCubeCtx", "glRender", "HideControllers", "dR_selectInvert", "PaintFluidsTool", "cameraSet", "EditOversamplingForCacheSettings", "FBXExportConstraints", "EnableRigidBodies", "pickWalk", "shaderfx", "BakeAllNonDefHistory", "refreshEditorTemplates", "SetBreakdownKey", "meshIntersectTest", "TimeEditorGhostTrackToggle", "ShowDeformingGeometry", "ScaleToolMarkingMenuPopDown", "FBXImportSkeletonDefinitionsAs", "ShowPolygonSurfaces", "polyExtrudeVertex", "ToggleUVs", "PerspGraphHypergraphLayout", "DuplicateEdges", "CreatePolygonPipe", "scrollField", "shapeEditor", "SplitEdgeRingTool", "gameExporter", "Fireworks", "GetHIKParentId", "ClearCurrentContainer", "PolyDisplayReset", "AssignOfflineFileFromRefEdOptions", "listInputDeviceButtons", "colorEditor", "getFluidAttr", "dagCommandWrapper", "SelectObjectsIlluminatedByLight", "SelectAll", "SculptMeshActivateBrushSize", "PolygonClearClipboard", "commandLogging", "agFormatIn", "ShotPlaylistEditor", "SetFullBodyIKKeysAll", "ConnectJointOptions", "Planar", "SendToUnitySelection", "SelectNextIntermediatObject", "MergeEdgeToolOptions", "ShowMeshPinchToolOptions", "nexMultiCutContext", "CreatePolygonConeOptions", "ToggleVisibilityAndKeepSelection", "PokePolygon", "closeSurface", "ShowMeshFillToolOptions", "Create3DContainerEmitter", "pushPinning", "CreatePassiveRigidBody", "TangentsLinear", "GoToNextDrivenKey", "PublishParentAnchorOptions", "polyMoveUV", "GpuCacheExportSelectionOptions", "FBXExportCacheFile", "dR_autoWeldTGL", "SmokeOptions", "dynGlobals", "threadCount", "CreateSubdivPlane", "CurveSmoothnessFine", "PreferencesWindow", "ShowMeshSprayToolOptions", "FBXExportFileVersion", "PreviousViewArrangement", "Redo", "AddWire", "SelectEdgeLoopSp", "StitchSurfacePointsOptions", "textFieldGrp", "SculptReferenceVectorMarkingMenuPress", "isTrue", "dR_vertUnlockAll", "curveSketchCtx", "MakeLightLinks", "FBXImportFillTimeline", "EnableNParticles", "dR_viewLightsTGL", "PaintGeomCacheTool", "userCtx", "saveMenu", "createPolyPlaneCtx", "RecentCommandsWindow", "webView", "DeleteAllNCloths", "GoToDefaultView", "CreateImagePlane", "ScaleToolOptions", "ctxData", "HIKUiControl", "jointCtx", "HypershadeExportSelectedNetwork", "CreatePolygonType", "instance", "dR_scaleRelease", "editImportedStatus", "HideNURBSSurfaces", "sbs_GetPackageFullPathNameFromSubstanceNode", "xgmNullRender", "igBrush", "retimeHelper", "xgmRebuildCurve", "FluidEmitter", "OutlinerToggleSetMembers", "EnableSnapshots", "unloadPlugin", "AddWireOptions", "ProportionalModificationTool", "SculptSurfacesTool", "keyframeRegionDirectKeyCtx", "ThreePointArcTool", "UniversalManipOptions", "dagObjectCompare", "xgmGrabBrushContext", "Radial", "dynTestData", "CreateSubdivSurface", "subdMirror", "PolyExtrudeOptions", "u3dOptimize", "dR_wireframeSmoothTGL", "CreateNSoftBody", "SculptPolygonsToolOptions", "ModifyUpperRadiusRelease", "renderSetupFind", "apfEntityNode", "MakeShadowLinks", "NodeEditorAutoSizeNodes", "Export", "Bend", "TimeEditorKeepTransitionsTogglePress", "SetMeshSmearTool", "fileDialog", "constrain", "xgmExport", "setToolTo", "TimeEditorPasteClips", "orbitCtx", "DeleteMemoryCaching", "profilerTool", "EmitFromObject", "SelectUVOverlappingComponents", "Goal", "substituteGeometry", "WarpImage", "GrowLoopPolygonSelectionRegion", "DeleteHair", "xgmGuideSculptToolCmd", "geometryDeleteCacheOpt", "UVEditorFrameAll", "AddTargetShape", "reference", "NodeEditorGraphRemoveSelected", "MergeMultipleEdges", "manipRotateContext", "FineLevelComponentDisplay", "UnlockCurveLength", "adskRepresentation", "polyColorMod", "cgfxShader", "subdPlanarProjection", "MarkingMenuPreferencesWindow", "PaintSetMembershipToolOptions", "UnpublishNode", "DisplayShadingMarkingMenu", "ConvertSelectionToUVEdgeLoop", "softMod", "ShowDynamicConstraints", "PerspRelationshipEditorLayout", "BendOptions", "sculptMeshCacheChangeCloneSource", "CreatePolygonTorusOptions", "FBXExportInputConnections", "ExportProxyContainer", "FBXImportResamplingRateSource", "melInfo", "exportEdits", "Undo", "SculptMeshInvertFreeze", "DeleteVertex", "polyInstallAction", "StitchEdgesTool", "ShelfPreferencesWindow", "CutPolygonOptions", "FBXImportConvertDeformingNullsToJoint", "createNode", "flushUndo", "ToggleViewAxis", "setAttrMapping", "toolDropped", "soundControl", "createRenderLayer", "testPa", "CreateSpotLightOptions", "clearShear", "joint", "LayoutUVRectangle", "CreateJiggleDeformer", "SelectUVBorder", "CopyKeysOptions", "texCutContext", "ToggleVertMetadata", "spotLight", "subdTransferUVsToCache", "untrim", "Unparent", "HypershadeShapeMenuStateNoShapes", "attachNclothCache", "dR_activeHandleYZ", "SelectSharedColorInstances", "showMetadata", "CreateReference", "RenameCurrentUVSet", "AddBifrostAdaptiveMesh", "igBrushContext", "CreatePolygonPrismOptions", "HypershadeDeleteAllBakeSets", "AddBifrostCollider", "unapplyOverride", "SmoothProxyOptions", "CreateCurveFromPolyOptions", "ShowResultsOptions", "AlembicImport", "InsertJointTool", "sbs_SetWorkflow", "HypershadeToggleCrosshairOnEdgeDragging", "ConvertInstanceToObject", "MatchRotation", "dynPaintCtx", "ParameterTool", "freeze", "PaintEffectsToCurve", "ikHandleCtx", "HypershadeDeleteSelected", "blendShape", "Ungroup", "illustratorCurves", "XgExpressionEditor", "ilrGetFileLayersCmd", "CenterPivot", "polyCheck", "DeleteAllClips", "PolyConvertToRingAndSplit", "NURBSSmoothnessFine", "fluidEmitter", "defineVirtualDevice", "geometryAppendCache", "NodeEditorToggleUseAssetsAndPublishedAttributes", "CollapseSubdivSurfaceHierarchyOptions", "CreateParticleDiskCache", "rampWidgetAttrless", "DisableParticles", "OutlinerToggleIgnoreUseColor", "OpenVisorForMeshes", "UpdateEraseSurface", "transformLimits", "graphTrackCtx", "ArtPaintSkinWeightsToolOptions", "TimeEditorImportAnimation", "TimeDraggerToolDeactivate", "nClothRemove", "FloatSelectedObjects", "NodeEditorExplodeCompound", "volumeBind", "HideLightManipulators", "dR_setExtendBorder", "Create2DContainerEmitterOptions", "NURBSSmoothnessMedium", "Smoke", "CreateGhost", "displayStats", "NURBSSmoothnessRough", "emitter", "HypershadeToggleUseAssetsAndPublishedAttributes", "UVSetEditor", "unassignInputDevice", "BrushPresetBlendShading", "XgmSetDensityBrushTool", "mouldSubdiv", "removeListItem", "loadFluid", "CreateEmptyGroup", "ExtendCurveOnSurfaceOptions", "AddBoatLocator", "AddFaceDivisions", "RemoveBifrostField", "freezeOptions", "DetachComponent", "xgmDraRender", "DisableSnapshots", "TimeEditorFrameCenterView", "trimCtx", "SelectAllStrokes", "polyDuplicateAndConnect", "timeWarp", "FitBSplineOptions", "ReassignBoneLatticeJoint", "polyMergeFacetCtx", "EnableIKSolvers", "hotkey", "psdEditTextureFile", "symmetrizeUV", "AddCombinationTargetOptions", "artAttrSkinPaintCtx", "xgmCopyDescription", "Boundary", "pfxstrokes", "XgmSplinePresetImport", "dR_bevelTool", "dR_customPivotToolRelease", "quit", "HypershadeConvertToFileTexture", "polySplitVertex", "CurveFlow", "FBXImportSetLockedAttribute", "ScriptPaintTool", "HypershadeEditTexture", "DetachCurve", "commandLine", "dR_selConstraintEdgeLoop", "PaintEffectsToCurveOptions", "FBXExportCameras", "ToggleSceneTimecode", "ClearInitialState", "MergeVerticesOptions", "ToggleFullScreenMode", "AddKeysTool", "addIK2BsolverCallbacks", "AddPondBoatLocator", "dR_extrudeBevelPress", "texTweakUVContext", "cMuscleBindSticky", "ShowCameras", "createNurbsSquareCtx", "dR_selectModeTweakMarquee", "UVIsolateLoadSet", "polyStraightenUVBorder", "TexSculptActivateBrushSize", "ToggleTangentDisplay", "UVCylindricProjectionOptions", "SelectSharedUVInstances", "artAttrSkinPaintCmd", "psdConvSolidTxOptions", "NodeEditorSetTraversalDepthUnlim", "ScriptEditor", "NodeEditorWindow", "GameExporterWnd", "controller", "SubdivSmoothnessMedium", "movIn", "dR_viewTop", "NCreateEmitterOptions", "ToggleProxyDisplay", "SelectUnmappedFaces", "SymmetrizeUVContext", "dR_activeHandleXZ", "dR_outlinerTGL", "PolyCreaseTool", "DeleteAllRigidBodies", "SelectObjectsShadowedByLight", "dR_targetWeldTool", "license", "SoftModDeformerOptions", "DisableConstraints", "polyOutput", "checkDefaultRenderGlobals", "CreateSubdivSphere", "UVUnstackShellsOptions", "GreasePencilTool", "TimeDraggerToolActivate", "MediumPolygonNormals", "FBXExportSkins", "HIKSetBodyPartKey", "TimeEditorToggleSnapToClipRelease", "arclen", "CreateDagContainer", "AddKeyToolActivate", "rename", "polyUniteSkinned", "saveToolSettings", "swatchDisplayPort", "SelectPointsMask", "SnapKeys", "polyOptUvs", "TimeEditorCreateGroupFromSelection", "surface", "Uniform", "CreateFlexorWindow", "FBXImportCacheFile", "HideSubdivSurfaces", "UnparentOptions", "SmoothHairCurves", "UntrimSurfacesOptions", "BevelOptions", "UVEditorInvertPin", "polyUVRectangle", "keyframeRegionTrackCtx", "GpuCacheExportAllOptions", "selectContext", "CreatePolygonGear", "OpenSceneOptions", "dR_curveSnapRelease", "FBXImportMode", "bulletConvexDecomposition", "FBXGetTakeReferenceTimeSpan", "nexOpt", "dR_softSelDistanceTypeSurface", "VolumeAxis", "dR_extrudeRelease", "BreakTangents", "TogglePolyDisplayLimitToSelected", "HypershadeToggleShowNamespace", "mirrorShape", "AnimationTurntableOptions", "BaseLevelComponentDisplay", "RemoveShrinkWrapSurfaces", "dR_viewRight", "hikCharacterToolWidget", "HideIntermediateObjects", "characterizationToolUICmd", "FBXExportDeleteOriginalTakeOnSplitAnimation", "dR_multiCutPress", "TimeEditorClipTrimToggle", "xgmGrabBrushToolCmd", "RenderViewPrevImage", "dR_viewFront", "DeletePolyElements", "workspace", "InTangentSpline", "GraphEditorDisplayValues", "u3dUnfold", "PlayblastOptions", "ToggleCVs", "dynPaintEditor", "DuplicateCurveOptions", "SelectAllFurs", "directKeyCtx", "setNClothStartState", "TrimToolOptions", "SetMeshKnifeTool", "ToggleColorFeedback", "CreateTextOptions", "ToggleSubdDetails", "TimeEditorSoloSelectedTracks", "fluidReplaceCache", "debugNamespace", "CreateActiveRigidBody", "ToggleHulls", "AttachToPathOptions", "GetHIKNodeName", "JointTool", "polyMoveFacetUV", "polySoftEdge", "normalConstraint", "DeleteAllStrokes", "DeleteAllHistory", "baseTemplate", "HideCameras", "SendAsNewSceneMotionBuilder", "DecreaseExposureFine", "createPolyCylinderCtx", "ToggleHikDetails", "CreatePolygonPlaneOptions", "SelectContiguousEdgesOptions", "SelectUVBackFacingComponents", "SaveSceneAsOptions", "hardenPointCurve", "SetMeshFoamyTool", "createPolyConeCtx", "LODGenerateMeshesOptions", "selLoadSettings", "FBXExportUpAxis", "ProfilerTool", "nucleusDisplayOtherNodes", "convertIffToPsd", "BevelPolygonOptions", "isDirty", "meshRemap", "dR_activeHandleXY", "polyMoveEdge", "ToggleCharacterControls", "lattice", "pointCurveConstraint", "AddPointsTool", "spotLightPreviewPort", "moduleInfo", "ShowStrokePathCurves", "NextViewArrangement", "ToggleCommandLine", "WhatsNewStartupDialogOff", "polyFlipEdge", "HypershadeSortByName", "ToggleVertIDs", "DisplacementToPolygon", "UVStraighten", "RemoveBifrostGuide", "filePathEditor", "DisableExpressions", "TanimLayer", "SendAsNewSceneMudbox", "sbs_SetGlobalTextureWidth", "MakePaintable", "DeleteCurrentUVSet", "polyPlane", "xgmDensityBrushContext", "texturePlacementContext", "turbulence", "dR_multiCutSlicePointCmd", "CustomNURBSComponentsOptions", "HypershadeSortByType", "GridUV", "sbs_GetGlobalTextureWidth", "SimplifyStrokePathCurves", "SelectCurveCVsAll", "SelectPolygonSelectionBoundary", "FrontPerspViewLayout", "NodeEditorShowConnectedAttrs", "EnableNRigids", "PublishChildAnchor", "renderLayerPostProcess", "polyPrimitive", "TransformPolygonComponent", "textCurves", "textureLassoContext", "vortex", "ikSystem", "HypershadeGraphRemoveDownstream", "ikSolver", "CreateDirectionalLight", "fluidCacheInfo", "soft", "AddPfxToHairSystem", "SnapToCurveRelease", "polyPoke", "SetMaxInfluences", "AssignTemplate", "CreateSubdivCube", "tumble", "workspaceControlState", "bezierAnchorPreset", "NodeEditorToggleLockUnlock", "dR_softSelStickyRelease", "ShrinkPolygonSelectionRegion", "deviceEditor", "SewUVsWithoutHotkey", "CreatePassiveRigidBodyOptions", "HypershadeTestTexture", "dR_customPivotTool", "AppendToPolygonTool", "DisableRigidBodies", "CreateNURBSCone", "sceneEditor", "RenderTextureRange", "insertListItemBefore", "NodeEditorGraphRearrange", "MoveIKtoFK", "GamePipeline", "CreatePolygonCylinder", "SetMeshPinchTool", "ToggleMeshUVBorders", "timeEditor", "ParticleInstancerOptions", "PerformanceSettingsWindow", "smoothTangentSurface", "SetFullBodyIKKeysSelected", "PolygonCollapseFaces", "XgmSplineCacheCreateOptions", "XgmSplineCacheExport", "SetEditor", "AimConstraintOptions", "CoarseLevelComponentDisplay", "PolyBrushMarkingMenu", "baseView", "ProjectTangentOptions", "CompleteCurrentTool", "NodeEditorSetSmallNodeSwatchSize", "PolygonPaste", "nurbsToSubdivPref", "audioTrack", "journal", "UnitizeUVsOptions", "polySmooth", "CircularFillet", "FrameSelectedWithoutChildren", "getModifiers", "texRotateContext", "ShowMeshKnifeToolOptions", "ConvertToBreakdown", "WhatsNewStartupDialogOn", "XgmSetFreezeBrushToolOption", "AlignSurfacesOptions", "dR_decreaseManipSize", "UVEditorToggleTextureBorderDisplay", "ChamferVertex", "about", "BrushPresetReplaceShadingOff", "pluginInfo", "GraphEditorFrameCenterView", "SetMeshCloneTargetTool", "ToggleCustomNURBSComponents", "createNurbsSphereCtx", "RenderDiagnostics", "dR_defLightTGL", "SelectAllAssets", "HypershadeSetLargeNodeSwatchSize", "RoundToolOptions", "ResolveInterpenetrationOptions", "LoadHIKCharacterDefinition", "WedgePolygon", "AttachCurveOptions", "FBXGetTakeLocalTimeSpan", "colorIndex", "NURBSSmoothnessMediumOptions", "ExtendSurfacesOptions", "CreatePolygonPlatonicOptions", "HideSculptObjects", "TangetConstraintOptions", "sbs_SetGlobalTextureHeight", "ToggleUVTextureImage", "SetMeshImprintTool", "createNurbsConeCtx", "TransferAttributes", "iconTextScrollList", "renderer", "RemoveFromContainer", "DisableAll", "adskAssetLibrary", "MakeMotionField", "cMuscleRelaxSetup", "revolve", "NodeEditorPickWalkDown", "xgmGeoRender", "LatticeUVTool", "HypershadeDuplicateWithConnections", "SelectEdgeRingSp", "PolyMergeVerticesOptions", "EPCurveTool", "prependListItem", "ProjectCurveOnMeshOptions", "NodeEditorTransforms", "AddOceanSurfaceLocator", "xgmSyncPatchVisibility", "PolyRemoveCrease", "CreaseProxyEdgeTool", "ScaleCurvature", "hotkeyMapSet", "nClothDeleteCacheFramesOpt", "DetachEdgeComponent", "CoarsenSelectedComponents", "TogglePanZoomRelease", "GetSettingsFromSelectedStroke", "setNodeTypeFlag", "CreateAmbientLightOptions", "TranslateToolWithSnapMarkingMenu", "SelectBorderEdgeTool", "HideSmoothSkinInfluences", "HypershadeSetSmallNodeSwatchSize", "cMuscleWeightPrune", "FBXImportMergeAnimationLayers", "fluidMergeCacheOpt", "cMuscleCache", "TesselateSubdivSurface", "arrayMapper", "printStudio", "imagePlane", "DeleteAllWires", "multiProfileBirailSurface", "MakeUVInstanceCurrent", "ToggleOriginAxis", "polyShortestPathCtx", "getInputDeviceRange", "alignCurve", "editRenderLayerGlobals", "SnapToMeshCenterPress", "xgmClumpMap", "AddPondDynamicBuoyOptions", "GraphEditorFrameSelected", "RemoveJoint", "DisplayShadingMarkingMenuPopDown", "ParentBaseWireOptions", "PointOnPolyConstraint", "HypershadeRefreshSelectedSwatches", "PickColorActivate", "Twist", "artAttr", "CreatePartitionOptions", "customerInvolvementProgram", "HypershadeFrameSelected", "OffsetCurveOnSurface", "attrNavigationControlGrp", "SetPassiveKey", "NodeEditorToggleSyncedSelection", "ShowFollicles", "DeleteAllLights", "SetFullBodyIKKeysOptions", "FilletBlendTool", "PolyAssignSubdivHole", "NodeEditorCreateTab", "CreatePlatonicSolid", "CreateUVsBasedOnCameraOptions", "HypershadeCollapseAsset", "XgmSplineGeometryConvert", "ModifyConstraintAxis", "Snap3PointsTo3PointsOptions", "rigidSolver", "polyUVStackSimilarShells", "HypershadeDisplayAsIcons", "manipOptions", "dR_convertSelectionToFace", "polyPrism", "dimWhen", "RaiseApplicationWindows", "DisplayViewport", "floatSlider2", "PaintEffectsToNurbsOptions", "SetMeshSprayTool", "paneLayout", "LayoutUVAlongOptions", "polyForceUV", "RenderIntoNewWindow", "CreatePolygonPlatonic", "UVStackSimilarShells", "containerBind", "blendShapeEditor", "polyTransfer", "percent", "MoveTool", "xgmPartBrushContext", "CreateConstraintClip", "LowQualityDisplay", "contextInfo", "CutCurveOptions", "FBXExport", "HypershadeSaveSwatchesToDisk", "FBXExportBakeComplexStart", "saveFluid", "DeleteAllFurs", "ToggleEvaluationManagerVisibility", "bifMeshImport", "DeleteAllMotionPaths", "RenderGlobalsWindow", "ExtractSubdivSurfaceVerticesOptions", "optionVar", "ambientLight", "OutlinerDoHide", "bakeDeformer", "texSelectContext", "subdDuplicateAndConnect", "offsetCurve", "listHistory", "polyCompare", "OrientConstraint", "AddToCurrentSceneMudbox", "GraphEditorFramePlaybackRange", "NodeEditorConnectionStyleSShape", "XgmSetWidthBrushTool", "SewUVs3D", "workspaceLayoutManager", "PolygonApplyColor", "treeLister", "AutobindContainer", "keyframeRegionSelectKeyCtx", "nurbsToSubdiv", "CurveSmoothnessCoarse", "UIModeMarkingMenuPopDown", "dR_pointSnapPress", "dR_createCameraFromView", "UnifyTangents", "symbolCheckBox", "KeyframeTangentMarkingMenuPopDown", "AddInbetween", "PixelMoveDown", "sbs_GetEnumName", "SoftModDeformer"]