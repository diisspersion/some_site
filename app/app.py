from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

import psutil
import os

# Получаем значения из системы,
# 'admin' и 'admin123' — значения по умолчанию для локальной разработки
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
SECRET_TOKEN = os.getenv("API_TOKEN", "fallback-token")

app = FastAPI(title="System Resource Monitor")
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="index.html",
                                      context={"request": request})


@app.post("/login")
async def login(data: LoginRequest):
    if data.username == ADMIN_USERNAME and data.password == ADMIN_PASSWORD:
        return {"message": "Успешный вход", "token": SECRET_TOKEN}
    return {"error": "Неверные данные"}, 400


@app.get("/stats", response_class=HTMLResponse)
async def stats_page(request: Request):
    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "processes": len(psutil.pids())
        }
    return templates.TemplateResponse("stats.html",
                                      {"request": request, **data})
