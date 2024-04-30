from sqlalchemy import MetaData, Table, Column, Integer, String, Double

anime_metadata = MetaData()

anime = Table(
    "anime",
    anime_metadata,
    Column('id', Integer, primary_key=True),
    Column('title_rus', String),
    Column('title_alt', String),
    Column('genre', String),
    Column('rating', Double),
    Column('caption', String),
    Column('image', String)
)
