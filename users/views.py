
from fastapi import APIRouter, Path

from users.schemas import CreateUser
from users import crud
router = APIRouter(prefix='/user', tags=['User'])

@router.post('/users/')
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)