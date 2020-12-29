#ifndef DOUBLE3ARRAY
#define DOUBLE3ARRAY
#include"import.h"
#include"iter.h"
#include"double3.h"
struct Double3Array
{
	PyObject_HEAD
	Double3 ** data;
};

static Double3Array* Double3Array_New(PyTypeObject* type, PyObject* args, PyObject* kw);
static void Double3Array_Del(Double3Array* self);
static PyObject* Double3Array_repr(Double3Array* self);
static Double3Array* Double3Array_iter(Double3Array* self);
static PyObject* Double3Array_Iter(PyObject* obj);

static PyObject* Double3Array_append(Double3Array* self, PyObject* args);
static PyObject* Double3Array_appstart(Double3Array* self, PyObject* args);
static PyObject* Double3Array_insert(Double3Array* self, PyObject* args);

static PyObject* Double3Array_InPlaceAdd(PyObject* o1, PyObject* o2);
static PyObject* Double3Array_InPlaceSub(PyObject* o1, PyObject* o2);
static PyObject* Double3Array_InPlaceMul(PyObject* o1, PyObject* o2);
static PyObject* Double3Array_InPlaceDivide(PyObject* o1, PyObject* o2);

static PyObject* Double3Array_getAllDis(Double3Array* self, PyObject* args);
void Double3ArrayClass_New(PyObject* m);

//–Ú¡–∑Ω∑®
static unsigned int Double3Array_Len(Double3Array* self);
static Double3* Double3Array_GetItem(Double3Array* self, Py_ssize_t* index);
static int Double3Array_SetItem(Double3Array* self, Py_ssize_t index, PyObject* val);


#endif