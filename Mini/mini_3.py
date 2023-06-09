import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline

user_data = pd.read_csv('/content/3_user_data.csv')

logs = pd.read_csv('/content/3_logs.csv')

user_data.describe()

user_data.dtypes

logs.dtypes

user_logs = user_data.merge(logs, on = 'client')

age_platform = user_logs[['platform', 'success', 'age']]

age = age_platform.query('success == True and platform == "computer"')

sns.countplot(x = age.age, data = age)

age_premium = user_logs[['premium', 'age']]

a = age_premium.query('premium == True')

b = age_premium.query('premium == False')

sns.distplot(a.age)
sns.distplot(b.age)

platform_premium = user_logs[['premium', 'platform']]


platform_premium.query('premium == True')\
              .groupby('platform', as_index=False)\
              .agg({'premium':'count'})



success_platform = logs[['platform', 'success']]

success_platform.platform.unique()

age_platform = logs[['platform', 'success', 'age']]

c = success_platform.query('success == True' and 'platform == "computer"')

c

success_platform.query('success == True').value_counts()

logs.platform.unique()

client_success = logs[['client', 'success']]

client_success

pip = client_success.groupby('client', as_index=False)\
              .agg({'success':'count'})

pip

sns.distplot(pip.success)

client_success_max = client_success.query('success == True')\
              .groupby('client', as_index=False)\
              .agg({'success':'count'})\
              .sort_values('success')\
              .query('success == 41')\
              .sort_values('client')

client_success_max.client.tolist()



client_success.query('success == True')\
              .groupby('client', as_index=False)\
              .agg({'success':'count'})\
              .sort_values('success')
              



