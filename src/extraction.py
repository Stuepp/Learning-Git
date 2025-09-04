import pandas as pd

READ_DATA = 'data/processed/bike_completed.csv'

def load_data():
  return pd.read_csv(READ_DATA)