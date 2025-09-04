import pandas as pd
import numpy as np
import streamlit as st

READ_DATA = 'data/processed/bike_completed.csv'

def load_data():
  return pd.read_csv(READ_DATA)

def main():
  df = load_data()

  st.dataframe(df)

if __name__ == '__main__':
  main()