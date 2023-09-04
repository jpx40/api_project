import fnmatch
import os

from fastapi import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import sql_tool
import yt
from sql_tool import create_connection

#db = create_connection(user="Jonas_P", password="Password", database="sys", host="10.0.0.200")


"""def get_db():
    db = create_connection(user="Jonas_P", password="Password", database="mysql", host="10.0.0.200")
    cursor = db.cursor(dictionary=True)
    try:
        yield cursor
    finally:
        cursor.close()
"""

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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




app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_template(request: Request):
    return templates.TemplateResponse("home/home.jinja2", {"request": request})

"""
@app.get("/api/users")
async def read_users():
    user = sql_tool.get_user()
    # sql_tool.db_close(connection)
    # json_compatible_item_data = jsonable_encoder(user)

    return {"user": user}

"""
"""@app.get("/api/arbeitzplatz")
async def read_arbeitzplatz():
    arbeitzplatz = sql_tool.get_arbeitzplatz(db)
    return arbeitzplatz


@app.get("/api/parkplatz/")
async def read_parkplatz():
    parkplatz = sql_tool.get_parkplatz(db)
    return parkplatz


@app.get("/api/game/")
async def read_game_scores():
    game = sql_tool.get_game(db)
    return {"game": game}

"""

"""
@app.get("/video-is-their/")
async def get_info(background_tasks: BackgroundTasks):

    if pathlib.Path('./video/*').is_file():
            return {"video": "true"}

"""
