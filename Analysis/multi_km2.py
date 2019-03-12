import pandas as pd
from sklearn.model_selection import KFold
#OLS
from sklearn.linear_model import LinearRegression
import numpy as np
from itertools import combinations

#To record every average score
total_r2 = []
total_adj_r2 = []

#List all the attributes that both ingatlan and alberlet have
attributes = ['apartment', 'house', 'number_of_whole_rooms', 'floor', 'number_of_half_rooms', 'furnish_furnished', 'furnish_partly_furnished', 'view_garden', 'view_panoramic', 'view_street', 'balcony', 'lift', 'air_conditioner', 'utility_double_comfort', 'heating_gas', 'heating_wall_heating', 'heating_combination', 'heating_ceiling', 'heating_central_heating', 'heating_electric', 'heating_floor', 'heating_circulating', 'heating_district', 'available_immediately', 'condition_of_property_renovated', 'parking']

my_list = list(combinations(attributes, 18))

my_list = [list(item) for item in my_list]

#print( my_list)

#Load data
data = pd.read_csv('kmeans_1.csv')
data = data[data.cluster == 0]

for item in my_list:
	test = data[item + ['price_per_sqm']]
	test = test.dropna()

	X = test[item]
	y = test['price_per_sqm']

	scores = []
	cv = KFold(n_splits = 10, random_state = 42, shuffle = False)
	for train_index, test_index in cv.split(X):

		X_train, X_test, y_train, y_test = X.iloc[train_index.tolist()], X.iloc[test_index], y.iloc[train_index], y.iloc[test_index]
		my_model = LinearRegression().fit(X_train, y_train)
		scores.append(my_model.score(X_test, y_test))

	r_square = np.mean(scores)
	adj_r = 1-(1-r_square)*(len(y)-1)/(len(y)-X.shape[1]-1)

	total_r2.append(r_square)
	total_adj_r2.append(adj_r)

	print('R Square:', r_square, '\n')
	print('Adjusted R Square:', adj_r, '\n')
	print('________________________________________________')

max_r2 = total_r2.index(max(total_r2))
max_adj_r2 = total_adj_r2.index(max(total_adj_r2))

#print('all combinations:', my_list, '\n')

#print('all R square:', total_r2, '\n')

#print('all adj R square:', total_adj_r2, '\n')

print('max R square', max(total_r2), 'index', max_r2, '\n')
print('max adjusted R sqaure', max(total_adj_r2), 'index', max_adj_r2, '\n')

print('max R square combination:', my_list[max_r2], '\n')
print('max ajd R square combination:', my_list[max_adj_r2], '\n')


