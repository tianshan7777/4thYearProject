#This is a spider for web http://www.towerbudapest.com/ 
#Properties for sale
#Type: apartments

from requests import get
from bs4 import BeautifulSoup
from time import time, sleep
from warnings import warn
from random import randint
from IPython.core.display import clear_output
import re
import pandas as pd
import math


#header = {'User-Agent': 'Client Name, ClientWeb.com',
#		   'Form': 'Client@example.com'}

#Changing the URL's parameter
pages = [str(i) for i in range(1, 28)]

#Lists to store the scraped data
#Lists to store the scraped data in
type_of_properties = []
prices = []
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
bedrooms = []
sizes = []
floors = []
garages = []
parkings = []
property_views = []
furnitures = []
elevators = []
air_conditoners = []
property_details = []
longitudes = []
latitudes = []
'''
num_of_rooms = []
type_of_buildings = []
deposits = []
utilities = []
common_costs = []
separate_rooms = []
balconies = []
shortest_rentals = []
availables = []
children_welcomes = []
ameri_kitchens = []
offices = []
pets = []
foreigners = []
washing_machines = []
areas = []
transportations = []
universities = []
'''
#Define strings used when the value is not available
#Use -1 to represent the none value
NOTFOUND = -1
#Use 0 to represent NO/NOT FURNISHED/NOT EQUIPPED
NO = 0
#Use 1 to represent YES/FURNISHED/EQUIPPED
YES = 1
#Use 0.5 to represent partly furnished/OPTIONAL
PARTLY = 0.5

#Mornitoring the loop as it is still going
start_time = time()
requests = 0

#Scrape the pages
for page in pages:

	#Make a request via Requests
	response = get("https://www.towerbudapest.com/en/sales/" + page)

	#Parse the html file with a BeautifulSoup parser
	page_url = BeautifulSoup(response.text, 'html.parser')

	property_containers = page_url.find_all("div", class_ = "col-sm-4")

	#For each property in the container
	for container in property_containers:
		#We mark houses as 2 here
		type_of_properties.append(2)
		
		#The street
		if container.find("h3", class_ = "item title") is not None:
			street = container.find("h3", class_ = "item tittle").text
			streets.append(street)
		else:
			streets.append(NOTFOUND)

		#The price
		if container.find("p", class_ = "item-price kill-margin") is not None:
			price = container.find("p", class_ = "item-price kill-margin").span.text
			prices.append(price)
			print(price)
		else:
			prices.append(NOTFOUND)
			print(NOTFOUND)

		#In order to gather more detailed information we dive into the child website by the link of the picture
		#Find the link to its child web
		if container.a is not None:
			sub_url = str(container.a['href'])
			print(sub_url)

			if sub_url == 'javascript:':
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
				streets.append(NOTFOUND)
				bedrooms.append(NOTFOUND)
				sizes.append(NOTFOUND)
				floors.append(NOTFOUND)
				garages.append(NOTFOUND)
				parkings.append(NOTFOUND)
				property_views.append(NOTFOUND)
				furnitures.append(NOTFOUND)
				elevators.append(NOTFOUND)
				air_conditoners.append(NOTFOUND)
				property_details.append(NOTFOUND)
				longitudes.append(NOTFOUND)
				latitudes.append(NOTFOUND)
			else:
				sub_response = get(sub_url)
				sub_page_html = BeautifulSoup(sub_response.text, 'html.parser')


				#Attributes for the heatmap later
				if sub_page_html.find_all('script', class_ = None, scr = None, type = None, ) is not None:
					script_text = str(sub_page_html.find_all('script', class_ = None, scr = None, type = None))
					#print(script_text)
					list_of_words = script_text.split()
					#print(list_of_words)
					if "['https://www.towerbudapest.com/resources/images/pin-orange-tower.png'," in list_of_words:
						lat = list_of_words[list_of_words.index("['https://www.towerbudapest.com/resources/images/pin-orange-tower.png',")+1].replace(',', '')
						lng = list_of_words[list_of_words.index("['https://www.towerbudapest.com/resources/images/pin-orange-tower.png',")+2].replace(',', '')
						print(lat, lng)
						latitudes.append(lat)
						longitudes.append(lng)
					elif "['https://www.towerbudapest.com/resources/images/pin-green-tower.png'," in list_of_words:
						lat = list_of_words[list_of_words.index("['https://www.towerbudapest.com/resources/images/pin-green-tower.png',")+1].replace(',', '')
						lng = list_of_words[list_of_words.index("['https://www.towerbudapest.com/resources/images/pin-green-tower.png',")+2].replace(',', '')
						print(lat, lng)
						latitudes.append(lat)
						longitudes.append(lng)
					else:
						latitudes.append(NOTFOUND)
						longitudes.append(NOTFOUND)
						print("lat & long not found.")
				else:
					#Use -1 to represent fake maps
					latitudes.append(NOTFOUND)
					longitudes.append(NOTFOUND)
					print(NOTFOUND)

				if sub_page_html.find('div', class_ = 'col-sm-4 col-md-3 property-details-sidebar') is not None:
					details = sub_page_html.find('div', class_ = 'col-sm-4 col-md-3 property-details-sidebar').findAll('li')

					#The number of bedrooms
					bedroom = details[1].text
					#print(details[1].text)
					if 'Studio' in bedroom:
						print('This is a studio:')
						bedrooms.append('Studio')
					else:
						bedroom = details[1].text[10: ]
						print(bedroom)
						bedrooms.append(bedroom)

					#The size
					size = details[2].text[5:]
					print(size)
					sizes.append(size)
					print(details[2].text)

					#The floor
					floor = details[3].text[6:]
					print(floor)
					floors.append(floor)
					print(details[3].text)

					#The garage
					garage = details[4].text[7:]
					print(garage)
					garages.append(garage)
					print(details[4].text)

					#The parking place
					parking = details[5].text[14:]
					print(parking)
					parkings.append(parking)
					print(details[5].text)

					#The view
					view = details[6].text[5:]
					print(view)
					property_views.append(view)
					print(details[6].text)

					#The furnishment
					furniture = details[7].text[10:]
					print(furniture)
					furnitures.append(furniture)
					print(details[7].text)

					#The elevator
					elevator = details[8].text[9:]
					print(elevator)
					elevators.append(elevator)
					print(details[8].text)

					#The air conditioner
					air_conditoner = details[9].text[16: ]
					print(air_conditoner)
					air_conditoners.append(air_conditoner)
					print(details[9].text)

					if sub_page_html.find('div', class_ = 'row property-details-content-description') is not None:
						if sub_page_html.find('div', class_ = 'row property-details-content-description').p is not None:
							detail = sub_page_html.find('div', class_ = "row property-details-content-description").p.text
							property_details.append(detail)
							print(detail)
						else:
							property_details.append(NOTFOUND)
					else:
						property_details.append(NOTFOUND)

					
 					#The district
					district = int(details[0].text[-1])
					if district == 1:
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
					elif district == 2:
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
					elif district == 3:
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
					elif district == 4:
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
					elif district == 5:
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
					elif district == 6:
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
					elif district == 7:
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
					elif district == 8:
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
					elif district == 9:
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
					elif district == 10:
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
					elif district == 11:
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
					elif district == 12:
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
					elif district == 13:
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
					elif district == 14:
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
					elif district == 15:
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
					elif district == 16:
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
					elif district == 17:
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
					elif district == 18:
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
					elif district == 19:
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
					elif district == 20:
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
					elif district == 21:
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
					elif district == 22:
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
					elif district == 23:
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

		else:
			print('container.a is none:', container.section)
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
			streets.append(NOTFOUND)
			bedrooms.append(NOTFOUND)
			sizes.append(NOTFOUND)
			floors.append(NOTFOUND)
			garages.append(NOTFOUND)
			parkings.append(NOTFOUND)
			property_views.append(NOTFOUND)
			furnitures.append(NOTFOUND)
			elevators.append(NOTFOUND)
			air_conditoners.append(NOTFOUND)
			property_details.append(NOTFOUND)
			longitudes.append(NOTFOUND)
			latitudes.append(NOTFOUND)
#Horizontal
'''properties = pd.DataFrame({
	'Type of properties': type_of_properties,
	'Price': prices,
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
	'Bedroom': bedrooms,
	'Size(sqm)': sizes,
	'Floor': floors,
	'Garage': garages,
	'Parking place': parkings,
	'View': property_views,
	'furniture': furnitures,
	'Elevator': elevators,
	'Air conditioner': air_conditoners,
	'Details': details,
	'Longitude': longitudes,
	'Latitude': latitudes 
})'''

my_dict = {
	'Type of properties': type_of_properties,
	'Price': prices,
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
	'Bedroom': bedrooms,
	'Size(sqm)': sizes,
	'Floor': floors,
	'Garage': garages,
	'Parking place': parkings,
	'View': property_views,
	'Furniture': furnitures,
	'Elevator': elevators,
	'Air conditioner': air_conditoners,
	'Details': property_details,
	'Longitude': longitudes,
	'Latitude': latitudes 
}


'''
print(type(my_dict))
print(type(type_of_properties))
print(type(prices))
print(type(streets))
print(type(bedrooms))
print(type(sizes))
print(type(floors))
print(type(garages))
print(type(parkings))
print(type(property_views))
print(type(furnitures))
print(type(elevators))
print(type(air_conditoners))
print(type(property_details))
print(type(longitudes))
print(type(latitudes))
print(type(district_23))'''

#Vertical
properties = pd.DataFrame.from_dict(my_dict, orient='index')

#Data Cleaning
#Convert price to int
'''
for p in properties.loc['Price', : ]:
	print('Price:', p)
properties.loc['Price', : ] = properties.loc['Price', : ].apply(lambda x: x.replace(' ', '').replace(')', '').replace('.', '').split('€',1)[1] if isinstance(x, str) else NOTFOUND).astype(int)
print(properties.loc['Price', : ])'''

#Convert bedroom to int
#We use -2 to represent studio here
for p in properties.loc['Bedroom', : ]:
	print('bedroom:', p)
properties.loc['Bedroom', : ] = properties.loc['Bedroom', : ].apply(lambda x: -2 if x == 'Studio' else (x.strip() if isinstance(x, str) else NOTFOUND)).astype(int)
print(properties.loc['Bedroom', : ])

#Convert size to int
for p in properties.loc['Size(sqm)', : ]:
	print('size: ', p)
properties.loc['Size(sqm)', : ] = properties.loc['Size(sqm)', : ].apply(lambda x:  str(x).strip()[ :-4] if isinstance(x, str) else NOTFOUND).astype(int)
print(properties.loc['Size(sqm)', : ])

#Convert location to int
for p in properties.loc['Latitude', : ]:
	print('Latitude: ', p)
properties.loc['Latitude', : ] = properties.loc['Latitude', : ].apply(lambda x:  x.strip() if isinstance(x, str) else NOTFOUND).astype(float)
print(properties.loc['Latitude', : ])

for p in properties.loc['Longitude', : ]:
	print('Longitude: ', p)
properties.loc['Latitude', : ] = properties.loc['Longitude', : ].apply(lambda x:  str(x).strip() if isinstance(x, str) else NOTFOUND).astype(float)
print(properties.loc['Longitude', : ])

#Convert logic to int
for p in properties.loc['Garage', : ]:
	print('garage: ', p)
properties.loc['Garage', : ] = properties.loc['Garage', : ].apply(lambda x: YES if x == 'Yes' else (NO if x == 'No' else (PARTLY if isinstance(x, str) else NOTFOUND)))

for p in properties.loc['Parking place', : ]:
	print('parking place: ', p)
properties.loc['Parking place', : ] = properties.loc['Parking place', : ].apply(lambda x: YES if x == 'Yes' else (NO if x == 'No' else (PARTLY if isinstance(x, str) else NOTFOUND)))

for p in properties.loc['Furniture', : ]:
	print('Furniture: ', p)
properties.loc['Furniture', : ] = properties.loc['Furniture', : ].apply(lambda x: YES if x == 'Yes' else (NO if x == 'No' else (PARTLY if isinstance(x, str) else NOTFOUND)))

for p in properties.loc['Elevator', : ]:
	print('Elevator: ', p)
properties.loc['Elevator', : ] = properties.loc['Elevator', : ].apply(lambda x: YES if x == 'Yes' else (NO if x == 'No' else (PARTLY if isinstance(x, str) else NOTFOUND)))

for p in properties.loc['Air conditioner', : ]:
	print('Air conditioner: ', p)
properties.loc['Air conditioner', : ] = properties.loc['Air conditioner', : ].apply(lambda x: YES if x == 'Yes' else (NO if x == 'No' else (PARTLY if isinstance(x, str) else NOTFOUND)))

#Clean the None value
for p in properties.loc['Floor', : ]:
	print('Floor: ', p)
properties.loc['Floor', : ] = properties.loc['Floor', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

for p in properties.loc['View', : ]:
	print('View: ', p)
properties.loc['View', : ] = properties.loc['View', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

for p in properties.loc['Details', : ]:
	print('Details: ', p)
properties.loc['Details', : ] = properties.loc['Details', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District I', : ] = properties.loc['District I', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District II', : ] = properties.loc['District II', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District III', : ] = properties.loc['District III', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District IV', : ] = properties.loc['District IV', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District V', : ] = properties.loc['District V', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District VI', : ] = properties.loc['District VI', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District VII', : ] = properties.loc['District VII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District VIII', : ] = properties.loc['District VIII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District IX', : ] = properties.loc['District IX', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District X', : ] = properties.loc['District X', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XI', : ] = properties.loc['District XI', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XII', : ] = properties.loc['District XII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XIII', : ] = properties.loc['District XIII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XIV', : ] = properties.loc['District XIV', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XV', : ] = properties.loc['District XV', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XVI', : ] = properties.loc['District XVI', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XVII', : ] = properties.loc['District XVII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XVIII', : ] = properties.loc['District XVIII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XIX', : ] = properties.loc['District XIX', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XX', : ] = properties.loc['District XX', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XXI', : ] = properties.loc['District XXI', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XXII', : ] = properties.loc['District XXII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

properties.loc['District XXIII', : ] = properties.loc['District XXIII', : ].apply(lambda x: x if isinstance(x, str) else NOTFOUND)

#Produce a .csv file
properties.to_csv('towerbudapest_sale_apartments.csv')











