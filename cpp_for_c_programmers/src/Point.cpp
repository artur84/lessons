/*
 * Point.cpp
 *
 *  Created on: 26/10/2015
 *      Author: CORE 7
 */

#include "Point.h"

Point::Point() :
		x(0.0), y(0.0) {
}

Point::Point(double x) :
		x(x) {
	/*** This constructor allows conversions from double to point
	 *  Example: Point s; double d=3.5; s=d; //it works ok!!
	 */
	y = 0.0;
}

Point::Point(double xcoord, double ycoord) :
		x(xcoord), y(ycoord) {

}

Point::~Point() {
}

double Point::getx() {
	return x;
}
double Point::gety() {
	return y;
}

void Point::setx(double v) {
	x = v;
}

void Point::sety(double v) {
	y = v;
}

