import numpy as np
import scipy
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    def __init__(self, x, y, order=3, num_points=100):
        spline=InterpolatedUnivariateSpline(x, y, k=order,ext='raise')
        norm=spline.integral(x.min(), x.max())
        self._x=x
        self._xmin=self._x.min()
        self._xmax=self._x.max()
        self._y=y/norm
        self._order=order
        super().__init__(self._x, self._y, k=order,ext='raise')
        self._icdf=self._get_icdf(num_points=num_points)

    def _get_icdf(self, num_points):
        x=np.linspace(self._xmin,self._xmax,num_points)
        vectorized_integral=np.vectorize(self.integral)
        Y=vectorized_integral(x[0],x)
        return InterpolatedUnivariateSpline(Y, x, k=self._order,ext='raise')
    
    def plot_starting_points(self):
        plt.plot(self._x, self._y, 'o', label='Data')
    def plot_pdf(self,npoints=100):
        x=np.linspace(self._xmin, self._xmax, npoints)
        plt.plot(x, self(x), label='PDF')

    def plot(self,npoints=100):
        self.plot_starting_points()
        self.plot_pdf(npoints)
        plt.legend()        
    def random(self, n):
        return self._icdf(np.random.rand(n))

if __name__=='__main__':
    x=np.linspace(0., 1., 4)
    y=np.exp(x)
    pdf=ProbabilityDensityFunction(x, y)
    pdf.plot()
    plt.show()
    sample=pdf.random(10000)
    plt.hist(sample, bins=30, density=True, alpha=0.5, label='Random samples')
    pdf.plot_pdf(100)
    plt.legend()
    plt.show()
