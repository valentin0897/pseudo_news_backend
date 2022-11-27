from fastapi import FastAPI

from app.rest.news.news_model import News
from app.rest.tags.tags_model import Tag
from app.rest.settings.settings_model import Settings
from app.db.db import Base, engine

from app.rest.tags.tags_controller import router as router_tags
from app.rest.news.news_controller import router as router_news
from app.rest.settings.settings_controller import router as router_settings

Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:4200/"
]

app.include_router(router_news)
app.include_router(router_tags)
app.include_router(router_settings)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)