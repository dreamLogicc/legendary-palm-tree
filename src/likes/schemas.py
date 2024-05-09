from pydantic import BaseModel


class Like(BaseModel):
    user_id: int
    anime_id: int
