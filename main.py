import fnmatch
import os
from typing import Annotated

import yaml
from fastapi import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import sql_tool
from sql_tool import create_connection

with open('~/.config/dashboard/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

db = create_connection(user=config["user"], password=config["password"], database=config["database"],
                       host=config["host"])



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
    foo = "parkplatz_besetzt"
    return templates.TemplateResponse("dashboard/home.jinja2",  {"request": request ,"foo": foo})


@app.get("/api/users")
async def read_users():
    user = sql_tool.get_user(db)
    # sql_tool.db_close()
    # json_compatible_item_data = jsonable_encoder(user)

    return  user
"""
@app.get("/api/arbeitzplatz")
async def read_arbeitzplatz():
    arbeitzplatz = sql_tool.get_arbeitzplatz(db)
    return arbeitzplatz
"""

@app.get("/api/parkplatz/")
async def read_parkplatz():
    parkplatz = sql_tool.get_parkplatzpublic(db)
    return parkplatz

"""
@app.get("/api/game/")
async def read_game_scores():
    game = sql_tool.get_game(db)
    return {"game": game}
"""


def generate_html_response():
    html_content = """
 <div id="container" x-data="two_value = false"  >
            <div  id="one" class="parkplatz_frei"><p class="inbox">
                1</p>
            </div>
    """
    return HTMLResponse(content=html_content, status_code=200)





@app.get("/api/html")
async def read_items():
    html_content = """

            <div  id="one" class="parkplatz_frei"><p class="inbox">
                1</p>
            </div>
    """
    return HTMLResponse(content=html_content, status_code=200)