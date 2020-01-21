from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

m = Basemap(projection='mill',
            llcrnrlat = 7,
            llcrnrlon = 65,
            urcrnrlat = 37,
            urcrnrlon = 100,
            resolution='l')
m.drawcoastlines()
m.drawcountries(linewidth=1)
#m.etopo()
#Dlat, Dlon = 28.7041, 77.1025
#xpt, ypt = m(Dlon, Dlat)
#m.plot(xpt, ypt, 'co', markersize=10)


lon = 77.1025
lat = 28.7041
angle=360
x,y = m(lon, lat)
if(angle>=0 and angle<45):
    x2,y2=m(lon,lat+1)
if(angle>=45 and angle<90):
    x2,y2=m(lon+1,lat+1)
if(angle>=90 and angle<135):
    x2,y2=m(lon+1,lat)
if(angle>=135 and angle<180):
    x2,y2=m(lon+1,lat-1)
if(angle>=180 and angle<225):
    x2,y2=m(lon,lat-1)
if(angle>=225 and angle<270):
    x2,y2=m(lon-1,lat-1)
if(angle>=270 and angle<315):
    x2,y2=m(lon-1,lat)
if(angle>=315 and angle<=360):
    x2,y2=m(lon-1,lat+1)
#x2, y2 = m(lon+0.5,lat+0.5)

plt.arrow(x,y,x2-x,y2-y,fc="k", ec="k", linewidth = 4, head_width=10, head_length=10)
#plt.show()


#plt.legend()
plt.title('Pollution Hotspots')
plt.show()

