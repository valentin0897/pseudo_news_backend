from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.future import select
from sqlalchemy.orm import relationship, Session

from db.db import Base
import rest.settings.settings_schema as schemas

class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    header_title = Column(String)


def get_all_settings(db: Session):
    return db.execute(select(Settings)).scalars().all()

def get_settings_by_id(db: Session, settings_id: int):
    return db.execute(select(Settings).filter(Settings.id == settings_id)).scalar()

def create_settings(db: Session, settings: schemas.SettingsCreate):
    db_settings = Settings(**settings.dict())
    db.add(db_settings)
    db.commit()
    db.refresh(db_settings)
    return db_settings

def update_settings(db: Session, settings_id: int, settings: dict):
    db_settings = get_settings_by_id(db, settings_id)
    for key in settings.keys():
        setattr(db_settings, key, settings[key])
    db.add(db_settings)
    db.commit()
    return db_settings

def delete_settings(db: Session, settings_id: int):
    db_settings = db.execute(select(Settings).filter(Settings.id == settings_id)).scalar()
    db.delete(db_settings)
    db.commit()