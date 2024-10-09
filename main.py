from src.extractors.csv_extractor import extract_from_csv
from src.extractors.api_extractor import extract_from_api
from src.extractors.db_extractor import extract_from_db, create_sample_db


def main():
    # Extract
    sales_df = extract_from_csv('data/sales_data.csv')
    api_data = extract_from_api('https://jsonplaceholder.typicode.com/posts')

    db_path = 'data/sample.db'
    create_sample_db(db_path)
    customers_df = extract_from_db(db_path, 'customers')

    # Transform (ще добавим по-късно)

    # Load (ще добавим по-късно)


if __name__ == "__main__":
    main()
