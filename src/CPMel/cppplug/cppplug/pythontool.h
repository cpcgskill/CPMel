#ifndef PYTHONTOOL
#define PYTHONTOOL
#include <Python.h>
#include <sstream>
#define CPNewPyObject(type, obj_type) (obj_type*)(type)->tp_alloc(type, 0)
#define CPStaticNewPyObject(type, obj_type) (obj_type*)(&type)->tp_alloc(&type, 0)
#define CPAutoNewPyObject(type, obj_type) (obj_type*)(type)->tp_alloc(type, 0)
#define CPDeletePyObject(ob) (((PyObject*)(ob))->ob_type)->tp_free(ob)
#define CPNewPyObjectClass(mode, name, type)     if (PyType_Ready(&type) < 0){return;}Py_INCREF(&type);PyModule_AddObject(mode, name, (PyObject*)&type)
#define CPPyObject_IsInstance(object, type) PyObject_IsInstance(object, (PyObject*)&type)
#define CPPrintfRefcnt(obj) printf("Refcnt:%I64d\n", obj->ob_refcnt)
#define CPPyClassObjectHEAD PyVarObject_HEAD_INIT(NULL, 0)
#endif