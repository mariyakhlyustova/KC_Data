import seaborn as sns
import pandas as pd



taxi = pd.read_csv('/content/3_taxi_peru.csv', parse_dates=['start_at', 'end_at', 'arrived_at'], sep = ';')

taxi

sns.countplot(x = taxi['icon'], data = taxi)

sns.countplot(x = taxi['source'], data = taxi, hue = taxi['end_state'])

taxi.driver_score

score_counts = taxi.driver_score.value_counts()

score_counts

all_score = score_counts.sum()

all_score

driver_score_counts = score_counts.apply(lambda x: x/all_score)\
 .mul(100).round(2).reset_index()\
 .rename(columns={'index':'driver_score', 'driver_score': 'percentage'})\
 .sort_values('driver_score')

taxi.rider_score.value_counts(normalize=True)

rider_score_counts = taxi.rider_score.value_counts(normalize=True)\
                         .mul(100).round(2).reset_index()\
                         .rename(columns={'index':'rider_score', 'rider_score': 'percentage'})\
                         .sort_values('rider_score')

driver_score_counts

rider_score_counts