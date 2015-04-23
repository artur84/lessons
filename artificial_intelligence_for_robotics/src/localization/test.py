'''
Created on 21/04/2015
This file is used to test new code on the fly
@author: Jesus Arturo Escobedo Cabello
'''

p = [0.0, 0.0, 1.0, 0.0, 0.0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

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

""" Moves the elements contained in the p vector (U) units to the left or to the right. 
    Considers the probabilities of undershooting and overshooting while moving
    Assumes a cyclic world where the last item is moved to the beginning every time 
    it gets out of the WORLD.
    @param p: A python array.
    @param U: An integer that indicates the number of spaces to be shifted,
    if it is positive shift to the right. 
"""
def inaccurate_move(p, U):
    q = []
    for i in range(len(p)):
        q.append(p[(i - U) % len(p)] * pExact +
                 p[(i - U + 1) % len(p)] * pUndershoot +
                 p[(i - U - 1) % len(p)] * pOvershoot)
                #Using %len(p) has the effect of rolling values
                #over to the beginning of the list if the index is
                #greater than (or less than) the number of elements
                #in the list.

    return q



if __name__ == '__main__':
    print 'prior= ', p
    for i in range(1000):
        p = inaccurate_move(p, 1)

    print 'posterior=', p
