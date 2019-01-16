import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDRgjNLfEQVB8t2WvZ2XqXDqAgrSpTOoeE')
# Look up an address with reverse geocoding

reverse_geocode_result = gmaps.reverse_geocode((47.478626,19.05361))
#print(type(reverse_geocode_result))
#print(type(reverse_geocode_result[0]))
#print(reverse_geocode_result[0])

#Convert dict to string
list_of_comp = str(reverse_geocode_result[0]).split(',')
#Find index
postcode_index = list_of_comp.index(" 'types': ['postal_code']}]")-1
#Format: e.g. " 'short_name': '1111'"
postcode = list_of_comp[postcode_index].replace(' ', '').replace("'", '').split(':')[-1]
print(postcode)