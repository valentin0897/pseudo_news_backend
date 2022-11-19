from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    img_url: str
    pub_time: str
    text: str
    short_description: str
    is_main_news: bool
    is_outer_link: bool
    outer_link: str
    tag_id: int

    class Config:
        orm_mode = True

class NewsCreate(NewsBase):
    pass