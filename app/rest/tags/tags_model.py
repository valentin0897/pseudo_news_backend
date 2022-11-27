from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select
from sqlalchemy.orm import relationship, Session

from app.db.db import Base
from app.rest.tags import tags_schema as schemas

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, unique=True)

    news = relationship("News", back_populates="tag")

def get_all_tags(db: Session):
    return db.execute(select(Tag)).scalars().all()

def get_tag_by_id(db: Session, tag_id: int):
    return db.execute(select(Tag).filter(Tag.id == tag_id)).scalar()

def get_tag_id_by_name(db: Session, tag_name: str):
    return db.execute(select(Tag).filter(Tag.tag == tag_name)).scalar()

def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def update_tag(db: Session, tag_id: int, tag: dict):
    db_tag = get_tag_by_id(db, tag_id)
    for key in tag.keys():
        setattr(db_tag, key, tag[key])
    db.add(db_tag)
    db.commit()
    return db_tag

def delete_tag(db: Session, tag_id: int):
    db_tag = db.execute(select(Tag).filter(Tag.id == tag_id)).scalar()
    db.delete(db_tag)
    db.commit()