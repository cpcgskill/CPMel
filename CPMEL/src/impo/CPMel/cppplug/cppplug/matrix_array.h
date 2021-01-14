#ifndef NEWARRAY
#define NEWARRAY
#include"pythontool.h"
#include"matrix_class.h"
#include"double3.h"

//这个函数有内存泄漏
static PyObject* NewMatrixs(PyObject* self, PyObject* args) {
	unsigned int len = PyObject_Length(args);
	PyObject* tuple = PyTuple_New(len);
	for (unsigned int i = 0; i < len; i++) {
		PyObject* item = PyObject_GetItem(args, PyInt_FromLong(i));
		PyObject* new_item = Matrix_New(&Matrix_Type, item, NULL);
		Py_XDECREF(item);
		if (new_item == NULL)
			return NULL;
		PyTuple_SetItem(tuple, i, new_item);
	}
	return tuple;
}
//这个函数有内存泄漏
static PyObject* NewDouble3s(PyObject* self, PyObject* args) {
	PyObject* in_v = NULL;
	if (!PyArg_ParseTuple(args, "O", &in_v)) { return NULL; }

	unsigned int len = PyObject_Length(in_v);
	PyObject* tuple = PyTuple_New(len);
	for (unsigned int i = 0; i < len; i++) {
		PyObject* item = PyObject_GetItem(in_v, PyInt_FromLong(i));
		Double3* data = NewDouble3Object;
		data->vlaue[0] = PyFloat_AsDouble(PyObject_GetItem(item, PyInt_FromLong(0)));
		data->vlaue[1] = PyFloat_AsDouble(PyObject_GetItem(item, PyInt_FromLong(1)));
		data->vlaue[2] = PyFloat_AsDouble(PyObject_GetItem(item, PyInt_FromLong(2)));
		PyTuple_SetItem(tuple, i, (PyObject*)data);
		//if (PyObject_Length(item) >= 3) {
		//	Double3* data = NewDouble3Object;
		//	data->vlaue[0] = PyFloat_AsDouble(PyObject_GetItem(item, PyInt_FromLong(0)));
		//	data->vlaue[1] = PyFloat_AsDouble(PyObject_GetItem(item, PyInt_FromLong(1)));
		//	data->vlaue[2] = PyFloat_AsDouble(PyObject_GetItem(item, PyInt_FromLong(2)));
		//	PyTuple_SetItem(tuple, i, (PyObject *)data);
		//}
		//else {
		//	Double3* data = NewDouble3Object;
		//	data->vlaue[0] = -1;
		//	data->vlaue[1] = -1;
		//	data->vlaue[2] = -1;
		//	PyTuple_SetItem(tuple, i, (PyObject*)data);
		//}
	}
	return tuple;
}
#endif