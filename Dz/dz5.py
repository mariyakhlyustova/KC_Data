import pandas as pd


retail = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-m-hljustova/Pd_pet/5_data.csv.zip', encoding='ISO-8859-1', compression='zip')

retail

retail.columns

retail_columns = retail.columns

retail_columns

retail_no_duplicates = retail.drop_duplicates()

retail_no_duplicates

duplicates = retail.shape[0] - retail_no_duplicates.shape[0]

duplicates

retail_c = retail_no_duplicates.InvoiceNo.str.startswith('C').value_counts()

retail_c

retail_no_duplicates.dtypes

retail = retail_no_duplicates.query('Quantity > 0')

retail.shape[0]

germany_top = retail.query('Country == "Germany"')\
      .groupby('CustomerID', as_index=False)\
      .agg({'InvoiceNo': 'nunique'})\
      #.quantile(q = 0.8)\
      #.query

germany_top

n = germany_top.InvoiceNo.quantile(0.8)

n

germany_top = germany_top.query('InvoiceNo > @n')

germany_top

germany_top = germany_top.CustomerID

germany_top

top_retail_germany = retail.query('CustomerID in @germany_top')

top_retail_germany

top_retail_germany.query('StockCode != "POST"')\
                  .groupby('StockCode', as_index=False)\
                  .agg({'Quantity':'count'})\
                  .sort_values('Quantity')

retail

retail['Revenue'] = retail.Quantity * retail.UnitPrice

retail

top_retail = retail.groupby('InvoiceNo', as_index=False)\
      .agg({'Revenue':'sum'})\
      .sort_values('Revenue', ascending=False) \
      .head()

top_InvoiceNo = top_retail.InvoiceNo.apply(lambda x: int(x)).to_list()

top_InvoiceNo