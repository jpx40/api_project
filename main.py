import os

from fastapi import BackgroundTasks
from fastapi.responses import FileResponse
import fnmatch
from fastapi import Depends, FastAPI, HTTPException

import sql_tool
from sql_tool import connection

from pydantic import BaseModel

import yt

app = FastAPI()


class Item(BaseModel):
    name: str


@app.get("/api/users/")
async def read_users():
    user = sql_tool.get_user(connection)
    # sql_tool.db_close(connection)
    return {"user": user}


@app.get("/api/arbeitzplatz")
async def read_arbeitzplatz():
    arbeitzplatz = sql_tool.get_arbeitzplatz(connection)
    return arbeitzplatz


@app.get("/api/parkplatz/")
async def read_parkplatz():
    parkplatz = sql_tool.get_parkplatz(connection)
    return parkplatz


@app.get("/api/game/")
async def read_game_scores():
    game = sql_tool.get_game(connection)
    return game


def match_mp4():
    for filename in os.listdir('./video'):
        fnmatch.fnmatch("./video/" + filename, "*.mp4")
        return "./video/" + filename


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
