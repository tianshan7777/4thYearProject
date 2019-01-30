import math
import pandas as pd

EARTH_R = 6378.1
#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 0.840
radius = WALKING_DIS / EARTH_R

lats_max = []
lats_min = []
lons_max = []
lons_min = []

def find_lat(lat):

	lat_min = lat - radius
	lat_max = lat + radius

	return (lat_max, lat_min)

def find_lon(lat, lon):

	lat_T = asin(sin(lat)/cos(radius))
	delta_lon = acos((cos(r)-sin(lat_T)*sin(lat))/(cos(lat_T)*cos(lat)))
	lon_min = lon - delta_lon 
	lon_max = lon + delta_lon

	return (lon_max, lon_min)

#Load .csv data
data = pd.read_csv('./MergedData/albert_PcDis.csv')
poi_data = pd.read_csv('./poi/amenity.csv')

latitudes = data[['Latitudes']]
longitudes = data[['Longitudes']]
coordinates = poi_data[['coordinate']]

#Conver pandas onject to numpy array
latitudes = latitudes.values
longitudes = longitudes.values

#Iterate through
for i, j in zip(latitudes, longitudes):
	#Convert to float
    lat = float(i[0]) 
    lon = float(j[0])

    lat_max, lat_min = find_lat(lat)
    lats_max.append(lat_max)
    lats_min.append(lon_min)

    lon_max, lon_min = find_lon(lat, lon)
    lons_max.append(lon_max)
    lons_min.append(lon_min)

    for point in coordinates:
    	if (point[0] < lat_max and  point[0] > lat_min):
    		if (point[1] < lon_max and poin[1] > lon_min):
    			print(point)







