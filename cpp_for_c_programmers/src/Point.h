/*
 * Point.h
 *
 *  Created on: 26/10/2015
 *      Author: CORE 7
 */

#ifndef POINT_H_
#define POINT_H_

class Point {
public:
	Point();
	virtual ~Point();
	//Access  x coordinate
	double getx();
	//Set x coordinate in the point
	void setx(double v);
private:
	double x, y; //x and y coordinates of the point
};

#endif /* POINT_H_ */
