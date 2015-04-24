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
    measurements = [5., 6., 7., 9., 10.]
    motion = [1.0, 1., 2., 1., 1.]
    measurement_sig = 4.
    motion_sig = 2.
    mu = 0.
    sig = 10000.
    for k in range(len(measurements)):
        [mu, sig] = update(mu, sig, measurements[k], measurement_sig)
        print 'update: ', [mu, sig]
        [mu, sig] = predict(mu, sig, motion[k], motion_sig)
        print 'predict: ', [mu, sig]
