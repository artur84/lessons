/*
 * ListElement.h
 *
 *  Created on: 29/10/2015
 *      Author: CORE 7
 */

#ifndef SRC_LISTELEMENT_H_
#define SRC_LISTELEMENT_H_

class ListElement {
public:
	ListElement(int n, ListElement* ptr);
	virtual ~ListElement();
	int d; //The data in the element
	ListElement* next; //The pointer to the next element
};

#endif /* SRC_LISTELEMENT_H_ */
