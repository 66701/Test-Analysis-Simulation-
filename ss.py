
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

data = pd.read_excel("stress_strain_2.xls")
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
    y=[0, Coordpairs_fem_y[i][0], Coordpairs_fem_u[i][0]]
    x=[0, Coordpairs_fem_y[i][1], Coordpairs_fem_u[i][1]]
    f = interpolate.interp1d(x, y,kind='linear')
    
    # t, c, k = interpolate.splrep(x, y, s=0, k=1)
    
    xnew = np.arange(0, x[2], .00001)
    ynew = f(xnew)   
    plt.plot(x, y, 'o', xnew, ynew, '--')
    
    # spline = interpolate.BSpline(t,c,k, extrapolate = False)
    # plt.plot(xnew, spline(xnew), 'r')


    yy=[0, Coordpairs_exp_y[i][0], Coordpairs_exp_u[i][0]]
    xx=[0, Coordpairs_exp_y[i][1], Coordpairs_exp_u[i][1]]
    
    g = interpolate.interp1d(xx, yy,kind='linear')
    
    xxnew = np.arange(0, x[2], .00001)
    yynew = g(xxnew)   
    plt.plot(xx, yy, 'o', xxnew, yynew, ':')
    
    
plt.show()
    
