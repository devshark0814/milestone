from sqlalchemy.orm.session  import Session
from sqlalchemy import func, case

from models.t_milestone import TMilestones
from models.m_project import MProject
from schemas.milestone import MilestoneCreateRequest, MilestoneUpdateRequest

# ------------------
# Create
# ------------------
def create(db: Session, request: MilestoneCreateRequest):
    model = TMilestones(
        project_id = request.project_id,
        assign_user_ids = request.assign_user_ids,
        start_date = request.start_date,
        end_date = request.end_date,
        progress = request.progress,
        color = request.color,
    )
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

# ------------------
# All
# ------------------
def all(db:Session):
    milestones = db.query(TMilestones, MProject).join(MProject, TMilestones.project_id == MProject.id).all()
    list = []
    for milestone in milestones:
        dict = {
            "id" : milestone.TMilestones.id,
            "project_id" : milestone.TMilestones.project_id,
            "assign_user_ids" : milestone.TMilestones.assign_user_ids,
            "start" : milestone.TMilestones.start_date,
            "end" : milestone.TMilestones.end_date,
            "progress" : milestone.TMilestones.progress,
            "color" : '#1E88E5' if not milestone.TMilestones.color else milestone.TMilestones.color,
            "title" : milestone.MProject.name,
            "project_description" : milestone.MProject.description,
            "project_priority" : milestone.MProject.priority,
            "project_sale_cost" : milestone.MProject.sale_cost,
        }
        list.append(dict)
    return list;

# ------------------
# Update
# ------------------
def update(db: Session, request: MilestoneUpdateRequest, id:int):
    m = db.query(TMilestones).filter(TMilestones.id == id).first()
    m.assign_user_ids = request.assign_user_ids
    m.start_date = request.start
    m.end_date = request.end
    m.progress = request.progress
    m.color = request.color
    db.add(m)
    db.commit()
    db.refresh(m)
    return m