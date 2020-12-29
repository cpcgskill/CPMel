#ifndef DOUBLE3
#define DOUBLE3
#include"pythontool.h"
#include"base_class.h"
struct Double3
{
    PyObject_HEAD
    double vlaue[3];
};

#define NewDouble3Object CPStaticNewPyObject(Double3_Type, Double3)
static PyObject* Double3_New(PyTypeObject* type, PyObject* args, PyObject* kw);
static void Double3_Dealloc(Double3* self);


static PyObject* x_get(Double3* self, void* closure);
static int x_set(Double3* self, PyObject* value, void* closure);
static PyObject* y_get(Double3* self, void* closure);
static int y_set(Double3* self, PyObject* value, void* closure);
static PyObject* z_get(Double3* self, void* closure);
static int z_set(Double3* self, PyObject* value, void* closure);

// 魔术方法
static PyObject* Double3_repr(Double3* self);
static PyObject* Double3_iter(Double3* self);
//数值类型
static Double3* Double3_ADD(Double3* o1, Double3* o2);
static Double3* Double3_Sub(Double3* o1, Double3* o2);
static Double3* Double3_Mul(Double3* o1, PyObject* o2);
static Double3* Double3_Divide(Double3* o1, PyObject* o2);
//Double3_Mapping 序列方法
static unsigned int Double3_Len(Double3* self);
static PyObject* Double3_GetItem(Double3* self, PyObject* item);
static int Double3_SetItem(Double3* o, PyObject* key, PyObject* v);
// 普通方法
static PyObject* Double3_Dis(Double3* self, PyObject* args);
static PyObject* Double3_compile(Double3* self);
static PyGetSetDef Double3_getseters[] = {
    {"x",
     (getter)x_get,
     (setter)x_set,
     "x",
     NULL},
    {"y",
     (getter)y_get,
     (setter)y_set,
     "y",
     NULL},
         {"z",
     (getter)z_get,
     (setter)z_set,
     "z",
     NULL},
    {NULL}  /* Sentinel */
};
static int Double3_SetItem(Double3* o, PyObject* key, PyObject* v);

PyMappingMethods Double3_Mapping = {
    (lenfunc)Double3_Len,
    (binaryfunc)Double3_GetItem,
    (objobjargproc)Double3_SetItem
};
static PyNumberMethods Double3_Number = {
    (binaryfunc)Double3_ADD,          /* nb_add */
    (binaryfunc)Double3_Sub,          /* nb_subtract */
    (binaryfunc)Double3_Mul,          /* nb_multiply */
    (binaryfunc)Double3_Divide,       /*nb_divide*/
    0,          /*nb_remainder*/
    0,       /*nb_divmod*/
    0,          /*nb_power*/
    0, /*nb_negative*/
    0, /*nb_positive*/
    0, /*nb_absolute*/
    0, /*nb_nonzero*/
    0,                  /*nb_invert*/
    0,                  /*nb_lshift*/
    0,                  /*nb_rshift*/
    0,                  /*nb_and*/
    0,                  /*nb_xor*/
    0,                  /*nb_or*/
    0,       /*nb_coerce*/
    0,        /*nb_int*/
    0,         /*nb_long*/
    0,        /*nb_float*/
    0,                  /* nb_oct */
    0,                  /* nb_hex */
    0,                  /* nb_inplace_add */
    0,                  /* nb_inplace_subtract */
    0,                  /* nb_inplace_multiply */
    0,                  /* nb_inplace_divide */
    0,                  /* nb_inplace_remainder */
    0,                  /* nb_inplace_power */
    0,                  /* nb_inplace_lshift */
    0,                  /* nb_inplace_rshift */
    0,                  /* nb_inplace_and */
    0,                  /* nb_inplace_xor */
    0,                  /* nb_inplace_or */
    0, /* nb_floor_divide */
    0,          /* nb_true_divide */
    0,                  /* nb_inplace_floor_divide */
    0,                  /* nb_inplace_true_divide */
};

static PyMethodDef Double3_methods[] = {
    {"dis", (PyCFunction)Double3_Dis,
    METH_VARARGS,
     "距离计算"
    },
    {"distanceTo", (PyCFunction)Double3_Dis,
    METH_VARARGS,
     "距离计算"
    },
    {"compile",
    (PyCFunction)Double3_compile,
    METH_NOARGS,
    "返回编译完成的值"
    },
    {NULL}  /* Sentinel */
};
/*
    Double3 * add(Double3 *other);
    Double3 * less(Double3 *other);
    Double3 * multiply(double other);
    Double3 * divide(double other);
*/
static PyTypeObject Double3_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "cppplug.Double3",            /* tp_name */
    sizeof(Double3),           /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Double3_Dealloc,/* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    (reprfunc)Double3_repr,    /* tp_repr */
    &Double3_Number,           /* tp_as_number */
    0,                         /* tp_as_sequence */
    &Double3_Mapping,          /* tp_as_mapping */
    0,                         /* tp_hash */
    0,                         /* tp_call */
    (reprfunc)Double3_repr,             /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_CHECKTYPES | Py_TPFLAGS_BASETYPE,   /* tp_flags *//*    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE 之前使用这种 但是如果有PyNumberMethods就要使用现在的*/
    "Double3 objects",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    (getiterfunc)Double3_iter,                         /* tp_iter */
    0,                         /* tp_iternext */
    Double3_methods,                   /* tp_methods */
    0,                         /* tp_members */
    Double3_getseters,                 /* tp_getset */
    &BaseData_Type,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    0,                         /* tp_init */
    0,                         /* tp_alloc */
    Double3_New,               /* tp_new */
};


#define Double3_New_ErrStr "输入参数应为 cls( (float, float, float..) )"
static PyObject* Double3_New(PyTypeObject* type, PyObject* args, PyObject* kw)
{
    PyObject* in_v = NULL;
    if (!PyArg_ParseTuple(args, "O", &in_v)) { return NULL; }
    Double3* data = NewDouble3Object;
    data->vlaue[0] = PyFloat_AsDouble(PyObject_GetItem(in_v, PyInt_FromLong(0)));
    data->vlaue[1] = PyFloat_AsDouble(PyObject_GetItem(in_v, PyInt_FromLong(1)));
    data->vlaue[2] = PyFloat_AsDouble(PyObject_GetItem(in_v, PyInt_FromLong(2)));
    //Py_INCREF(self);
    // Double3* self = Double3_newObject(data);
    return (PyObject*)data;
}
static void Double3_Dealloc(Double3* self)
{
    //在这里Py_TYPE获得的是PyTypeObject而不是class Curve
    CPDeletePyObject(self);
    return;
}

//数值类型函数实现
static Double3* Double3_ADD(Double3* o1, Double3* o2)
{
    if (PyObject_IsInstance((PyObject*)o1, (PyObject*)&Double3_Type) && PyObject_IsInstance((PyObject*)o2, (PyObject*)&Double3_Type))
    {
        Double3* self = NewDouble3Object;
        self->vlaue[0] = o1->vlaue[0] + o2->vlaue[0];
        self->vlaue[1] = o1->vlaue[1] + o2->vlaue[1];
        self->vlaue[2] = o1->vlaue[2] + o2->vlaue[2];
        return self;
    }
    return NULL;
}
static Double3* Double3_Sub(Double3* o1, Double3* o2)
{
    if (PyObject_IsInstance((PyObject*)o1, (PyObject*)&Double3_Type) && PyObject_IsInstance((PyObject*)o2, (PyObject*)&Double3_Type))
    {
        Double3* self = NewDouble3Object;
        self->vlaue[0] = o1->vlaue[0] - o2->vlaue[0];
        self->vlaue[1] = o1->vlaue[1] - o2->vlaue[1];
        self->vlaue[2] = o1->vlaue[2] - o2->vlaue[2];
        return self;
    }
    return NULL;
}
static Double3* Double3_Mul(Double3* o1, PyObject* o2)
{
    if (PyObject_IsInstance((PyObject*)o1, (PyObject*)&Double3_Type) && (PyFloat_Check(o2) || PyInt_Check(o2)))
    {
        double fo2 = PyFloat_AsDouble(o2);
        Double3* self = NewDouble3Object;
        self->vlaue[0] = o1->vlaue[0] * fo2;
        self->vlaue[1] = o1->vlaue[1] * fo2;
        self->vlaue[2] = o1->vlaue[2] * fo2;
        return self;
    }
    return NULL;
}
static Double3* Double3_Divide(Double3* o1, PyObject* o2)
{
    if (PyObject_IsInstance((PyObject*)o1, (PyObject*)&Double3_Type) && (PyFloat_Check(o2) || PyInt_Check(o2)))
    {
        double fo2 = PyFloat_AsDouble(o2);
        Double3* self = NewDouble3Object;
        self->vlaue[0] = o1->vlaue[0] / fo2;
        self->vlaue[1] = o1->vlaue[1] / fo2;
        self->vlaue[2] = o1->vlaue[2] / fo2;
        return self;
    }
    return NULL;
}
//getset方法
static PyObject* x_get(Double3* self, void* closure)
{
    return PyFloat_FromDouble(self->vlaue[0]);
}
static int x_set(Double3* self, PyObject* value, void* closure)
{
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "无法删除这个属性");
        return -1;
    }
    if (PyFloat_Check(value))
    {
        self->vlaue[0] = PyFloat_AsDouble(value);
        return 0;
    }
    else if (PyInt_Check(value))
    {
        self->vlaue[0] = _PyInt_AsInt(value);
        return 0;
    }
    else if (PyLong_Check(value))
    {
        self->vlaue[0] = PyLong_AsDouble(value);
        return 0;
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "类型应该为Float类型");
        return -1;
    }
}
static PyObject* y_get(Double3* self, void* closure)
{
    return PyFloat_FromDouble(self->vlaue[1]);
}
static int y_set(Double3* self, PyObject* value, void* closure)
{
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "无法删除这个属性");
        return -1;
    }
    if (PyFloat_Check(value))
    {
        self->vlaue[1] = PyFloat_AsDouble(value);
        return 0;
    }
    else if (PyInt_Check(value))
    {
        self->vlaue[1] = _PyInt_AsInt(value);
        return 0;
    }
    else if (PyLong_Check(value))
    {
        self->vlaue[1] = PyLong_AsDouble(value);
        return 0;
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "类型应该为Float类型");
        return -1;
    }
}
static PyObject* z_get(Double3* self, void* closure)
{
    return PyFloat_FromDouble(self->vlaue[2]);
}
static int z_set(Double3* self, PyObject* value, void* closure)
{
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "无法删除这个属性");
        return -1;
    }
    if (PyFloat_Check(value))
    {
        self->vlaue[2] = PyFloat_AsDouble(value);
        return 0;
    }
    else if (PyInt_Check(value))
    {
        self->vlaue[2] = _PyInt_AsInt(value);
        return 0;
    }
    else if (PyLong_Check(value))
    {
        self->vlaue[2] = PyLong_AsDouble(value);
        return 0;
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "类型应该为Float类型");
        return -1;
    }
}
// 字符串魔术方法
static PyObject* Double3_repr(Double3* self)
{
    std::ostringstream ostr;
    ostr << "Double3(" << self->vlaue[0] << ", " << self->vlaue[1] << ", " << self->vlaue[2] << ")";
    std::string s = ostr.str();
    return PyUnicode_FromString(s.c_str());
}
// 迭代器魔术方法
static PyObject* Double3_iter(Double3* self) {
    return (PyObject*)Iter_newObject((PyObject *)self, 3);
}
// 普通方法

static PyObject* Double3_Dis(Double3* self, PyObject* args)
{
    PyObject* py_other = NULL;
    if (!PyArg_ParseTuple(args, "O", &py_other)) { return NULL; }
    if (PyObject_IsInstance(py_other, (PyObject*)&Double3_Type))
    {
        Double3* other = (Double3*)py_other;
        return PyFloat_FromDouble(sqrt(pow(self->vlaue[0] - other->vlaue[0], 2) + pow(self->vlaue[1] - other->vlaue[1], 2) + pow(self->vlaue[2] - other->vlaue[2], 2)));
    }
    PyErr_SetString(PyExc_TypeError, "类型应该为Double3类型");
    return NULL;
}
static PyObject* Double3_compile(Double3* self) {
    PyObject* tuple = PyTuple_New(3);
    PyTuple_SetItem(tuple, 0, PyFloat_FromDouble(self->vlaue[0]));
    PyTuple_SetItem(tuple, 1, PyFloat_FromDouble(self->vlaue[1]));
    PyTuple_SetItem(tuple, 2, PyFloat_FromDouble(self->vlaue[2]));
    return tuple;
}
// 序列函数实现
static unsigned int Double3_Len(Double3* self)
{
    return 3;
}
static PyObject* Double3_GetItem(Double3* self, PyObject* item)
{
    if (!PyInt_Check(item))
    {
        PyErr_SetString(PyExc_TypeError, "index = 0 or 1 or 2 type = int");
        return NULL;
    }
    int item_int = _PyInt_AsInt(item);
    if (item_int >= 0 && item_int < 3)
    {
        return PyFloat_FromDouble(self->vlaue[item_int]);
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "index = 0 or 1 or 2 type = int");
        return NULL;
    }

}
static int Double3_SetItem(Double3* self, PyObject* key, PyObject* v) {
    if (!PyInt_Check(key))
    {
        PyErr_SetString(PyExc_TypeError, "index = 0 or 1 or 2 type = int");
        return NULL;
    }
    int key_int = _PyInt_AsInt(key);
    if (key_int >= 0 && key_int < 3)
    {
        self->vlaue[key_int] = PyFloat_AsDouble(v);
        return 0;
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "index = 0 or 1 or 2 type = int");
        return -1;
    }
}
#endif