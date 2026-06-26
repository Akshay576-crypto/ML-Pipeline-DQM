def report_generate(file_name,total_records,total_columns,profile,quality_report):

    return { "datasetsummary": 
            { "file_name": file_name,
              "total_records": total_records,
                "total_column": total_columns
            },
              "data_profile": profile, 
              "quality_report": quality_report }
