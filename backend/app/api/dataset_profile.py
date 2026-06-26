from fastapi import APIRouter
from app.database.db import get_connection

router = APIRouter()

@router.get("/dataset-profile/{upload_id}")
def dataset_profile(upload_id: int):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        u.upload_id,
        u.file_name,
        u.total_records,
        u.total_columns,
        d.missing_values,
        d.duplicate_records,
        d.anomaly_count,
        d.quality_score
    FROM uploads u
    JOIN dataset_profile d
    ON u.upload_id = d.upload_id
    WHERE u.upload_id = %s
    """

    cursor.execute(query, (upload_id,))
    result = cursor.fetchone()

    connection.close()

    return result