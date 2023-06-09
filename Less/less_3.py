import pandas as pd
from google.colab import drive
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline


df = pd.read_csv('/content/drive/MyDrive/Data/lesson_3_data_1_.csv', encoding='windows-1251')

user_df = df[['tc', 'art_sp']]

user_df

user_df = user_df.rename(columns={'tc':'user', 'art_sp':'brand'})

user_df 

user_df.brand

# brand_name = 'MARAVILLA 500 G Store_Brand'
# brand_name.split(' ')[-1]
#   def split_brand(brand_df):
#     return brand_df.split(' ')[-1]
# split_brand(brand_name)
# Store_Brand
# user_df ['brand_name'] = user_df.brand.apply(split_brand)

# lambda x: x.split(' ')[-1]
# def f(x):
#   return x.split(' ')[-1]

user_df ['brand_name'] = user_df.brand.apply(lambda x: x.split(' ')[-1])

user_df.head()

buy_count = user_df.groupby('user', as_index=False)\
                   .agg({'brand_name':'count'})\
                   .rename(columns={'brand_name':'counts_buys'})\
                   .query('counts_buys >= 5')

user_unique_brand = user_df.groupby('user', as_index=False)\
                           .agg({'brand_name':pd.Series.nunique})\
                           .rename(columns={'brand_name':'unique_brand'})

lovely_brand_bay_df = user_df.groupby(['user', 'brand_name'], as_index=False)\
       .agg({'brand':'count'})\
       .sort_values(['user', 'brand'], ascending=[False, False])\
       .groupby('user')\
       .head(1)\
       .rename(columns={'brand_name':'lovely_brand', 'brand': 'lovely_brand_bay'})

loyalty_df = buy_count.merge(user_unique_brand, on='user')\
         .merge(lovely_brand_bay_df, on='user')

loyalty_df.head()

loyal_user = loyalty_df[loyalty_df.unique_brand ==1]

loyalty_df['loyalty_score'] = loyalty_df.lovely_brand_bay/loyalty_df.counts_buys

loyalty_df

ax = sns.distplot(loyalty_df.loyalty_score, kde=False)

brands_loyalty = loyalty_df.groupby('lovely_brand',  as_index=False)\
          .agg({'loyalty_score':'median', 'user':'count'})

ax = sns.barplot(x='lovely_brand', y='user', data=brands_loyalty)



