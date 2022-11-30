from fastapi import APIRouter, Depends, File, UploadFile, Form
import uuid
import os

from sqlalchemy.orm import Session
from app.rest.news.news_model import update_news

from app.db.db import get_db

router = APIRouter(prefix="/upload", tags=["upload"])

path_to_asset = "../../../images/"

@router.post("/")
def get_all(db: Session = Depends(get_db), file: UploadFile = File(...), news_id: str = Form()):
    base_path = f"{os.path.abspath(os.path.pardir)}"
    assets_location = f"/frontend/src/assets/images/"
    file_name = f"{str(uuid.uuid4())}.{file.content_type.split('/')[1]}"
    file_location = f"{base_path}{assets_location}{file_name}"
    print(file_location)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    src = f"/assets/images/{file_name}"
    update_news(db, int(news_id), {"img_url": src})
    

    return {"file": src}