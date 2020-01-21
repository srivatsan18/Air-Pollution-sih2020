# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 02:30:48 2020

@author: Abhishek
"""
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Abhishek\\Anaconda3\\Library\\share";
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
            llcrnrlat = 7,
            llcrnrlon = 65,
            urcrnrlat = 37,
            urcrnrlon = 100,
            resolution='l')
m.drawcoastlines()
m.drawcountries(linewidth=1)
m.etopo()
xs=[]
ys=[]
Dlat, Dlon = 28.7041, 77.1025
xpt, ypt = m(Dlon, Dlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'co', markersize=10)

Clat, Clon = 13.0827, 80.2707
xpt, ypt = m(Clon, Clat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'ro', markersize=10)
m.plot(xs,ys,color='orange',label='Delhi to Chennai')
plt.legend()
plt.title('Pollution Hotspots')
plt.show()