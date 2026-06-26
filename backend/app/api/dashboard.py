from app.database.db import get_connection
from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard-history")
def dashboard_history():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT COUNT(*) AS total_runs,
        AVG(quality_score) AS average_quality_score,
        MAX(quality_score) AS best_quality_score,
        MIN(quality_score) AS worst_quality_score,
        SUM(anomaly_count) AS total_anamolies
        FROM pipeline_runs"""
    
    cursor.execute(query)
    result = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()

    return result

@router.get("/quality-trend")
def quality_trend():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """SELECT upload_time,quality_score FROM pipeline_runs ORDER BY upload_time"""

    cursor.execute(query)

    result = cursor.fetchall()

    connection.close()

    return result
