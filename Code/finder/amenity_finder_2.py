from math import asin, sin, acos, cos, radians, sqrt
import pandas as pd

EARTH_R = 6378.1
#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 1.68
radius = WALKING_DIS / EARTH_R

lats_max = []
lats_min = []
lons_max = []
lons_min = []

sustenance_list = []
school_list = []
education_list = []
financial_list = []
healthcare_list = []
arts_list = []
entertainment_list = []
religion_list = []
police_list = []
government_list = []
vending_machine_list = []
transportation_bicycle_list = []
transportation_car_list = []
fuel_list = []
parking_list = []
coworking_space_list = []
recycling_list = []
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
data = pd.read_csv('./real_sale_apar/real_sale_apar_33.csv')
poi_data = pd.read_csv('./osm_data_clean/amenity_clean.csv')

latitudes = data[['Latitude']]
longitudes = data[['Longitude']]
coordinates = poi_data['coordinate']
poi_types = poi_data['amenity_types']

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
    lats_max.append(lat_max)
    print("lat min:", lat_min)
    lats_min.append(lat_min)

    lon_max, lon_min = find_lon(lat, lon)
    print("lon max:", lon_max)
    lons_max.append(lon_max)
    print("lon min:", lon_min)
    lons_min.append(lon_min)

    counter = 0
    sustenance = 0
    school = 0
    education = 0
    financial = 0
    healthcare = 0
    arts = 0
    entertainment = 0
    religion= 0
    police = 0
    government = 0
    transportation_bicycle = 0
    vending_machine = 0
    transportation_car = 0
    fuel = 0
    parking = 0
    coworking_space = 0
    recycling = 0
    other = 0

    for poi in coordinates:

        print("amenity type:", str(poi_types[counter]))

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
                    if str(poi_types[counter]) == 'Sustenance':
                        sustenance += 1
                    elif str(poi_types[counter]) == 'School':
                        school += 1
                    elif str(poi_types[counter]) == 'Education':
                        education += 1
                    elif str(poi_types[counter]) == 'Financial':
                        financial += 1
                    elif str(poi_types[counter]) == 'Healthcare':
                        healthcare += 1
                    elif str(poi_types[counter]) == 'Arts':
                        arts += 1
                    elif str(poi_types[counter]) == 'Entertainment':
                        entertainment += 1
                    elif str(poi_types[counter]) == 'Religion':
                        religion += 1
                    elif str(poi_types[counter]) == 'Police':
                        police += 1
                    elif str(poi_types[counter]) == 'Government':
                        government += 1
                    elif str(poi_types[counter]) == 'Vending Machine':
                        vending_machine += 1
                    elif str(poi_types[counter]) == 'Transportation: Bicycle':
                        transportation_bicycle += 1
                    elif str(poi_types[counter]) == 'Transportation: Car':
                        transportation_car += 1
                    elif str(poi_types[counter]) == 'Fuel Station':
                        fuel += 1
                    elif str(poi_types[counter]) == 'Parking':
                        parking += 1
                    elif str(poi_types[counter]) == 'Coworking Space':
                        coworking_space += 1
                    elif str(poi_types[counter]) == 'Recycling':
                        recycling += 1
                    else:
                        other += 1
                        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&This is Others&&&&&&&&&&&&&&&&&&&&&&&&&&&&7')

        counter += 1

    sustenance_list.append(sustenance)
    school_list.append(school)
    education_list.append(education)
    financial_list.append(financial)
    healthcare_list.append(healthcare)
    arts_list.append(arts)
    entertainment_list.append(entertainment)
    religion_list.append(religion)
    police_list.append(police)
    government_list.append(government)
    vending_machine_list.append(vending_machine)
    transportation_bicycle_list.append(transportation_bicycle)
    transportation_car_list.append(transportation_car)
    fuel_list.append(fuel)
    parking_list.append(parking)
    coworking_space_list.append(coworking_space)
    recycling_list.append(recycling)
    other_list.append(other)

data['Amenity: Sustenance'] = pd.Series(sustenance_list)
data['Amenity: School'] = pd.Series(school_list)
data['Amenity: Education'] = pd.Series(education_list)
data['Amenity: Financial'] = pd.Series(financial_list)
data['Amenity: Healthcare'] = pd.Series(healthcare_list)
data['Amenity: Arts'] = pd.Series(arts_list)
data['Amenity: Entertainment'] = pd.Series(entertainment_list)
data['Amenity: Religion'] = pd.Series(religion_list)
data['Amenity: police'] = pd.Series(police_list)
data['Amenity: Government'] = pd.Series(government_list)
data['Amenity: Vending_machine'] = pd.Series(vending_machine_list)
data['Amenity: Transportation_bicycle'] = pd.Series(transportation_bicycle_list)
data['Amenity: Transportation_car'] = pd.Series(transportation_car_list)
data['Amenity: Fuel'] = pd.Series(police_list)
data['Amenity: Parking'] = pd.Series(parking_list)
data['Amenity: Coworking_space'] = pd.Series(coworking_space_list)
data['Amenity: Recycling'] = pd.Series(recycling_list)
data['Amenity: Others'] = pd.Series(other_list)
data.to_csv('real_sale_apar_33_amenity_20minswalk.csv', index=False)







