//============================================================================
// Name        : cpp_for_c_programmers.cpp
// Author      : Arturo Escobedo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdlib> //For srand function
#include <ctime>
#include <random>
#include "Point.h"
#include "List.h"
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

bool** draw_random_graph(int size, double density) {
	/*** Creates a random graph
	 * 	size is the size of the graf
	 * 	density a value between (0 and 1)
	 * 	is the probability to generate a link between to given nodes of the graph
	 */
	bool** graph;
	srand(time(0));
	graph = new bool*[size];
	for (int i = 0; i < size; i++) {
		graph[i] = new bool[size];
	}
	//Init with the given density
	for (int i = 0; i < size; ++i)
		for (int j = i; j < size; ++j)
			if (i == j)
				graph[i][j] = 0; //no loops
			else
				graph[i][j] = graph[j][i] = ((static_cast<float>(rand())
						/ RAND_MAX) < density); //prob() < density?

	return graph;
}

void print_graph(bool** graph, int size) {
	//Init with a given density
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cout << graph[i][j];
		}
		cout << endl;
	}
}

int main() {
	cout << "template for sum()" << endl;
	int a[] = { 1, 2, 3 };
	double b[] = { 2.1, 2.2, 2.3 };
	cout << sum(a, 3) << endl;
	cout << sum(b, 3) << endl;
	srand(time(0));

	cout << "template for substract()" << endl;
	cout << substract(a, 3) << endl;
	cout << substract(b, 3) << endl;
	/***
	 * Using Point Class
	 */
	Point pointa(0, 2), pointb(3.4, 5.6);

	cout << "a= " << pointa << " b= " << pointb << endl;

	/***
	 * Graphs
	 */
	cout << "**graphs " << endl;

	int size = 7;
	double density = 0.99;

	bool** graph = draw_random_graph(size, density);
	print_graph(graph, size);

	/***
	 * Lists
	 */
	cout << endl;
	cout << "****Lists********" << endl;
	int arrayA[7] = { 0, 1, 2, 3, 4, 5 };
	List la(arrayA, 7);
	List lb;
	la.prepend(9);
	la.prepend(8);
	cout << "list la" << endl;
	la.print();
	for (int i = 0; i < 40; i++) {
		lb.prepend(i);
	}
	cout << "list lb" << endl;
	lb.print();

}
