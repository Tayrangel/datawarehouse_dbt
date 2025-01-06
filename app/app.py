#import
import pandas as pd
import numpy as np
import os
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

#import das variáveis de ambiente
dotenv_path = os.path.join(os.path.dirname(__file__), '../src/.env')
load_dotenv(dotenv_path=dotenv_path)

#Conexão com banco de dados
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

#Função
def get_data():
    query = f"""
        SELECT 
            * 
        FROM public.fct_commodities
    """
    df = pd.read_sql(query, engine)
    return df

#Streamlit page
st.set_page_config(page_title='Dashboard - Commodities', layout='wide')
st.title('Dashboard - Commodities')
st.write('Here you will find information about commodities')

df = get_data()

#Line chart
df['extract_dt'] = pd.to_datetime(df['extract_dt']).dt.strftime('%Y-%m-%d') #'extract_dt' to date
df_pivot = df.pivot_table(index='extract_dt', columns='symbol', values='profit_vl', aggfunc='sum') #Grouping the data to have column for 'symbol' and 'profit_vl'

st.subheader("Commodities by profit")
st.line_chart(df_pivot)

#Bar chart and table
df_grouped = df.groupby(['extract_dt', 'action']).agg({'total_vl': 'sum'}).reset_index() #Grouping the data by 'extract_dt' and 'action'
df_pivot_action = df_grouped.pivot_table(index='extract_dt', columns='action', values='total_vl', aggfunc='sum', fill_value=0) #Pivot table to have columns for 'action'

col1, col2 = st.columns(2) #Layout to show the bar chart and the table

with col1:
    st.subheader("Buying and selling commodity stocks")
    st.bar_chart(df_pivot_action)

with col2:
    st.subheader("Commodities table")
    st.dataframe(df, use_container_width=True) #Table with all width of the container