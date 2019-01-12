#A cleaner for cleanning data in s_alberlet_apas.csv
import pandas as pd
import numpy as np

#transform rows to columns
data = pd.read_csv('realestatehungary_rent_apas.csv')
data.T.to_csv('c_realestatehungary_rent_apas.csv',header=False)

#Drop the first column
#data = pd.read_csv('./data/output.csv', )
#data.drop('Unnamed: 0', axis = 1, inplace = True)

#Go through the whole sheet and fill empty cells with -1
