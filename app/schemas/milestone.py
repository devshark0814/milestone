from datetime import datetime, date
from pydantic import BaseModel, Field

# for Create-----------------------------------
class MilestoneCreateRequest(BaseModel):
  project_id: int = Field(..., description="プロジェクトID", example=1)
  assign_user_ids: str = Field(None, description="アサインメンバーリスト", example=[1,2,3])
  start_date: date = Field(None, description="開始日", example="2022-01-01")
  end_date: date = Field(None, description="終了日", example="2022-01-01")
  progress: int = Field(None, description="進捗率", example=50)
  color: str = Field(None, description="マイルストーン色", example="#3D8080ED")
  class Config():
      orm_mode = True

class MilestoneCreateResponse(BaseModel):
  id: int = Field(..., description="登録後のmilestone_id", exmaple=1)
  class Config():
      orm_mode = True
# ---------------------------------------------

class MilestoneResponse(BaseModel):
  id: int = Field(..., description="milestone_id", exmaple=1)
  project_id: int = Field(..., description="milestone_id", exmaple=1)
  assign_user_ids: str = Field(None, description="アサインメンバーリスト", example=[1,2,3])
  start: date = Field(None, description="開始日", example="2022-01-01")
  end: date = Field(None, description="終了日", example="2022-01-01")
  progress: int = Field(None, description="進捗率", example=50)
  color: str = Field(None, description="マイルストーン色", example="#3D8080ED")
  title: str = Field(..., description="プロジェクト名", example="LP構成簡単くん")
  project_description: str = Field(..., description="プロジェクト説明", example="XXXXをするプロジェクト")
  project_priority: int = Field(..., description="優先度", example=1)
  project_sale_cost: int = Field(None, description="見積工数", example=1)
  class Config():
      orm_mode = True


# for Update-----------------------------------
class MilestoneUpdateRequest(BaseModel):
  assign_user_ids: str = Field(None, description="アサインメンバーリスト", example=[1,2,3])
  start: date = Field(None, description="開始日", example="2022-01-01")
  end: date = Field(None, description="終了日", example="2022-01-01")
  progress: int = Field(None, description="進捗率", example=50)
  color: str = Field(None, description="マイルストーン色", example="#3D8080ED")
  class Config():
      orm_mode = True

class MilestoneUpdateResponse(BaseModel):
  id: int = Field(..., description="更新後のmilestone_id", exmaple=1)
  class Config():
      orm_mode = True
# ---------------------------------------------