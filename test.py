report = {"datasetsummary":{
        "file_name":file_name,
        "total_records":total_records,
        "total_column":total_columns
    },

    "data_profile":profile,
    "quality_report":{
        "missing_percentage":quality_report["Missingpercentage"],
        "duplicate_percentage":quality_report["Duplicatepercentage"],
        "Quality_score":quality_report["Qualityscore"],
        "Quality_status":quality_report["Qualitystatus"]
    }
              }
    