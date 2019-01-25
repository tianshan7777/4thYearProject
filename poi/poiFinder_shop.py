import json
import pandas as pd

shape = []
coord = []
poi_type = []

with open('shop.geojson') as f:
	data = json.load(f)

for feature in data['features']:
	print('---------Start--------')

	if 'shop' in feature['properties']:
		print(feature['properties']['shop'])
		poi_type.append(feature['properties']['shop'])
	else:
		print(feature['properties']['@relations'][0]['reltags']['shop'])
		poi_type.append(feature['properties']['@relations'][0]['reltags']['shop'])

	print(feature['geometry']['type'])
	shape.append(feature['geometry']['type'])

	if feature['geometry']['type'] == 'Polygon' or feature['geometry']['type'] == 'LineString':
		print(feature['geometry']['coordinates'][0][0])
		coord.append(feature['geometry']['coordinates'][0][0])
	elif feature['geometry']['type'] == 'MultiPolygon':
		print(feature['geometry']['coordinates'][0][0][0])
		coord.append(feature['geometry']['coordinates'][0][0][0])
	else:
		print(feature['geometry']['coordinates'])
		coord.append(feature['geometry']['coordinates'])

	print('--------End-------')

my_dict = {
	'poi shape': shape,
	'poi type': poi_type,
	'coordinate': coord
}

properties = pd.DataFrame.from_dict(my_dict)

properties.to_csv('shop.csv')
