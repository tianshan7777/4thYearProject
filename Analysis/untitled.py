import pandas as pd
import numpy as np
from itertools import combinations

#To record every average score
total_r2 = []
total_adj_r2 = []

#List all the attributes that both ingatlan and alberlet have
attributes = ['apartment', 'house', 'number_of_whole_rooms', 'floor', 'number_of_half_rooms', 'furnish_furnished', 'furnish_partly_furnished', 'view_garden', 'view_panoramic', 'view_street', 'balcony', 'lift', 'air_conditioner', 'utility_double_comfort', 'heating_gas', 'heating_wall_heating', 'heating_combination', 'heating_ceiling', 'heating_central_heating', 'heating_electric', 'heating_floor', 'heating_circulating', 'heating_district', 'available_immediately', 'condition_of_property_renovated', 'parking']

my_list = list(combinations(attributes, 21))

my_list = [list(item) for item in my_list]

print(my_list[8752])