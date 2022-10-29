from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.user as user_crud
from database import get_db

import schemas.user as user_schema

router = APIRouter()

@router.get('/users', response_model=List[user_schema.User])
def all_user(db: Session = Depends(get_db)):
  return user_crud.all(db)


@router.post(
    '/users',
    description="ユーザー登録",
    response_model=user_schema.UserCreateResponse)
def create_user(
    user_body: user_schema.UserCreateRequest,
    db: Session = Depends(get_db)
):
    res = user_crud.create(db, user_body)
    return res

@router.get(
    '/users/{id}',
    description="ユーザー取得",
    response_model=user_schema.UserSelectResponse)
def read_user(
    id: int ,
    db: Session = Depends(get_db)
):
    res = user_crud.select(db, id)
    return res


@router.put(
    '/users',
    description="ユーザー更新",
    response_model=user_schema.UserUpdateResponse)
def update_user(
    user_body: user_schema.UserUpdateRequest,
    db: Session = Depends(get_db)
):
    res = user_crud.update(db, user_body)
    return res