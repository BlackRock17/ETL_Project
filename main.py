from src.extractors.csv_extractor import extract_from_csv


def main():
    # Extract
    sales_df = extract_from_csv('data/sales_data.csv')

    # Transform (ще добавим по-късно)

    # Load (ще добавим по-късно)


if __name__ == "__main__":
    main()
