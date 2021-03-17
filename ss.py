# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:15:02 2021

@author: Jonah Pedra
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

data = pd.read_excel("stress_strain.xls")
data_numpy = data.to_numpy()

Coordpairs_fem_y = []
Coordpairs_fem_u = []
Coordpairs_exp_y = []
Coordpairs_exp_u = []

for i in range(1, len(data_numpy[:,3])):
    coord = [data_numpy[i,3],data_numpy[i,5]]
    Coordpairs_fem_y.append(coord)

    coord = [data_numpy[i,4],data_numpy[i,6]]
    Coordpairs_fem_u.append(coord)
    
    coord = [data_numpy[i,8],data_numpy[i,10]]
    Coordpairs_exp_y.append(coord)
    
    coord = [data_numpy[i,9],data_numpy[i,11]]
    Coordpairs_exp_u.append(coord)

Polyfit_fem=[]
Polyfit_exp=[]

for i in range(len(Coordpairs_fem_y)):
    x=[0, Coordpairs_fem_y[i][0], Coordpairs_fem_u[i][0]]
    y=[0, Coordpairs_fem_y[i][1], Coordpairs_fem_u[i][1]]
    Polyfit_fem.append(Polynomial(lagrange(x,y)).coef)
    
    xx=[0, Coordpairs_exp_y[i][0], Coordpairs_exp_u[i][0]]
    yy=[0, Coordpairs_exp_y[i][1], Coordpairs_exp_u[i][1]]
    Polyfit_exp.append(Polynomial(lagrange(xx,yy)).coef)

def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

linn = np.linspace(0, .1, 1000)
coeffs = Polyfit_exp[0]
plt.plot(linn, PolyCoefficients(linn, coeffs))
plt.show()
    
