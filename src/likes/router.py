from fastapi import APIRouter, Depends
from sqlalchemy import insert, delete, select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.anime.models import anime
from src.auth.models import User
from src.database import get_async_session
from src.likes.models import likes
from src.likes.schemas import Like

router = APIRouter(prefix='/likes', tags=['Likes'])


@router.post('/add_to_liked')
async def add_liked(like: Like, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(likes).values(**like.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 200}


@router.post('/remove_from_liked')
async def remove_from_liked(like: Like, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(likes).where(
        and_(likes.c.anime_id == like.dict()['anime_id'], likes.c.user_id == like.dict()['user_id']))
    await session.execute(stmt)
    await session.commit()
    return {'status': 200}


@router.get('/get_liked_list')
async def get_liked_list(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(anime).join(likes).where(likes.c.user_id == user_id)
    result = await session.execute(query)
    print(query)
    return [dict(r._mapping) for r in result]
