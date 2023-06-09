import pandas as pd
import os

folder_data = [i for i in os.listdir('/home/jupyter-an.karpov/shared/Res_Tree') if not i.startswith('.')]

# for i in folder_data:
#     if not i.startswith('.'):
#         print(i)

# [i for i in folder_data if not i.startswith('.')]

# x = ['1', '2', 'start', '3', '4', 'end', '5', '6', 'start', '7', '8', 'end']
# scanning = False
# for i in x:
#     if i == 'end':
#         scanning = False
#         continue    
    
#     if scanning:
#         print(i)
    
    
#     if i == 'start':
#         scanning = True
#         continue



folder_data

p = '/home/jupyter-an.karpov/shared/Res_Tree/F000545/res_2019.09.11_0.0_6493B6_Container-dat_2125_91-105-165_F000545/meals_list_2.txt'
          
          

all_data = open(p).readlines()



all_data = []

scanning = False
for i in meal_data:
    if i.startswith('-------------'):
        scanning = False
        continue    
        
    if scanning:
        if 'Meal#;' in i:
            col_name = i
            continue
        all_data.append([value.strip() for value in i.split(';')])
        
    
    if 'Non-deleted saved meals' in i:
        scanning = True
        continue
        



final_col_names = [col.strip() for col in col_name.split(';')]



meal_df = pd.DataFrame(all_data, columns=final_col_names[0:17])

meal_df = meal_df.astype({'Minutes': 'int', 'Pro': 'float'})

meal_df.head()

meal_df['Date'] = pd.to_datetime(meal_df.Date)

user_meal_df = meal_df[['Date', 'Pro', 'Minutes']]



df = user_meal_df.groupby('Date', as_index=False) \
    .agg({'Minutes': 'sum'})

df.to_csv('df_minutes.csv', index=False)

