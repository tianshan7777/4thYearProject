import json
import pandas as pd

shape = []
coord = []
poi_type = []

with open('leisure.geojson') as f:
	data = json.load(f)

for feature in data['features']:
	print('---------Start--------')

	if 'leisure' in feature['properties']:
		print(feature['properties']['leisure'])
		poi_type.append(feature['properties']['leisure'])
	else:
		print(feature['properties']['@relations'][0]['reltags']['leisure'])
		poi_type.append(feature['properties']['@relations'][0]['reltags']['leisure'])

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

properties.to_csv('leisure.csv')