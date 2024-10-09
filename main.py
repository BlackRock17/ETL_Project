from src.extractors.csv_extractor import extract_from_csv
from src.extractors.api_extractor import extract_from_api
from src.extractors.db_extractor import extract_from_db, create_sample_db
from src.transformers.data_transformer import transform_sales_data, transform_api_data, transform_customer_data


def main():
    # Extract
    sales_df = extract_from_csv('data/sales_data.csv')
    api_data = extract_from_api('https://jsonplaceholder.typicode.com/posts')
    db_path = 'data/sample.db'
    create_sample_db(db_path)
    customers_df = extract_from_db(db_path, 'customers')

    # Transform
    daily_sales = transform_sales_data(sales_df)
    posts_df = transform_api_data(api_data)
    categorized_customers = transform_customer_data(customers_df)

    # Print transformed data
    print("\nTransformed daily sales:")
    print(daily_sales)
    print("\nTransformed posts data:")
    print(posts_df.head())
    print("\nTransformed customer data:")
    print(categorized_customers)

    # Load (ще добавим по-късно)


if __name__ == "__main__":
    main()