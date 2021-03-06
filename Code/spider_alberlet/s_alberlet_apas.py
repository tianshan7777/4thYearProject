#This is a spider for web alberlet.hu
#properties for rent
#type: apartment

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



#Python Requests doe not necessarily need a request headers while sending requests
#but there are few smart websites that does not let you to 
#get read anything important unless cerain heaers are not set in it.
#Also, it is a good idea to scrape with a header that has your name and emial so that a website can identigy you
#And follow up if they have any questions. 
#So, it is always good to make you requests as legitimate as you can.
#The least you should do is to set a User-Agent

#header = {'User-Agent': 'Client Name, ClientWeb.com',
#			'From': 'ClientEmail@example.com'}

#By analysing the urls
#e.g. https://www.alberlet.hu/en/sublet_to_let/county:budapest/property-type:apartment/search:normal/limit:24
#https://www.alberlet.hu/en/sublet_to_let/page:2/county:budapest/property-type:apartment/search:normal/limit:24
#One can easily see that by changing the 'page' parameter, we can scrape over multiple pages

#Changing the URL's parameter
#pages = [str(i) for i in range(1, 150)]
pages = [str(i) for i in range(1, 3)]

#Lists to store the scraped data in
houses = []
apartments = []
rooms = []
prices_per_month = []
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
sizes = []
#
num_of_rooms = []
whole_rooms = []
half_rooms = []
#
type_of_buildings = []
deposits = []
utilities = []
common_costs = []
separate_rooms = []
#
furnitures = []
furnished = []
empty = []
equipped = []
luxury = []
partly_furnished = []
#
floors = []
balconies = []
#
property_views = []
views_panoramic = []
views_courtyard = []
views_street = []
views_garden = []
views_street = []
views_park = []
#
shortest_rentals = []
availables = []
children_welcomes = []
ameri_kitchens = []
offices = []
pets = []
foreigners = []
washing_machines = []
details = []
longitudes = []
latitudes = []
areas = []
transportations = []
universities = []

#Define strings used when the value is not available
#Use -1 to represent the none value
NOTFOUND = -1
#Use 0 to represent NO/NOT FURNISHED/NOT EQUIPPED
NO = 0
#Use 1 to represent YES/FURNISHED/EQUIPPED
YES = 1
#Use 0.5 to represent partly furnished/OPTIONAL
PARTLYFURNISHED = 0.5

#Mornitoring the loop as it is still going
start_time = time()
requests = 0

#Scrape the pages
#For every page in range 1 to 4
for page in pages:
	#Make a request
	response = get('https://www.alberlet.hu/en/sublet_to_let/page:' + page + '/county:budapest/property-type:apartment/search:normal/limit:24')
	#Alternatively, including the header:
	#response = get('https://www.alberlet.hu/en/sublet_to_let/page:' + page + '/county:budapest/property-type:apartment/search:normal/limit:24', headers = headers)

	#Controlling the rate of craling is beneficial for us and for the website that we are scraping.
	#If we avoid hammering the server with tens of requests per second,
	#then we are much less likely to get our IP ADDRESS BANNED.
	#We also avoid disrupting the activity of the website we scrape by allowing the server to respond to other users' requests too

	#To mimic human behaviour, we will vary the amout of waiting time between requests by
	#using the randint() function from  random module.
	'''
	#Pause the loop
	sleep(randint(3,8))

	#Monitor the requests
	requests += 1
	elapsed_time = time() - start_time
	print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
	
	#Our work will look a bit messy as the output accumulates.
	#To avoid that, we will clear the output after each iteration, and replace it with info
	#about the most recent request.
	clear_output(wait = True)'''

	#To monitor the status code, we wil set the program to warn us if there is something off
	#A successful request is indicated by a status code of 200.

	#Throw a warning if the status code is not 200
	if response.status_code != 200:
		warn('Request: {}; Status Code: {}'.format(requests, response.status_code))

	#Break the loop if the number of requests is greater than expect
	if requests > 100:
		warn('The number of requests is greater than expect')
		break 

	#Parse the html with a BeautifulSoup object
	page_html = BeautifulSoup(response.text, 'html.parser')

	#By analysing the website we find that each page contains several (usually 4) class = boxes-grid row advert-list
	#in which we can find the item list

	#Select all the item lists
	property_containers = page_html.find_all('div', class_ = 'boxes-grid row advert-list')

	#print(type(property_containers))
	#print(len(property_containers))

	#For each property list (usually contains 6 properties )in these 4 divs
	for container in property_containers:

		#Select all the items under one list
		property_items = container.find_all('div', class_ = 'col-sm-6 col-lg-4 advert-list__item')
		#print(type(property_containers))
		#print(len(property_containers))

		#For each property in the property list
		for item in property_items:

			#type of properties
			houses.append(0)
			apartments.append(1)
			rooms.append(0)

			#The price
			price = item.b.text
			prices_per_month.append(price)

			def district_helper(district):
				return district.replace("Budapest,", "").replace(". District", "").replace(" ","")

			#The district
			district = item.find('span', class_ = 'advert__city').text
			district_num = roman.fromRoman(district_helper(district))
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

			#The street
			street = item.find('span', class_ = 'advert__street').text
			streets.append(street)

			#The size
			size = item.find('span', class_ = 'advert__rooms').previousSibling
			sizes.append(size)

			#The number of rooms
			num_of_room = item.find('span', class_ = 'advert__rooms').text.strip()
			num_of_rooms.append(num_of_room)
			list_of_num_of_room = num_of_room.split(' ')
			if '+' in list_of_num_of_room:
				whole_rooms.append(int(list_of_num_of_room[0].strip()))
				half_rooms.append(int(list_of_num_of_room[list_of_num_of_room.index('half')-1].strip()))
			elif 'half' in list_of_num_of_room:
				whole_rooms.append(0)
				half_rooms.append(int(list_of_num_of_room[list_of_num_of_room.index('half')-1].strip()))
			elif 'room' in list_of_num_of_room:
				whole_rooms.append(int(list_of_num_of_room[list_of_num_of_room.index('room')-1].strip()))
				half_rooms.append(0)
			else:
				whole_rooms.append(NOTFOUND)
				half_rooms.append(NOTFOUND)

			#In order to gather more detailed information we dive into the sub website by the link listed

			#Find the link to its detailed web
			sub_url = str(item.a['href'])
			print(sub_url)

			#Some urls are not completed so we need to examine them
			if "https://www.alberlet.hu" not in sub_url:
				if "alberlet.hu" in sub_url:
					#split the url address by "/"
					url_part = []
					url_part = sub_url.split("/")
					#Select the last part which indicates the child location
					#print(url_part)

					sub_url = "https://www.alberlet.hu/en/sublet_to_let" + url_part[-1]
					print("adjust url is :" + sub_url)
				else:
					#Sometimes it just does not have the heading part
					sub_url = "https://www.alberlet.hu" + sub_url
					print("adjust url is :" + sub_url)

			#Repeat the previous steps for data scraping on the sub website
			sub_response = get(sub_url)

			#Throw a warning if the status code is not 200
			#If page not found, fill all the attributes up with NOTFOUND
			if response.status_code != 200:
				warn('Request: {}; Status Code: {}'.format(requests, response.status_code))
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
				type_of_buildings.append(NOTFOUND)
				deposits.append(NOTFOUND)
				utilities.append(NOTFOUND)
				common_costs.append(NOTFOUND)
				separate_rooms.append(NOTFOUND)
				furnitures.append(NOTFOUND)
				floors.append(NOTFOUND)
				balconies.append(NOTFOUND)
				property_views.append(NOTFOUND)
				shortest_rentals.append(NOTFOUND)
				availables.append(NOTFOUND)
				children_welcomes.append(NOTFOUND)
				ameri_kitchens.append(NOTFOUND)
				offices.append(NOTFOUND)
				pets.append(NOTFOUND)
				foreigners.append(NOTFOUND)
				washing_machines.append(NOTFOUND)
				details.append(NOTFOUND)
				latitudes.append(NOTFOUND)
				longitudes.append(NOTFOUND)

			else:
				sub_page_html = BeautifulSoup(sub_response.text, 'html.parser')
			
				#The type of the building
				if sub_page_html.find('td', text = "Type of the building") is not None:
					if sub_page_html.find('td', text = "Type of the building").find_next_sibling() is not None:
						type_of_building = sub_page_html.find('td', text = "Type of the building").find_next_sibling().text
						#print(type_of_building)
						type_of_buildings.append(type_of_building)
					else:
						type_of_buildings.append(NOTFOUND)
				else:
					type_of_buildings.append(NOTFOUND)

				#The rental price 
				#Already scraped from the main page
				'''if sub_page_html.find('td', text = "New rental price") is not None:
					rental_price = sub_page_html.find('td', text = "New rental price").find_next_sibling().text
					print(rental_price)
				else:
					rental_price = sub_page_html.find('td', text = "Rental price").find_next_sibling().text
					print(rental_price)'''

				#The deposit
				if sub_page_html.find('td', text = "Deposit") is not None:
					deposit = sub_page_html.find('td', text = "Deposit").find_next_sibling().text
					#print(deposit)
					deposits.append(deposit)
				else:
					deposits.append(NOTFOUND)

				#The utility fees
				if sub_page_html.find('td', text = "Utilities") is not None:
					utility = sub_page_html.find('td', text = "Utilities").find_next_sibling().text
					#print(utility)
					utilities.append(utility)
				else:
					utilities.append(NOTFOUND)

				#The common cost
				if sub_page_html.find('td', text = "Common cost") is not None:
					common_cost = sub_page_html.find('td', text = "Common cost").find_next_sibling().text
					#print(common_cost)
					common_costs.append(common_cost)
				else:
					common_costs.append(NOTFOUND)

				#The size
				#Already scraped from the main page
				'''if sub_page_html.find('td', text = "Size") is not None:
					property_size = sub_page_html.find('td', text = "Size").find_next_sibling().text
					print(property_size)

					else:
					property_size.append(NOTFOUND)'''

				#The number of rooms
				#Already scraped from the main page
				'''if sub_page_html.find('td', text = "Number of rooms") is not None:
					property_rooms = sub_page_html.find('td', text = "Number of rooms").find_next_sibling().text
					print(property_rooms)

					else:
					property_rooms.append(NOTFOUND)'''

				#The number of separate rooms
				if sub_page_html.find('td', text = "Separate rooms") is not None:
					separate_room = sub_page_html.find('td', text = "Separate rooms").find_next_sibling().text
					#print(separate_room)
					separate_rooms.append(separate_room)
				else:
					separate_rooms.append(NOTFOUND)

				#The furniture status
				if sub_page_html.find('td', text = "Furniture") is not None:
					furniture = sub_page_html.find('td', text = "Furniture").find_next_sibling().text.strip().lower()
					#print(furniture)
					furnitures.append(furniture)
					list_of_furniture = furniture.split(',')
					if 'partly furnished' in list_of_furniture:
						partly_furnished.append(1)
						furnished.append(0)
						if 'empty' in list_of_furniture:
							empty.append(1)
							if 'equipped' in list_of_furniture:
								equipped.append(1)
							else:
								equipped.append(0)
							if 'luxury' in list_of_furniture:
								luxury.append(1)
							else:
								luxury.append(0)
						else:
							empty.append(0)
							if 'equipped' in list_of_furniture:
								equipped.append(1)
							else:
								equipped.append(0)
							if 'luxury' in list_of_furniture:
								luxury.append(1)
							else:
								luxury.append(0)
					elif 'furnished' in list_of_furniture:
						partly_furnished.append(0)
						furnished.append(1)
						if 'empty' in list_of_furniture:
							empty.append(1)
							if 'equipped' in list_of_furniture:
								equipped.append(1)
							else:
								equipped.append(0)
							if 'luxury' in list_of_furniture:
								luxury.append(1)
							else:
								luxury.append(0)
						else:
							empty.append(0)
							if 'equipped' in list_of_furniture:
								equipped.append(1)
							else:
								equipped.append(0)
							if 'luxury' in list_of_furniture:
								luxury.append(1)
							else:
								luxury.append(0)
					elif 'empty' in list_of_furniture:
						empty.append(1)
						if 'partly furnished' in list_of_furniture:
							partly_furnished.append(1)
						else:
							partly_furnished.append(0)
						if 'furnished' in list_of_furniture:
							furnished.append(1)
						else:
							furnished.append(0)
						if 'equipped' in list_of_furniture:
							equipped.append(1)
						else:
							equipped.append(0)
						if 'luxury' in list_of_furniture:
							luxury.append(1)
						else:
							luxury.append(0)
					else:
						partly_furnished.append(0)
						furnished.append(0)
						empty.append(0)
						equipped.append(0)
						luxury.append(0)
				else:
					furnitures.append(NOTFOUND)
					partly_furnished.append(NOTFOUND)
					furnished.append(NOTFOUND)
					empty.append(NOTFOUND)
					equipped.append(NOTFOUND)
					luxury.append(NOTFOUND)

				#The number of floor
				if sub_page_html.find('td', text = "Floor") is not None:
					floor = sub_page_html.find('td', text = "Floor").find_next_sibling().text.strip()
					#print(floor)
					floors.append(floor)
					if floor == 'Ground floor':
						floors.append(0)
					elif floor == 'Half ground floor':
						floors.append(0.5)
					elif floor == 'Over 10':
						floors.append(10)
					elif floor == 'Half floor':
						floors.append(0.5)
					else:
						floors.append(-1)
				else:
					floors.append(NOTFOUND)

				#The number of balconies if possible
				if sub_page_html.find('td', text = "Number pf balconies") is not None:
					balcony = sub_page_html.find('td', text = "Number of balconies").find_next_sibling().text
					#print(balcony)
					balconies.append(balcony)
				else:
					balconies.append(NOTFOUND)

				#The view of the flat
				if sub_page_html.find('td', text = "View") is not None:
					property_view = sub_page_html.find('td', text = "View").find_next_sibling().text.strip().lower()
					#print(property_view)
					property_views.append(property_view)
					list_of_view = property_view.split(' ')
					if 'garden' in list_of_view:
						views_garden.append(1)
						views_panoramic.append(0)
						views_courtyard.append(0)
						views_street.append(0)
						views_park.append(0)
					elif 'panoramic' in list_of_view:
						views_garden.append(0)
						views_panoramic.append(1)
						views_courtyard.append(0)
						views_street.append(0)
						views_park.append(0)
					elif 'courtyard' in list_of_view:
						views_garden.append(0)
						views_panoramic.append(0)
						views_courtyard.append(1)
						views_street.append(0)
						views_park.append(0)
					elif 'street' in list_of_view:
						views_garden.append(0)
						views_panoramic.append(0)
						views_courtyard.append(0)
						views_street.append(1)
						views_park.append(0)
					elif 'park' in list_of_view:
						views_garden.append(0)
						views_panoramic.append(0)
						views_courtyard.append(0)
						views_street.append(0)
						views_park.append(1)
					else:
						views_garden.append(0)
						views_panoramic.append(0)
						views_courtyard.append(0)
						views_street.append(0)
						views_park.append(0)
				else:
					property_views.append(NOTFOUND)
					views_garden.append(NOTFOUND)
					views_panoramic.append(NOTFOUND)
					views_courtyard.append(NOTFOUND)
					views_street.append(NOTFOUND)
					views_park.append(NOTFOUND)

				#The shortest rental period
				if sub_page_html.find('td', text = "Shortest rental period") is not None:
					shortest_rental = sub_page_html.find('td', text = "Shortest rental period").find_next_sibling().text
					#print(shortest_rental)
					shortest_rentals.append(shortest_rental)
				else:
					shortest_rentals.append(NOTFOUND)

				#When the flat is available
				if sub_page_html.find('td', text = "Available from") is not None:
					available = sub_page_html.find('td', text = "Available from").find_next_sibling().text
					#print(available)
					availables.append(available)
				else:
					availables.append(NOTFOUND)

				#If the flat is children friendly
				if sub_page_html.find('td', text = "Gyermekbarát") is not None:
					children_welcome = sub_page_html.find('td', text = "Gyermekbarát").find_next_sibling().text
					#print(children_welcome)
					children_welcomes.append(children_welcome)
				else:
					children_welcomes.append(NOTFOUND)

				#By investing the pages we know that as long as american kitchen item appears, it implies
				#the flat has an American kitchen
				if sub_page_html.find('td', text = "American kitchen") is not None:
					ameri_kitchens.append(YES)
				else:
					ameri_kitchens.append(NOTFOUND)
			
				#If the flat can be used as an office
				if sub_page_html.find('td', text = "Office use, too") is not None:
					office = sub_page_html.find('td', text = "Office use, too").find_next_sibling().text
					#print(office)
					offices.append(office)
				else:
					#print(NOTFOUND)
					offices.append(NOTFOUND)
	
				#If the flat is pets friendly
				if sub_page_html.find('td', text = "Pets allowed") is not None:
					pet = sub_page_html.find('td', text = "Pets allowed").find_next_sibling().text
					#print(pets)
					pets.append(pet)
				else:
					pets.append(NOTFOUND)

				#If the flat is foreigners friendly
				if sub_page_html.find('td', text = "To foreigners, too") is not None:
					foreigner = sub_page_html.find('td', text = "To foreigners, too").find_next_sibling().text
					#print(foreigners)
					foreigners.append(foreigner)
				else:
					foreigners.append(NOTFOUND)

				#By investing the pages we know that as long as washing machine item appears, it implies
				#the flat has a washing machine
				if sub_page_html.find('td', text = "Has washing machine") is not None:
					washing_machines.append(YES)
				else:
					washing_machines.append(NOTFOUND)

				#Details
				#Attributes for natural language processing later
				#By analysing the website, we find that the description right after the 'detail' title is just a repitition of the table
				#So, we'll just extract data about the transportation and near university here
				if sub_page_html.find('div', class_ = "profile__text") is not None:
					if sub_page_html.find('div', class_ = "profile__text").p is not None:
						detail = sub_page_html.find('div', class_ = "profile__text").p.text
						details.append(detail)
					else:
						details.append(NOTFOUND)
				else:
					details.append(NOTFOUND)

				#Area
				if sub_page_html.find('div', class_ = 'profile__text'):
					if sub_page_html.find('div', class_ = 'profile__text').find('b', text = "Area: ") is not None:
						area = sub_page_html.find('div', class_ = 'profile__text').find('b', text = "Area: ").next_sibling
						areas.append(area)
				else:
					areas.append(NOTFOUND)

				#Transportation
				if sub_page_html.find('div', class_ = 'profile__text')is not None:
					if sub_page_html.find('div', class_ = 'profile__text').find('b', text = "Transportation: ") is not None:
						transportation = sub_page_html.find('div', class_ = 'profile__text').find('b', text = "Transportation: ").next_sibling
						#print(transportation)
						transportations.append(transportation)
				else:
					transportations.append(NOTFOUND)

				#Near universities
				if sub_page_html.find('div', class_ = 'profile__text') is not None:
					if sub_page_html.find('div', class_ = 'profile__text').find('b', text = "Near universities: ") is not None:
						university = sub_page_html.find('b', text = "Near universities: ").find_next_sibling().text
						universities.append(university)
				else:
					universities.append(NOTFOUND)
				
				#Attributes for the heatmap later
				if sub_page_html.find('a', class_ = 'btn btn--primary btn--small btn-get-direction') is not None:
					latitude_longitude = sub_page_html.find('a', class_ = 'btn btn--primary btn--small btn-get-direction')['onclick']
					latitudes.append(latitude_longitude[25:40])
					longitudes.append(latitude_longitude[44:59]) 
					print(latitude_longitude[25:40])
					print(latitude_longitude[44:59])
				elif sub_page_html.find_all("script", type = "text/javascript") is not None:
					script_text = str(sub_page_html.find_all("script", type = "text/javascript"))
					#print(script_text)
					list_of_words = script_text.split()
					if "lat:" in list_of_words:
						lat = list_of_words[list_of_words.index("lat:")+1]
						lng = list_of_words[list_of_words.index("lng:")+1]
						latitudes.append(lat.replace("'", "").replace(",",""))
						longitudes.append(lng.replace("'","").replace(",", ""))
						print(lat.replace("'", "").replace(",",""), lng.replace("'","").replace(",", ""))
					else:
						latitudes.append(NOTFOUND)
						longitudes.append(NOTFOUND)
						print("lat & long not found.")
				else:
					#Use -1 to represent fake maps
					latitudes.append(NOTFOUND)
					longitudes.append(NOTFOUND)
					print(NOTFOUND)
				#Since all of the latitude and longitude follow the same format
				#e.g. CP.MapDirections.deploy("47.489264600000", "19.069734900000", "0");
				#by counting and slicing the string, we can get the pair of latitude and longitude

'''#If want vertically arranged
properties = pd.DataFrame({
	'Type of properties': type_of_properties,
	'Price per month': prices_per_month,
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
	'Street': streets,
	'Size(sqm)': sizes,
	'Number of rooms': num_of_rooms,
	'Type of the building': type_of_buildings,
	'Deposit': deposits,
	'Utilities': utilities,
	'Common cost': common_costs,
	'Number of separate rooms': separate_rooms,
	'Furniture': furnitures,
	'Floor': floors,
	'Balconies': balconies,
	'View': property_views,
	'Shortest rental period': shortest_rentals,
	'Children welcomed': children_welcomes,
	'American kitchen': ameri_kitchens,
	'Can be an office': offices,
	'Foreigners welcomed': foreigners,
	'Washing machine': washing_machines,
	'Details': details,
	'Area': areas,
	'Transportation': transportations,
	'Near universities': universities,
	'Latitude': latitudes,
	"Longitude": longitudes
})'''

#If want horizontally arranged
my_dict = {
	'Houses': houses,
	'Apartments': apartments,
	'Rooms': rooms,
	'Price per month': prices_per_month,
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
	'Street': streets,
	'Size(sqm)': sizes,
	#
	'Number of rooms': num_of_rooms,
	'Number of rooms: whole rooms': whole_rooms,
	'Number of rooms: half rooms': half_rooms,
	#
	'Type of the building': type_of_buildings,
	'Deposit': deposits,
	'Utilities': utilities,
	'Common cost': common_costs,
	'Number of separate rooms': separate_rooms,
	#
	'Furniture': furnitures,
	'Furniture: furnished': furnished,
	'Furniture: partly_furnished': partly_furnished,
	'Furniture: empty': empty,
	'Furniture: equipped': equipped,
	'Furniture: luxury': luxury,
	#
	'Floor': floors,
	'Balconies': balconies,
	#
	'View': property_views,
	'View: panoramic': views_panoramic,
	'View: garden': views_garden,
	'View: street': views_street,
	'View: park': views_park,
	'View: courtyard': views_courtyard,
	#
	'Shortest rental period': shortest_rentals,
	'Children welcomed': children_welcomes,
	'American kitchen': ameri_kitchens,
	'Can be an office': offices,
	'Foreigners welcomed': foreigners,
	'Washing machine': washing_machines,
	'Details': details,
	'Area': areas,
	'Transportation': transportations,
	'Near universities': universities,
	'Latitude': latitudes,
	'Longitude': longitudes
}

properties = pd.DataFrame.from_dict(my_dict, orient = 'index')

#print(properties.info())
#properties.head(10)

#Cleaning our data

#If vertically arranged
#Rearrange the columns
'''properties = properties[[
	#'Longitude and latitude', 
	'District', 'Size', 'Price per month', 'Street', 'Number of rooms', 'Type of the building', 'Deposit', 'Utilities',
	'Foreigners welcomed', 'Children welcomed', 'Can be an office', 'Common cost', 'Number of separate rooms', 'Furniture', 
	'Floor', 'Balconies', 'View', 'Shortest rental period', 'Details']] '''

#Data Cleaning
#Convert price to int
for p in properties.loc["Price per month", : ]:
	print("price per month: ", p)

properties.loc["Price per month", : ] = properties.loc["Price per month", : ].apply(lambda x:str(x).replace(" ", "")).astype(int)

#def district_helper(district):
#	return district.replace("Budapest,", "").replace(". District", "").replace(" ","")
#
#Convert district number to int
#properties.loc["District", : ] = properties.loc["District", : ].apply(lambda x: roman.fromRoman(district_helper(x)))


#Convert the size to int
for p in properties.loc["Size(sqm)", : ]:
	print("size: ", p)

properties.loc["Size(sqm)", : ] = properties.loc["Size(sqm)", : ].apply(lambda x:str(x).strip()[ :-4]).astype(int)

#Convert deposit to int
for p in properties.loc["Deposit", : ]:
	print("deposit: ", p)

properties.loc["Deposit", : ] = properties.loc["Deposit", : ].apply(lambda x: x if x == -1 else str(x).replace(" ","").strip()[ :-4]).astype(int)

#Convert utilities to int
for p in properties.loc["Utilities", : ]:
	print("utilities: ", p)

properties.loc["Utilities", : ] = properties.loc["Utilities", : ].apply(lambda x: x if x == -1 else str(x).replace(" ", "").strip()[ :-10]).astype(int)

#Convert common cost to int
for p in properties.loc["Common cost", : ]:
	print("common cost: ", p)

properties.loc["Common cost", : ] = properties.loc["Common cost", : ].apply(lambda x: x if isinstance(x, int) else str(x).replace(" ", "").strip()[ :-10]).astype(int)

#Convert number of separate rooms to int
for p in properties.loc["Number of separate rooms", : ]:
	print("number of separate rooms: ", p)

properties.loc["Number of separate rooms", : ] = properties.loc["Number of separate rooms"].apply(lambda x: 0 if "No" in str(x) else x).astype(int)

#Convert number of separate rooms to int
for p in properties.loc["Floor", : ]:
	print("Floor: ", p)

properties.loc["Floor", : ] = properties.loc["Floor"].astype(float)

#We use 0,0 in case there is no latitude and longitude information
properties.loc["Latitude", : ] = properties.loc["Latitude"].apply(lambda x: 0 if x == "" else x).astype(float)

properties.loc["Longitude", : ] = properties.loc["Longitude"].apply(lambda x: 0 if x == "" else x).astype(float)

print(properties[0])

#Produce a .csv file
properties.to_csv('alberlet_rent_apartments.csv')

#Draw a simple graph
#x-axis: price
#y-axis: number of houses

# This import registers the 3D projection, but is otherwise unused.
'''
fig = plt.figure()
ax = plt.axes(projection='3d')
zdata = properties.loc["Price per month", : ]
xdata = properties.loc["District", : ]
ydata = properties.loc["Number of separate rooms", : ]
ax.scatter3D(xdata, ydata, zdata, c=zdata)

ax.set_xlabel("District")
ax.set_ylabel("Number of seperate rooms")
ax.set_zlabel("Price per month")

plt.show()'''

	



















	












