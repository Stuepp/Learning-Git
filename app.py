import streamlit as st
from src.extraction import load_data

# stramlit page configs
st.set_page_config(layout='wide')


# Data description modification

# Remote repository updated, now it's diff from local one -- Answears section

def print_msg(msg):
  print(f'{msg}')
  return None

def main():
  df_raw = load_data()
  ping = 'pong'

  print_msg(ping)

  # callign data modification section

  # calling answears section

  return None

if __name__ == '__main__':
  main()
