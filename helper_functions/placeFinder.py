from googleplaces import GooglePlaces, types, lang
import pandas as pd
import numpy as np

#Create lists for later
lats = []
lons = []
accountings = []
atms = []
bakeries = []
banks = []
bars = []
bus_stations = []
cafes = []
clothing_stores = []
convenience_stores = []
department_stores = []
doctors = []
gas_stations = []
gyms = []
hospitals = []
laundries = []
meal_deliveries = []
meal_takeaways = []
parks = []
pharmacies = []
physiotherapists = []
polices = []
post_offices = []
restaurants = []
schools = []
shopping_malls = []
stores = []
subway_stations = []
supermarkets = []
taxi_stands = []
transit_stations = []
travel_agencies = []

beauty_salons = []
hair_cares = []
book_stores = []
libraries = []
car_repairs = []
car_washes = []
parkings = []
casinos = []
movie_theaters = []
night_clubs = []
real_estate_agencies = []


distances_to_danube = []
distances_to_center = []

WALKING_DISTANCE = 1000
DRIVING_DISTANCE = 8300


#Load .csv data
data = pd.read_csv('realestatehungary_sale_houses_pc1.csv')

latitude = data[['Latitude']]
longitude = data[['Longitude']]

#Convert pandas series to numpy arrays
latitude = latitude.values
longitude = longitude.values

#Searching
google_places = GooglePlaces("MyKey")

for i , j in zip(latitude, longitude):
        #Convert to string
        lat = str(i[0]) 
        lon = str(j[0])
        coordinate = lat + ' ' + lon
        print(lat, lon)
        lats.append(float(lat))
        lons.append(float(lon))

        if float(lat) == 0 or float(lat) == -1:

                accountings.append(-1)
                atms.append(-1)
                bakeries.append(-1)
                banks.append(-1)
                bars.append(-1)
                bus_stations.append(-1)
                cafes.append(-1)
                clothing_stores.append(-1)
                convenience_stores.append(-1)
                department_stores.append(-1)
                doctors.append(-1)
                gas_stations.append(-1)
                gyms.append(-1)
                hospitals.append(-1)
                laundries.append(-1)
                meal_deliveries.append(-1)
                meal_takeaways .append(-1)
                parks.append(-1)
                pharmacies.append(-1)
                physiotherapists.append(-1)
                post_offices.append(-1)
                restaurants.append(-1)
                schools.append(-1)
                shopping_malls.append(-1)
                stores.append(-1)
                subway_stations.append(-1)
                #supermarkets.append(-1)
                taxi_stands.append(-1)
                transit_stations.append(-1)
                travel_agencies.append(-1)

                beauty_salons.append(-1)
                hair_cares.append(-1)
                book_stores.append(-1)
                libraries.append(-1)
                car_repairs.append(-1)
                car_washes.append(-1)
                parkings.append(-1)
                casinos.append(-1)
                movie_theaters.append(-1)
                night_clubs.append(-1)
                real_estate_agencies.append(-1)

        else:

                num_of_accountings = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_ACCOUNTING]).places)
                accountings.append(num_of_accountings)
                print(num_of_accountings)
        
                num_of_atms = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_ATM]).places)
                atms.append(num_of_atms)
                print(num_of_atms)

                num_of_bakeries = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_BAKERY]).places)
                print (num_of_bakeries)
                bakeries.append(num_of_bakeries)

                num_of_banks = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_BANK]).places)
                print (num_of_banks)
                banks.append(num_of_banks)

                num_of_bars = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_BAR]).places)
                print (num_of_bars)
                bars.append(num_of_bars)

                num_of_bus_stations = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_BUS_STATION]).places)
                print (num_of_bus_stations)
                bus_stations.append(num_of_bus_stations)

                num_of_cafes = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_CAFE]).places)
                print (num_of_cafes)
                cafes.append(num_of_cafes)

                num_of_clothing_stores = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_CLOTHING_STORE]).places)
                print (num_of_clothing_stores)
                clothing_stores.append(num_of_clothing_stores)

                num_of_convenience_stores = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_CONVENIENCE_STORE]).places)
                print (num_of_convenience_stores)
                convenience_stores.append(num_of_convenience_stores)

                num_of_department_stores = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_DEPARTMENT_STORE]).places)
                print (num_of_department_stores)
                department_stores.append(num_of_department_stores)

                num_of_doctors = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_DOCTOR]).places)
                print (num_of_doctors)
                doctors.append(num_of_doctors)

                num_of_gyms = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_GYM]).places)
                print (num_of_gyms)
                gyms.append(num_of_gyms)

                num_of_laundries = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_LAUNDRY]).places)
                print (num_of_laundries)
                laundries.append(num_of_laundries)

                num_of_parks = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_PARK]).places)
                print (num_of_parks)
                parks.append(num_of_parks)

                num_of_pharmacies = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_PHARMACY]).places)
                print (num_of_pharmacies)
                laundries.append(num_of_pharmacies)

                num_of_physiotherapists = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_PHYSIOTHERAPIST]).places)
                print (num_of_physiotherapists)
                physiotherapists.append(num_of_physiotherapists)

                num_of_polices = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_POLICE]).places)
                print (num_of_polices)
                polices.append(num_of_polices)

                num_of_post_offices = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_POST_OFFICE]).places)
                print (num_of_post_offices)
                post_offices.append(num_of_post_offices)

                num_of_restaurants = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_RESTAURANT]).places)
                print (num_of_restaurants)
                restaurants.append(num_of_restaurants)

                num_of_schools = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_SCHOOL]).places)
                print (num_of_schools)
                schools.append(num_of_schools)

                num_of_stores = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_STORE]).places)
                print (num_of_stores)
                stores.append(num_of_stores)

                num_of_subway_stations = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_SUBWAY_STATION]).places)
                print (num_of_subway_stations)
                laundries.append(num_of_subway_stations)
                '''
                num_of_supermarkets = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_SUPERMARKET]).places)
                print (num_of_supermarkets)
                supermarkets.append(num_of_supermarkets)'''

                num_of_taxi_stands = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_TAXI_STAND]).places)
                print (num_of_taxi_stands)
                taxi_stands.append(num_of_taxi_stands)

                num_of_transit_stations = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_TRANSIT_STATION]).places)
                print (num_of_transit_stations)
                transit_stations.append(num_of_transit_stations)

                num_of_beauty_salons = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_BEAUTY_SALON]).places)
                print (num_of_beauty_salons)
                beauty_salons.append(num_of_beauty_salons)

                num_of_hair_cares = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_HAIR_CARE]).places)
                print (num_of_hair_cares)
                hair_cares.append(num_of_hair_cares)

                num_of_book_stores= len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_BOOK_STORE]).places)
                print (num_of_book_stores)
                book_stores.append(num_of_book_stores)

                num_of_libraries = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_LIBRARY]).places)
                print (num_of_libraries)
                libraries.append(num_of_libraries)

                num_of_gas_stations = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_GAS_STATION]).places)
                print (num_of_gas_stations)
                gas_stations.append(num_of_gas_stations)

                num_of_shopping_malls = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_SHOPPING_MALL]).places)
                print (num_of_shopping_malls)
                shopping_malls.append(num_of_shopping_malls)

                num_of_hospitals = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_HOSPITAL]).places)
                print (num_of_hospitals)
                hospitals.append(num_of_hospitals)

                num_of_meal_deliveries = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_MEAL_DELIVERY]).places)
                print (num_of_meal_deliveries)
                meal_deliveries.append(num_of_meal_deliveries)

                num_of_meal_takeaways = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_MEAL_TAKEAWAY]).places)
                print (num_of_meal_takeaways)
                meal_takeaways.append(num_of_meal_takeaways)

                num_of_travel_agencies = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_TRAVEL_AGENCY]).places)
                print (num_of_travel_agencies)
                travel_agencies.append(num_of_travel_agencies)

                num_of_car_repairs = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_CAR_REPAIR]).places)
                print (num_of_car_repairs)
                car_repairs.append(num_of_car_repairs)

                num_of_car_washes = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_CAR_WASH]).places)
                print (num_of_car_washes)
                car_washes.append(num_of_car_washes)

                num_of_parkings = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_PARKING]).places)
                print (num_of_parkings)
                parkings.append(num_of_parkings)

                num_of_casinos = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_CASINO]).places)
                print (num_of_casinos)
                casinos.append(num_of_casinos)

                num_of_movie_theaters = len(google_places.nearby_search(location = coordinate, radius = DRIVING_DISTANCE, types = [types.TYPE_MOVIE_THEATER]).places)
                print (num_of_movie_theaters)
                movie_theaters.append(num_of_movie_theaters)

                num_of_night_clubs = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_NIGHT_CLUB]).places)
                print (num_of_night_clubs)
                night_clubs.append(num_of_night_clubs)

                num_of_real_estate_agencies = len(google_places.nearby_search(location = coordinate, radius = WALKING_DISTANCE, types = [types.TYPE_REAL_ESTATE_AGENCY]).places)
                print (num_of_real_estate_agencies)
                real_estate_agencies.append(num_of_real_estate_agencies)

data['Lats'] = pd.Series(lats)
data['Lons'] = pd.Series(lons)
data['Accounting'] = pd.Series(accountings)
data['ATM'] = pd.Series(atms)
data['Backery'] = pd.Series(bakeries)
data['Bank'] = pd.Series(banks)
data['Bar'] = pd.Series(bars)
data['Bus station'] = pd.Series(bus_stations)
data['Cafe'] = pd.Series(cafes)
data['Clothing store'] = pd.Series(clothing_stores)
data['Convenience store'] = pd.Series(convenience_stores)
data['Department store'] = pd.Series(department_stores)
data['Doctor'] = pd.Series(doctors)
data['Gym'] = pd.Series(gyms)
data['Laundry'] = pd.Series(laundries)
data['Park'] = pd.Series(parks)
data['Pharmacy'] = pd.Series(pharmacies)
data['Physiotherapist'] = pd.Series(physiotherapists)
data['Police'] = pd.Series(polices)
data['Post office'] = pd.Series(post_offices)
data['Restaurant'] = pd.Series(restaurants)
data['School'] = pd.Series(schools)
data['Store'] = pd.Series(stores)
data['Subway'] = pd.Series(subway_stations)
#data['Supermarket'] = pd.Series(supermarkets)
data['Taxi stand'] = pd.Series(taxi_stands)
data['Transit station'] = pd.Series(transit_stations)
data['Beauty salon'] = pd.Series(beauty_salons)
data['Hair care'] = pd.Series(hair_cares)
data['Book store'] = pd.Series(book_stores)
data['Library'] = pd.Series(libraries)
data['Gas station'] = pd.Series(gas_stations)
data['Shopping mall'] = pd.Series(shopping_malls)
data['Hospital'] = pd.Series(hospitals)
data['Meal delivery'] = pd.Series(meal_deliveries)
data['Meal takeaway'] = pd.Series(meal_takeaways)
data['Travel agency'] = pd.Series(travel_agencies)
data['Car repair'] = pd.Series(car_repairs)
data['Car wash'] = pd.Series(car_washes)
data['Parking'] = pd.Series(parkings)
data['Casino'] = pd.Series(casinos)
data['Movie theater'] = pd.Series(movie_theaters)
data['Night clubs'] = pd.Series(night_clubs)
data['Real Estate Agency'] = pd.Series(real_estate_agencies)


data.to_csv('realestatehungary_sale_houses_pc1_pl.csv', index=False)




