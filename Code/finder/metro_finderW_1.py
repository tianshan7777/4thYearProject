from math import asin, sin, acos, cos, radians, sqrt
import pandas as pd

EARTH_R = 6378.1
#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 2.52
radius = WALKING_DIS / EARTH_R


metro_list = []

#Calculate distance between two pointss
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

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

#Load .csv data
data = pd.read_csv('./MergedData/realestatehungary_rent_houses_dis.csv')
poi_data = pd.read_csv('./osm_data_clean/metro_station_clean.csv')

latitudes = data[['Latitude']]
longitudes = data[['Longitude']]
coordinates = poi_data['coordinate']

#Conver pandas onject to numpy array
latitudes = latitudes.values
longitudes = longitudes.values

#Iterate through
for i, j in zip(latitudes, longitudes):

    #Convert to float
    lat = float(i[0]) 
    lon = float(j[0])
    print("original:", lat, lon)

    lat, lon = map(radians, [lat, lon])
    print("in radians:", lat, lon)

    lat_max, lat_min = find_lat(lat)
    print("lat max:", lat_max)
    print("lat min:", lat_min)

    lon_max, lon_min = find_lon(lat, lon)
    print("lon max:", lon_max)
    print("lon min:", lon_min)

    metro = 0

    for poi in coordinates:

        print("poi:", poi)

        point = poi.split(',')
        #Convert to float
        point[0] = radians(float(point[0]))
        point[1] = radians(float(point[1]))
        print(point)

        if (point[1] < lat_max and  point[1] > lat_min):
            if (point[0] < lon_max and point[0] > lon_min):
                print("_____________within area_______________:", point)

                haversine_dis = haversine(point[0], point[1], lon, lat)
                print("==========Haversine Calculated===========:", haversine_dis)

                if haversine_dis <= WALKING_DIS:
                    print("******************Accept*******************")
                    metro += 1

    metro_list.append(metro)

data['metro_station'] = pd.Series(metro_list)
data.to_csv('realestatehungary_rent_houses_dis_dis_metro_30minswalk.csv', index=False)







