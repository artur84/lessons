//============================================================================
// Name        : cpp_for_c_programmers.cpp
// Author      : Arturo Escobedo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
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

int main() {
	cout << "template for sum()" << endl;
	int a[] = { 1, 2, 3 };
	double b[] = { 2.1, 2.2, 2.3 };
	cout << sum(a, 3) << endl;
	cout << sum(b, 3) << endl;

	cout << "template for substract()" << endl;
	cout << substract(a, 3) << endl;
	cout << substract(b, 3) << endl;
}
