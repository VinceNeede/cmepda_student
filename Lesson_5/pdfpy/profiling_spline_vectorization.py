'''
This is a script used to compare different methods for the vectorization of the bounds from scipy.interpolate.InterpolatedUnivariateSpline.integrate
The methods are:
- brute_force: a for loop that computes the integral of the spline from the first point to the current point
- numpy_vectorization: a numpy vectorization of the integral method
- binning: a for loop that computes the integral of the spline from the current point to the next point and then uses a cumulative sum to get the integral from the first point to the current point
- numpy_vectorization_binning: a numpy vectorization of the integral method that computes the integral of the spline from the current point to the next point
    and then uses a cumulative sum to get the integral from the first point to the current point
'''
import argparse
import time

import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
from tqdm import tqdm

def brute_force(spline, x):
    Y=np.zeros(x.shape)
    for j,el in enumerate(x):
        Y[j]=spline.integral(x[0],el)
    return Y
def numpy_vectorization(spline, x):
    vectorized_integral = np.vectorize(spline.integral)
    return vectorized_integral(x[0],x)

def binning(spline, x):
    Y=np.zeros(len(x))
    Y[0]=0.
    for j in range(len(x)-1):
        Y[j+1]=spline.integral(x[j],x[j+1])
    return Y.cumsum()

def numpy_vectorization_binning(spline, x):
    vectorized_integral = np.vectorize(spline.integral)
    Y=np.zeros(len(x))
    Y[0]=0.
    Y[1:]=vectorized_integral(x[0:-1],x[1:])
    return Y.cumsum()    



if __name__=='__main__':
    parser=argparse.ArgumentParser(description="This is a script used to compare different methods for the vectorization of the bounds from scipy.interpolate.InterpolatedUnivariateSpline.integrate\n\
    The methods are:\n\
    - brute_force: a for loop that computes the integral of the spline from the first point to the current point\n\
    - numpy_vectorization: a numpy vectorization of the integral method\n\
    - binning: a for loop that computes the integral of the spline from the current point to the next point and then uses a cumulative sum to get the integral from the first point to the current point\n\
    - numpy_vectorization_binning: a numpy vectorization of the integral method that computes the integral of the spline from the current point to the next point\
    and then uses a cumulative sum to get the integral from the first point to the current point")
    parser.add_argument('--npoints', type=int,nargs=3,default=[10, 1000, 10], help='Number of points to use for spline interpolation, start stop step, default (10, 1000, 10)')
    parser.add_argument('--nruns', type=int, default=100, help='Number of runs to use for the vectorization of the spline integration, default 100')
    args=parser.parse_args()
    npoints=np.arange(*args.npoints)
    nruns=args.nruns

    x=np.linspace(0., 1., 100)
    y=np.exp(x)
    spline=InterpolatedUnivariateSpline(x, y, k=3,ext='raise')

    for vectorization_method in [brute_force, numpy_vectorization, binning, numpy_vectorization_binning]:
        times=np.zeros(len(npoints)+1)
        times[0]=time.time()
        for i,N in enumerate(tqdm(npoints)):
            X=np.linspace(0., 1., N)
            ture_Y=np.exp(X)-1
            for _ in range(nruns):
                Y=vectorization_method(spline, X)
                if not np.allclose(Y, ture_Y):
                    print('Error in the vectorization method', vectorization_method.__name__)
            times[i+1]=time.time()
        times=(times[1:]-times[0:-1])/nruns
        plt.plot(npoints,times , label=vectorization_method.__name__)
        plt.xlabel('length of the array')
        plt.ylabel('time per run')
    plt.legend()
    plt.savefig('profiling_spline_vectorization.png', dpi=300, bbox_inches='tight')
    plt.show()