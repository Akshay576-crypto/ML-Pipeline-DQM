from fastapi import APIRouter , HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

REPORT_FOLDER = "data/reports"

@router.get("/download-report/{filename}")
def download_report(filename:str):

    file_path = os.path.join(REPORT_FOLDER,filename)

    if not os.path.exists(file_path):

        raise HTTPException(status_code=404,detail="File Not Found")
    
    return FileResponse(path=file_path,filename=filename,media_type="application/pdf")


