import pandas as pd

bookings = pd.read_csv('/content/KC/2_bookings.csv', sep = ';')

bookings.describe()

bookings

bookings_head = bookings.head(7)

bookings.dtypes.sort_values()

bookings.columns = bookings.columns.str.replace(' ', '_').str.lower()

bookings.columns

br = bookings[['country', 'is_canceled']]

br.query("is_canceled == 0" ).value_counts()

ht = bookings[['hotel','stays_total_nights']]

ht.query("hotel == 'City Hotel'").aggregate({'stays_total_nights': 'mean'}).round(2)

ht.query("hotel == 'Resort Hotel'").aggregate({'stays_total_nights': 'mean'}).round(2)

er = bookings[['reserved_room_type','assigned_room_type']]

er[er['assigned_room_type'] != er['reserved_room_type']].value_counts().sum()

ym = bookings[['arrival_date_year', 'arrival_date_month']]

ym.query('arrival_date_year == 2016').value_counts()

ym.query('arrival_date_year == 2017').value_counts()

yb = bookings[['hotel', 'is_canceled', 'arrival_date_year', 'arrival_date_month']]

yb

yb.query("hotel == 'City Hotel'").query('is_canceled == 1').query('arrival_date_year == 2015').value_counts()

yb.query("hotel == 'City Hotel'").query('is_canceled == 1').query('arrival_date_year == 2016').value_counts()

yb.query("hotel == 'City Hotel'").query('is_canceled == 1').query('arrival_date_year == 2017').value_counts()

litle = bookings[['adults', 'children', 'babies']]

litle.mean()

bookings['total_kids'] = bookings.children + bookings.babies

ch = bookings[['hotel', 'total_kids']]

ch

ch.groupby('hotel').aggregate({'total_kids': 'mean'}).round(2)

bookings.total_kids

bookings['has_kids'] = bookings.total_kids > 0

bookings.has_kids

ya = bookings[['has_kids', 'is_canceled']]

ya

chis = ya.query('has_kids == True').query('is_canceled == 1').shape[0]

zn = ya.query('has_kids == True').shape[0]

zn

cr = chis/zn*100

cr

chis1 = ya.query('has_kids == False').query('is_canceled == 1').shape[0]

zn1 = ya.query('has_kids == False').shape[0]

zn1

zn +zn1

cr1 = chis1/zn1*100

cr1