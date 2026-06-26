from app.database.db import get_connection
from fastapi import APIRouter

router = APIRouter()
@router.get("/analytics-report")
def analytics_report():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM pipeline_runs
    ORDER BY upload_time DESC
    LIMIT 10
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    if not rows:
        return {
            "quality_score": 0,
            "anomaly_count": 0,
            "total_records": 0,
            "quality_status": "No Data",
            "history": []
        }

    latest = rows[0]

    history = []

    for r in rows[::-1]:
        history.append({
            "month": str(r["upload_time"]),
            "score": r["quality_score"]
        })

    return {
        "quality_score": latest["quality_score"],
        "anomaly_count": latest["anomaly_count"],
        "total_records": latest["total_records"],
        "quality_status": latest["quality_status"],
        "history": history
    }
