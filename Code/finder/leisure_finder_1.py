from math import asin, sin, acos, cos, radians, sqrt
import pandas as pd

EARTH_R = 6378.1
#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 2.52
radius = WALKING_DIS / EARTH_R

amusement_arcade_list = []
dance_list = []
dog_park_list = []
fitness_centre_list = []
fitness_station_list = []
garden_list = []
ice_rink_list = []
nature_reserve_list = []
park_list = []
pitch_list = []
playground_list = []
sports_centre_list = []
stadium_list = []
swimming_pool_list = []
track_list = []
water_park_list = []
other_list = []

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
data = pd.read_csv('./MergedData/albert_PcDis.csv')
poi_data = pd.read_csv('./osm_data_clean/leisure_clean.csv')

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
    amusement_arcade = 0
    dance = 0
    dog_park = 0
    fitness_centre = 0
    fitness_station = 0
    garden = 0
    ice_rink = 0
    nature_reserve = 0
    park = 0
    pitch = 0
    playground = 0
    sports_centre = 0
    stadium = 0
    swimming_pool = 0
    track = 0
    water_park = 0
    other = 0

    for poi in coordinates:

        print("leisure type:", str(poi_types[counter]))

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
                    if str(poi_types[counter]) == 'amusement_arcade':
                        amusement_arcade += 1
                    elif str(poi_types[counter]) == 'dance':
                        dance += 1
                    elif str(poi_types[counter]) == 'dog_park':
                        dog_park += 1
                    elif str(poi_types[counter]) == 'fitness_centre':
                        fitness_centre += 1
                    elif str(poi_types[counter]) == 'fitness_station':
                        fitness_station += 1
                    elif str(poi_types[counter]) == 'garden':
                        garden += 1
                    elif str(poi_types[counter]) == 'ice_rink':
                        ice_rink += 1
                    elif str(poi_types[counter]) == 'nature_reserve':
                        nature_reserve += 1
                    elif str(poi_types[counter]) == 'park':
                        park += 1
                    elif str(poi_types[counter]) == 'pitch':
                        pitch += 1
                    elif str(poi_types[counter]) == 'playground':
                        playground += 1
                    elif str(poi_types[counter]) == 'sports_centre':
                        sports_centre += 1
                    elif str(poi_types[counter]) == 'stadium':
                        stadium += 1
                    elif str(poi_types[counter]) == 'swimming_pool':
                        swimming_pool += 1
                    elif str(poi_types[counter]) == 'track':
                        track += 1
                    elif str(poi_types[counter]) == 'water_park':
                        water_park += 1
                    else:
                        other += 1
                        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&This is Others&&&&&&&&&&&&&&&&&&&&&&&&&&&&7')

        counter += 1

    amusement_arcade_list.append(amusement_arcade)
    dance_list.append(dance)
    dog_park_list.append(dog_park)
    fitness_centre_list.append(fitness_centre)
    fitness_station_list.append(fitness_station)
    garden_list.append(garden)
    ice_rink_list.append(ice_rink)
    nature_reserve_list.append(nature_reserve)
    park_list.append(park)
    pitch_list.append(pitch)
    playground_list.append(playground)
    sports_centre_list.append(sports_centre)
    stadium_list.append(stadium)
    swimming_pool_list.append(swimming_pool)
    track_list.append(track)
    water_park_list.append(water_park)
    other_list.append(other)
    
data['leisure_amusement_arcade'] = pd.Series(amusement_arcade_list)
data['leisure_dance'] = pd.Series(dance_list)
data['leisure_dog_park'] = pd.Series(dog_park_list)
data['leisure_fitness_centre'] = pd.Series(fitness_centre_list)
data['leisure_fitness_station'] = pd.Series(fitness_station_list)
data['leisure_garden'] = pd.Series(garden_list)
data['leisure_ice_rink'] = pd.Series(ice_rink_list)
data['leisure_nature_reserve'] = pd.Series(nature_reserve_list)
data['leisure_park'] = pd.Series(park_list)
data['leisure_pitch'] = pd.Series(pitch_list)
data['leisure_playground'] = pd.Series(playground_list)
data['leisure_sports_centre'] = pd.Series(sports_centre_list)
data['leisure_stadium'] = pd.Series(stadium_list)
data['leisure_swimming_pool'] = pd.Series(park_list)
data['leisure_track'] = pd.Series(track_list)
data['leisure_Coworking_space'] = pd.Series(coworking_space_list)
data['leisure_water_park'] = pd.Series(water_park_list)
data['leisure_Others'] = pd.Series(other_list)
data.to_csv('albert_PcDis_leisure_30minswalk.csv', index=False)







