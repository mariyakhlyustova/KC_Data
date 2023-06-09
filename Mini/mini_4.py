import pandas as pd
import os
import seaborn as sns

way = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-m-hljustova/shared/homeworks/python_ds_miniprojects/4/data/'

way

os.listdir(way)

way1 = way + '/' + os.listdir(way)[0]
way2 = way1 + '/' + os.listdir(way1)[0]
way3 = way2 + '/' + os.listdir(way2)[0]
df = pd.read_csv(way3)
df['name'] = os.listdir(way1)[0]
df['date'] = os.listdir(way)[0]

df

date = 0
df = pd.DataFrame()
for i in os.listdir(way):
    way1 = way + '/' + os.listdir(way)[date]
    date +=1
    name = 0
    for j in os.listdir(way1):
        way2 = way1 + '/' + os.listdir(way1)[name]
        way3 = way2 + '/' + os.listdir(way2)[0]
        df1 = pd.read_csv(way3)
        df1['name'] = j
        df1['date'] = i
        df = pd.concat([df, df1])
        name +=1

df

df6 = df.drop_duplicates(subset = ['product_id', 'name', 'date'])

df6.groupby(['name', 'product_id'], as_index = False)\
   .agg({'date': 'count'})\
   .query('date > 1')



df5 = df.groupby('date', as_index = False)\
    .agg({'quantity': 'sum'})

df5

ax = sns.barplot(x = df5.date, y = df5.quantity)



df4 = df.groupby('product_id', as_index = False)\
    .agg({'quantity': 'sum'})

df.query('product_id == 56').sum()

ax = sns.barplot(x = df4.product_id, y = df4.quantity)



df.quantity.sum()



df.groupby('name', as_index = False)\
    .agg({'quantity': 'sum'})



way1 = way + '/' + os.listdir(way)[0]  # os.path.join is better for constructing path

way1

os.listdir(way1)

way2 = way1 + '/' + os.listdir(way1)[0]

way2

 os.listdir(way2)[0]

way3 = way2 + '/' + os.listdir(way2)[0]

way3

date = os.listdir(path)[0]  # os.path.join is better for constructing path
name = os.listdir(path)[-1]

date

name