from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.anime.models import anime
from src.anime.schemas import AnimeAdd
from src.database import get_async_session

router = APIRouter(
    prefix='/anime',
    tags=['Anime']
)


@router.get('/get_anime_list')
async def get_anime_list(offset: int, session: AsyncSession = Depends(get_async_session)):
    query = select(anime).offset(offset).limit(10)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router.get('/get_anime_info')
async def get_anime_info(idx: int, session: AsyncSession = Depends(get_async_session)):
    query = select(anime).where(anime.c.id == idx)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]

@router.post('/add_anime')
async def add_anime(anime_info: AnimeAdd, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(anime).values(**anime_info.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 200}
