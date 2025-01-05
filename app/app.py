#import
import pandas as pd
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

st.dataframe(df)