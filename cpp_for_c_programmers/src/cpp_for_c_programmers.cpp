//============================================================================
// Name        : cpp_for_c_programmers.cpp
// Author      : Arturo Escobedo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "Point.h"
using namespace std;

template<class T> //T is generic type
T sum(const T data[], int size, T s = 0) {
	for (int i = 0; i < size; i++) {
		s += data[i];
	}
	return s;
}

template<class T> //T is generic type
T substract(const T data[], int size, T s = 0) {
	for (int i = 0; i < size; i++) {
		s -= data[i];
	}
	return s;
}
/***
 * Overloaded operators
 *
 */
Point operator+(const Point& p1, const Point& p2) {
	Point sum;
	sum.x = p1.x + p2.x;
	sum.y = p1.y + p2.y;
	return sum;
}

// Note: operator<<() is not a member function of any class.
std::ostream & operator<<(std::ostream& out, Point& point) {
	/* Because operator<<() is a friend of Point, it can
	 directly access any member of this class */
	out << "(" << point.getx() << "," << point.gety() << ")";
	return out;
}

int main() {
	cout << "template for sum()" << endl;
	int a[] = { 1, 2, 3 };
	double b[] = { 2.1, 2.2, 2.3 };
	cout << sum(a, 3) << endl;
	cout << sum(b, 3) << endl;

	cout << "template for substract()" << endl;
	cout << substract(a, 3) << endl;
	cout << substract(b, 3) << endl;
	/***
	 * Using Point Class
	 */
	Point pointa(0, 2), pointb(3.4, 5.6);

	cout << "a= " << pointa << " b= " << pointb << endl;

}
