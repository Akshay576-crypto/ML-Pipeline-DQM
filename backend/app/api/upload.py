from fastapi import UploadFile , File , APIRouter
import os
import pandas as pd
from app.database.db import get_connection
from app.api.profile_service import generate_profile
from app.api.quality_core import calculate_quality_score
import traceback
from app.api.report import report_generate
from app.api.anamoly import detect_anamolies
from app.api.pipeline_history import save_pipeline_run
from app.api.pdf_report import generate_pdf_report


router = APIRouter()
UPLOAD_FOLDER = "data/raw"
REPORT_FOLDER = "data/reports"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_file(file : UploadFile = File(...)):

    try:
        file_path = os.path.join(UPLOAD_FOLDER , file.filename)

        with open(file_path , "wb") as f:
            f.write(await file.read())

        df = pd.read_csv(file_path)

        #calculate metadata
        total_record = len(df)
        total_columns = len(df.columns)

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        
        query = """INSERT INTO uploads(file_name,total_records,total_columns)VALUES(%s,%s,%s)"""

        values = (file.filename,total_record,total_columns)
        cursor.execute(query,values)
        connection.commit()

        profile = generate_profile(df)
        quality_report = calculate_quality_score(df)
        
        anamoly_report = detect_anamolies(df)

        report = report_generate(file.filename,
                                 total_record,
                                 total_columns,
                                 profile,
                                 quality_report)
        pdf_path = os.path.join(
            REPORT_FOLDER,
            f"{file.filename}_report.pdf"
        )

        generate_pdf_report(report,pdf_path)

        save_pipeline_run(file.filename,
                          total_record,
                          total_columns,
                          quality_report,
                          anamoly_report)

        return {"Message":"File Uploaded Sucessfully",
                "filename":file.filename,
                "Total_record":total_record,
                "Total_columns":total_columns,
                "Message":"File Uploaded and Meta Data stored",
                "profile":profile,
                "QualityReport":quality_report,
                "report":report,
                "Anamoly_score":anamoly_report,
                "pdf_report":pdf_path}
    
    except Exception as e:
        return {
        "status": "error",
        "error_type": type(e).__name__,
        "message": str(e),
        "traceback": traceback.format_exc()
        }
    

