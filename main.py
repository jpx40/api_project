import fnmatch
import os

from fastapi import BackgroundTasks
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

import sql_tool
import yt
from sql_tool import create_connection

db = create_connection(user="Jonas_P", password="Password", database="sys", host="10.0.0.200")


def get_db():
    db = create_connection(user="Jonas_P", password="Password", database="mysql", host="10.0.0.200")
    cursor = db.cursor(dictionary=True)
    try:
        yield cursor
    finally:
        cursor.close()


app = FastAPI()

origins = [

    "http://localhost:63342",
    "http://localhost:8080",
    "http://127.0.0.1:*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str


@app.get("/api/users")
async def read_users():
    user = sql_tool.get_user(cursor)
    # sql_tool.db_close(connection)
    # json_compatible_item_data = jsonable_encoder(user)

    return {"user": user}


@app.get("/api/arbeitzplatz")
async def read_arbeitzplatz():
    arbeitzplatz = sql_tool.get_arbeitzplatz(cursor)
    return arbeitzplatz


@app.get("/api/parkplatz/")
async def read_parkplatz():
    parkplatz = sql_tool.get_parkplatz(cursor)
    return parkplatz


@app.get("/api/game/")
async def read_game_scores():
    game = sql_tool.get_game(db)
    return {"game": game}


def htmlReader(path):
    with open(path, "r") as f:
        string = f.read()

    return string


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
async def get_vd(backround: BackgroundTasks):
    backround.add_task(yt.down("https://youtube.com/shorts/pkWXI8L9uIo?si=9TA8XH1cMtpq_hxy"))
    file_path = match_mp4()
    return file_path


subapi = FastAPI()


@app.get("/sub", response_class=FileResponse)
def read_sub():
    return "assets/styles/global.css"

# app.mount("/subapi", subapi)
