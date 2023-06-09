import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline 

df = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-m-hljustova/Pd_pet/transaction_data.csv')

df.head()

df.query('transaction == "successfull"')\
  .groupby('name', as_index=False)\
  .agg({'transaction': 'count'})\
  .sort_values('transaction', ascending=False)

df_succ = df.query('transaction == "successfull"')\
  .groupby('name', as_index=False)\
  .agg({'transaction': 'count'})

ax = sns.distplot(df_succ.transaction)

df_succ.describe()

df.dtypes

df.describe()

top_transaction = df.transaction.value_counts()

top_transaction

df1 = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-m-hljustova/Pd_pet/transaction_data_updated.csv')

df1.head()

df1['date'] = pd.to_datetime(df1.date)

df1['true_minute'] = df1.date.dt.hour * 60 + df1.date.dt.minute

df1.head()

df1 = df1.groupby('true_minute', as_index=False)\
   .agg({'transaction': 'count'})\

ax = sns.barplot(x='true_minute', y='transaction', data=df1)

df1.dtypes

df1.describe()

user_vs_minute_pivot = df1.groupby(['minute', 'name'], as_index=False)\
   .agg({'transaction': 'count'})\
   .pivot(index='minute', columns='name', values='transaction')\
   .reset_index()\
   .fillna(0)

user_vs_minute_pivot

