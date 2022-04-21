# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/18 2:31
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import maya.cmds as mc

window = {'Windows': ['colorEditor', 'confirmDialog', 'createEditor', 'defaultNavigation', 'editor', 'editorTemplate',
                      'fontDialog', 'layoutDialog', 'minimizeApp', 'progressWindow', 'promptDialog',
                      'refreshEditorTemplates', 'scriptEditorInfo', 'showSelectionInTitle', 'showWindow',
                      'toggleWindowVisibility', 'window', 'windowPref', 'workspaceControlState', 'workspacePanel'],
          'Misc_UI': ['annotate', 'autoPlace', 'buttonManip', 'callbacks', 'disableIncorrectNameWarning', 'grabColor',
                      'headsUpDisplay', 'headsUpMessage', 'hotkey', 'hotkeyCheck', 'hotkeyCtx', 'hotkeySet',
                      'inViewMessage', 'linearPrecision', 'loadPrefObjects', 'loadUI', 'mayaDpiSetting', 'multiTouch',
                      'nameCommand', 'overrideModifier', 'saveAllShelves', 'savePrefObjects', 'savePrefs', 'saveShelf',
                      'scmh', 'setMenuMode', 'setNodeTypeFlag', 'setStartupMessage', 'textManip',
                      'thumbnailCaptureComponent'],
          'Menus': ['artBuildPaintMenu', 'attrEnumOptionMenu', 'attrEnumOptionMenuGrp', 'attributeMenu', 'hotBox',
                    'menu', 'menuEditor', 'menuItem', 'menuSet', 'menuSetPref', 'optionMenu', 'optionMenuGrp',
                    'popupMenu', 'radioMenuItemCollection', 'saveMenu'],
          'Layouts': ['columnLayout', 'dockControl', 'flowLayout', 'formLayout', 'frameLayout', 'gridLayout', 'layout',
                      'menuBarLayout', 'paneLayout', 'rowColumnLayout', 'rowLayout', 'scrollLayout', 'shelfLayout',
                      'shelfTabLayout', 'tabLayout', 'toolBar', 'workspaceControl', 'workspaceLayoutManager'],
          'Controls': ['attrColorSliderGrp', 'attrControlGrp', 'attrFieldGrp', 'attrFieldSliderGrp',
                       'attrNavigationControlGrp', 'button', 'canvas', 'channelBox', 'checkBox', 'checkBoxGrp',
                       'cmdScrollFieldExecuter', 'cmdScrollFieldReporter', 'cmdShell', 'colorIndexSliderGrp',
                       'colorInputWidgetGrp', 'colorSliderButtonGrp', 'colorSliderGrp', 'commandLine', 'componentBox',
                       'control', 'falloffCurve', 'falloffCurveAttr', 'floatField', 'floatFieldGrp', 'floatScrollBar',
                       'floatSlider', 'floatSlider2', 'floatSliderButtonGrp', 'floatSliderGrp', 'gradientControl',
                       'gradientControlNoAttr', 'helpLine', 'hudButton', 'hudSlider', 'hudSliderButton',
                       'iconTextButton', 'iconTextCheckBox', 'iconTextRadioButton', 'iconTextRadioCollection',
                       'iconTextScrollList', 'iconTextStaticLabel', 'image', 'intField', 'intFieldGrp', 'intScrollBar',
                       'intSlider', 'intSliderGrp', 'layerButton', 'messageLine', 'nameField', 'nodeTreeLister',
                       'palettePort', 'picture', 'progressBar', 'radioButton', 'radioButtonGrp', 'radioCollection',
                       'rangeControl', 'scriptTable', 'scrollField', 'separator', 'shelfButton', 'soundControl',
                       'swatchDisplayPort', 'switchTable', 'symbolButton', 'symbolCheckBox', 'text', 'textField',
                       'textFieldButtonGrp', 'textFieldGrp', 'textScrollList', 'timeControl', 'timeField',
                       'timeFieldGrp', 'timePort', 'toolButton', 'toolCollection', 'treeLister', 'treeView'],
          'Panels': ['canCreateCaddyManip', 'componentEditor', 'contentBrowser', 'getPanel', 'hardwareRenderPanel',
                     'hotkeyEditorPanel', 'hyperGraph', 'hyperPanel', 'hyperShade', 'inViewEditor', 'modelEditor',
                     'modelPanel', 'nodeEditor', 'nodeOutliner', 'outlinerEditor', 'outlinerPanel', 'panel',
                     'panelConfiguration', 'panelHistory', 'saveViewportSettings', 'scriptedPanel', 'scriptedPanelType',
                     'setFocus', 'spreadSheetEditor', 'viewManip', 'visor', 'webBrowser', 'webBrowserPrefs']}
list_commands = ['listInputDevices', 'listAttr', 'listDeviceAttachments', 'listConnections', 'listCameras', 'listRelatives', 'listInputDeviceButtons', 'listInputDeviceAxes', 'listSets', 'listAnimatable', 'listAttrPatterns', 'listNodeTypes', 'listNodesWithIncorrectNames', 'listHistory']

def selected(*args, **kwargs):
    return mc.ls(*args, sl=True, **kwargs)


commands = (getattr(mc, i) for i in dir(mc))
commands = [(i.__name__, i) for i in commands if callable(i)]

list_commands = (getattr(mc, i) for i in list_commands)
list_commands = [(i.__name__, i) for i in list_commands if callable(i)]

ui_commands = {i for v in window.values() for i in v} & set((i for i in commands if callable(i)))
ui_commands = [(i, commands[i]) for i in ui_commands]
other_commands = [
    ('selected', selected)
]
