import os
import pathlib
from pathlib import Path

from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
import fnmatch
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

from pydantic import BaseModel

import yt

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

class Item(BaseModel):
    name: str

"""
def is_file_their():
    filename =  pathlib.Path('./video/*')
    if filename.is_file():
        return True
        """
def match_mp4():
    for filename in os.listdir('./video'):
        fnmatch.fnmatch("./video/" + filename , "*.mp4")
        return  "./video/" + filename

"""
@app.get("/video-is-their/")
async def get_info(background_tasks: BackgroundTasks):

    if pathlib.Path('./video/*').is_file():
            return {"video": "true"}

"""



@app.post("/items/")
async def create_item(item: Item, background_tasks: BackgroundTasks):
    background_tasks.add_task(yt.down(item.name))
    return {"message": "video gedownloaded"}

@app.get("/video/", response_class=FileResponse)
async def get_vd():
    yt.down()
    file_path = match_mp4()
    return file_path
