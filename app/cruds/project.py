from sqlalchemy.orm.session  import Session
from sqlalchemy import func, case

from models.m_project import MProject
from schemas.project import ProjectCreateRequest, ProjectUpdateRequest

# ------------------
# Create
# ------------------
def create(db: Session, request: ProjectCreateRequest):
    model = MProject(
        name = request.name,
        description = request.description,
        planned_release_date = request.planned_release_date,
        fact_release_date = request.fact_release_date,
        priority = request.priority,
        sale_cost = request.sale_cost,
    )
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

# ------------------
# All
# ------------------
def all(db:Session):
    return db.query(MProject).all()

# ------------------
# Update
# ------------------
def update(db: Session, request: ProjectUpdateRequest, id:int):
    p = db.query(MProject).filter(MProject.id == id).first()
    p.name = request.name
    p.description = request.description
    p.planned_release_date = request.planned_release_date
    p.fact_release_date = request.fact_release_date
    p.priority = request.priority
    p.sale_cost = request.sale_cost
    db.add(p)
    db.commit()
    db.refresh(p)
    return p