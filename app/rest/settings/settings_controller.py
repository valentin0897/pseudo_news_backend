from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from rest.settings import settings_model as models
from rest.settings import settings_schema as schemas
from db.db import get_db

router = APIRouter(prefix="/settings", tags=["settings"])

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    result = models.get_all_settings(db)
    return result

@router.get("/{settings_id}")
def get_settings_by_id(settings_id: int, db: Session = Depends(get_db)):
    result = models.get_settings_by_id(db, settings_id)
    return result

@router.patch("/{settings_id}")
def update_settings(settings_id: int, settings: schemas.SettingsBase, db: Session = Depends(get_db)):
    settings_dict = settings.dict(exclude_unset=True)
    updated_settings = models.update_settings(db, settings_id, settings_dict)
    return updated_settings

@router.post("/")
def create_settings(settings: schemas.SettingsCreate, db: Session = Depends(get_db)):
    created_settings = models.create_settings(db, settings)
    return created_settings

@router.delete("/{settings_id}")
def delete_settings(settings_id: int, db: Session = Depends(get_db)):
    deleted_settings = models.delete_settings(db, settings_id)
    return deleted_settings