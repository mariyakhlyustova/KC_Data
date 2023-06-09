import pandas as pd


from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/2_taxi_nyc.csv')

df

df.dtypes


taxi = df

taxi.columns

taxi = taxi.rename(columns = {'pcp 01' : 'pcp_01', 'pcp 06' : 'pcp_06', 'pcp 24' : 'pcp_24'})

taxi[['borough', 'hday', 'pickups']]

taxi.pickups.sum()

taxi.groupby('borough').aggregate({'pickups': 'sum'})

min_pickups = taxi.groupby('borough').aggregate({'pickups': 'sum'}).idxmin()

min_pickups

taxi.query("hday == 'Y'" ).groupby('borough', as_index = False).aggregate({'pickups': 'sum'})

pickups_by_mon_bor = taxi.groupby(['borough', 'pickup_month'], as_index = False)\
    .aggregate({'pickups': 'sum'})\
    .sort_values('pickups', ascending = False)

pickups_by_mon_bor

pickup_mean = taxi.groupby(['borough', 'hday'])\
    .aggregate({'pickups': 'mean'})

pickup_mean

pickup_mean.to_csv('pickup_mean.csv') # save file in csv

def temp_to_celcius(fr):
  cel = (fr - 32)*5/9
  return cel

taxi['temp'][:5]


taxi['temp_C'] = temp_to_celcius(taxi['temp'])


taxi['temp_C'][:5]