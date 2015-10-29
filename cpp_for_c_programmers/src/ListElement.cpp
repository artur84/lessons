/*
 * ListElement.cpp
 *
 *  Created on: 29/10/2015
 *      Author: CORE 7
 */

#include "ListElement.h"

ListElement::ListElement(int n = 0, ListElement* ptr = 0) :
		d(n), next(ptr) {
}

ListElement::~ListElement() {
	// TODO Auto-generated destructor stub
}

