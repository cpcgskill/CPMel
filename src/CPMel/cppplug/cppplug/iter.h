#ifndef ITER
#define ITER
#include"pythontool.h"
struct Iter
{
	PyObject_HEAD
	PyObject * data;
	unsigned int len;
	unsigned int current_pos;
};
Iter * Iter_newObject(PyObject * obj);
Iter * Iter_newObject(PyObject * obj, unsigned int len);
void Iter_Delete(Iter * self);

static PyObject *Iter_New(PyTypeObject *type, PyObject *args, PyObject *kw);
static void Iter_Dealloc(Iter *self);
static PyObject * Iter_Iter(PyObject *obj);
static PyObject * Iter_next(Iter *it);
/*---------------------------data---------------------------*/

/*
	Iter * add(Iter *other);
	Iter * less(Iter *other);
	Iter * multiply(double other);
	Iter * divide(double other);
*/
static PyTypeObject Iter_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "cppplug.Iter",            /* tp_name */
	sizeof(Iter),           /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Iter_Dealloc,/* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    0,                         /* tp_repr */
    0,           /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash */
    0,                         /* tp_call */
	0,             /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_CHECKTYPES,   /* tp_flags *//*    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE 之前使用这种 但是如果有PyNumberMethods就要使用现在的*/
    "Iter objects",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    Iter_Iter,                         /* tp_iter */
	(iternextfunc)Iter_next,                         /* tp_iternext */
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
	Iter_New,               /* tp_new */
};


Iter * Iter_newObject(PyObject * obj)
{
	Iter *self = (Iter *)(&Iter_Type)->tp_alloc(&Iter_Type, 0);
	Py_INCREF(obj);
	self -> data = obj;
	self->len = PyObject_Length(obj);
	self->current_pos = 0;
	return self;
}
Iter * Iter_newObject(PyObject * obj, unsigned int len)
{
	Iter *self = (Iter *)(&Iter_Type)->tp_alloc(&Iter_Type, 0);
	Py_INCREF(obj);
	self -> data = obj;
	self->len = len;
	self->current_pos = 0;
	return self;
}
void Iter_Delete(Iter * self)
{
	Py_DECREF(self->data);
}

/*------------------------------------------------------*/

static PyObject *Iter_New(PyTypeObject *type, PyObject *args, PyObject *kw)
{
	PyObject * obj = NULL;
	int len = -1;
	if (!PyArg_ParseTuple(args, "O|i",&obj, &len) ){return NULL;}  
	//Py_INCREF(self);
	if(len < 0)
		len = PyObject_Length(obj);
	Iter *self = Iter_newObject(obj, len);
	return (PyObject *) self;
}

static void Iter_Dealloc(Iter *self)
{
	//在这里Py_TYPE获得的是PyTypeObject而不是class Curve
	Iter_Delete(self);
	Py_TYPE(self)->tp_free(self);
	return ;
}
static PyObject * Iter_Iter(PyObject *obj)
{
    Py_INCREF(obj);
    return obj;
}

static PyObject * Iter_next(Iter *it)
{
	if(it->current_pos < it->len)
	{
		PyObject * item = PyObject_GetItem(it->data, PyInt_FromLong(it->current_pos));
		if(item == NULL)
		{
			PyErr_SetString(PyExc_StopIteration, "被迭代对象不可获得组件(item)");
			return NULL;
		}
		it->current_pos += 1;
		return item;
	}
	PyErr_SetString(PyExc_StopIteration, "iter end");
    return NULL;
}

#endif