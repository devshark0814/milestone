from sqlalchemy import create_engine

from models.m_user import Base
from models.m_project import Base as Base2
from models.t_milestone import Base as Base3
from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    'root',
    'root',
    DB_HOST,
    DB_NAME,
)
engine = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Base2.metadata.drop_all(bind=engine)
    Base2.metadata.create_all(bind=engine)

    Base3.metadata.drop_all(bind=engine)
    Base3.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()