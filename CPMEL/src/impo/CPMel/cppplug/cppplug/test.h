#ifndef DOUBLE3
#define DOUBLE3
#include"double3data.h"
#include"import.h"
struct Double3
{
	PyObject_HEAD
	Double3Data * data;
};
Double3 * Double3_newObject();
Double3 * Double3_newObject(double x, double y, double z);
void Double3_Delete(Double3 * self);



static PyObject *Double3_New(PyTypeObject *type, PyObject *args, PyObject *kw);
static void Double3_Dealloc(Double3 *self);
static PyObject * x_get(Double3 *self, void *closure);
static int x_set(Double3 *self, PyObject *value, void *closure);
static PyObject * y_get(Double3 *self, void *closure);
static int y_set(Double3 *self, PyObject *value, void *closure);
static PyObject * z_get(Double3 *self, void *closure);
static int z_set(Double3 *self, PyObject *value, void *closure);
static PyObject * dis(Double3 *self, PyObject *args);
void Double3Class_New(PyObject *m);
// 魔术方法
static PyObject * str(Double3 *self);
//数值类型
static Double3 * Double3_ADD(PyObject *o1, PyObject *o2);
static Double3 * Double3_Sub(PyObject *o1, PyObject *o2);
static Double3 * Double3_Mul(PyObject *o1, PyObject *o2);
static Double3 * Double3_Divide(PyObject *o1, PyObject *o2);
//Double3_Mapping 序列方法
static unsigned int Double3_Len(Double3 *self);
static PyObject * Double3_GetItem(Double3 *self, PyObject *item);
/*---------------------------data---------------------------*/

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
PyMappingMethods Double3_Mapping = {
	(lenfunc)Double3_Len,
	(binaryfunc)Double3_GetItem,
	NULL
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
	{"dis", (PyCFunction)dis,
	METH_VARARGS,
     "距离计算"
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
    "data.Double3",            /* tp_name */
	sizeof(Double3),           /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Double3_Dealloc,/* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    0,                         /* tp_repr */
    &Double3_Number,           /* tp_as_number */
    0,                         /* tp_as_sequence */
    &Double3_Mapping,                         /* tp_as_mapping */
    0,                         /* tp_hash */
    0,                         /* tp_call */
	(reprfunc)str,             /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_CHECKTYPES | Py_TPFLAGS_BASETYPE,   /* tp_flags *//*    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE 之前使用这种 但是如果有PyNumberMethods就要使用现在的*/
    "Double objects",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Double3_methods,                   /* tp_methods */
    0,                         /* tp_members */
    Double3_getseters,                 /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    0,                         /* tp_init */
    0,                         /* tp_alloc */
	Double3_New,               /* tp_new */
};


Double3 * Double3_newObject()
{
	Double3 *self = (Double3 *)(&Double3_Type)->tp_alloc(&Double3_Type, 0);
	self -> data = new Double3Data();
	return self;
}
Double3 * Double3_newObject(double x, double y, double z)
{
	Double3 *self = (Double3 *)(&Double3_Type)->tp_alloc(&Double3_Type, 0);
	self -> data = new Double3Data(x, y, z);
	return self;
}
Double3 * Double3_newObject(Double3Data *data)
{
	Double3 *self = (Double3 *)(&Double3_Type)->tp_alloc(&Double3_Type, 0);
	self -> data = data;
	return self;
}
void Double3_Delete(Double3 * self)
{
	delete self->data;
}


/*------------------------------------------------------*/

static PyObject *Double3_New(PyTypeObject *type, PyObject *args, PyObject *kw)
{
	Double3Data * data = new Double3Data;
	if (!PyArg_ParseTuple(args, "ddd",&(data->x), &(data->y), &(data->z) ) ){return NULL;}  
	//Py_INCREF(self);
	Double3 *self = Double3_newObject(data);
	return (PyObject *) self;
}

static void Double3_Dealloc(Double3 *self)
{
	//在这里Py_TYPE获得的是PyTypeObject而不是class Curve
	Double3_Delete(self);
	Py_TYPE(self)->tp_free(self);
	return ;
}
// 普通方法

static PyObject * dis(Double3 *self, PyObject *args)
{
	PyObject * py_other = NULL;
	if (!PyArg_ParseTuple(args, "O",&py_other)){return NULL;}  
	if(PyObject_IsInstance(py_other, (PyObject *)&Double3_Type))
	{
		return PyFloat_FromDouble(self->data->dis(
			((Double3 *)py_other)->data
			));
	}
	PyErr_SetString(PyExc_TypeError, "类型应该为Double3类型");
	return NULL;
}

//getset方法
static PyObject * x_get(Double3 *self, void *closure)
{
	return PyFloat_FromDouble(self->data->x);
}

static int x_set(Double3 *self, PyObject *value, void *closure)
{
  if (value == NULL) {
    PyErr_SetString(PyExc_TypeError, "无法删除这个属性");
    return -1;
  }
  if(PyFloat_Check(value))
  {
	  self->data->x = PyFloat_AsDouble(value);
	  return 0;
  }
  else if(PyInt_Check(value))
  {
	  self->data->x = _PyInt_AsInt(value);
	  return 0;
  }
  else if(PyLong_Check(value))
  {
	  self->data->x = PyLong_AsDouble(value);
	  return 0;
  }
  else
  {
	  PyErr_SetString(PyExc_TypeError, "类型应该为Float类型");
	  return -1;
  }
}

static PyObject * y_get(Double3 *self, void *closure)
{
	return PyFloat_FromDouble(self->data->z);
}

static int y_set(Double3 *self, PyObject *value, void *closure)
{
  if (value == NULL) {
    PyErr_SetString(PyExc_TypeError, "无法删除这个属性");
    return -1;
  }
  if(PyFloat_Check(value))
  {
	  self->data->z = PyFloat_AsDouble(value);
	  return 0;
  }
  else if(PyInt_Check(value))
  {
	  self->data->z = _PyInt_AsInt(value);
	  return 0;
  }
  else if(PyLong_Check(value))
  {
	  self->data->z = PyLong_AsDouble(value);
	  return 0;
  }
  else
  {
	  PyErr_SetString(PyExc_TypeError, "类型应该为Float类型");
	  return -1;
  }
}
static PyObject * z_get(Double3 *self, void *closure)
{
	return PyFloat_FromDouble(self->data->z);
}

static int z_set(Double3 *self, PyObject *value, void *closure)
{
  if (value == NULL) {
    PyErr_SetString(PyExc_TypeError, "无法删除这个属性");
    return -1;
  }
  if(PyFloat_Check(value))
  {
	  self->data->z = PyFloat_AsDouble(value);
	  return 0;
  }
  else if(PyInt_Check(value))
  {
	  self->data->z = _PyInt_AsInt(value);
	  return 0;
  }
  else if(PyLong_Check(value))
  {
	  self->data->z = PyLong_AsDouble(value);
	  return 0;
  }
  else
  {
	  PyErr_SetString(PyExc_TypeError, "类型应该为Float类型");
	  return -1;
  }
}

// 字符串魔术方法
static PyObject * str(Double3 *self)
{
	std::ostringstream ostr;
	ostr << "Double3(" << self->data->x << ", " << self->data->y << ", " << self->data->z << ")";
	std::string s = ostr.str();
	return PyUnicode_FromString(s.c_str());
}

/*
	Double3 * add(Double3 *other);
	Double3 * less(Double3 *other);
	Double3 * multiply(double other);
	Double3 * divide(double other);
*/

void Double3Class_New(PyObject *m)
{
	if (m == NULL)
        return;
	//Python类声明

	//Type.tp_del这个是python3.*的析构函数
	if (PyType_Ready(&Double3_Type) < 0)
        return;
	Py_INCREF(&Double3_Type);
    PyModule_AddObject(m, "Double3", (PyObject *)&Double3_Type);
}
//数值类型函数实现
static Double3 * Double3_ADD(PyObject *o1, PyObject *o2)
{
	if(PyObject_IsInstance(o1, (PyObject *)&Double3_Type) && PyObject_IsInstance(o2, (PyObject *)&Double3_Type))
	{
		return Double3_newObject(((Double3 *)o1)->data->add(
			((Double3 *)o2)->data)
			);
	}
	return NULL;
}
static Double3 * Double3_Sub(PyObject *o1, PyObject *o2)
{
	if(PyObject_IsInstance(o1, (PyObject *)&Double3_Type) && PyObject_IsInstance(o2, (PyObject *)&Double3_Type))
	{
		
		Double3Data * a= ((Double3 *)o1)->data->less(((Double3 *)o1)->data);
		
		return Double3_newObject(a);
	}
	return NULL;
}
static Double3 * Double3_Mul(PyObject *o1, PyObject *o2)
{
	if(PyObject_IsInstance(o1, (PyObject *)&Double3_Type) && (PyFloat_Check(o2) || PyInt_Check(o2)))
	{
		return Double3_newObject(((Double3 *)o1)->data->multiply(PyFloat_AsDouble(o2)));
	}
	return NULL;
}
static Double3 * Double3_Divide(PyObject *o1, PyObject *o2)
{
	if(PyObject_IsInstance(o1, (PyObject *)&Double3_Type) && (PyFloat_Check(o2) || PyInt_Check(o2)))
	{
		return Double3_newObject(((Double3 *)o1)->data->divide(PyFloat_AsDouble(o2)));
	}
	return NULL;
}
// 序列函数实现
static unsigned int Double3_Len(Double3 *self)
{
	return 3;
}
static PyObject * Double3_GetItem(Double3 *self, PyObject *item)
{
	if (!PyInt_Check(item))
	{
		PyErr_SetString(PyExc_TypeError, "需要 int类型");
		return NULL;
	}
	unsigned int item_int = _PyInt_AsInt(item);
	if(item_int == 0)
	{
		return PyFloat_FromDouble(self->data->x);
	}
	else if(item_int == 1)
	{
		return PyFloat_FromDouble(self->data->y);
	}
	else if(item_int == 2)
	{
		return PyFloat_FromDouble(self->data->z);
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "只有0，1，2是正确的索引");
		return NULL;
	}
	
}
#endif