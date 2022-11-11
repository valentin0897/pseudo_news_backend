from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.future import select
from sqlalchemy.orm import relationship, Session

from db.db import Base
import rest.news.news_schema as schemas

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    img_url = Column(String)
    pub_time = Column(String)
    text = Column(String)
    short_description = Column(String)
    is_outer_link = Column(Boolean)
    outer_link = Column(String)

    tag_id = Column(Integer, ForeignKey("tags.id"))
    tag = relationship("Tag", back_populates="news")


def get_all_news(db: Session):
    return db.execute(select(News)).scalars().all()

def get_news_by_id(db: Session, news_id: int):
    return db.execute(select(News).filter(News.id == news_id)).scalar()

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