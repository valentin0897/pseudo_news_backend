from pydantic import BaseModel

class SettingsBase(BaseModel):
    header_title: str
    is_active: bool

    class Config:
        orm_mode = True

class SettingsCreate(SettingsBase):
    pass