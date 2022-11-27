from fastapi import FastAPI

from rest.news.news_model import News
from rest.tags.tags_model import Tag
from rest.settings.settings_model import Settings
from db.db import Base, engine

from rest.tags.tags_controller import router as router_tags
from rest.news.news_controller import router as router_news
from rest.settings.settings_controller import router as router_settings

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

@app.get("/")
async def root():
    return {"message": "Hello World!"}