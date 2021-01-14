#!/usr/bin/python
# -*-coding:utf-8 -*-
class windows:
    import windows as windows_names

    Windows = [i for i in windows_names.Windows.split("\n") if len(i) > 3]
    Panels = [i for i in windows_names.Panels.split("\n") if len(i) > 3]
    Controls = [i for i in windows_names.Controls.split("\n") if len(i) > 3]
    Layouts = [i for i in windows_names.Layouts.split("\n") if len(i) > 3]
    Menus = [i for i in windows_names.Menus.split("\n") if len(i) > 3]
    Misc_UI = [i for i in windows_names.Misc_UI.split("\n") if len(i) > 3]



class system:
    import system as system_names

    Files = [i for i in system_names.Files.split("\n") if len(i) > 3]
    Devices = [i for i in system_names.Devices.split("\n") if len(i) > 3]
    Plug_ins = [i for i in system_names.Plug_ins.split("\n") if len(i) > 3]
    Localization = [i for i in system_names.Localization.split("\n") if len(i) > 3]
    Utilities = [i for i in system_names.Utilities.split("\n") if len(i) > 3]

#
# simpleCommandWraps = {
#     'createRenderLayer': [(toPyNode, Always)],
#     'createDisplayLayer': [(toPyNode, Always)],
#     'distanceDimension': [(toPyNode, Always)],
#     'listAttr': [(util.listForNone, Always)],
#     'instance': [(toPyNodeList, Always)],
#
#     'getPanel': [(toPyType('pymel.core.uitypes', 'Panel'),
#                   Flag('containing', 'c', None) |
#                   Flag('underPointer', 'up') |
#                   Flag('withFocus', 'wf')),
#                  (toPyTypeList('pymel.core.uitypes', 'Panel'),
#                   ~Flag('typeOf', 'to', None))
#                  ],
#
#     'textScrollList': [(util.listForNone,
#                         Flag('query', 'q') &
#                         (Flag('selectIndexedItem', 'sii') |
#                          Flag('allItems', 'ai') |
#                          Flag('selectItem', 'si')))
#                        ],
#
#     'optionMenu': [(util.listForNone,
#                     Flag('query', 'q') &
#                     (Flag('itemListLong', 'ill') |
#                      Flag('itemListShort', 'ils')))
#                    ],
#
#     'optionMenuGrp': [(util.listForNone,
#                        Flag('query', 'q') &
#                        (Flag('itemListLong', 'ill') |
#                         Flag('itemListShort', 'ils')))
#                       ],
#
#     'modelEditor': [(toPyNode,
#                      Flag('query', 'q') & Flag('camera', 'cam'))
#                     ],
#
#     'ikHandle': [(toPyNode,
#                   Flag('query', 'q') & Flag('endEffector', 'ee')),
#                  (toPyNodeList,
#                   Flag('query', 'q') & Flag('jointList', 'jl')),
#                  ],
#     'skinCluster': [(toPyNodeList,
#                      Flag('query', 'q') &
#                      (Flag('geometry', 'g') |
#                       Flag('deformerTools', 'dt') |
#                       Flag('influence', 'inf') |
#                       Flag('weightedInfluence', 'wi'))),
#                     ],
#     'addDynamic': [(toPyNodeList, Always)],
#     'addPP': [(toPyNodeList, Always)],
#     'animLayer': [(toPyNode,
#                    Flag('query', 'q') &
#                    (Flag('root', 'r') |
#                     Flag('bestLayer', 'bl') |
#                     Flag('parent', 'p'))),
#                   (toPyNodeList,
#                    Flag('query', 'q') &
#                    (Flag('children', 'c') |
#                     Flag('attribute', 'at') |
#                     Flag('bestAnimLayer', 'blr') |
#                     Flag('animCurves', 'anc') |
#                     Flag('baseAnimCurves', 'bac') |
#                     Flag('blendNodes', 'bld') |
#                     Flag('affectedLayers', 'afl') |
#                     Flag('parent', 'p')))
#                   ],
#     'annotate': [(lambda res: toPyNode(res.strip()), Always)],
#     'arclen': [(toPyNode, Flag(' constructionHistory', 'ch'))],
#     'art3dPaintCtx': [(splitToPyNodeList,
#                        Flag('query', 'q') &
#                        (Flag('shapenames', 'shn') |
#                         Flag('shadernames', 'hnm')))
#                       ],
#     'artAttrCtx': [(splitToPyNodeList,
#                     Flag('query', 'q') &
#                     Flag('paintNodeArray', 'pna'))
#                    ],
#     'container': [(toPyNodeList,
#                    Flag('query', 'q') &
#                    (Flag('nodeList', 'nl') |
#                     Flag('connectionList', 'cl'))),
#                   (toPyNode,
#                    Flag('query', 'q') &
#                    (Flag('findContainer', 'fc') |
#                     Flag('asset', 'a'))),
#                   (lambda res: [(toPyNode(res[i]), res[i + 1]) for i in range(0, len(res), 2)],
#                    Flag('query', 'q') &
#                    Flag('bindAttr', 'ba') & ~(Flag('publishName', 'pn') | Flag('publishAsParent', 'pap') | Flag('publishAsChild', 'pac'))),
#                   (raiseError(ValueError, 'In query mode bindAttr can *only* be used with the publishName, publishAsParent and publishAsChild flags'),
#                    Flag('query', 'q') &
#                    Flag('unbindAttr', 'ua') & ~(Flag('publishName', 'pn') | Flag('publishAsParent', 'pap') | Flag('publishAsChild', 'pac'))),
#                   ],
# }