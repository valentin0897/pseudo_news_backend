from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.future import select
from sqlalchemy.orm import relationship, Session

from app.db.db import Base
import app.rest.news.news_schema as schemas
from app.rest.tags.tags_model import Tag, create_tag
from app.rest.tags.tags_schema import TagCreate
from app.rest.tags_news.tags_news_model import tags_news

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    img_url = Column(String)
    pub_time = Column(String)
    text = Column(String)
    short_description = Column(String)
    is_main_news = Column(Boolean)
    is_external_link = Column(Boolean)
    external_link = Column(String)

    tags = relationship("Tag", secondary=tags_news, back_populates="news")


def get_all_news(db: Session):
    return db.execute(select(News)).scalars().all()

def get_main_news(db: Session):
    return db.execute(select(News).filter(News.is_main_news == True)).scalars().all()

def get_regular_news(db: Session):
    return db.execute(select(News).filter(News.is_main_news == False)).scalars().all()

def get_news_by_id(db: Session, news_id: int):
    return db.execute(select(News).filter(News.id == news_id)).scalar()

def get_tags_by_news_id(db: Session, news_id: int):
    return db.execute(select(Tag).select_from(News).join(News.tags).filter(News.id == news_id)).scalars().all()

def get_news_by_tag_id(db: Session, tag_id: int):
    return db.execute(select(News).select_from(Tag).join(Tag.news).filter(Tag.id == tag_id)).scalars().all()

def create_news(db: Session, news: schemas.NewsCreate):
    db_news = News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def update_news(db: Session, news_id: int, news: dict):
    db_news = get_news_by_id(db, news_id)
    for key in news.keys():
        setattr(db_news, key, news[key])
    db.add(db_news)
    db.commit()
    return db_news

def delete_news(db: Session, news_id: int):
    db_news = db.execute(select(News).filter(News.id == news_id)).scalar()
    db.delete(db_news)
    db.commit()

def add_link(db: Session, news_id: int, tag: str):
    db_news = db.execute(select(News).filter(News.id == news_id)).scalar()
    db_tag = db.execute(select(Tag).filter(Tag.tag == tag)).scalar()
    if not(db_tag):
        news_tag = create_tag(db, TagCreate(tag=tag))
        db_news.tags.append(news_tag)
    else:
        db_news.tags.append(db_tag)
    db.add(db_news)
    db.commit()

def delete_link(db: Session, news_id: int, tag: str):
    db_news = db.execute(select(News).filter(News.id == news_id)).scalar()
    db_tag = db.execute(select(Tag).filter(Tag.tag == tag)).scalar()
    db_news.tags.remove(db_tag)
    db.add(db_news)
    db.commit()
