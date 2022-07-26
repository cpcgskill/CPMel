# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/3/17 23:11
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

import os.path
import unittest
import functools
import sys
import subprocess

import cpmel.cmds as cc
from maya.cmds import file, about


def file_new(fn):
    @functools.wraps(fn)
    def _(*args, **kwargs):
        cc.mel.eval("file -f -new")
        return fn(*args, **kwargs)

    return _


def init_scene():
    cc.mel.eval("""
    sphere -p 0 0 0 -ax 0 1 0 -ssw 0 -esw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -nsp 4 -ch 1;

    polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1 -n test_poly;
    doGroup 0 1 1;
    doGroup 0 1 1;
    doGroup 0 1 1;
    doGroup 0 1 1;
    doGroup 0 1 1;
    setKeyframe {"group5"};
    select -d;
    joint -p -4.543955 0 1.230543 ;
    joint -p -3.664643 0 1.463731 ;
    joint -e -zso -oj xyz -sao yup joint1;
    joint -p -2.198807 0 1.640811 ;
    joint -e -zso -oj xyz -sao yup joint2;
    joint -p -0.875126 0 1.653785 ;
    joint -e -zso -oj xyz -sao yup joint3;
    joint -p -0.319182 0 1.648354 ;
    joint -e -zso -oj xyz -sao yup joint4;
    joint -p 0.428169 0 1.740151 ;
    joint -e -zso -oj xyz -sao yup joint5;
    joint -p 1.099981 0 1.981978 ;
    joint -e -zso -oj xyz -sao yup joint6;
    joint -p 1.531153 0 2.026986 ;
    joint -e -zso -oj xyz -sao yup joint7;
    joint -p 1.881464 0 1.853958 ;
    joint -e -zso -oj xyz -sao yup joint8;
    joint -p 1.901977 0 1.796982 ;
    joint -e -zso -oj xyz -sao yup joint9;

    curve -d 3 -p -1 0 1 -p 0 0 1 -p 1 0 1 -p 1 0 0 -p 1 0 -1 -p 0 0 -1 -p -1 0 -1 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 4 -k 4 ;

    """)


def open_maya_gui():
    test_file_path = "C:\\Users\\PC\\Documents\\maya\\projects\\default\\scenes\\test.ma"
    file(rename=test_file_path)
    file(save=True, type='mayaAscii')
    maya_executable = os.sep.join([os.path.dirname(sys.executable), 'maya.exe'])
    subprocess.call([maya_executable, test_file_path])


class Test(unittest.TestCase):

    @file_new
    def test_node_type(self):
        init_scene()

        # test Node
        print("\n## test Node type: ")

        o = cc.new_object('group5')

        print('obj {} >> '.format(o), o, type(o))
        print('obj.t >> ', o.t)
        print('api1_node_object >> ', o.api1_node_object())
        print('api2_node_object >> ', o.api2_node_object())
        print('api1_m_fn_dependency_node >> ', o.api1_m_fn_dependency_node())
        print('api2_m_fn_dependency_node >> ', o.api2_m_fn_dependency_node())

        print('api1_m_fn >> ', o.api1_m_fn())
        print('api2_m_fn >> ', o.api2_m_fn())

        print('attr >> ', o.attr("tx"))
        print('attr set item >> o[t] = (5, 5, 5)')
        o['t'] = (5, 5, 5)
        print('attr get item >> ', o['t'])

    @file_new
    def test_dag_node_type(self):
        init_scene()

        # test DagNode
        print("\n## test DagNode type: ")

        o = cc.new_object('group5')

        print('api1_m_dag_path >> ', o.api1_m_dag_path())
        print('api2_m_dag_path >> ', o.api2_m_dag_path())

        print('full_path_name >> ', o.full_path_name())

        cc.new_object('group4').get_scale(),
        cc.new_object('group4').set_matrix(o.get_matrix())
        print('get_matrix set_matrix end >> ',
              "get_translation: ", cc.new_object('group4').get_translation(),
              "get_rotation: ", cc.new_object('group4').get_rotation(),
              "get_scale: ", cc.new_object('group4').get_scale(),
              "get_matrix: ", cc.new_object('group4').get_matrix(),
              )

        a, b, c = (cc.createNode('transform'),
                   cc.createNode('transform'),
                   cc.createNode('transform'))
        print('test hierarchy: ', b.set_parent(a).add_child(c).childs)

    @file_new
    def test_attr_type(self):
        init_scene()

        print("\n## test attr type: ")
        o = cc.new_object('group5.t')
        print("obj >> ", o, type(o))
        print('name >> ', o.name())
        print('node >> ', o.node())

        print('.worldMatrix[0] >> ', cc.new_object('group5.worldMatrix')[0])

        print('attr set value >> ', o.set_value((1, 1, 1)))
        print('attr get value >> ', o.get_value())

        print('api1_m_plug >> ', o.api1_m_plug())
        print('api2_m_plug >> ', o.api2_m_plug(), type(o.api2_m_plug()))

    @file_new
    def test_component_type(self):
        init_scene()

        print("\n## test component type: ")
        o = cc.new_object('test_poly.vtx[*]')
        print("obj >> ", o, type(o))
        print('name >> ', o.name())
        print('node >> ', o.node())
        print('api1_m_component >> ', o.api1_m_component())
        print('api2_m_component >> ', o.api2_m_component())
        print('to list >> ', list(o))
        print('to get_point >> ', [i.get_point() for i in o])

    @file_new
    def test_transform_node_type(self):
        init_scene()

        print("\n## test transform node type: ")
        o = cc.new_object('test_poly')
        print("obj >> ", o, type(o))
        print('obj vtx >> ', o.vtx)
        print('obj e >> ', o.e)
        print('obj f >> ', o.f)
        print('obj vtxFace >> ', o.vtxFace)
        print('obj vtxFace list >> ', list(o.vtxFace))

        print('to get_points >> ', o.shape.get_points())

    @file_new
    def test_joint_node_type(self):
        init_scene()

        print("\n## test joint node type: ")
        o = cc.new_object('joint1')
        print("obj >> ", o, type(o))

    @file_new
    def test_curve_node_type(self):
        init_scene()

        print("\n## test curve node type: ")
        o = cc.new_object('curve1')
        print("obj >> ", o, type(o))
        print("obj cv >> ", o.cv)
        print("obj ep >> ", o.ep)
        print("obj u >> ", o.u)
        print("obj get set points >> ", o.shape.set_points(o.shape.get_points()))

    @file_new
    def test_surface_node_type(self):
        init_scene()

        print("\n## test surface node type: ")
        o = cc.new_object('nurbsSphere1')
        print("obj >> ", o, type(o))
        print("obj cv >> ", o.cv)
        print("obj u >> ", o.u)
        print("obj v >> ", o.v)
        print("obj uv >> ", o.uv)
        print("obj sf >> ", o.sf)
        print("obj sf >> ", list(o.sf))
        print("obj get set points >> ", o.shape.set_points(o.shape.get_points()))

    @file_new
    def test_skin_cluster_filter_node_type(self):
        cc.mel.eval("""
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;

select -d;
joint -p 0 0 2 ;
joint -p 2 0 0 ;
joint -e -zso -oj xyz -sao yup joint1;
joint -p 0 0 -2 ;
joint -e -zso -oj xyz -sao yup joint2;
joint -p -2 0 0 ;
joint -e -zso -oj xyz -sao yup joint3;

select -r joint4 joint3 joint2 joint1 ;

parent -w;

select -r joint4 joint3 joint2 joint1 ;
select -tgl pSphere1 ;

SmoothBindSkin;
        """)

        print("\n## test skin_cluster filter node type: ")
        o = cc.new_object('skinCluster1')
        geo = cc.new_object('pSphere1.vtx[*]')
        print("get blend weights >> ", o.get_blend_weights(geo))
        print("set blend weights >> ", o.unsafe_set_blend_weights(geo, (0.5 for i in o.get_blend_weights(geo))))
        print("set blend weights end >> ", o.get_blend_weights(geo))

        print("get weights >> ", o.get_weights(geo, [0]))
        print("set weights >> ", o.unsafe_set_weights(geo, [0], (i * 0.5 for i in o.get_weights(geo, [0]))))
        print("set weights end >> ", o.get_weights(geo, [0]))

        # print("obj >> ", o, type(o))
        # print("obj cv >> ", o.cv)
        # print("obj u >> ", o.u)
        # print("obj v >> ", o.v)
        # print("obj uv >> ", o.uv)
        # print("obj sf >> ", o.sf)
        # print("obj sf >> ", list(o.sf))
        # print("obj get set points >> ", o.shape.set_points(o.shape.get_points()))

    @file_new
    def test_hash_func(self):
        init_scene()
        print("\n## test hash func: ")

        o = cc.new_object('group5')
        print("group5 __hash__ >> ", hash(o), {o: o})

        o = cc.new_object('group5.t')
        print("group5.t __hash__ >> ", hash(o), {o: o})
        o = cc.new_object('group5.r')
        print("group5.r __hash__ >> ", hash(o), {o: o})
        o = cc.new_object('group5.s')
        print("group5.s __hash__ >> ", hash(o), {o: o})

        o = cc.new_object('test_poly.vtx[*]')
        print("test_poly.vtx[*] __hash__ >> ", hash(o), {o: o})
        print("test_poly.vtx all __hash__ >> ", {hash(i): i for i in o}, len({hash(i): i for i in o}))

    @file_new
    def test_eq(self):
        cc.mel.eval('''
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
select -r pSphere1 ;
doGroup 0 1 1;
doGroup 0 1 1;
''')
        obj = cc.new_object('pSphere1')
        obj_two = cc.new_object('pSphere1')
        grp_1 = cc.new_object('group1')
        grp_2 = cc.new_object('group2')
        self.assertTrue(obj in [obj, grp_1, grp_2], msg="check list in")

        self.assertTrue(obj != grp_1, msg="check not __eq__")
        self.assertTrue(obj == obj, msg="check __eq__")
        self.assertTrue((obj != obj_two) == False, msg="check __eq__")

        self.assertTrue(obj.vtx == obj.vtx, msg="check __eq__")
        vtxs = list(obj.vtx)
        self.assertTrue(vtxs[0] == vtxs[0], msg="check __eq__")
        self.assertTrue(vtxs[0] != vtxs[1], msg="check __eq__")
        self.assertTrue(obj.vtx != vtxs[1], msg="check __eq__")
        self.assertTrue(obj.vtx != grp_2, msg="check __eq__")
        self.assertTrue(vtxs[0] != grp_2, msg="check __eq__")
        self.assertTrue(obj.vtx != grp_2.t, msg="check __eq__")
        self.assertTrue(vtxs[0] != grp_2.t, msg="check __eq__")

    @file_new
    def test_shift(self):
        cc.mel.eval('''
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
select -r pSphere1 ;
doGroup 0 1 1;
doGroup 0 1 1;
''')
        obj = cc.new_object('pSphere1')
        grp_1 = cc.new_object('group1')
        grp_2 = cc.new_object('group2')
        self.assertTrue(grp_1.t >> obj.t << grp_2.t == grp_2.t, msg="check __lshift__ and __rshift__")
        self.assertTrue(grp_1.t >> obj.t << grp_2.t == grp_2.t, msg="check __lshift__ and __rshift__")

        # self.assertTrue(grp_1.t << grp_2.t == grp_2.t, msg="check __lshift__")
        # self.assertTrue(grp_1.t >> grp_2.t == grp_2.t, msg="check __rshift__")
        # self.assertTrue(grp_1.t << grp_2.t == grp_2.t, msg="check __lshift__")
        open_maya_gui()
