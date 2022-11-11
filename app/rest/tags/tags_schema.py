from pydantic import BaseModel

class TagBase(BaseModel):
    tag: str

    class Config:
        orm_mode = True


class TagCreate(TagBase):
    tag: str