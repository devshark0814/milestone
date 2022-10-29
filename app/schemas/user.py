from datetime import datetime
from doctest import Example
from lib2to3.pytree import Base
from typing import Optional
from unicodedata import name
from venv import create

from pydantic import BaseModel, Field

# 共通的な部分を書き出し
class UserBase(BaseModel):
    name: str = Field(None, example="下津曲 翔平")
    image: str = Field(False, description="/XXX/XXXXX/XXX.png")
    class Config():
        orm_mode = True

# selectで使用する部分
class User(UserBase):
    id: int
    created_at: datetime = Field(None, description="2022-01-01 09:00:00")
    updated_at: datetime = Field(None, description="2022-01-01 09:00:00")
    deleted_at: datetime = Field(None, description="2022-01-01 09:00:00")
    class Config():
        orm_mode = True

# createで使用する部分
class UserCreateRequest(BaseModel):
    name: str = Field(..., description="氏名", example="下津曲 翔平")
    image: str = Field(None, description="画像URLパス", example="/XXX/XXXXX/XXX.png")

class UserCreateResponse(BaseModel):
    id: int = Field(..., description="登録後のuser_id")
    class Config():
        orm_mode = True

#----------------------------------
# selectで使用する部分
#----------------------------------
class UserSelectRequest(BaseModel):
    id: int = Field(..., description="ユーザーID", example="1")

class UserSelectResponse(BaseModel):
    id: int = Field(..., description="更新したuser_id")
    name: str = Field(..., description="氏名", example="下津曲 翔平")
    image: str = Field(None, description="画像URLパス", example="/XXX/XXXXX/XXX.png")
    created_at: datetime = Field(None, description="2022-01-01 09:00:00")
    updated_at: datetime = Field(None, description="2022-01-01 09:00:00")
    deleted_at: datetime = Field(None, description="2022-01-01 09:00:00")
    class Config():
        orm_mode = True

#----------------------------------
# updateで使用する部分
#----------------------------------
class UserUpdateRequest(BaseModel):
    id: int = Field(..., description="ユーザーID", example="1")
    name: str = Field(..., description="氏名", example="下津曲 翔平")
    image: str = Field(None, description="画像URLパス", example="/XXX/XXXXX/XXX.png")

class UserUpdateResponse(BaseModel):
    id: int = Field(..., description="更新したuser_id")
    class Config():
        orm_mode = True