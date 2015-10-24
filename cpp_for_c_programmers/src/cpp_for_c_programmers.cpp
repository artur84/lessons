//============================================================================
// Name        : cpp_for_c_programmers.cpp
// Author      : Arturo Escobedo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

double suma_array(double my_array[], int size) {
	double result=0;
	for(int i=0; i<size;i++){
		result += my_array[i];
	}
	return result;
}

int main() {
	double result;
	double my_array[8] = {1.0,2.0,3.0};
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	result = suma_array(my_array,8);
	cout << result;
	return 0;
}
