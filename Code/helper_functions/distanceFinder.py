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
distance_eco = []
distance_crime = []
distance_uni1 = []
distance_uni2 = []
distance_uni3 = []
distance_uni4 = []
distance_uni5 = []
distance_uni6 = []
distance_uni7 = []
distance_uni8 = []
distance_uni9 = []
distance_uni10 = []
distance_uni11 = []
distance_uni12 = []
distance_uni13 = []
distance_uni14 = []
distance_uni15 = []
distance_uni16 = []
distance_uni17 = []
distance_uni18 = []
distance_uni19 = []
distance_uni20 = []
distance_uni21 = []
distance_uni22 = []
distance_uni23 = []

danube1_lat = 47.613102
danube1_lon = 19.099054
danube2_lat = 47.505876
danube2_lon = 19.042173
danube3_lat = 47.468786
danube3_lon = 19.067475
danube4_lat = 47.389489
danube4_lon = 19.013785
danube5_lat = 47.372738
danube5_lon = 18.962511

#city center
centre_lat = 47.496523
centre_lon  = 19.050703

#train stations
keleti_lat = 47.501399
keleti_lon = 19.083842
nyugati_lat = 47.511605
nyugati_lon = 19.057232
deli_lat = 47.501400
deli_lon = 19.024618

#airport
bud_lat = 47.438604
bud_lon = 19.252274

#eco cluster
eco1_lat = 47.480566
eco1_lon = 19.066220
eco2_lat = 47.513699
eco2_lon = 19.052038

#crime
crime_lat = 47.500000
crime_lon = 19.063473

uni1_lat = 47.495310
uni1_lon = 19.066199
uni2_lat = 47.492289
uni2_lon = 19.063975
uni3_lat = 47.492289
uni3_lon = 19.063975
uni4_lat = 47.481685
uni4_lon = 19.055525
uni5_lat = 47.508151
uni5_lon = 19.124532
uni6_lat = 47.493670
uni6_lon = 19.070319
uni7_lat = 47.506396
uni7_lon = 19.135193
uni8_lat = 47.500628
uni8_lon = 19.049594
uni9_lat = 47.486353
uni9_lon = 19.057894
uni10_lat = 47.481863
uni10_lon = 19.072607
uni11_lat = 47.503298
uni11_lon = 19.064364
uni12_lat = 47.507556
uni12_lon = 19.067052
uni13_lat = 47.562145
uni13_lon = 19.053866
uni15_lat = 47.489138
uni15_lon = 19.061707
uni16_lat = 47.519134
uni16_lon = 19.114884
uni18_lat = 47.516669
uni18_lon = 18.991171
uni19_lat = 47.481841
uni19_lon = 19.085383 
uni20_lat = 47.534178
uni20_lon = 19.034398
uni21_lat = 47.491841
uni21_lon = 19.065751
uni22_lat = 47.487433
uni22_lon = 19.067518
uni23_lat = 47.493458
uni23_lon = 19.024270


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
def distance_to_danube(dabube1_lat, danube1_lon, danube2_lat, danube2_lon, lat, lon):
	dabube1_lat, danube1_lon, danube2_lat, danube2_lon, lat, lon = map(radians, [dabube1_lat, danube1_lon, danube2_lat, danube2_lon, lat, lon])

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

        list_shortest = []

        d11 = distance_to_danube(dabube1_lat, danube1_lon, danube2_lat, danube2_lon, lat, lon)
        print(d11)
        list_shortest.append(d11)

        d12 = distance_to_danube(dabube2_lat, danube2_lon, danube3_lat, danube3_lon, lat, lon)
        print(d12)
        list_shortest.append(d12)

        d13 = distance_to_danube(dabube3_lat, danube3_lon, danube4_lat, danube4_lon, lat, lon)
        print(d13)
        list_shortest.append(d13)

        d14 = distance_to_danube(dabube4_lat, danube4_lon, danube5_lat, danube5_lon, lat, lon)
        print(d14)
        list_shortest.append(d14)

        print(min(list_shortest))
        distance_danube.append(min(list_shortest))

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

        d7 = haversine(lon, lat, crime_lon, crime_lat)
        print(d7)
        distance_crime.append(d7)

        d8 = haversine(lon, lat, uni1_lon, uni1_lat)
        print(d8)
        distance_uni1.append(d8)

        d9 = haversine(lon, lat, uni2_lon, uni2_lat)
        print(d9)
        distance_uni2.append(d9)

        d10 = haversine(lon, lat, uni3_lon, uni3_lat)
        print(d10)
        distance_uni3.append(d10)

        d11 = haversine(lon, lat, uni4_lon, uni4_lat)
        print(d11)
        distance_uni4.append(d11)

        d12 = haversine(lon, lat, uni5_lon, uni5_lat)
        print(d12)
        distance_uni5.append(d12)

        d13 = haversine(lon, lat, uni6_lon, uni6_lat)
        print(d13)
        distance_uni6.append(d13)

        d14 = haversine(lon, lat, uni7_lon, uni7_lat)
        print(d14)
        distance_uni7.append(d14)

        d15 = haversine(lon, lat, uni8_lon, uni8_lat)
        print(d15)
        distance_uni8.append(d15)

        d16 = haversine(lon, lat, uni9_lon, uni9_lat)
        print(d16)
        distance_uni9.append(d16)

        d17 = haversine(lon, lat, uni10_lon, uni10_lat)
        print(d17)
        distance_uni10.append(d17)

        d18 = haversine(lon, lat, uni11_lon, uni11_lat)
        print(d18)
        distance_uni11.append(d18)

        d19 = haversine(lon, lat, uni12_lon, uni12_lat)
        print(d19)
        distance_uni12.append(d19)

        d20 = haversine(lon, lat, uni13_lon, uni13_lat)
        print(d20)
        distance_uni13.append(d20)

        d21 = haversine(lon, lat, uni14_lon, uni14_lat)
        print(d21)
        distance_uni14.append(d21)

        d22 = haversine(lon, lat, uni15_lon, uni15_lat)
        print(d22)
        distance_uni15.append(d22)

        d23 = haversine(lon, lat, uni16_lon, uni16_lat)
        print(d23)
        distance_uni16.append(d23)

        d24 = haversine(lon, lat, uni17_lon, uni17_lat)
        print(d24)
        distance_uni17.append(d24)

        d25 = haversine(lon, lat, uni18_lon, uni18_lat)
        print(d25)
        distance_uni18.append(d25)

        d26 = haversine(lon, lat, uni19_lon, uni19_lat)
        print(d26)
        distance_uni19.append(d26)

        d27 = haversine(lon, lat, uni20_lon, uni20_lat)
        print(d27)
        distance_uni20.append(d27)

        d28 = haversine(lon, lat, uni21_lon, uni21_lat)
        print(d28)
        distance_uni21.append(d28)

        d29 = haversine(lon, lat, uni22_lon, uni22_lat)
        print(d29)
        distance_uni22.append(d29)

        d30 = haversine(lon, lat, uni23_lon, uni23_lat)
        print(d30)
        distance_uni23.append(d30)

        d31 = distance_to_danube(eco1_lat, eco1_lon, eco2_lat, eco2_lon, lat, lon)
        print(d31)
        distance_eco.append(d31)

data['Lats'] = pd.Series(lats)
data['Lons'] = pd.Series(lons)
data['Distace to Danube'] = pd.Series(distance_danube)
data['Distace to City Centre'] = pd.Series(distance_centre)
data['Distace to Keleti'] = pd.Series(distance_keleti)
data['Distace to Nyugati'] = pd.Series(distance_nyugati)
data['Distance to Deli'] = pd.Series(distance_deli)
data['Distance to Airport'] = pd.Series(distance_bud)
data['Distance to Eco Zone'] = pd.Series(distance_eco)
data['Distance to Crime Pot'] = pd.Series(distance_crime)
data['Distance to Uni1'] = pd.Series(distance_uni1)
data['Distance to Uni2'] = pd.Series(distance_uni2)
data['Distance to Uni3'] = pd.Series(distance_uni3)
data['Distance to Uni4'] = pd.Series(distance_uni4)
data['Distance to Uni5'] = pd.Series(distance_uni5)
data['Distance to Uni6'] = pd.Series(distance_uni6)
data['Distance to Uni7'] = pd.Series(distance_uni7)
data['Distance to Uni8'] = pd.Series(distance_uni8)
data['Distance to Uni9'] = pd.Series(distance_uni9)
data['Distance to Uni10'] = pd.Series(distance_uni10)
data['Distance to Uni11'] = pd.Series(distance_uni11)
data['Distance to Uni12'] = pd.Series(distance_uni12)
data['Distance to Uni13'] = pd.Series(distance_uni13)
data['Distance to Uni14'] = pd.Series(distance_uni14)
data['Distance to Uni15'] = pd.Series(distance_uni15)
data['Distance to Uni16'] = pd.Series(distance_uni16)
data['Distance to Uni17'] = pd.Series(distance_uni17)
data['Distance to Uni18'] = pd.Series(distance_uni18)
data['Distance to Uni19'] = pd.Series(distance_uni19)
data['Distance to Uni20'] = pd.Series(distance_uni20)
data['Distance to Uni21'] = pd.Series(distance_uni21)
data['Distance to Uni22'] = pd.Series(distance_uni22)
data['Distance to Uni23'] = pd.Series(distance_uni23)


data.to_csv('towerbudapest_longtermrent_apartments_dis.csv', index=False)








