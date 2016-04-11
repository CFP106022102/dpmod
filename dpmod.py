import numpy as np
import matplotlib.pyplot as plt

class Lorentz:
    
    def __init__(self, A=22, E0=32, G = 1):
        self.E = np.linspace(E0-5, E0+4, 100)
        self.A = A
        self.E0 = E0
        self.G = G

        self.param = {'Amp.': self.A,
                       'E0 (eV)': self.E0,
                       'Gamma (eV^-1)': self.G}
        return None

    def p(self):
        p = self.param.values()
        return p

    def func(self):
        E = self.E

        p = self.p()
        A = p[0]
        E0 = p[1]
        G = p[2]

        e1 = []
        
        for l in E:
            e1.append(1 + ((E0**2-l**2)/((E0**2-l**2)**2+(G*l)**2)))
        
        return e1

    def plot(self):
        E = self.E

        l1, = plt.plot(E, self.func())
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
