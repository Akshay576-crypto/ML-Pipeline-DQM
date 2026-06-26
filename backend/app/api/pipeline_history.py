from app.database.db import get_connection


def save_pipeline_run(file_name,total_record,total_columns,quality_report,anomaly_report):
    
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """INSERT INTO pipeline_runs
    (file_name,
      total_records, 
      total_columns, 
      quality_score, 
      quality_status, 
      anomaly_count, 
      anomaly_percentage
      )
    VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    value = (file_name,
             total_record,
             total_columns,
             quality_report["QualityScore"],
             quality_report["QualityStatus"],
             anomaly_report["anomaly_count"],
             anomaly_report["anomaly_percentage"],
             )
    
    cursor.execute(query,value)

    connection.commit()
    cursor.close()
    connection.close()
    
              






