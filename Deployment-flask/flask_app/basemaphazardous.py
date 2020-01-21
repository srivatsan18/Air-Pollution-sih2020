# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 03:11:25 2020

@author: Abhishek
"""

# -- coding: utf-8 --
"""
Created on Mon Jan 20 22:07:40 2020

@author: robin
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


m = Basemap(projection='mill',
            llcrnrlat = 7,
            llcrnrlon = 65,
            urcrnrlat = 37,
            urcrnrlon = 100,
            resolution='l')


lat=[17.38714,
 26.148043,
 24.833946,
 30.741482,
 28.653229,
 23.033863,
 28.205523,
 30.8381,
 12.972442,
 9.939093,
 18.516726,
 21.146633,
 19.997454,
 19.970324,
 19.21833,
 19.07609,
 24.813967,
 30.900965000000006,
 31.326015,
 30.663738,
 25.1695181,
 26.92207,
 27.560932,
 24.879999,
 26.263863,
 24.57127,
 13.067439,
 27.17667,
 26.85,
 26.449923,
 28.535517,
 28.6692,
 22.59577,
 22.572645]


lon=[78.49168399999998,
 91.731377,
 92.779282,
 76.768066,
 77.308601,
 72.585022,
 76.795311,
 76.9585,
 77.58064300000002,
 76.270523,
 73.856255,
 79.08886,
 73.789803,
 79.30336,
 72.978088,
 72.877426,
 93.950279,
 75.857277,
 75.57618000000002,
 76.300042,
 75.854838,
 75.778885,
 76.625015,
 74.629997,
 73.008957,
 73.691544,
 80.237617,
 78.008072,
 80.949997,
 80.33187099999998,
 77.391029,
 77.4538,
 88.263641,
 88.363892]

typ=[1,
 1,
 2,
 4,
 3,
 4,
 4,
 4,
 1,
 2,
 3,
 1,
 4,
 1,
 1,
 4,
 2,
 3,
 1,
 4,
 4,
 1,
 1,
 4,
 1,
 1,
 1,
 3,
 1,
 1,
 1,
 4,
 4,
 4]


m.drawcoastlines()
m.drawcountries(linewidth=1)
m.etopo()

i=0
a=0
b=0
c=0
d=0
while(i<34):
    xpt, ypt = m(lon[i], lat[i])
    if(typ[i]==1):
        if(a==0):
            m.plot(xpt, ypt, 'co', color='red', markersize=7, label='RRO' )
            a=a+1
        else:
            m.plot(xpt, ypt, 'co', color='red', markersize=7 )
    if(typ[i]==2):
        if(b==0):
            m.plot(xpt, ypt, 'co', color='black', markersize=7, label='RO' )
            b=b+1
        else:
            m.plot(xpt, ypt, 'co', color='black', markersize=7 )
    if(typ[i]==3):
        if(c==0):
            m.plot(xpt, ypt, 'co', color='blue', markersize=7, label='R' )
            c=c+1
        else:
            m.plot(xpt, ypt, 'co', color='blue', markersize=7 )
    if(typ[i]==4):
        if(d==0):
            m.plot(xpt, ypt, 'co', color='white', markersize=7,label='I')
            d=d+1
        else:
            m.plot(xpt, ypt, 'co', color='white', markersize=7)
    i=i+1


plt.legend()
plt.title('Pollution Hotspots')
plt.show()