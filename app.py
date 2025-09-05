import streamlit as st
from src.extraction import load_data

# stramlit page configs
st.set_page_config(layout='wide')


# Data description modification

# Remote repository updated, now it's diff from local one -- Answears section

def main():
  df_paw = load_data()

  # callign data modification section

  # little junior aka juninho added - calling answear section to main - app.py

  st.dataframe(df_paw)

if __name__ == '__main__':
  main()
