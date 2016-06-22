import numpy as np
import matplotlib.pyplot as plt

class Lorentz:
    """Lorentz Oscillator Class"""
    
    def __init__(self, A=22, E0=10, G = 0.1):
        self.E = np.linspace(E0-5, E0+20, 100)
        self.A = A #Amplitude [dimentionless]
        self.E0 = E0 #Resonant Energy [eV]
        self.G = G #Damping [eV]

        self.param = {'A' : {'value': self.A, 
                             'units': 'eV$^{2}$', 
                             'label': 'Oscillator Amplitude'},
                      'E0': {'value': self.E0, 
                             'units': 'eV', 
                             'label': 'Resonant Energy'},
                      'G' : {'value': self.G, 
                             'units': 'eV', 
                             'label': 'Damping constant'}
                      }

    def func(self):
        """
        Calculate real and imaginary parts of dielectic permittivity
        Return as complex function
        """
        E = self.E

        A = self.param['A'].get('value', None)
        E0 = self.param['E0'].get('value', None)
        G = self.param['G'].get('value', None)

        dp = [] #Define list for holding complex permittivity
        

        for x in E:
            real = 1 + A*((E0**2-x**2)/((E0**2-x**2)**2+(G*x)**2))
            imag = A*((G*x)/((E0**2-x**2)**2 + (G*x)**2))
            dp.append(np.complex(real, imag))
        
        return dp

    def plot(self):
        E = self.E
        dp = self.func()
        l1, = plt.plot(E, np.real(dp))
        l2, = plt.plot(E, np.imag(dp))
        plt.show()

        
       

class Material:
    def __init__(self):
        self.config = []
        self.add()
        return None

    def add(self, mod=Lorentz()):
        self.config.append(mod)

    def dp(self, E=None):
        return None
