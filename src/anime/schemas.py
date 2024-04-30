from pydantic import BaseModel


class AnimeAdd(BaseModel):
    id: int
    title_rus: str
    title_alt: str
    genre: str
    rating: float
    caption: str
    image: str