import streamlit as st
from src.extraction import load_data

# stramlit page configs
st.set_page_config(layout='wide')


# Data description modification

def main():
  df_raw = load_data()

  # callign data modification section

  st.dataframe(df_raw)

if __name__ == '__main__':
  main()