from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.history import router as history_router
from app.api.dashboard import router as dashboard_router
from app.api.alerts import router as alert_router
from app.api.anamoly_trend import router as anamoly_tren
from app.api.download_report import router as download_report
from app.api.analytics_report import router as analytics_report
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.responses import HTMLResponse
import os
from app.api.dataset_profile import router as dataset_profile_router


app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.include_router(upload_router)
app.include_router(history_router)
app.include_router(dashboard_router)
app.include_router(alert_router)
app.include_router(anamoly_tren)
app.include_router(download_report)
app.include_router(analytics_report)
app.include_router(dataset_profile_router)

@app.get("/", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )

@app.get("/upload-page", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="upload.html"
    )

@app.get("/report-page", response_class=HTMLResponse)
async def report_page(request: Request):
    return templates.TemplateResponse(
         request=request,
        name="report.html"
    )

@app.get("/anamolies-page", response_class=HTMLResponse)
async def report_page(request: Request):
    return templates.TemplateResponse(
         request=request,
        name="anamolies.html"
    )


@app.get("/", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse(
         request=request,
        name="dashboard.html"
    )
