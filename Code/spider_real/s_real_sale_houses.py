#This is a spider for web https://realestatehungary.hu/
#properties for sale
#type: houses

from requests import get
from bs4 import BeautifulSoup
from time import time, sleep
from warnings import warn
from random import randint
from IPython.core.display import clear_output
from mpl_toolkits import mplot3d
#Once this submodule is imported, a three-dimensional axes can be created by passing the keyword projection='3d' to any of the normal axes creation routines:

import re
import pandas as pd 
#For converting the district numbers into int
import roman
import matplotlib.pyplot as plt

#Changing the URL's parameter
pages = [str(i) for i in range(1, 615)]

#Lists to store the scraped data in
#property types
houses = []
apartments = []
rooms = []
#Prices
prices_HUF = []
prices_euro = []
prices_per_sqm_HUF = []
prices_per_sqm_euro = []
#
district_1 = []
district_2 = []
district_3 = []
district_4 = []
district_5 = []
district_6 = []
district_7 = []
district_8 = []
district_9 = []
district_10 = []
district_11 = []
district_12 = []
district_13 = []
district_14 = []
district_15 = []
district_16 = []
district_17 = []
district_18 = []
district_19 = []
district_20 = []
district_21 = []
district_22 = []
district_23 = []
streets = []
#locations = []
transportations = []
sizes = []
num_of_rooms = []
whole_rooms = []
half_rooms = []
#properties_detail = []
name_of_buildings = []
#property condition
condition_of_properties = []
newly_built = []
good_condition = []
renovated = []
medium_condition = []
needs_renovation = []
mint = []
#Utility levels
utility_levels = []
double_comfort = []
luxury = []
full_comfort = []
#
energies = []
floors = []
floors_of_the_building = []
elevators = []
ceiling_heights = []
#heating
heatings = []
gas = []
wall_heating = []
combination_boiler = []
ceiling_heating = []
#air conditioner
air_conditioners = []
air_conditioning = []
accessibiles = []
#Bathroom
bathrooms = []
bathroom_separate = []
bathroom_together = []
#
orientations = []
views = []
views_garden = []
views_panoramic = []
views_else = []
barconies = []
gardens = []
attics = []
parkings = []
latitudes = []
longitudes = []

def district_filter(district_num):
	if district_num == 1:
		district_1.append(1)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 2:
		district_1.append(0)
		district_2.append(1)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 3:
		district_1.append(0)
		district_2.append(0)
		district_3.append(1)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 4:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(1)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 5:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(1)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 6:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(1)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 7:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(1)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 8:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(1)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 9:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(1)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 10:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(1)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 11:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(1)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 12:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(1)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 13:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(1)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 14:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(1)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 15:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(1)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 16:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(1)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 17:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(1)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(1)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 18:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(1)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 19:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(1)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 20:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(1)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 21:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(1)
		district_22.append(0)
		district_23.append(0)
	elif district_num == 22:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(1)
		district_23.append(0)
	elif district_num == 23:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(1)
	else:
		district_1.append(0)
		district_2.append(0)
		district_3.append(0)
		district_4.append(0)
		district_5.append(0)
		district_6.append(0)
		district_7.append(0)
		district_8.append(0)
		district_9.append(0)
		district_10.append(0)
		district_11.append(0)
		district_12.append(0)
		district_13.append(0)
		district_14.append(0)
		district_15.append(0)
		district_16.append(0)
		district_17.append(0)
		district_18.append(0)
		district_19.append(0)
		district_20.append(0)
		district_21.append(0)
		district_22.append(0)
		district_23.append(0)
#Define strings used when the value is not available
#Use -1 to represent the none value
NOTFOUND = -1
#Use 0 to represent NO/NOT FURNISHED/NOT EQUIPPED
NO = 0
#Use 1 to represent YES/FURNISHED/EQUIPPED
YES = 1
#Use 0.5 to represent partly furnished/OPTIONAL
PARTLYFURNISHED = 0.5
#HUF to euros
HUF_EURO = 0.0031
#Mornitoring the loop as it is still going
start_time = time()
requests = 0

#Scrape the pages
#For every page in range 1 to 4
for page in pages:
	#print('entre page')
	#Make a request
	response = get('https://realestatehungary.hu/szukites/elado+haz+budapest?page=' + page)

	#Parse the html with a BeautifulSoup object
	page_html = BeautifulSoup(response.text, 'html.parser')

	#print(response.text)

	containers = page_html.find_all('div', class_ = 'listing js-listing ')

	#print(containers)

	#For each property
	for container in containers:

		#print('enter container')

		#type of properties
		houses.append(1)
		apartments.append(0)
		rooms.append(0)

		#Save and print the child web
		sub_url = str(container.a['href'])
		sub_url = 'https://realestatehungary.hu' + sub_url
		print(sub_url)

		#The price
		if container.find('div', class_ = 'price') is not None:
			if container.find('div', class_ = 'price').text is not None:
				price = container.find('div', class_ = 'price').text
				print('price:', price)
				prices_HUF.append(price)
			else:
				prices_HUF.append(NOTFOUND)
				print('Price not found 2')
		else:
			prices_HUF.append(NOTFOUND)
			print('Price not found 1')

		#Price per sqm
		if container.find('div', class_ = 'price--sqm') is not None:
			price_per_sqm = container.find('div', class_ = 'price--sqm').text
			#print('price per sqm:', price_per_sqm)
			prices_per_sqm_HUF.append(price_per_sqm)
		else:
			prices_per_sqm_HUF.append(NOTFOUND)

		#District and street
		if container.find('div', class_ = 'listing__address') is not None:
			address = container.find('div', class_ = 'listing__address').text
			#print(address)
			district = str(address.split(',', 1)[1])
			street = address.split(',', 1)[0]
			#print('district:', district)
			#print('street；', street)
			
			streets.append(street)

			district = district.replace(' ', '').replace('.district', '')
			if district == 'Budakeszi' or 'Pomáz' or 'Érd' or 'Dunakeszi':
				district_1.append(0)
				district_2.append(0)
				district_3.append(0)
				district_4.append(0)
				district_5.append(0)
				district_6.append(0)
				district_7.append(0)
				district_8.append(0)
				district_9.append(0)
				district_10.append(0)
				district_11.append(0)
				district_12.append(0)
				district_13.append(0)
				district_14.append(0)
				district_15.append(0)
				district_16.append(0)
				district_17.append(0)
				district_18.append(0)
				district_19.append(0)
				district_20.append(0)
				district_21.append(0)
				district_22.append(0)
				district_23.append(0)
			else:
				district_num = roman.fromRoman(district)
				#print(district_num)
				district_filter(district_num)
		else:
			streets.append(NOTFOUND)
			district_filter(0)

		#Size
		if container.find('div', class_ = 'listing__parameter listing__data--area-size') is not None:
			size = container.find('div', class_ = 'listing__parameter listing__data--area-size').text
			sizes.append(size)
		else:
			sizes.append(NOTFOUND)

		#Number of rooms
		if container.find('div', class_ = 'listing__parameter listing__data--room-count') is not None:
			num_of_room = container.find('div', class_ = 'listing__parameter listing__data--room-count').text.strip()
			num_of_rooms.append(num_of_room)
			list_of_words = num_of_room.split(' ')
			if '+' in list_of_words:
				#print('NUMBER OF ROOMS:', list_of_words)
				#print(list_of_words[0].strip())
				#print(list_of_words[2].strip())
				whole_rooms.append(int(list_of_words[0].strip()))
				half_rooms.append(int(list_of_words[2].strip()))
			elif 'half' in list_of_words:
				whole_rooms.append(0)
				half_rooms.append(int(list_of_words[list_of_words.index('half')-1].strip()))
				#print('NUMBER OF half ROOMS:', list_of_words[list_of_words.index('+')+1])
			elif 'room' in list_of_words:
				whole_rooms.append(int(list_of_words[list_of_words.index('room')-1].strip()))
				half_rooms.append(0)
				#print('NUMBER OF whole ROOMS:', list_of_words[list_of_words.index('room')-1])
			else:
				whole_rooms.append(NOTFOUND)
				half_rooms.append(NOTFOUND)
		else:
			num_of_rooms.append(NOTFOUND)
			whole_rooms.append(NOTFOUND)
			half_rooms.append(NOTFOUND)

		sub_response = get(sub_url)

		sub_page_html = BeautifulSoup(sub_response.text, 'html.parser')

		#More details
		if sub_page_html.find('div', class_ = 'paramterers') is not None:
			details = sub_page_html.find('div', class_ = 'paramterers').findAll('td')
			detail = ''
			for item in details:
				detail =  detail + ',' + item.text
			#print('details: ', detail)
			list_of_words = detail.split(',')
			#print('list of words:', list_of_words)
			if 'Name of Residential complex' in list_of_words:
				name_of_building = list_of_words[list_of_words.index('Name of Residential complex')+1]
				#print('Name of Residential complex:', name_of_building)
				name_of_buildings.append(name_of_building)
			else:
				name_of_buildings.append(NOTFOUND)
				#print('Name of Residential complex not found')

			if 'Condition of property' in list_of_words:
				condition = list_of_words[list_of_words.index('Condition of property')+1].strip()
				#print('Condition of property:', condition)
				condition_of_properties.append(condition)
				if condition == 'newly built':
					newly_built.append(1)
					good_condition.append(0)
					renovated.append(0)
					medium_condition.append(0)
					needs_renovation.append(0)
					mint.append(0)
				elif condition == 'in good condition':
					newly_built.append(0)
					good_condition.append(1)
					renovated.append(0)
					medium_condition.append(0)
					needs_renovation.append(0)
					mint.append(0)
				elif condition == 'renovated':
					newly_built.append(0)
					good_condition.append(0)
					renovated.append(1)
					medium_condition.append(0)
					needs_renovation.append(0)
					mint.append(0)
				elif condition == 'in medium condition':
					newly_built.append(0)
					good_condition.append(0)
					renovated.append(0)
					medium_condition.append(1)
					needs_renovation.append(0)
					mint.append(0)
				elif condition == 'needs renovation':
					newly_built.append(0)
					good_condition.append(0)
					renovated.append(0)
					medium_condition.append(0)
					needs_renovation.append(1)
					mint.append(0)
				elif condition == 'mint':
					newly_built.append(0)
					good_condition.append(0)
					renovated.append(0)
					medium_condition.append(0)
					needs_renovation.append(0)
					mint.append(1)
				else:
					newly_built.append(0)
					good_condition.append(0)
					renovated.append(0)
					medium_condition.append(0)
					needs_renovation.append(0)
					mint.append(0)
			else:
				condition_of_properties.append(NOTFOUND)
				newly_built.append(0)
				good_condition.append(0)
				renovated.append(0)
				medium_condition.append(0)
				needs_renovation.append(0)
				mint.append(0)
				#print('condition not found')

			if 'Utility level' in list_of_words:
				utility = list_of_words[list_of_words.index('Utility level')+1].strip()
				#print('Utility level:', utility)
				utility_levels.append(utility)
				if utility == 'double comfort':
					double_comfort.append(1)
					full_comfort.append(0)
					luxury.append(0)
				elif utility == 'full comfort':
					double_comfort.append(0)
					full_comfort.append(1)
					luxury.append(0)
				elif utility == 'luxury':
					double_comfort.append(0)
					full_comfort.append(0)
					luxury.append(1)
				else:
					double_comfort.append(0)
					full_comfort.append(0)
					luxury.append(0)
			else:
				utility_levels.append(NOTFOUND)
				double_comfort.append(0)
				full_comfort.append(0)
				luxury.append(0)
				#print('Utility level not found')

			if 'Energy Performance Certificate' in list_of_words:
				energy = list_of_words[list_of_words.index('Energy Performance Certificate')+1]
				#print('Energy Performance Certificate:', energy)
				energies.append(energy)
			else:
				energies.append(NOTFOUND)
				#print('Energy Performance Certificate not found')

			if 'Floor' in list_of_words:
				t = list_of_words[list_of_words.index('Floor')+1]
				#print('Floor:', t)
				floors.append(t)
			else:
				floors.append(NOTFOUND)
				#print('Floor not found')

			if 'Floors of the building' in list_of_words:
				t = list_of_words[list_of_words.index('Floors of the building')+1]
				#print('Floors of the building:', t)
				floors_of_the_building.append(t)
			else:
				floors_of_the_building.append(NOTFOUND)
				#print('Floors of the building not found')

			if 'Elevator' in list_of_words:
				t = list_of_words[list_of_words.index('Elevator')+1]
				#print('Elevator:', t)
				elevators.append(t)
			else:
				elevators.append(NOTFOUND)
				#print('Elevator not found')

			if 'ceiling height' in list_of_words:
				t = list_of_words[list_of_words.index('ceiling height')+1]
				print('ceiling height:', t)
				ceiling_heights.append(t)
			else:
				ceiling_heights.append(NOTFOUND)
				#print('ceiling height not found')

			if 'Heating' in list_of_words:
				t = list_of_words[list_of_words.index('Heating')+1].strip()
				heatings.append(t)
				heating = t.split(' ')
				#print('Heating:', heating)
				if 'gáz' in heating or 'gas' in heating:
					gas.append(1)
					ceiling_heating.append(0)
					combination_boiler.append(0)
					wall_heating.append(0)
				elif 'falfűtés' in heating:
					gas.append(0)
					ceiling_heating.append(0)
					combination_boiler.append(0)
					wall_heating.append(1)
				elif 'ceiling' in heating:
					gas.append(0)
					ceiling_heating.append(1)
					combination_boiler.append(0)
					wall_heating.append(0)
				elif 'combination' in heating:
					gas.append(0)
					ceiling_heating.append(0)
					combination_boiler.append(1)
					wall_heating.append(0)
				else:
					gas.append(0)
					ceiling_heating.append(0)
					combination_boiler.append(0)
					wall_heating.append(0)
			else:
				heatings.append(NOTFOUND)
				gas.append(NOTFOUND)
				ceiling_heating.append(NOTFOUND)
				combination_boiler.append(NOTFOUND)
				wall_heating.append(NOTFOUND)
				#print('Heating not found')

			if 'Air conditioning' in list_of_words:
				t = list_of_words[list_of_words.index('Air conditioning')+1].strip()
				#print('Air conditioning:', t)
				air_conditioning.append(t)
				if t == 'available':
					air_conditioners.append(YES)
				else:
					air_conditioners.append(NO)
			else:
				air_conditioning.append(NOTFOUND)
				air_conditioners.append(NOTFOUND)
				#print('Air conditioning not found')

			if 'Accessible' in list_of_words:
				t = list_of_words[list_of_words.index('Accessible')+1]
				#print('Accessible:', t)
				accessibiles.append(t)
			else:
				accessibiles.append(NOTFOUND)
				#print('Accessible not found')

			if 'Bathroom and toilet' in list_of_words:
				t = list_of_words[list_of_words.index('Bathroom and toilet')+1].strip()
				#print('Bathroom and toilet:', t)
				bathrooms.append(t)
				bathroom = t.split(' ')
				if 'separate' in bathroom:
					bathroom_separate.append(1)
					if 'together' in bathroom:
						bathroom_together.append(0)
					else:
						bathroom_together.append(0)
				elif 'together' in bathroom:
					bathroom_separate.append(0)
					bathroom_together.append(1)
				else:
					bathroom_separate.append(NOTFOUND)
					bathroom_together.append(NOTFOUND)
			else:
				bathrooms.append(NOTFOUND)
				bathroom_separate.append(NOTFOUND)
				bathroom_together.append(NOTFOUND)
				#print('Bathroom and toilet not found')

			if 'Orientation' in list_of_words:
				t = list_of_words[list_of_words.index('Orientation')+1]
				#print('Orientation:', t)
				orientations.append(t)
			else:
				orientations.append(NOTFOUND)
				#print('Orientation not found')

			if 'Views' in list_of_words:
				t = list_of_words[list_of_words.index('Views')+1]
				views.append(t)
				if 'garden' in t:
					views_garden.append(1)
					views_panoramic.append(0)
					views_else.append(0)
				elif 'panoramic' in t:
					views_garden.append(0)
					views_panoramic.append(1)
					views_else.append(0)
				else:	
					views_garden.append(NO)
					views_panoramic.append(NO)
					views_else.append(NO)
			else:
				views.append(NOTFOUND)
				views_garden.append(0)
				views_panoramic.append(0)
				views_else.append(0)
				#print('Views not found')

			if 'Balcony' in list_of_words:
				t = list_of_words[list_of_words.index('Balcony')+1]
				#print('Balcony:', t)
				barconies.append(t)
			else:
				barconies.append(NOTFOUND)
				#print('Balcony not found')

			if 'Garden access' in list_of_words:
				t = list_of_words[list_of_words.index('Garden access')+1]
				#print('Garden access:', t)
				gardens.append(t)
			else:
				gardens.append(NOTFOUND)
				#print('Garden access not found')

			if 'Attic' in list_of_words:
				t = list_of_words[list_of_words.index('Attic')+1]
				#print('Attic:', t)
				attics.append(t)
			else:
				attics.append(NOTFOUND)
				#print('Attic not found')

			if 'Parking' in list_of_words:
				t = list_of_words[list_of_words.index('Parking')+1]
				#print('Parking:', t)
				parkings.append(t)
			else:
				parkings.append(NOTFOUND)
				#print('Parking not found')
				#properties_detail.append(detail)
		else:
			#print('details not found')
			properties_detail.append(NOTFOUND)


		#transportation
		if sub_page_html.find('div', class_ = 'public-transport-group') is not None:
			transport = sub_page_html.findAll('div', class_ = 'public-transport-group')
			transportation = ''
			for item in transport:
				transportation  = transportation + item.text
			#print('transport:', transportation)
			transportations.append(transportation)
		else:
			transportations.append(NOTFOUND)

		#location
		if sub_page_html.find('a', class_ = 'static-map') is not None:
			#print('find map link')
			location = sub_page_html.find('a', class_ = 'static-map').find('img')['src'].split('=')[3]
			#print(type(location))
			location.replace('&markers', '')
			#print('location', location)
			lat = location.split(',')[0]
			lon = location.split(',')[1]
			#locations.append(location)
			latitudes.append(lat)
			longitudes.append(lon)
		else:
			#locations.append(NOTFOUND)
			latitudes.append(NOTFOUND)
			longitudes.append(NOTFOUND)
			#print('location not found')
'''
		else:
			district_1.append(NOTFOUND)
			district_2.append(NOTFOUND)
			district_3.append(NOTFOUND)
			district_4.append(NOTFOUND)
			district_5.append(NOTFOUND)
			district_6.append(NOTFOUND)
			district_7.append(NOTFOUND)
			district_8.append(NOTFOUND)
			district_9.append(NOTFOUND)
			district_10.append(NOTFOUND)
			district_11.append(NOTFOUND)
			district_12.append(NOTFOUND)
			district_13.append(NOTFOUND)
			district_14.append(NOTFOUND)
			district_15.append(NOTFOUND)
			district_16.append(NOTFOUND)
			district_17.append(NOTFOUND)
			district_18.append(NOTFOUND)
			district_19.append(NOTFOUND)
			district_20.append(NOTFOUND)
			district_21.append(NOTFOUND)
			district_22.append(NOTFOUND)
			district_23.append(NOTFOUND)
			prices.append(NOTFOUND)
			prices_per_sqm.append(NOTFOUND)
			streets.append(NOTFOUND)
			sizes.append(NOTFOUND)
			num_of_rooms.append(NOTFOUND)
			condition_of_properties.append(NOTFOUND)
			utility_levels.append(NOTFOUND)
			energies.append(NOTFOUND)
			floors.append(NOTFOUND)
			floors_of_the_building.append(NOTFOUND)
			elevators.append(NOTFOUND)
			ceiling_heights.append(NOTFOUND)
			heatings.append(NOTFOUND)
			air_conditioners.append(NOTFOUND)
			accessibiles.append(NOTFOUND)
			bathrooms.append(NOTFOUND)
			orientations.append(NOTFOUND)
			views.append(NOTFOUND)
			gardens.append(NOTFOUND)
			attics.append(NOTFOUND)
			parkings.append(NOTFOUND)'''

my_dict = {
	'Houses': houses,
	'Apartments': apartments,
	'Rooms': rooms,
	'District I': district_1,
	'District II': district_2,
	'District III': district_3,
	'District IV': district_4,
	'District V': district_5,
	'District VI': district_6,
	'District VII': district_7,
	'District VIII': district_8,
	'District IX': district_9,
	'District X': district_10,
	'District XI': district_11,
	'District XII': district_12,
	'District XIII': district_13,
	'District XIV': district_14,
	'District XV': district_15,
	'District XVI': district_16,
	'District XVII': district_17,
	'District XVIII': district_18,
	'District XIX': district_19,
	'District XX': district_20,
	'District XXI': district_21,
	'District XXII': district_22,
	'District XXIII': district_23,
	#Prices
	'Price(HUF millions)': prices_HUF,
	'Price per sqm (HUF)': prices_per_sqm_HUF,
	#
	'Street': streets,
	'Size(sqm)': sizes,
	'Floor': floors,
	'Name of Residential complex': name_of_buildings,
	'Parking place': parkings,
	#Views
	'View': views,
	'View: Garden view': views_garden,
	'View: View: Panoramic view': views_panoramic,
	'View: Else view': views_else,
	#
	'Elevator': elevators,
	#
	'Air conditioning': air_conditioning,
	'Air conditioner': air_conditioners,
	#Number of rooms
	'Number of rooms': num_of_rooms,
	'Number of rooms: whole rooms': whole_rooms,
	'Number of rooms: half rooms': half_rooms,
	#Conditions
	'Condition of property': condition_of_properties,
	'Condition of property: Newly build': newly_built,
	'Condition of property: In good condition': good_condition,
	'Condition of property: Renovated': renovated,
	'Condition of property: In medium condition': medium_condition,
	'Condition of property: Needs renovation': needs_renovation,
	'Condition of property: Mint': mint,
	#Utility levels
	'Utility level': utility_levels,
	'Utility: double comfort': double_comfort,
	'Utility: full comfort': full_comfort,
	'Utility luxury': luxury,
	#
	'Energy Performance Certificate': energies,
	'Floors of the building': floors_of_the_building,
	'Ceiling height': ceiling_heights,
	#Heating methods
	'Heating': heatings,
	'Heating: gas': gas,
	'Heating: wall_heating': wall_heating,
	'Heating: combination': combination_boiler,
	'Heating: ceiling': ceiling_heating,
	#
	'Accessible': accessibiles,
	#Bathroom
	'Bathroom and toilet': bathrooms,
	'Bathroom: separate': bathroom_separate,
	'Bathroom: together': bathroom_together,
	#
	'Orientation': orientations,
	'Garden access': gardens,
	'Balcony': barconies,
	'Attic': attics,
	'Transportation': transportations,
	'Latitude': latitudes,
	'Longitude': longitudes
}

#Vertical
properties = pd.DataFrame.from_dict(my_dict, orient='index')

#Clean data
print(properties.loc['Price(HUF millions)', : ])
properties.loc['Price(HUF millions)', : ] = properties.loc['Price(HUF millions)', : ].apply(lambda x:str(x)[ : -13].replace(' ', '')).astype(float)
print(properties.loc['Price(HUF millions)', : ])

print(properties.loc['Size(sqm)', : ])
properties.loc['Size(sqm)', : ] = properties.loc['Size(sqm)', : ].apply(lambda x:str(x)[ : -9].replace(' ', '')).astype(float)
print(properties.loc['Size(sqm)', : ])

print(properties.loc['Parking place', : ])
properties.loc['Parking place', : ] = properties.loc['Parking place', : ].apply(lambda x: NOTFOUND if str(x) == 'not specified' or '' else YES).astype(float)
print(properties.loc['Parking place', : ])

#We use 0,0 in case there is no latitude and longitude information
properties.loc["Latitude", : ] = properties.loc["Latitude"].apply(lambda x: 0 if x == '' else x).astype(float)

properties.loc["Longitude", : ] = properties.loc["Longitude"].apply(lambda x: 0 if x == '' else str(x).replace('&markers', '')).astype(float)

#Produce a .csv file
properties.to_csv('realestatehungary_sale_houses.csv')







