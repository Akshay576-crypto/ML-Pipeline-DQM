import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anamolies(df):

    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:

        return {
            "anomaly_count":0,
            "anomaly_percentage":0,
            "message":"No Numeric Columns Found"
        }
    model = IsolationForest(contamination=0.05,random_state=42)

    prediction = model.fit_predict(numeric_df)

    anomaly_count = (prediction == -1).sum()

    anomaly_percentage = round(anomaly_count/len(df) * 100,2)

    return {
        "Total_record":len(df),
        "anomaly_count":int(anomaly_count),
        "anomaly_percentage":anomaly_percentage
    }


