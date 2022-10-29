from typing import List
from fastapi import APIRouter

import schemas.user as user_schema

router = APIRouter()

@router.get('/users', response_model=List[user_schema.User])
async def list_users():
  return [user_schema.User(id=1, name="下津曲 翔平", image="", created_at="", updated_at="", deleted_at="")]


@router.post('/users', response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreateRequest):
    return user_schema.UserCreateResponse(id=1, **user_body.dict())