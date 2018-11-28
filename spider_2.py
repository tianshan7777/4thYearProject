#This is a spider for web http://www.towerbudapest.com/ 
#Properties for sale
#Type: apartments
#Scrape the first 2 pages. Can be adjusted later

from requests import get
from bs4 import BeautifulSoup
from time import time, sleep
from warnings import warn
from import randint
from IPthon.core,display import clear_output

import re
import pandas as pd


#header = {'User-Agent': 'Client Name, ClientWeb.com',
#		   'Form': 'Client@example.com'}

#Changing the URL's parameter
pages = [str(i) for i in range(1, 3)]

#Lists to store the scraped data
prices_forint = []
prices_euro = []
streets = []
districts = []
types_of_buildings = []
sizes = []
floors = []
garages = []
parking_places = []
furnishes = []
elevators = []
air_conditioners = []
descriptions = []
longitude_latitudes = []

#Define strings used when the value is not available
NOTFOUND = "No info available"
YES = "yes"

#Mornitoring the loop as it is still going
start_time = time()
requests = 0

#Scrape the pages
for page in pages:

	#Make a request via Requests
	response = get("https://www.towerbudapest.com/en/sales/" + page)
	#Alternatively, including the header:
	#response = get('https://www.alberlet.hu/en/sublet_to_let/page:' + page + '/county:budapest/property-type:apartment/search:normal/limit:24', headers = headers)

	#To mimic the human beings, pause the loop
	sleep(randint(3,8))

	#Mornitor the requests
	requests += 1
	elasped_time = time() - start_time
	print("Requests: {}; Frenquencies: {} requests/s".format(requests, requests/elasped_time))
	clear_output(wait = True)

	#Throw a warning if the status code is not 200
	if response.status_code != 200:
		warn('Request: {}; Status Code: {}'.format(requests, response.status_code))

	#Break the loop if the number of requests is greater than expect
	if requests > 100:
		warn('The number of requests is greater than expect')
		break

	#Parse the html file with a BeautifulSoup parser
	page_url = BeautifulSoup(response.text, 'html.parser')

	property_containers = page_url.find_all("div", class_ = "col-sm-4")

	#For each property in the container
	for container in property_containers:
		#The street
		street = container.find("h3", class_ = "item tittle").text
		streets.append(street)

		#The price
		price = container.find("p", class_ = "item-price kill-margin").span.text
		prices.append(price)
		print(price)

		#In order to gather more detailed information we dive into the child website by the link of the picture

		#Find the link to its child web
		sub_url = str(container.section['data-href'])









