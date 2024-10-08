from src.extractors.csv_extractor import extract_from_csv
from src.extractors.api_extractor import extract_from_api


def main():
    # Extract
    sales_df = extract_from_csv('data/sales_data.csv')
    api_data = extract_from_api('https://jsonplaceholder.typicode.com/posts')

    # Transform (ще добавим по-късно)

    # Load (ще добавим по-късно)


if __name__ == "__main__":
    main()
