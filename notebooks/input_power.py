import numpy as np


class InputPower(object):
    """Setup an initial power object given input parameters"""


    def __init__(self,P0=1.0,k0=1,kF=10,r_SiIII=20,f_SiIII=0.05):
        """Define here your favorite power spectrum."""

        self.P0=P0
        self.k0=k0
        self.kF=kF
        self.r_SiIII=r_SiIII
        self.f_SiIII=f_SiIII


    def get_true_p1d(self,k):
        """Evaluate power spectrum at input wavenumbers k"""

        if np.any(k<0):
            raise ValueError('get_true_p1d shold receive non-negative values')

        # white noise at low-k
        P = self.P0*np.ones_like(k)

        # small enhancement at low-k
        P *= (1+k/self.k0)
        
        # suppressed at k0
        P *= 1/(1+(k/self.k0)**2)

        # further suppressed with a Gaussian at kF=10
        P *= np.exp(-(k/self.kF)**2)

        # SiIII(1207) contamination
        P *= (1+self.f_SiIII*np.cos(k*self.r_SiIII))
        
        return P


