from sqlalchemy import MetaData, Table, Column, Integer, String, Double

anime_metadata = MetaData()

anime = Table(
    "anime",
    anime_metadata,
    Column('id', Integer, primary_key=True),
    Column('title_rus', String, nullable=False),
    Column('title_alt', String, nullable=False),
    Column('genre', String, nullable=False),
    Column('rating', Double, nullable=False),
    Column('caption', String),
    Column('image', String)
)
