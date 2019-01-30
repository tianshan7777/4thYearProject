import json
import pandas as pd

shape = []
coord = []
poi_type = []

with open('tourism.geojson') as f:
	data = json.load(f)

for feature in data['features']:
	print('---------Start--------')

	if 'tourism' in feature['properties']:
		print(feature['properties']['tourism'])
		poi_type.append(feature['properties']['tourism'])
	else:
		print(feature['properties']['@relations'][0]['reltags']['tourism'])
		poi_type.append(feature['properties']['@relations'][0]['reltags']['tourism'])

	print(feature['geometry']['type'])
	shape.append(feature['geometry']['type'])

	if feature['geometry']['type'] == 'Polygon':
		print(feature['geometry']['coordinates'][0][0])
		coord.append(feature['geometry']['coordinates'][0][0])
	elif feature['geometry']['type'] == 'LineString':
		print(feature['geometry']['coordinates'][0])
		coord.append(feature['geometry']['coordinates'][0])
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

properties.to_csv('tourism.csv')
