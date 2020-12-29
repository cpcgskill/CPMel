#ifndef DOUBLE3DATA
#define DOUBLE3DATA
#include<math.h>
class Double3Data
{
public:
	Double3Data();
	Double3Data(double x, double y, double z);
	Double3Data * add(Double3Data *other);
	Double3Data * less(Double3Data *other);
	Double3Data * multiply(double other);
	Double3Data * divide(double other);
	double dis(Double3Data *other);
	~Double3Data();
	double x;
	double y;
	double z;
private:
};


Double3Data::Double3Data()
{
}
Double3Data::Double3Data(double x, double y, double z)
{
	this -> x = x;
	this -> y = y;
	this -> z = z;
}
Double3Data * Double3Data::add(Double3Data *other)
{
	return new Double3Data(x + other->x, y + other->y, z + other->z);
}
Double3Data * Double3Data::less(Double3Data *other)
{
	return new Double3Data(x - other->x, y - other->y, z - other->z);
}
Double3Data * Double3Data::multiply(double other)
{
	return new Double3Data(x * other, y * other, z * other);
}
Double3Data * Double3Data::divide(double other)
{
	return new Double3Data(x / other, y / other, z / other);
}
double Double3Data::dis(Double3Data *d3)
{
	//outdis = sqrt(pow(pt.x, 2) + pow(pt.y, 2) + pow(pt.z, 2));
	return sqrt(pow(this->x - d3->x, 2) + pow(this->y - d3->y, 2) + pow(this->z - d3->z, 2));
}
Double3Data::~Double3Data()
{
}
#endif