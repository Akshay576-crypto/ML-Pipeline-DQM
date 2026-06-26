import pandas as pd

def calculate_missing_percentage(df):

    total_missing_values = df.isnull().sum().sum()
    total_cells = df.shape[0]*df.shape[1]

    if total_cells == 0:
        return 0
    
    missing_percentage = (total_missing_values/total_cells) * 100

    return round(missing_percentage,2)

def calculate_duplicate_percentage(df):

    total_row = len(df)

    duplicate_row = df.duplicated().sum()

    if total_row == 0:
        return 0
    
    duplicate_percentage = (duplicate_row/total_row) * 100
    return round(duplicate_percentage,2)

def calculate_quality_score(df):

    missing_percentage = calculate_missing_percentage(df)
    duplicate_percentage = calculate_duplicate_percentage(df)

    quality_score = 100 - missing_percentage - duplicate_percentage
    if quality_score <= 0:
        quality_score = 0
    
    quality_score = round(quality_score,2)

    if quality_score >=90 :
        quality_status = "Excellent"

    elif quality_score >= 75:
        quality_status = "Good"
    
    elif quality_score >= 50:
        quality_status = "Fair"

    else:
        quality_status = "Poor"

    return {
        "MissingPercentage":missing_percentage,
        "DuplicatePercentage":duplicate_percentage,
        "QualityScore":quality_score,
        "QualityStatus":quality_status
    }


    
    

    