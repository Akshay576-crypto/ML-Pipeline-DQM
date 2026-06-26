from fastapi import APIRouter
from app.database.db import get_connection

router =APIRouter()

@router.get("/pipeline-history")
def get_pipeline_histort():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """SELECT * FROM pipeline_runs ORDER BY upload_time DESC"""

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close() 
    conn.close() 
    return { "total_runs": len(data), "history": data }


