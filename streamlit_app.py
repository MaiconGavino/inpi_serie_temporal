import streamlit as st
import pandas as pd

def main():
    df = pd.read_excel("inpi_db.xlsx", decimal='.')
    st.dataframe(df)
    
if __name__ == '__main__':
    main()