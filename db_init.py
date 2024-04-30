import pandas as pd
from sqlalchemy import create_engine, NullPool
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

conn_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

db = create_engine(conn_string)
conn = db.connect()

data = pd.read_csv('anime_data.csv')

data.to_sql('anime', if_exists='append', con=conn, index=False)




