from sqlalchemy.orm.session  import Session

from models.m_user import User
from schemas.user import UserCreateRequest, UserUpdateRequest

def all(db: Session):
    return db.query(User).all()

def create(db: Session, request: UserCreateRequest):
    # user = user_model.User(**user_create.dict())

    user = User(
        name = request.name,
        image = request.image,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def select(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def update(db: Session, request: UserUpdateRequest):
    user = db.query(User).filter(User.id == request.id).first()
    user.name = request.name
    user.image = request.image
    db.add(user)
    db.commit()
    db.refresh(user)
    return user