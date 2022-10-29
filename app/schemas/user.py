from datetime import datetime
from typing import Optional
from unicodedata import name
from venv import create

from pydantic import BaseModel, Field

# 共通的な部分を書き出し
class UserBase(BaseModel):
    name: str = Field(None, example="下津曲 翔平")
    image: str = Field(False, description="/XXX/XXXXX/XXX.png")

# selectで使用する部分
class User(UserBase):
    id: int
    created_at: datetime = Field(None, description="2022-01-01 09:00:00")
    updated_at: datetime = Field(None, description="2022-01-01 09:00:00")
    deleted_at: datetime = Field(None, description="2022-01-01 09:00:00")

# createで使用する部分
class UserCreateRequest(UserBase):
    pass

class UserCreateResponse(BaseModel):
    id:int