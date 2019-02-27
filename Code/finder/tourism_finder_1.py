from math import asin, sin, acos, cos, radians, sqrt
import pandas as pd

EARTH_R = 6378.1
#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 0.84
radius = WALKING_DIS / EARTH_R

apartment_list = []
attraction_list = []
gallery_list = []
guest_house_list = []
hostel_list = []
hotel_list = []
information_list = []
motel_list = []
museum_list = []

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
poi_data = pd.read_csv('./osm_data_clean/tourism_clean.csv')

latitudes = data[['Latitude']]
longitudes = data[['Longitude']]
coordinates = poi_data['coordinate']
poi_types = poi_data['poi_type']

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

    counter = 0
    apartment = 0
    attraction = 0
    gallery = 0
    guest_house = 0
    hostel = 0
    hotel = 0
    information = 0
    motel = 0
    museum = 0
    other = 0

    for poi in coordinates:

        print("tourism type:", str(poi_types[counter]))

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
                    if str(poi_types[counter]) == 'apartment':
                        apartment += 1
                    elif str(poi_types[counter]) == 'attraction':
                        attraction += 1
                    elif str(poi_types[counter]) == 'gallery':
                        gallery += 1
                    elif str(poi_types[counter]) == 'guest_house':
                        guest_house += 1
                    elif str(poi_types[counter]) == 'hostel':
                        hostel += 1
                    elif str(poi_types[counter]) == 'hotel':
                        hotel += 1
                    elif str(poi_types[counter]) == 'information':
                        information += 1
                    elif str(poi_types[counter]) == 'motel':
                        motel += 1
                    elif str(poi_types[counter]) == 'museum':
                        museum += 1
                    else:
                        other += 1

        counter += 1

    apartment_list.append(apartment)
    attraction_list.append(attraction)
    gallery_list.append(gallery)
    guest_house_list.append(guest_house)
    hostel_list.append(hostel)
    hotel_list.append(hotel)
    information_list.append(information)
    motel_list.append(motel)
    museum_list.append(museum)
    
data['tourism_apartment'] = pd.Series(apartment_list)
data['tourism_attraction'] = pd.Series(attraction_list)
data['tourism_gallery'] = pd.Series(gallery_list)
data['tourism_guest_house'] = pd.Series(guest_house_list)
data['tourism_hostel'] = pd.Series(hostel_list)
data['tourism_hotel'] = pd.Series(hotel_list)
data['tourism_information'] = pd.Series(information_list)
data['tourism_motel'] = pd.Series(motel_list)
data['tourism_museum'] = pd.Series(museum_list)

data.to_csv('realestatehungary_rent_houses_dis_tourism_10inswalk.csv', index=False)







