from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession

from src.anime.models import anime
from src.anime.schemas import AnimeAdd
from src.database import get_async_session

router = APIRouter(
    prefix='/anime',
    tags=['Anime']
)


@router.get('/get_anime_list')
async def get_anime_list(page: int, list_size: int, session: AsyncSession = Depends(get_async_session)):
    query = select(anime).offset((page - 1) * list_size).limit(list_size)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router.get('/ordered_anime_list_by_alphabet')
async def get_in_alphabet_order(page: int, list_size: int, session: AsyncSession = Depends(get_async_session)):
    query = select(anime).order_by(anime.c.title_rus).offset((page - 1) * list_size).limit(list_size)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router.get('/ordered_anime_list_by_rating')
async def ordered_anime_list_by_rating(order_type: int, page: int, list_size: int,
                                       session: AsyncSession = Depends(get_async_session)):
    if not order_type:
        query = select(anime).order_by(desc(anime.c.rating)).offset((page - 1) * list_size).limit(list_size)
    else:
        query = select(anime).order_by(asc(anime.c.rating)).offset((page - 1) * list_size).limit(list_size)
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
