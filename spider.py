#This is a spider for web albertlet.hu
#properties for rent
#type: apartment
#Scrape the first 70 pages. Can be changed later


from requests import get
from bs4 import BeautifulSoup
from time import time, sleep
from warnings import warn
from random import randint
from IPython.core.display import clear_output

import re
import pandas as pd 
#import matplotlib.pyplot as plt


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
pages = [str(i) for i in range(1, 3)]

#Lists to store the scraped data in
prices_per_month = []
districts = []
streets = []
sizes = []
num_of_rooms = []
type_of_buildings = []
deposits = []
utilities = []
common_costs = []
separate_rooms = []
furnitures = []
floors = []
balconies = []
property_views = []
shortest_rentals = []
availables = []
children_welcomes = []
ameri_kitchens = []
offices = []
pets = []
foreigners = []
washing_machines = []
details = []
locations = []
areas = []
transportations = []
universities = []

#Define strings used when the value is not available

#Use -1 to represent the none value
NOTFOUND = -1
#Use 0 to represent NO
NO = 0
#Use 1 to represent YES
YES = 1

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


			#The price
			price = item.b.text
			prices_per_month.append(price)

			#The district
			district = item.find('span', class_ = 'advert__city').text
			districts.append(district)

			#The street
			street = item.find('span', class_ = 'advert__street').text
			streets.append(street)

			#The size
			size = item.find('span', class_ = 'advert__rooms').previousSibling
			sizes.append(size)

			#The number of rooms
			num_of_room = item.find('span', class_ = 'advert__rooms').text
			num_of_rooms.append(num_of_room)

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
				locations.append(NOTFOUND)

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
					furniture = sub_page_html.find('td', text = "Furniture").find_next_sibling().text
					#print(furniture)
					furnitures.append(furniture)
				else:
					furnitures.append(NOTFOUND)

				#The number of floor
				if sub_page_html.find('td', text = "Floor") is not None:
					floor = sub_page_html.find('td', text = "Floor").find_next_sibling().text
					#print(floor)
					floors.append(floor)
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
					property_view = sub_page_html.find('td', text = "View").find_next_sibling().text
					#print(property_view)
					property_views.append(property_view)
				else:
					property_views.append(NOTFOUND)

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
				'''
				#Attributes for the heatmap later
				if sub_page_html.find('a', class_ = 'btn btn--primary btn--small btn-get-direction') is not None:
					latitude_longitude = sub_page_html.find('a', class_ = 'btn btn--primary btn--small btn-get-direction')['onclick']
				else:
					latitude_longitude = NOTFOUND
				#print(latitude_longitude)
				#Since all of the latitude and longitude follow the same format
				#e.g. CP.MapDirections.deploy("47.489264600000", "19.069734900000", "0");
				#by counting and slicing the string, we can get the pair of latitude and longitude
				location = latitude_longitude[25:40] + "," + latitude_longitude[44:59]
				#print(location)
				locations.append(location)'''

#If want vertically arranged
'''properties = pd.DataFrame({
	'Price per month': prices_per_month,
	'District': districts,
	'Street': streets,
	'Size': sizes,
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
	'Longitude and latitude': locations
})'''

#If want horizontally arranged
my_dict = {
	'Price per month': prices_per_month,
	'District': districts,
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
	'Longitude and latitude': locations
}

properties = pd.DataFrame.from_dict(my_dict, orient='index')

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

#Convert price to int
for p in properties.loc["Price per month", : ]:
	p = int(p.replace(" ", ""))
	print(p)

#Delete the white space in size and number of rooms
for p in properties.loc["Size(sqm)", : ]:
	p = int(p.strip()[ :-4])
	print(p)

for p in properties.loc["Number of separate rooms", : ]:
	if p.is_integer():
		p = p
	else:
		p = int(p.strip())
	print(p)

#Produce a .csv file
properties.to_csv('alberlet_rent.csv')

#Draw a simple graph
#x-axis: price
#y-axis: number of houses
#fig, axes = plt.subplot(nrows = 1, ncols = 1, figsize = (16, 4))


		



















	












