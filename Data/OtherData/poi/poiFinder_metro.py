import json
import pandas as pd

shape = []
coord = []
poi_type = []
railway_type = []

with open('metro_station.geojson') as f:
	data = json.load(f)

for feature in data['features']:
	print('---------Start--------')

	if 'public_transport' in feature['properties']:
		print(feature['properties']['public_transport'])
		poi_type.append(feature['properties']['public_transport'])
	else:
		print('error')
		poi_type.append(-1)

	if 'railway' in feature['properties']:
		print(feature['properties']['railway'])
		railway_type.append(feature['properties']['railway'])
	else:
		print('error')
		railway_type.append(-1)

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
	'coordinate': coord,
	'railway type': railway_type
}

properties = pd.DataFrame.from_dict(my_dict)

properties.to_csv('metro_station.csv')

