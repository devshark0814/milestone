from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.milestone as milestone_crud
from database import get_db

import schemas.milestone as milestone_schema

router = APIRouter()

@router.post('/milestones', description="マイルストーン登録", response_model=milestone_schema.MilestoneCreateResponse)
def create_milestone(body: milestone_schema.MilestoneCreateRequest,db: Session = Depends(get_db)):
    res = milestone_crud.create(db, body)
    return res

@router.get('/milestones', description="マイルストーン一覧", response_model=List[milestone_schema.MilestoneResponse])
def select_all(db:Session = Depends(get_db)):
    res = milestone_crud.all(db)
    return res

@router.put('/milestones/{id}', description="マイルストーン更新", response_model=milestone_schema.MilestoneUpdateResponse)
def project_update(id: int, body: milestone_schema.MilestoneUpdateRequest, db:Session = Depends(get_db)):
    res = milestone_crud.update(db, body, id)
    return res