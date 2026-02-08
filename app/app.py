from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import psutil
import os

# Fetch environment variables with default fallback values
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
SECRET_TOKEN = os.getenv("API_TOKEN", "fallback-token")

app = FastAPI(title="System Resource Monitor")

# Mount static files (CSS, JS, images) and initialize templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Pydantic model for login data validation
class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Render the initial login page."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/login")
async def login(data: LoginRequest):
    """Verify credentials and return a redirect URL on success."""
    if data.username == ADMIN_USERNAME and data.password == ADMIN_PASSWORD:
        return {"redirect_url": "/stats"}

    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/stats", response_class=HTMLResponse)
def stats_page(request: Request):
    """Collect system metrics and render the statistics dashboard."""
    data = {
        # interval=1 blocks for 1 second to measure CPU usage accurately
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "processes": len(psutil.pids())
    }
    return templates.TemplateResponse(
        "stats.html",
        {"request": request, **data}
    )
