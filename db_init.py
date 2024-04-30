import pandas as pd
from sqlalchemy import create_engine


conn_string = 'postgresql://postgres:1337@localhost/anime'
    
db = create_engine(conn_string) 
conn = db.connect()

data = pd.read_csv('anime_data.csv').drop(['Unnamed: 6'], axis = 1)

data.to_sql('anime_info', con=conn, if_exists='replace', index=False)




