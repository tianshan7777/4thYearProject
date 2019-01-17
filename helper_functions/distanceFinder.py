from math import radians, cos, sin, asin, acos, sqrt, atan2, degrees, pi, fabs
import pandas as pd
import numpy as np

EARTH_RADIUS = 6371

lats = []
lons = []

distance_danube = []
distance_centre = []
distance_keleti = []
distance_nyugati = []
distance_deli = []
distance_bud = []

danube1_lat = 0.831005396986
danube1_lon = 0.333341376315
danube2_lat = 0.826810253783
danube2_lon = 0.330958251395

centre_lat = 47.496523
centre_lon  = 19.050703
keleti_lat = 47.501399
keleti_lon = 19.083842
nyugati_lat = 47.511605
nyugati_lon = 19.057232
deli_lat = 47.501400
deli_lon = 19.024618
bud_lat = 47.438604
bud_lon = 19.252274

#Calculate distance between two pointss
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

#Calculate the distance from a point to the line
def distance_to_danube(lat, lon):
	lat, lon = map(radians, [lat, lon])

	#bearing between danube1 and the property
	y = sin(lon - danube1_lon) * cos(lat)
	x = cos(danube1_lat) * sin(lat) - sin(danube1_lat) * cos(lat) * cos(lat - danube1_lat)
	bearing1 = atan2(y, x)
	bearing1 = 2 * pi - ((bearing1 + 2 * pi) % (2 * pi))
	print(bearing1)

	y2 = sin(danube2_lon - danube1_lon) * cos(danube2_lat)
	x2 = cos(danube1_lat) * sin(danube2_lat) - sin(danube1_lat) * cos(danube2_lat) * cos(danube2_lat - danube1_lat)
	bearing2 = atan2(y2, x2)
	bearing2 = 2 * pi  - ((bearing2 + 2 * pi ) % (2 * pi ))
	print(bearing2)

	dLon = lon - danube1_lon

	distance = acos(sin(danube1_lat) * sin(lat)+cos(danube1_lat)*cos(lat)*cos(dLon)) * EARTH_RADIUS
	min_distance = fabs(asin(sin(distance/EARTH_RADIUS)*sin(bearing1 - bearing2)) * EARTH_RADIUS)

	return min_distance

#Load .csv data
data = pd.read_csv('towerbudapest_longtermrent_apartments_pc.csv')

latitude = data[['Latitude']]
longitude = data[['Longitude']]

#Convert pandas series to numpy arrays
latitude = latitude.values
longitude = longitude.values

for i , j in zip(latitude, longitude):
		#Convert to float
        lat = float(i[0]) 
        lon = float(j[0])
        print(lat, lon)
        lats.append(lat)
        lons.append(lon)

        d1 = distance_to_danube(lat, lon)
        print(d1)
        distance_danube.append(d1)

        d2 = haversine(lon, lat, centre_lon, centre_lat)
        print(d2)
        distance_centre.append(d2)

        d3 = haversine(lon, lat, keleti_lon, keleti_lat)
        print(d3)
        distance_keleti.append(d3)

        d4 = haversine(lon, lat, nyugati_lon, nyugati_lat)
        print(d4)
        distance_nyugati.append(d4)

        d5 = haversine(lon, lat, deli_lon, deli_lat)
        print(d5)
        distance_deli.append(d5)

        d6 = haversine(lon, lat, bud_lon, bud_lat)
        print(d6)
        distance_bud.append(d6)

data['Lats'] = pd.Series(lats)
data['Lons'] = pd.Series(lons)
data['Distace to Danube'] = pd.Series(distance_danube)
data['Distace to City Centre'] = pd.Series(distance_centre)
data['Distace to Keleti'] = pd.Series(distance_keleti)
data['Distace to Nyugati'] = pd.Series(distance_nyugati)
data['Distance to Deli'] = pd.Series(distance_deli)
data['Distance to Airport'] = pd.Series(distance_bud)


data.to_csv('towerbudapest_longtermrent_apartments_dis.csv', index=False)








