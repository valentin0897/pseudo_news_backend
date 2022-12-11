from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    img_url: str
    pub_time: str
    text: str
    short_description: str
    is_main_news: bool
    is_external_link: bool
    external_link: str

    class Config:
        orm_mode = True

class NewsUpdate(BaseModel):
    title: str | None
    img_url: str | None
    pub_time: str | None
    text: str | None
    short_description: str | None
    is_main_news: bool | None
    is_external_link: bool | None
    external_link: str | None

    class Config:
        orm_mode = True

class NewsCreate(NewsBase):
    pass

class NewsTagCreate(BaseModel):
    tag: str
    news_id: int