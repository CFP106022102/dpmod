import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def hello(E, u='eV'):
    if u=='eV':
        return E 
    else:
        return 'blergy'

def unit(E, u='eV'):
    h=6.63e-34
    e=1.602e-19
    c=3e8
    if u=='eV':
        return E
    elif u=='nm':
        x = (h*c)/(E*e*1e-9)
        return x
    elif u=='micron':
        x = (h*c)/(E*e*1e-6)
        return x

def plot(osc, units='eV'):

    fig = plt.figure(figsize=(9,7))
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    x = unit(osc.E, u=units)
    e = osc.func()

    e1, = ax1.plot(x, np.real(e), color='red', label='$e_{1}$')
    e2, = ax2.plot(x, -np.imag(e), color='blue', label='$e_{2}$')

    ax1.set_xlim(min(x), max(x))
    ax1.set_ylim(min(np.real(e)), max(np.real(e)))
    ax2.set_ylim(min(-np.imag(e)), max(-np.imag(e)))

    
    plt.show

class Lorentz:
    
    def __init__(self, E=np.linspace(5, 15, 100), A=10, E0=11, G = 1):
        self.E = E
        self.A = A
        self.E0 = E0
        self.G = G
        self.param = {'Amp.': self.A,
                      'E0': self.E0,
                      'Damping': self.G}

        return None

    def func(self):
        E = self.E

        A = self.A
        E0 = self.E0
        G = self.G

        e1 = []
        e2 = []
        
        for l in E:
            e1.append(1 + A**2*((E0**2-l**2)/((E0**2-l**2)**2+(G*l)**2)))
            e2.append((A**2*G*l)/((E0**2-l**2)**2+(G*l)**2))
        
        return np.array(e1) - np.array(e2)*1j

    def plot(self, units='eV'):
        plot(self, units='eV')
        

    def table(self):
        table = []
        count = 1
        param = self.param
        for p in param:
            table.append([count, p, param[p]])
            count +=1

        print tabulate(table,
                       headers = ['#', 'Parameter', 'Value'],
                       tablefmt = 'orgtbl')
            
        

class Material:
    def __init__(self):
        self.config = []
        self.add()
        return None

    def add(self, mod=Lorentz()):
        self.config.append(mod)

    def dp(self, E=None):
        return None

    def plot(self):
        return None 

    def table(self, item=None):
        if item==None:
            table = []
            count = 1
            for item in self.config:
                table.append([count, item.__class__.__name__])
                count += 1

            print tabulate(table,
                           headers = ['#', 'Name'],
                           tablefmt = 'orgtbl')

        else:
            self.config[item-1].table()
