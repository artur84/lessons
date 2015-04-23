'''
Created on 21/04/2015
This file is used to test new code on the fly
@author: Jesus Arturo Escobedo Cabello
'''

p = [0.2, 0.2, 0.5, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

""" Moves the elements contained in the p vector EXACTLY (U) units to the left or to the right. 
    Assumes a cyclic world where the last item is moved to the beginning every time 
    it gets out of the WORLD.
    @param p: A python array.
    @param U: An integer that indicates the number of spaces to be shifted,
    if it is positive shift to the right. 
"""
def accurate_move(p, U):
    q = []
    for i in range(len(p)):
        q.append(p[(i - U) % len(p)])    #Using %len(p) has the effect of rolling values
                                    #over to the beginning of the list if the index is
                                    #greater than (or less than) the number of elements
                                    #in the list.

    return q


if __name__ == '__main__':
    print 'prior= ', p
    print 'posterior=', accurate_move(p, -3)
