#ifndef DOUBLE3ARRAYDATA
#define DOUBLE3ARRAYDATA
#include"double3data.h"

class Double3ArrayData
{
public:
	Double3ArrayData();
	Double3ArrayData(unsigned int len);
	Double3ArrayData(Double3Data ** double3s, unsigned int len);
	bool set(Double3Data * val, unsigned int index);
	bool set(double x, double y, double z, unsigned int index);
	Double3Data * get(unsigned int index);
	bool appstart(Double3Data * val);
	bool append(Double3Data * val);
	bool insert(Double3Data * val, unsigned int index = 0);
	bool remove(unsigned int index = 0);
	bool removes(unsigned int start = 0, unsigned int end = 0);
	void allAdd(Double3Data *other);
	void allLess(Double3Data *other);
	void allMultiply(double other);
	void allDivide(double other);
	~Double3ArrayData();
	Double3Data ** items;
	unsigned int len;
private:
};


Double3ArrayData::Double3ArrayData()
{
	this->items = NULL;
	this->len = 0;
}
Double3ArrayData::Double3ArrayData(unsigned int len)
{
	this->items = new Double3Data * [len];
	this->len = len;
	for(unsigned int i = 0; i < len; i++)
	{
		this->items[i] = NULL;
	}
}
Double3ArrayData::Double3ArrayData(Double3Data ** double3s, unsigned int len)
{

	this->items = double3s;
	this->len = len;
}
bool Double3ArrayData::set(double x, double y, double z, unsigned int index)
{
	if (index < this->len)
	{
		if(this->items[index]!=NULL)
		{
			this->items[index]->x = x;
			this->items[index]->y = y;
			this->items[index]->z = z;
			return true;
		}
		else
		{
		this->items[index] = new Double3Data(x, y, z);
		return true;
		}
	}
	else
	{
		return false;	
	}
		
}
bool Double3ArrayData::set(Double3Data * val, unsigned int index)
{
	if (index < this->len)
	{
		this->items[index] = val;
		return true;
	}
	else
	{
		return false;	
	}
		
}
Double3Data * Double3ArrayData::get(unsigned int index)
{
	if(index < this->len)
	{
		Double3Data * val = this->items[index];
	
		if (val == NULL)
		{
			return new Double3Data(0, 0, 0);
		}
		
		return new Double3Data(val->x, val->y, val->z);
	}
	else
	{
		return NULL;
	}

}
bool Double3ArrayData::appstart(Double3Data * val)
{
	Double3Data ** test_items = this->items;
	this->items = new Double3Data * [len + 1];
	if(this->items == NULL)
	{
		this->items = test_items;
		return false;
	}
	this->items[0] = new Double3Data(*val);
	for(unsigned int i = 1; i <= len; i++)
		this->items[i] = test_items[i - 1];
	len += 1;
	delete test_items;
	return true;
}
bool Double3ArrayData::append(Double3Data * val)
{
	Double3Data ** test_items = this->items;
	this->items = new Double3Data * [len + 1];
	if(this->items == NULL)
	{
		this->items = test_items;
		return false;
	}
	for(unsigned int i = 0; i < len; i++)
		this->items[i] = test_items[i];
	this->items[len] = new Double3Data(*val);
	len += 1;
	delete test_items;
	return true;
}
bool Double3ArrayData::insert(Double3Data * val, unsigned int index)
{
	if(index < this->len)
	{
	Double3Data ** test_items = this->items;
	this->items = new Double3Data * [len + 1];
	if(this->items == NULL)
	{
		this->items = test_items;
		return false;
	}
	for(unsigned int i = 0; i < index; i++){this->items[i] = test_items[i];}
	this->items[index] = new Double3Data(*val);
	for(unsigned int i = index+1; i <= len; i++){this->items[i] = test_items[i-1];}
	len += 1;
	delete test_items;
	return true;
	}
	else
	{
		return false;
	}

}

bool Double3ArrayData::remove(unsigned int index)
{
	if(index < this->len)
	{
		unsigned int array_end = this->len - 1;
		for(unsigned int i = index; i < array_end; i++)
			this->items[i] = this->items[i + 1];
		this->len -= 1;
		return true;
	}
	else
	{
		return false;
	}
}
bool Double3ArrayData::removes(unsigned int start, unsigned int end)
{
	int size = (end - start);
	if(size < 0)
		return false;
	if(end < this->len)
	{
		unsigned int array_end = this->len - size;
		for(unsigned int i = start; i < array_end; i++)
			this->items[i] = this->items[i + size];
		this->len -= size;
		return true;
	}
	else
	{
		return false;
	}

}

void Double3ArrayData::allAdd(Double3Data *other)
{
	for(unsigned int i = 0; i < this->len; i++)
	{
		Double3Data * val = this->get(i);
		val->x += other->x;
		val->y += other->y;
		val->z += other->z;
	}
}
void Double3ArrayData::allLess(Double3Data *other)
{
	for(unsigned int i = 0; i < this->len; i++)
	{
		Double3Data * val = this->get(i);
		val->x -= other->x;
		val->y -= other->y;
		val->z -= other->z;
	}
}
void Double3ArrayData::allMultiply(double other)
{
	for(unsigned int i = 0; i < this->len; i++)
	{
		Double3Data * val = this->get(i);
		val->x *= other;
		val->y *= other;
		val->z *= other;
	}
}
void Double3ArrayData::allDivide(double other)
{
	for(unsigned int i = 0; i < this->len; i++)
	{
		Double3Data * val = this->get(i);
		val->x /= other;
		val->y /= other;
		val->z /= other;
	}
}

Double3ArrayData::~Double3ArrayData()
{
	if(this->items == NULL)
		return;
	for(unsigned int i = 0; i < this->len; i++)
	{
		if (this->items[i] != NULL)
			delete this->items[i];
	}
	delete this->items;
}
#endif