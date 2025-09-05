import streamlit as st
from src.extraction import load_data

# stramlit page configs
st.set_page_config(layout='wide')


# Data description modification

# Remote repository updated, now it's diff from local one -- Answears section

def main():
  df = load_data()

  # callign data modification section

  # calling answears section

  st.dataframe(df)

if __name__ == '__main__':
  main()
