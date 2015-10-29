/*
 * ListElement.cpp
 *
 *  Created on: 29/10/2015
 *      Author: CORE 7
 */

#include "ListElement.h"
#include <iostream>
using namespace std;

ListElement::ListElement(int n = 0, ListElement* ptr = 0) :
		d(n), next(ptr) {
}

ListElement::~ListElement() {
	cout << "ListElement Destructor was called" << endl;
}

