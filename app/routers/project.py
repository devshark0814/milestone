from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.project as project_crud
from database import get_db

import schemas.project as project_schema

router = APIRouter()

@router.post('/projects', description="プロジェクト登録", response_model=project_schema.ProjectCreateResponse)
def create_project(user_body: project_schema.ProjectCreateRequest,db: Session = Depends(get_db)):
    res = project_crud.create(db, user_body)
    return res

@router.get('/projects', description="プロジェクト一覧", response_model=List[project_schema.ProjectResponse])
def select_all(db:Session = Depends(get_db)):
    res = project_crud.all(db)
    return res

@router.put('/projects/{id}', description="プロジェクト更新", response_model=project_schema.ProjectUpdateResponse)
def project_update(id: int, body: project_schema.ProjectUpdateRequest, db:Session = Depends(get_db)):
    res = project_crud.update(db, body, id)
    return res