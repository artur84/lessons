/*
 * List.cpp
 *
 *  Created on: 29/10/2015
 *      Author: CORE 7
 */

#include "List.h"
#include <iostream>
using namespace std;

List::List() :
		head(0), cursor(0) {
}

List::List(const int* arr, int n) {
	/*** Constructs a list from a given array
	 *   arr: The array of "n" elements
	 *   n: Number of elements in the array
	 */
	head = 0;
	cursor = 0;
	for (int i = 0; i < n; i++) {
		cursor = head = new ListElement(arr[i], head);
	}
}

List::List(const List& lst) {
	/*** Constructs a referential copy from another list
	 * lst: The initial list.
	 */
	if (lst.head == 0) {
		head = 0;
		cursor = 0;
	} else {
		head = lst.head;
		cursor = lst.cursor;
	}

}
List::~List() {
// TODO Auto-generated destructor stub
}

void List::prepend(int n) {
	if (head == 0) {
		cursor = head = new ListElement(n, head);
	} else {
		head = new ListElement(n, head);
	}
}

void List::print() {
	ListElement* h = head;
	while (h != 0) {
		cout << h->d << "-->";
		h = h->next;
	}
	cout << "###" << endl;
}
