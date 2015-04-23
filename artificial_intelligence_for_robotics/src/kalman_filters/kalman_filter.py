'''
Created on 23/04/2015

@author: Arturo Escobedo
'''

def update(mean1, var1, mean2, var2):
    new_mean = (var1 * mean2 + var2 * mean1) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

if __name__ == '__main__':
    print update(10., 8. , 13. , 2.)
    print 'prediction'
    print predict(10., 4. , 12. , 4.)
