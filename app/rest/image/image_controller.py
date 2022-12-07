import os
import os
import uuid

from fastapi import APIRouter, Depends, File, UploadFile, Form
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.rest.news.news_model import update_news, get_news_by_id

router = APIRouter(prefix="/upload", tags=["upload"])

assets_location = os.getenv("PATH_TO_ASSETS")

@router.post("/")
def get_all(db: Session = Depends(get_db), file: UploadFile = File(...), news_id: str = Form()):
    abs_base_path = f"{os.path.abspath(os.path.pardir)}"
    file_name = f"{str(uuid.uuid4())}.{file.content_type.split('/')[1]}" ## TODO test it on other img types
    file_location = f"{abs_base_path}{assets_location}{file_name}"

    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    src = f"/assets/images/{file_name}"

    news = get_news_by_id(db, int(news_id))
    previous_file_name = news.img_url.split("/")[3] ## TODO get rid_off this
    path_to_previous_image = f"{abs_base_path}{assets_location}{previous_file_name}"

    update_news(db, int(news_id), {"img_url": src})
    delete_image(path_to_previous_image)
    
    return {"file": src}

def delete_image(path: str):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")