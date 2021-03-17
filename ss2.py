
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

data = pd.read_excel("stress_strain_3.xls")
data_numpy = data.to_numpy()


Coordpairs_EXPTAN = []
Coordpairs_EXPLONG = []
Coordpairs_EXP3 = []
Coordpairs_EXP2 = []
Coordpairs_EXP1 = []



for i in range(1, len(data_numpy[:,0])):
    coord = [data_numpy[i,0],data_numpy[i,1]]
    Coordpairs_EXPTAN.append(coord)
    
    coord = [data_numpy[i,2],data_numpy[i,3]]
    Coordpairs_EXPLONG.append(coord)
    
    coord = [data_numpy[i,4],data_numpy[i,5]]
    Coordpairs_EXP3.append(coord)
    
    coord = [data_numpy[i,6],data_numpy[i,7]]
    Coordpairs_EXP2.append(coord)

    coord = [data_numpy[i,8],data_numpy[i,9]]
    Coordpairs_EXP1.append(coord)

def plotr(coord):
    y=[0]
    x=[0]
    for i in range(len(coord)):
        x.append(coord[i][0])
        y.append(coord[i][1])
    x=(list(dict.fromkeys(x)))
    y=(list(dict.fromkeys(y)))
    f = interpolate.interp1d(x, y,kind='slinear')
    xnew = np.arange(0, x[-1], .001)
    ynew = f(xnew)   
    plt.plot(x, y, 'o', xnew, ynew, '-')
    plt.show()
    
