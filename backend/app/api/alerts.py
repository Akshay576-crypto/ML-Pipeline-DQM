from fastapi import APIRouter
from app.database.db import get_connection

router = APIRouter()

@router.get("/alert")
def get_alerts():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """SELECT * FROM pipeline_runs
    ORDER BY upload_time DESC LIMIT 1"""

    cursor.execute(query)

    latest_run = cursor.fetchone()

    cursor.close()
    connection.close()

    if not latest_run:

        return {
            "Toatal_Alerts":0,
            "Alerts":[]
        }
    
    alerts = []

    if latest_run["quality_score"]<80:
        
        alerts.append({
            "Type":"Quality_Alerts",
            "severity":"High",
            "message":f"quality drop score{latest_run['quality_score']}"
        })
    
    if latest_run["quality_score"]>10:
        
        alerts.append({
            "Type":"ANOMOLY_ALERT",
            "severity":"MEDIUM",
            "message":f"anamoly percentage reached{latest_run['quality_score']}"
        })

    return {
        "total_alerts":len(alerts),
        "alerts":alerts
    }
    

