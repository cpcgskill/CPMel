# CPMel

一个现代的maya python库

## 目录

- [快速开始](#快速开始)
- [功能介绍](#功能介绍)
- [版权说明](#版权说明)

### 快速开始

#### 安装

注意下方的python是你的Python, 正常情况下可以直接通过python调用, 而Maya的python一般是C:\Program Files\Autodesk\Maya2018\bin\mayapy.exe

```commandline
python -m pip install cpmel
```

在windows下maya的安装例子

注意:

1. 请将Maya路径替换为自己的。
2. 请使用cmd

```commandline
"C:\Program Files\Autodesk\Maya2018\bin\mayapy.exe" -m pip install cpmel
```

#### maya命令调用

获得选择列表

```python
import cpmel.cmds as cc
sel = cc.ls(sl=True)
```

创建关节

```python
import cpmel.cmds as cc
cc.select(cl=True)
jin = cc.joint()
```

### 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE