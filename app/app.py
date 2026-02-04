from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import psutil

app = FastAPI(title="System Resource Monitor")
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request})

@app.post("/login")
async def login(data: LoginRequest):
    # Тут ваша логика проверки пароля
    if data.username == "admin" and data.password == "1234":
        return {"message": "Успешный вход", "token": "fake-jwt-token"}
    
    return {"error": "Неверные данные"}, 400

@app.get("/stats", response_class=HTMLResponse)
async def stats_page(request: Request):
    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "processes": len(psutil.pids())
        }
    
    return templates.TemplateResponse("stats.html", {"request": request, **data})


