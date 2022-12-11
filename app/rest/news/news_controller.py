from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.rest.news import news_model as models
from app.rest.news import news_schema as schemas
from app.db.db import get_db

router = APIRouter(prefix="/news", tags=["news"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    result = models.get_all_news(db)
    return result

@router.get("/{news_id}")
def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    result = models.get_news_by_id(db, news_id)
    return result

@router.get("/{news_id}/tags/")
def get_tags_by_news_id(news_id: int, db: Session = Depends(get_db)):
    result = models.get_tags_by_news_id(db, news_id)
    return result

@router.get("/{tag_id}/news/")
def get_news_by_tag_id(tag_id: int, db: Session = Depends(get_db)):
    result = models.get_news_by_tag_id(db, tag_id)
    return result

@router.get("/main/")
def get_main_news(db: Session = Depends(get_db)):
    result = models.get_main_news(db)
    return result

@router.get("/regular/")
def get_regular_news(db: Session = Depends(get_db)):
    result = models.get_regular_news(db)
    return result

@router.patch("/{news_id}")
def update_news(news_id: int, news: schemas.NewsUpdate, db: Session = Depends(get_db)):
    news_dict = news.dict(exclude_unset=True)
    updated_news = models.update_news(db, news_id, news_dict)
    return updated_news

@router.post("/")
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    created_news = models.create_news(db, news)
    return created_news

@router.delete("/{news_id}")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    deleted_news = models.delete_news(db, news_id)
    return deleted_news

@router.post("/add_link/")
def add_tag(link: schemas.NewsTagCreate, db: Session = Depends(get_db)):
    tags_news = models.add_link(db, link.news_id, link.tag)
    return tags_news

@router.post("/delete_link/")
def delete_tag(link: schemas.NewsTagCreate, db: Session = Depends(get_db)):
    tags_news = models.delete_link(db, link.news_id, link.tag)
    return tags_news