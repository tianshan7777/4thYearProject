import pandas as pd 

shop_types = []

shops = pd.read_csv('./poi/shop.csv')

poi_types = shops['poi type']

for i in poi_types:
	print(i)
	
	if i == 'alcohol':
		shop_types.append('food, beverages')
	elif i == 'bakery':
		shop_types.append('food, beverages')
	elif i == 'beverages':
		shop_types.append('food, beverages')
	elif i == 'brewing_supplies':
		shop_types.append('food, beverages')
	elif i == 'butcher':
		shop_types.append('food, beverages')
	elif i == 'cheese':
		shop_types.append('food, beverages')
	elif i == 'chocolate':
		shop_types.append('food, beverages')
	elif i == 'coffee':
		shop_types.append('food, beverages')
	elif i == 'confectionery':
		shop_types.append('food, beverages')
	elif i == 'convenience':
		shop_types.append('food, beverages')
	elif i == 'deli':
		shop_types.append('food, beverages')
	elif i == 'diary':
		shop_types.append('food, beverages')
	elif i == 'farm':
		shop_types.append('food, beverages')
	elif i == 'frozen_food':
		shop_types.append('food, beverages')
	elif i == 'greengrocer':
		shop_types.append('food, beverages')
	elif i == 'health_food':
		shop_types.append('food, beverages')
	elif i == 'ice_cream':
		shop_types.append('food, beverages')
	elif i == 'pasta':
		shop_types.append('food, beverages')
	elif i == 'pastry':
		shop_types.append('food, beverages')
	elif i == 'seafood':
		shop_types.append('food, beverages')
	elif i == 'spices':
		shop_types.append('food, beverages')
	elif i == 'tea':
		shop_types.append('food, beverages')
	elif i == 'water':
		shop_types.append('food, beverages')
	elif i == 'department_store':
		shop_types.append('Department Store')
	elif i == 'general':
		shop_types.append('Convenience')
	elif i == 'kiosk':
		shop_types.append('Convenience shop')
	elif i == 'mall':
		shop_types.append('Mall')
	elif i == 'supermarket':
		shop_types.append('Supermarket')
	elif i == 'wholesale':
		shop_types.append('Wholesale')	
	elif i == 'baby_goods':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'bag':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'boutique':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'clothes':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'fabric':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'fashion':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'jewelry':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'leather':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'sewing':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'shoes':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'tailor':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'watches':
		shop_types.append('Clothing, shoes, accessories')
	elif i == 'charity':
		shop_types.append('Discount store, charity')
	elif i == 'second_hand':
		shop_types.append('Discount store, charity')
	elif i == 'variety_store':
		shop_types.append('Discount store, charity')
	elif i == 'beauty':
		shop_types.append('Beauty')
	elif i == 'chemist':
		shop_types.append('Beauty')
	elif i == 'cosmetics':
		shop_types.append('Beauty')
	elif i == 'hairdresser':
		shop_types.append('Beauty')
	elif i == 'hairdresser_supply':
		shop_types.append('Beauty')
	elif i == 'hearing_aids':
		shop_types.append('Health')
	elif i == 'herbalist':
		shop_types.append('Health')
	elif i == 'massage':
		shop_types.append('Health')
	elif i == 'medical_supply':
		shop_types.append('Health')
	elif i == 'nutrition_supplements':
		shop_types.append('Health')
	elif i == 'optician':
		shop_types.append('Health')
	elif i == 'perfumery':
		shop_types.append('Beauty')
	elif i == 'tattoo':
		shop_types.append('Beauty')
	elif i == 'art':
		shop_types.append('Art, music, hobbies')
	elif i == 'collector':
		shop_types.append('Art, music, hobbies')
	elif i == 'craft':
		shop_types.append('Art, music, hobbies')
	elif i == 'frame':
		shop_types.append('Art, music, hobbies')
	elif i == 'games':
		shop_types.append('Art, music, hobbies')
	elif i == 'model':
		shop_types.append('Art, music, hobbies')
	elif i == 'music':
		shop_types.append('Art, music, hobbies')
	elif i == 'musical_instrument':
		shop_types.append('Art, music, hobbies')
	elif i == 'photo':
		shop_types.append('Art, music, hobbies')
	elif i == 'camera':
		shop_types.append('Art, music, hobbies')
	elif i == 'trophy':
		shop_types.append('Art, music, hobbies')
	elif i == 'video':
		shop_types.append('Art, music, hobbies')
	elif i == 'video_games':
		shop_types.append('Art, music, hobbies')
	elif i == 'anime':
		shop_types.append('Stationery, gifts, books, newspapers')
	elif i == 'books':
		shop_types.append('Stationery, gifts, books, newspapers')
	elif i == 'gift':
		shop_types.append('Stationery, gifts, books, newspapers')
	elif i == 'lottery':
		shop_types.append('Stationery, gifts, books, newspapers')
	elif i == 'newsagent':
		shop_types.append('Stationery, gifts, books, newspapers')
	elif i == 'stationery':
		shop_types.append('Stationery, gifts, books, newspapers')
	elif i == 'ticket':
		shop_types.append('Stationery, gifts, books, newspapers')
	elif i == 'laundry':
		shop_types.append('Laundry')
	elif i == 'religion':
		shop_types.append('Religin')
	elif i == 'travel_agency':
		shop_types.append('Travel Agency')
	else:
		shop_types.append('others')

shops['shop_types'] = pd.Series(shop_types)
shops.to_csv('shop_clean.csv', index=False)






