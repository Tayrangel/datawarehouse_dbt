#import
import yfinance as yf
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

#import das variáveis de ambiente
load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F'] # Adicionar outros ativos depois de testar os primeiro , 'HG=F', 'PL=F', 'PA=F', 'NG=F', 'RB=F', 'HO=F', 'ZC=F', 'ZW=F', 'ZS=F', 'ZL=F', 'ZM'

#Conexão com banco de dados
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

#Funções
#Extrair a cotação dos ativos
def search_data_commodities(symbol, period ='5d', interval = '1d'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period = period, interval = interval)[['Close']]
    data['symbol'] = symbol
    return data

def search_all_data_commodities(commodities):
    all_data = []
    for symbol in commodities:
        data = search_data_commodities(symbol)
        all_data.append(data)
    return pd.concat(all_data)

def save_data_postgres(df, schema='public'):
    df.to_sql('commodities', engine, schema=schema, if_exists='replace', index=True, index_label='date')

#Concatenar os ativos e salvar
if __name__ == "__main__":
    concat_data = search_all_data_commodities(commodities)
    save_data_postgres(concat_data, schema='public')
    