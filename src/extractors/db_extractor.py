import pandas as pd
from sqlalchemy import create_engine


def extract_from_db(db_path, table_name):
    # Create a database connection
    engine = create_engine(f'sqlite:///{db_path}')

    # Retrieve data from the table
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)

    print(f"Extracted data from database table '{table_name}':")
    print(df.head())

    return df


def create_sample_db(db_path):
    # Create a sample database and table
    engine = create_engine(f'sqlite:///{db_path}')
    df = pd.DataFrame({
        'id': range(1, 6),
        'customer': ['A', 'B', 'C', 'D', 'E'],
        'total_spent': [100.0, 200.5, 150.75, 300.25, 180.5]
    })
    df.to_sql('customers', engine, index=False, if_exists='replace')
    print("Sample database created.")
