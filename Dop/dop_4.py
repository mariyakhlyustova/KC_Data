import pandas as pd

inn = pd.read_excel('/mnt/HC_Volume_18315164/home-jupyter/jupyter-m-hljustova/shared/homeworks/python_ds_miniprojects/4_inn/inn.xls')

inn = inn.rename(columns = {'income,RUB' : 'income_RUB'})

iin = pd.read_csv('~/home/jupyter-m-hljustova/shared/homeworks/python_ds_miniprojects/4_inn/necessary_inn.txt', header = None)

ini = iin[0].tolist()

inn = inn.query('head_inn in @ini').sum()

inn['income_RUB']

