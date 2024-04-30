from fastapi import FastAPI, Depends
from fastapi_users import fastapi_users, FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate
from src.auth.user_manager import get_user_manager

app = FastAPI(title='Anime App')

users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"
