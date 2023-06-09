import pandas as pd
import seaborn as sns

taxi = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-m-hljustova/Pd_pet/3_taxi_peru.csv', parse_dates=['start_at', 'end_at', 'arrived_at'], sep = ';')

taxi

taxi['month'] = taxi.start_at.dt.month

taxi

taxi1 = taxi.groupby('month', as_index = False)\
    .agg({'user_id': 'nunique'})

taxi1

ax = sns.barplot(x = taxi1.month, y = taxi1.user_id )

ax = sns.countplot(taxi.month)

taxi['weekday'] = taxi.start_at.dt.strftime('%A')

ax = sns.countplot(taxi['weekday'], order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

taxi.weekday.unique()

taxi = taxi.query('start_type == "asap" or start_type == "reserved"')

taxi['wait_time'] = (taxi.arrived_at - taxi.start_at).astype('timedelta64[m]')

taxi.query('start_type == "reserved" and wait_time > 0.0')\
    .groupby('driver_id')\
    .agg({'driver_id': 'count'})\
    .idxmax()
    

taxi.shape[0]

taxi.shape[1]

df_shape = f'df has {taxi.shape[0]} rows and {taxi.shape[1]} columns'

df_shape

taxi.isna().sum()

taxi.dtypes

df = df.astype({'age': 'int'})

df = df.drop(columns=['sex', 'age'])

taxi.drop_duplicates(subset='user_id')

