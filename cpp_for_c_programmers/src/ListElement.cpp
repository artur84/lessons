/*
 * ListElement.cpp
 *
 *  Created on: 29/10/2015
 *      Author: CORE 7
 */

#include "ListElement.h"

ListElement::ListElement() :
		d(0), next(0) {
}
ListElement::ListElement(int n, ListElement* ptr) :
		d(n), next(ptr) {
}

ListElement::~ListElement() {
	// TODO Auto-generated destructor stub
}

