import pandas as pd
from sqlalchemy import create_engine

def load_to_csv(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"Data loaded to CSV: {file_path}")

def load_to_json(df, file_path):
    df.to_json(file_path, orient='records')
    print(f"Data loaded to JSON: {file_path}")

def load_to_db(df, table_name, db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql(table_name, engine, index=False, if_exists='replace')
    print(f"Data loaded to database table: {table_name}")