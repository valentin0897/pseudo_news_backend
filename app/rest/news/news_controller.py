from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from rest.news import news_model as models
from rest.news import news_schema as schemas
from db.db import get_db

router = APIRouter(prefix="/news", tags=["news"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    result = models.get_all_news(db)
    return result

@router.get("/{news_id}")
def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    result = models.get_news_by_id(db, news_id)
    return result

@router.patch("/{news_id}")
def update_news(news_id: int, news: schemas.NewsBase, db: Session = Depends(get_db)):
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