# CPMel

一个现代的maya python库  

#### ta有以下设计目标

1. 相对较快地初始化速度
2. 易于与maya-api1、maya-api2交互
3. 易于扩展
4. 够用的性能

## 目录

- [快速开始](#快速开始)
    * [安装](#安装)
    * [测试](#测试)
- [使用教程](#使用教程)
    * [命令调用](#命令调用) 
      * [获得选择列表](#获得选择列表)
      * [创建关节](#创建关节)
      * [创建UI](#创建UI)
    * [与api交互](#与api交互)
      * [获得节点的函数集对象](#获得节点的函数集对象)
      * [获得属性的MPlug对象](#获得属性的MPlug对象) 
      * [一些其他的](#一些其他的)
    * [常用的对象方法](#常用的对象方法)
      * [名称相关操作](#名称相关操作)
      * [dag相关操作](#dag相关操作)
    * [附加特性](#附加特性)
      * [属性相关操作](#属性相关操作)
- [版权说明](#版权说明)

## 快速开始

### 安装

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

### 测试

执行以下程序应当可以获得选择列表，如果正确那么恭喜你安装完成！

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

sel = cc.ls(sl=True)
```

## 使用教程

### 命令调用

#### 获得选择列表

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

sel = cc.ls(sl=True)
```

#### 创建关节

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

cc.select(cl=True)
jin = cc.joint()
```

#### 创建UI

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

window_name = 'your_window_name'
if cc.window(window_name, ex=True):
    cc.deleteUI(window_name)
cc.window(window_name)
with cc.flowLayout():
    cc.button()
    cc.button()
    cc.button()
cc.showWindow()
```

### 与api交互

#### 获得节点的函数集对象

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

node = cc.createNode('transform')
# api1版本的函数集对象
node.api1_m_fn()
# api2版本的函数集对象
node.api2_m_fn()
```

#### 获得属性的MPlug对象

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

node = cc.createNode('transform')
attr = node.tx
# api1版本的
attr.api1_m_plug()
# api2版本的
attr.api2_m_plug()
```

#### 一些其他的

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

node = cc.createNode('transform')

# api1版本
node.api1_m_fn_dependency_node()
node.api1_node_object()
node.api1_m_dag_path()
# api2版本
node.api2_m_fn_dependency_node()
node.api2_node_object()
node.api2_m_dag_path()
```

### 常用的对象方法

#### 名称相关操作

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

node = cc.createNode('transform')
# 获得最短名称
node.name()
# 仅获得节点名称
node.node_name()
# 获得完整路径
node.full_path_name()
```

#### dag相关操作

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

node_a = cc.createNode('transform')
node_b = cc.createNode('transform')
node_c = cc.createNode('transform')

# 设置父对象
node_a.parent = node_b
# or node_a.set_parent(node_b)
# 获得父对象
print('获得父对象', node_a.parent)
# or node_a.get_parent()
# 添加子对象
node_c.add_child(node_b)
# 获得子对象
print('获得子对象', node_c.childs)
# or node_c.get_childs()
```

### 附加特性

#### 属性相关操作

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

node = cc.createNode('transform')
# 获得属性
# 方法1
tx_attr = node.tx
# 方法2 ps: 在节点属性名称与对象属性冲突时可以使用这个
tx_attr = node.attr('tx')

# 读写属性
# 方法1
# 写
node['tx'] = 1.0
# 读
tx_val = node['tx']
# 方法2
# 写
node.tx.set_value(1.0)
# 读
tx_val = node.tx.get_value()

# 连接属性
# 方法1
node.tx >> node.ty
# 方法2
node.tx.connect(node.ty)
# 断开属性连接
node.tx.disconnect(node.ty)
```

## 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE