#!/usr/bin/python
# -*-coding:utf-8 -*-
from collections import Iterable
import types
import re

import maya.mel as mel
import maya.cmds as mc

no_proc = {u"exec", u"print", u"is"}
procs = set([i for i in mc.melInfo() if mel.eval("whatIs %s"%i) != "Command"]) - no_proc


head_string = """
class mel(base.melbase):
"""

# isinstance(l, Iterable)
boody_string = '''    <<name>> = partial(melProc, "<<name>>")'''

end_string = """"""

# re.sub(r"<<name>>", "")

com_re = re.compile(r"<<name>>")

python_scripts = [head_string]

for i in procs:
    python_scripts.append(com_re.sub(r"%s" % i, boody_string))

python_scripts.append(end_string)


print "\n".join(python_scripts)