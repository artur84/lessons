/*
 * Point.h
 *
 *  Created on: 26/10/2015
 *      Author: CORE 7
 */

#ifndef POINT_H_
#define POINT_H_
#include <iostream>

class Point {

private:
	double x, y; //x and y coordinates of the point
public:
	Point();
	Point(double xcoord, double ycoord);

	virtual ~Point();
	//Access  x coordinate
	double getx();
	//Access  x coordinate
	double gety();
	//Set y coordinate in the point
	void setx(double v);
	//Set y coordinate in the point
	void sety(double v);

	/***
	 * Overloading operators
	 */
	// Friend functions are not members of the class
	//but can directly access any member of this class */
	friend Point operator+(const Point& p1, const Point& p2);
	friend std::ostream& operator<<(std::ostream& out, const Point& point);

};

#endif /* POINT_H_ */
