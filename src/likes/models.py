from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey

from src.anime.models import anime
from src.auth.models import user

likes_metadata = MetaData()

likes = Table(
    "like",
    likes_metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("anime_id", Integer, ForeignKey(anime.c.id))
)
