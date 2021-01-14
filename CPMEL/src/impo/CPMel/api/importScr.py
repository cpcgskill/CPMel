#OpenMaya
import maya.OpenMaya as om
import re
class_list = [i for i in dir(om) if not re.match("M.*", i) is None and re.match(".*_", i) is None]
print "from maya.OpenMaya import " + ",".join(class_list)

#OpenMayaAnim
import maya.OpenMayaAnim as omaim
import re
class_list = [i for i in dir(omaim) if not re.match("M.*", i) is None and re.match(".*_", i) is None]
print "from maya.OpenMayaAnim import " + ",".join(class_list)

#OpenMayaFX
import maya.OpenMayaFX as omfx
import re
class_list = [i for i in dir(omfx) if not re.match("M.*", i) is None and re.match(".*_", i) is None]
print "from maya.OpenMayaFX import " + ",".join(class_list)

#OpenMayaRender
import maya.OpenMayaRender as omrd
import re
class_list = [i for i in dir(omrd) if not re.match("M.*", i) is None and re.match(".*_", i) is None]
print "from maya.OpenMayaRender import " + ",".join(class_list)

#OpenMayaUI
import maya.OpenMayaUI as omui
import re
class_list = [i for i in dir(omui) if not re.match("M.*", i) is None and re.match(".*_", i) is None]
print "from maya.OpenMayaUI import " + ",".join(class_list)

#OpenMayaMPx
import maya.OpenMayaMPx as ompx
import re
class_list = [i for i in dir(ompx) if not re.match("M.*", i) is None and re.match(".*_", i) is None]
print "from maya.OpenMayaMPx import " + ",".join(class_list)