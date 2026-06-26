import pandas as pd

def generate_profile(df):

    profile = []

    for column in df.columns:

        column_profile = {
            "column_name":column,
            "data_type": str(df[column].dtype),
            "missing_value":int(df[column].isnull().sum()),
            "missing_percentage": round((df[column].isnull().sum()/len(df))*100,2),
            "unique_value":int(df[column].nunique())
        }

        # if data is numerical column 

        if pd.api.types.is_numeric_dtype(df[column]):

            column_profile["min"] = float(df[column].min())
            column_profile["max"] = float(df[column].max())
            column_profile["mean"] = round(float(df[column].mean()),2)
            column_profile["median"] = round(float(df[column].median()),2)
            column_profile["std"] = round(float(df[column].std()),2)

            profile.append(column_profile)

    return profile