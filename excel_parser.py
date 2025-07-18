import pandas as pd

def normalize_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def process_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)
    df = normalize_column_names(df)
    return df