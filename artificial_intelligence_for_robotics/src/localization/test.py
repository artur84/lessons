'''
Created on 21/04/2015
This file is used to test new code on the fly
@author: Jesus Arturo Escobedo Cabello
'''

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p,Z):
    q=[]
    for i in range(len(p)):
        hit = (Z==world[i])
        q.append(p[i] * (hit * pHit + (1-hit)*pMiss))
    s=sum(q)
    for i in range(len(q)):
        q[i]=q[i]/s
    return q


if __name__ == '__main__':
    print 'prior= ', p 
    for i in range(len(measurements)):
        p=sense(p,measurements[i])
    print 'posterior=', p