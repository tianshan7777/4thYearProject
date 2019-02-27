import pandas as pd 

amenity_types = []

amenities = pd.read_csv('./poi/amenity.csv')

poi_types = amenities['poi type']

for i in poi_types:
	print(i)
	
	if i == 'bar':
		amenity_types.append('Sustenance')
	elif i == 'bbq':
		amenity_types.append('Sustenance')
	elif i == 'biergarten':
		amenity_types.append('Sustenance')
	elif i == 'cafe':
		amenity_types.append('Sustenance')
	elif i == 'fast_food':
		amenity_types.append('Sustenance')
	elif i == 'food_court':
		amenity_types.append('Sustenance')
	elif i == 'food':
		amenity_types.append('Sustenance')
	elif i == 'pub':
		amenity_types.append('Sustenance')
	elif i == 'restaurant':
		amenity_types.append('Sustenance')
	elif i == 'kindergarten':
		amenity_types.append('School')
	elif i == 'library':
		amenity_types.append('Education')
	elif i == 'archive':
		amenity_types.append('Education')
	elif i == 'public_bookcase':
		amenity_types.append('Education')
	elif i == 'school':
		amenity_types.append('School')
	elif i == 'music_school':
		amenity_types.append('School')
	elif i == 'driving_school':
		amenity_types.append('School')
	elif i == 'language_school':
		amenity_types.append('School')
	elif i == 'research_institute':
		amenity_types.append('Education')
	elif i == 'college':
		amenity_types.append('School')
	elif i == 'university':
		amenity_types.append('School')
	elif i == 'atm':
		amenity_types.append('Financial')
	elif i == 'bank':
		amenity_types.append('Financial')
	elif i == 'bureau_de_change':
		amenity_types.append('Financial')
	elif i == 'clinic':
		amenity_types.append('Healthcare')
	elif i == 'dentist':
		amenity_types.append('Healthcare')
	elif i == 'doctors':
		amenity_types.append('Healthcare')
	elif i == 'hospital':
		amenity_types.append('Healthcare')
	elif i == 'nursing_home':
		amenity_types.append('Healthcare')
	elif i == 'pharmacy':
		amenity_types.append('Healthcare')
	elif i == 'social_facility':
		amenity_types.append('Healthcare')	
	elif i == 'veterinary':
		amenity_types.append('Healthcare')
	elif i == 'arts_centre':
		amenity_types.append('Arts')
	elif i == 'cinema':
		amenity_types.append('Entertainment')
	elif i == 'community_centre':
		amenity_types.append('Entertainment')
	elif i == 'fountain':
		amenity_types.append('Arts')
	elif i == 'nightclub':
		amenity_types.append('Entertainment')
	elif i == 'social_centre':
		amenity_types.append('Entertainment')
	elif i == 'theatre':
		amenity_types.append('Entertainment')
	elif i == 'place_of_worship':
		amenity_types.append('Religion')
	elif i == 'police':
		amenity_types.append('Police')
	elif i == 'townhall':
		amenity_types.append('Government')
	elif i == 'courthouse':
		amenity_types.append('Government')
	elif i == 'vending_machine':
		amenity_types.append('Vending Machine')
	elif i == 'bicycle_parking':
		amenity_types.append('Transportation: Bicycle')
	elif i == 'bicycle_rental':
		amenity_types.append('Transportation: Bicycle')
	elif i == 'car_rental':
		amenity_types.append('Transportation: Car')
	elif i == 'car_wash':
		amenity_types.append('Transportation: Car')
	elif i == 'fuel':
		amenity_types.append('Fuel Station')
	elif i == 'parking':
		amenity_types.append('Parking')
	elif i == 'parking_space':
		amenity_types.append('Parking')
	elif i == 'coworking_space':
		amenity_types.append('Coworking Space')
	elif i == 'internet_cafe':
		amenity_types.append('Entertainment')
	elif i == 'recycling':
		amenity_types.append('Recycling')
	else:
		amenity_types.append('others')

amenities['amenity_types'] = pd.Series(amenity_types)
amenities.to_csv('amenity_clean.csv', index=False)






