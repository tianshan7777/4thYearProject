
import pandas as pd
import googlemaps
import numpy as np

#Lists for saving full addr, postalcode and district info
full_addrs = []
postcodes = []
districts = []
lats = []
lons = []

#Load .csv data
data = pd.read_csv('realestatehungary_rent_apas.csv')

latitude = data[['Latitude']]
longitude = data[['Longitude']]
#print(lat.loc[[0]])

#Convert pandas series to numpy arrays
latitude = latitude.values
longitude = longitude.values
#print(lat[0])
#print(type(lat))
#print(str(lat[0]))
#print(type(str(lat[0])))

#Reverse geocoding
gmaps = googlemaps.Client(key='AIzaSyDRgjNLfEQVB8t2WvZ2XqXDqAgrSpTOoeE')

for i , j in zip(latitude, longitude):

		#print(type(str(i)))
		#Convert to float
		lat = float(i[0]) 
		lon = float(j[0])
		print(lat, lon)
		lats.append(lat)
		lons.append(lon)

		reverse_geocode_result = gmaps.reverse_geocode((lat,lon))

		#Convert dict to string
		list_of_comp = str(reverse_geocode_result).split(',')
		#Find index
		if " 'types': ['postal_code']}]" in list_of_comp:
			postcode_index = list_of_comp.index(" 'types': ['postal_code']}]")-1
			#Format: e.g. " 'short_name': '1111'"
			postcode = list_of_comp[postcode_index].replace(' ', '').replace("'", '').split(':')[-1]
			print(postcode)
			postcodes.append(int(postcode))

			#Find district
			district = list(postcode)[1] + list(postcode)[2]
			districts.append(int(district))
			print(district)
		else:
			lats.append(-1)
			lons.append(-1)
			postcodes.append(-1)
			districts.append(-1)

#print(districts)
#print(postcodes)

#Create new columns for full addr, postcode and district
data['Lats'] = pd.Series(lats)
data['Lons'] = pd.Series(lons)
data['Postcode'] = pd.Series(postcodes)
data['District'] = pd.Series(districts)

data.to_csv('output.csv', index=False)	




