import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import statsmodels.formula.api as sm
import seaborn as sns
from pprint import pprint
import wbdata

ind = pd.read_csv('individual.csv')
ind['region'] = 'region'
ind['income'] = 'income'


### Add a 'region' column using wbdata

# requires changing some country name data
for idx, item in enumerate(ind['country']):
   if 'Bosnia Herzegovina' in item:
       ind['country'][idx] = 'Bosnia and Herzegovina'

for idx, item in enumerate(ind['country']):
   if 'South Korea' in item:
       ind['country'][idx] = 'Korea, Rep.'


country_list = list(ind['country'])
new_country_set = sorted(set(country_list))



country_name = []
region = []
income = []

for country in new_country_set:
    hoop = wbdata.search_countries(country)
    for key, val in hoop[0].items():
        if key == 'name':
            country_name.append(val)
        if key == 'region':
            region.append(val['value'])
        if key == 'incomeLevel':
            income.append(val['value'])

data = pd.DataFrame()
data['country'] = country_name
data['region'] = region
data['income'] = income

data['country'][59] = 'South Africa'          ### Don't forget about me!!!
data['region'][59] = 'Sub-Saharan Africa '
data['income'][59] = 'Upper middle income'
data['country'][19] = 'Egypt'
data['country'][32] = 'Iran'
data['country'][55] = 'Russia'
data['country'][73] = 'Venezuela'



for country in new_country_set:
    yellow = data.loc[(data['country'] == country)] # the row in data where country = Afghanistan - there is only one
    ind.loc[ind['country'] == country, 'income'] = yellow['income'].values
    ind.loc[ind['country'] == country, 'region'] = yellow['region'].values

ind.to_csv('new_individual.csv')












