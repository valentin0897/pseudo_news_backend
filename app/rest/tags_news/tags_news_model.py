from sqlalchemy import Table, ForeignKey, Column

from app.db.db import Base


tags_news = Table(
    "tags_news",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("news_id", ForeignKey("news.id"), primary_key=True)
)