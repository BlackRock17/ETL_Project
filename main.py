from src.extractors.csv_extractor import extract_from_csv
from src.extractors.api_extractor import extract_from_api
from src.extractors.db_extractor import extract_from_db, create_sample_db
from src.transformers.data_transformer import transform_sales_data, transform_api_data, transform_customer_data
from src.loaders.data_loader import load_to_csv, load_to_json, load_to_db


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

    # Load
    load_to_csv(daily_sales, 'data/daily_sales.csv')
    load_to_json(posts_df, 'data/posts.json')
    load_to_db(categorized_customers, 'categorized_customers', 'data/etl_results.db')


if __name__ == "__main__":
    main()