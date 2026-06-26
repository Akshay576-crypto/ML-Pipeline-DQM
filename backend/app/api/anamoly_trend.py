from fastapi import APIRouter
from app.database.db import get_connection

router = APIRouter()

@router.get("/anamoly-trend")
def anamoly_trend():

    connnection = get_connection()
    cursor = connnection.cursor(dictionary=True)

    query = """SELECT upload_time,anomaly_percentage FROM pipeline_runs ORDER BY upload_time"""

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connnection.close()

    return result
