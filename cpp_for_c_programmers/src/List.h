/*
 * List.h
 *
 *  Created on: 29/10/2015
 *      Author: CORE 7
 */

#ifndef SRC_LIST_H_
#define SRC_LIST_H_
#include "ListElement.h"
class List {
public:
	List();
	List(const int* arr, int n);
	List(const List& lst);
	virtual ~List();
	void prepend(int n); //insert at front value n
	int get_element(); //Returns the element currently pointed by cursor
	void advance();
	void print();

private:
	ListElement* head;
	ListElement* cursor;

};

#endif /* SRC_LIST_H_ */
