#include "base_class.h"
#include"iter.h"
#include"double3.h"
#include"matrix_class.h"
#include"matrix_array.h"
//有参数t无参数METH_NOARGS单参数METH_O键值对参数METH_KEYWORDS

static PyMethodDef SpamMethods[] = {
	{"NewMatrixs",
	(PyCFunction)NewMatrixs,
	METH_VARARGS,
	"创建Matrix矩阵元组"
	},
	{"NewDouble3s",
	(PyCFunction)NewDouble3s,
	METH_VARARGS,
	"创建Double3矩阵元组"
	},
    {0, 0, 0, 0}
};

PyMODINIT_FUNC initcppplug(void)
{
	PyObject *m = NULL;
    m = Py_InitModule3("cppplug", 
		SpamMethods,
		"cppplug");
	if (m == NULL)
        return;
	CPNewPyObjectClass(m, "BaseData", BaseData_Type);
	CPNewPyObjectClass(m, "Iter", Iter_Type);
	CPNewPyObjectClass(m, "Double3", Double3_Type);
	CPNewPyObjectClass(m, "Matrix", Matrix_Type);
	// PyImport_Import();
}