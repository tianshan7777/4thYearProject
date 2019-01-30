from math import asin, sin, acos, cos, radians
import pandas as pd

EARTH_R = 6378.1
#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 0.840
radius = WALKING_DIS / EARTH_R

lats_max = []
lats_min = []
lons_max = []
lons_min = []
related_points = []

def find_lat(lat):

    lat_min = lat - radius
    lat_max = lat + radius

    return (lat_max, lat_min)

def find_lon(lat, lon):

    lat_T = asin(sin(lat)/cos(radius))
    delta_lon = acos( ( cos(radius) - sin(lat_T) * sin(lat) ) / ( cos(lat_T) * cos(lat) ) )
    lon_min = lon - delta_lon 
    lon_max = lon + delta_lon

    return (lon_max, lon_min)

def counter(poi_type):
    if 'animal' in poi_type:
        animal += 1
    elif 'art' in poi_type:
        art += 1
    elif 'atm' in poi_type or 'bank' in poi_type:
        finance += 1
    elif 'bar' in poi_type:
        night_life += 1
    elif 'bicycle' in poi_type:
        bicycle += 1
    elif 'biergarden' in poi_type:
        


#Load .csv data
data = pd.read_csv('./MergedData/albert_PcDis.csv')
poi_data = pd.read_csv('./poi/amenity.csv')

latitudes = data[['Latitude']]
longitudes = data[['Longitude']]
coordinates = poi_data['coordinate']
poi_types = poi_data['poi type']

#Conver pandas onject to numpy array
latitudes = latitudes.values
longitudes = longitudes.values

#Iterate through
for i, j in zip(latitudes, longitudes):

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    #Convert to float
    lat = float(i[0]) 
    lon = float(j[0])
    print("original:", lat, lon)

    lat, lon = map(radians, [lat, lon])
    print("in radians:", lat, lon)

    lat_max, lat_min = find_lat(lat)
    print("lat max:", lat_max)
    lats_max.append(lat_max)
    print("lat min:", lat_min)
    lats_min.append(lat_min)

    lon_max, lon_min = find_lon(lat, lon)
    print("lon max:", lon_max)
    lons_max.append(lon_max)
    print("lon min:", lon_min)
    lons_min.append(lon_min)

    new_list = []
    i = 0

    for poi in coordinates:

        print("poi type:", poi_types[i])
        i += 1

        print("poi:", poi)

        point = poi.split(',')
        #Convert to float
        point[0] = radians(float(point[0]))
        point[1] = radians(float(point[1]))
        print(point)

        if (point[1] < lat_max and  point[1] > lat_min):
            if (point[0] < lon_max and point[0] > lon_min):
                print("_____________within area_______________:", point)
                new_list.append(poi_types[i])

    related_points.append(new_list)

data['related_points'] = pd.Series(related_points)
data['related_points'] = pd.Series(related_points)
data['related_points'] = pd.Series(related_points)
data['related_points'] = pd.Series(related_points)
data['related_points'] = pd.Series(related_points)
data.to_csv('10minswalk.csv', index=False)







