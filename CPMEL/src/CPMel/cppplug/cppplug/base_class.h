#ifndef BASECLASS
#define BASECLASS

#include"pythontool.h"

struct BaseData {
    PyObject_HEAD
        /* Type-specific fields go here. */
} ;
static PyObject* BaseData_New(PyTypeObject* type, PyObject* args, PyObject* kw);

static PyObject* BaseData_compile(BaseData* self);

static PyMethodDef BaseData_SpamMethods[] = {
    {"compile",
    (PyCFunction)BaseData_compile,
    METH_NOARGS,
    "返回编译完成的值"
    },
    {0, 0, 0, 0}
};

static PyTypeObject BaseData_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "cppplug.BaseData",             /* tp_name */
    sizeof(BaseData), /* tp_basicsize */
    0,                         /* tp_itemsize */
    0,                         /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /* tp_flags */
    "最基本的CPMel数据对象",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    BaseData_SpamMethods,                   /* tp_methods */
    0,                         /* tp_members */
    0,                 /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    0,                         /* tp_init */
    0,                         /* tp_alloc */
    BaseData_New,               /* tp_new */
};
static PyObject* BaseData_compile(BaseData* self) { 
    Py_RETURN_NONE;
}


static PyObject* BaseData_New(PyTypeObject* type, PyObject* args, PyObject* kw)
{
    BaseData* self = CPNewPyObject(type, BaseData);
    return (PyObject*)self;
}
#endif
