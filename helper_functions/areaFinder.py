import math

EARTH_R = 6378.1

#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 0.840
#Budapest inside built-up area speed limit: 50km/h
DRIVING_DIS = 8.3

radiu_w = WALKING_DIS / EARTH_R
radiu_d = DRIVING_DIS / EARTH_R

def find_lat(lat):
	lat_min_w = lat - radiu_w
	lat_max_w = lat - radiu_d

	return (lat_min_w, lat_max_w)
