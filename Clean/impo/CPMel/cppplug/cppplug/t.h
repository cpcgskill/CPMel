#ifndef MATRIX
#define MATRIX
#include"pythontool.h"
struct Matrix
{
    PyObject_HEAD
    double val[4][4];
};

#define NewMatrixObject CPNewPyObject(Matrix_Type, Matrix)
static PyObject* Matrix_New(PyTypeObject* type, PyObject* args, PyObject* kw);
static void Matrix_Dealloc(Matrix* self);

// 魔术方法
static PyObject* Matrix_repr(Matrix* self);
//数值类型
static Matrix* Matrix_ADD(Matrix* o1, Matrix* o2);
static Matrix* Matrix_Sub(Matrix* o1, Matrix* o2);
static Matrix* Matrix_Mul(Matrix* o1, Matrix* o2);
//Matrix_Mapping 序列方法
static unsigned int Matrix_Len(Matrix* self);
static PyObject* Matrix_GetItem(Matrix* self, PyObject* item);



PyMappingMethods Matrix_Mapping = {
    (lenfunc)Matrix_Len,
    (binaryfunc)Matrix_GetItem,
    NULL
};

static PyNumberMethods Matrix_Number = {
    (binaryfunc)Matrix_ADD,          /* nb_add */
    (binaryfunc)Matrix_Sub,          /* nb_subtract */
    (binaryfunc)Matrix_Mul,          /* nb_multiply */
    0,       /*nb_divide*/
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

/*
    Matrix * add(Matrix *other);
    Matrix * less(Matrix *other);
    Matrix * multiply(double other);
    Matrix * divide(double other);
*/
static PyTypeObject Matrix_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "cppplug.Matrix",            /* tp_name */
    sizeof(Matrix),           /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Matrix_Dealloc,/* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    (reprfunc)Matrix_repr,    /* tp_repr */
    & Matrix_Number,           /* tp_as_number */
    0,                         /* tp_as_sequence */
    & Matrix_Mapping,          /* tp_as_mapping */
    0,                         /* tp_hash */
    0,                         /* tp_call */
    (reprfunc)Matrix_repr,             /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_CHECKTYPES | Py_TPFLAGS_BASETYPE,   /* tp_flags *//*    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE 之前使用这种 但是如果有PyNumberMethods就要使用现在的*/
    "Matrix objects",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    0,                   /* tp_methods */
    0,                         /* tp_members */
    0,                 /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    0,                         /* tp_init */
    0,                         /* tp_alloc */
    Matrix_New,               /* tp_new */
};


static PyObject* Matrix_New(PyTypeObject* type, PyObject* args, PyObject* kw)
{
    Matrix* data = NewMatrixObject;
    //PyArg_ParseTuple
    unsigned int len = PyObject_Length(args);
    if (len == 4) {
        for (unsigned int i = 0; i < 4; i++) {
            PyObject* item = PyObject_GetItem(args, PyInt_FromLong(i));
            if (PyObject_Length(item) == 4) {
                for (unsigned int t = 0; t < 4; t++) {
                    data->val[i][t] = PyFloat_AsDouble(PyObject_GetItem(item, PyInt_FromLong(t)));
                }
            }
            else {
                PyErr_SetString(PyExc_ValueError, "仅支持（（int*4）*4）或 （int * 16）");
                return nullptr;
            }
        }
    }
    else if (len == 16) {
        unsigned int pos = 0;
        for (unsigned int i = 0; i < 4; i++) {
            for (unsigned int t = 0; t < 4; t++) {
                data->val[i][t] = PyFloat_AsDouble(PyObject_GetItem(args, PyInt_FromLong(pos)));
                pos++;
            }
        }
    }
    else {
        PyErr_SetString(PyExc_ValueError, "仅支持（（int*4）*4）或 （int * 16）");
        return NULL;
    }
    return (PyObject*)data;
}
static void Matrix_Dealloc(Matrix* self)
{
    //在这里Py_TYPE获得的是PyTypeObject而不是class Curve
    CPDeletePyObject(self);
    return;
}
//数值类型
static Matrix* Matrix_ADD(Matrix* o1, Matrix* o2) {
    if (PyObject_IsInstance((PyObject*)o1, (PyObject*)&Matrix_Type) && PyObject_IsInstance((PyObject*)o2, (PyObject*)&Matrix_Type))
    {
        Matrix* self = NewMatrixObject;
        for (unsigned int i = 0; i < 4; i++) {
            for (unsigned int t = 0; t < 4; t++) {
                self->val[i][t] = o1->val[i][t] + o2->val[i][t];
            }
        }
        return self;
    }
    return NULL;
}
static Matrix* Matrix_Sub(Matrix* o1, Matrix* o2) {
    if (PyObject_IsInstance((PyObject*)o1, (PyObject*)&Matrix_Type) && PyObject_IsInstance((PyObject*)o2, (PyObject*)&Matrix_Type))
    {
        Matrix* self = NewMatrixObject;
        for (unsigned int i = 0; i < 4; i++) {
            for (unsigned int t = 0; t < 4; t++) {
                self->val[i][t] = o1->val[i][t] - o2->val[i][t];
            }
        }
        return self;
    }
    return NULL;
}
static Matrix* Matrix_Mul(Matrix* o1, Matrix* o2) {
    if (PyObject_IsInstance((PyObject*)o1, (PyObject*)&Matrix_Type) && PyObject_IsInstance((PyObject*)o2, (PyObject*)&Matrix_Type))
    {
        Matrix* self = NewMatrixObject;
        for (unsigned int i = 0; i < 4; i++) {
            for (unsigned int t = 0; t < 4; t++) {
                self->val[i][t] = o1->val[i][t] * o2->val[t][i];
            }
        }
        return self;
    }
    return NULL;
}
// 字符串魔术方法
static PyObject* Matrix_repr(Matrix* self)
{
    std::ostringstream ostr;
    ostr << "Matrix(";
    for (unsigned int i = 0; i < 16; i++) {
        ostr << self->val[i];
        if (i < 15) {
            ostr << ", ";
        }
    }
    ostr << ")";
    std::string s = ostr.str();
    return PyUnicode_FromString(s.c_str());
}
//类构建函数
void NewMatrixClass_SSS(PyObject* m)
{
    if (m == NULL)
        return;
    //Python类声明

    //Type.tp_del这个是python3.*的析构函数
    if (PyType_Ready(&Matrix_Type) < 0)
        return;
    Py_INCREF(&Matrix_Type);
    PyModule_AddObject(m, "Matrix", (PyObject*)&Matrix_Type);
}

// 序列函数实现
static unsigned int Matrix_Len(Matrix* self)
{
    return 16;
}
static PyObject* Matrix_GetItem(Matrix* self, PyObject* item)
{
    if (PyObject_Length(item) == 2)
    {
        unsigned int r = _PyInt_AsInt(PyObject_GetItem(item, PyInt_FromLong(0)));
        unsigned int w = _PyInt_AsInt(PyObject_GetItem(item, PyInt_FromLong(1)));
        return PyFloat_FromDouble(self->val[r][w]);
    }
    else {
        PyErr_SetString(PyExc_TypeError, "需要(0~4, 0~4)的参数");
        return NULL;
    }
}
#endif