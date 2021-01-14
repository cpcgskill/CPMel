#include"import.h"
class Numbr
{
public:
	Numbr(PyObject * m);
	~Numbr();
	PyGetSetDef * getSetDef();

private:

};

Numbr::Numbr(PyObject* m)
{
	static PyGetSetDef* getseters = getSetDef();
}

Numbr::~Numbr()
{
}