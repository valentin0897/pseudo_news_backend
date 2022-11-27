from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.rest.tags import tags_model as models
from app.rest.tags import tags_schema as schemas
from app.db.db import get_db

router = APIRouter(prefix="/tag", tags=["tag"])


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    result = models.get_all_tags(db)
    return result

@router.get("/name/")
def get_tag_by_name(tag: str = "", db: Session = Depends(get_db)):
    result = models.get_tag_id_by_name(db, tag)
    return result

@router.get("/{tag_id}")
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
    result = models.get_tag_by_id(db, tag_id)
    return result

@router.patch("/{tag_id}")
def update_tag(tag_id: int, tag: schemas.TagBase, db: Session = Depends(get_db)):
    tag_dict = tag.dict(exclude_unset=True)
    updated_tag = models.update_tag(db, tag_id, tag_dict)
    return updated_tag

@router.post("/")
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    created_tag = models.create_tag(db, tag)
    return created_tag

@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    deleted_tag = models.delete_tag(db, tag_id)
    return deleted_tag