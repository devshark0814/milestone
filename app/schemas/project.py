from datetime import datetime, date
from pydantic import BaseModel, Field

# for Create-----------------------------------
class ProjectCreateRequest(BaseModel):
  name: str = Field(..., description="プロジェクト名", example="LP構成簡単くん")
  description: str = Field(..., description="プロジェクト説明", example="XXXXをするプロジェクト")
  planned_release_date: date = Field(None, description="リリース予定日", example="2022-01-01")
  fact_release_date: date = Field(None, description="リリース日", example="2022-01-01")
  priority: int = Field(..., description="優先度", example=1)
  sale_cost: int = Field(None, description="見積工数", example=1)
  class Config():
      orm_mode = True

class ProjectCreateResponse(BaseModel):
  id: int = Field(..., description="登録後のproject_id", exmaple=1)
  class Config():
      orm_mode = True
# ---------------------------------------------

# 一件分のモデル定義
class ProjectResponse(BaseModel):
  id: int = Field(..., description="登録後のproject_id", exmaple=1)
  name: str = Field(..., description="プロジェクト名", example="LP構成簡単くん")
  description: str = Field(..., description="プロジェクト説明", example="XXXXをするプロジェクト")
  planned_release_date: date = Field(None, description="リリース予定日", example="2022-01-01")
  fact_release_date: date = Field(None, description="リリース日", example="2022-01-01")
  priority: int = Field(..., description="優先度", example=1)
  sale_cost: int = Field(None, description="見積工数", example=1)
  created_at: datetime = Field(None, description="作成日時", example="2022-01-01 09:00:00")
  updated_at: datetime = Field(None, description="更新日時", example="2022-01-01 09:00:00")
  deleted_at: datetime = Field(None, description="削除日時", example="2022-01-01 09:00:00")
  class Config():
      orm_mode = True

# for Update-----------------------------------
class ProjectUpdateResponse(BaseModel):
  id: int = Field(..., description="更新後のproject_id", exmaple=1)
  class Config():
      orm_mode = True

class ProjectUpdateRequest(BaseModel):
  name: str = Field(..., description="プロジェクト名", example="LP構成簡単くん")
  description: str = Field(..., description="プロジェクト説明", example="XXXXをするプロジェクト")
  planned_release_date: date = Field(None, description="リリース予定日", example="2022-01-01")
  fact_release_date: date = Field(None, description="リリース日", example="2022-01-01")
  priority: int = Field(..., description="優先度", example=1)
  sale_cost: int = Field(None, description="見積工数", example=1)
  class Config():
      orm_mode = True
# ---------------------------------------------