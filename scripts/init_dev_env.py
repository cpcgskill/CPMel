# -*-coding:utf-8 -*-
"""
:创建时间: 2024/9/6 15:00
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""

from __future__ import unicode_literals, print_function, division

if False:
    from typing import *

import sys
import os
import subprocess
import shutil

python_interpreter = sys.executable

PATH = os.path.dirname(os.path.abspath(os.path.normpath(__file__)))

os.chdir(PATH)
os.chdir("..")

if os.path.exists("dev-lib"):
    print("remove dev-lib")
    shutil.rmtree("dev-lib")

os.makedirs("dev-lib")

# "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install -e . --target=dev-lib
command = [python_interpreter, "-m", "pip", "install", "-e", ".", "--target=dev-lib"]
print(*command)
subprocess.call(command)
