from fastapi import FastAPI, Depends, Path, HTTPException
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pymysql
from database import engineconn
from models import Test

templates = Jinja2Templates(directory="templates")

app = FastAPI(docs_url="/documentation", redoc_url=None)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# app = FastAPI()
#
# engine = engineconn()
# session = engine.sessionmaker()
#
# class Item(BaseModel):
#     name : str
#     number : int
#
# @app.get("/")
# async def first_get():
#     example = session.query(Test).all()
#     return example
