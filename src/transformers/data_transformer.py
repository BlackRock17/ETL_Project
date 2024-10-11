import pandas as pd


def transform_sales_data(df):
    # Calculation of total sales value
    df['total_value'] = df['quantity'] * df['price']

    # Convert the date to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Group by date and calculate daily sales
    daily_sales = df.groupby('date')['total_value'].sum().reset_index()
    daily_sales.columns = ['date', 'daily_total']

    return daily_sales


def transform_api_data(data):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Selecting only the required columns
    df = df[['userId', 'id', 'title']]

    # Renaming columns
    df.columns = ['user_id', 'post_id', 'post_title']

    return df


def transform_customer_data(df):
    # Categorize customers based on total spend
    df['category'] = pd.cut(df['total_spent'],
                            bins=[0, 100, 200, float('inf')],
                            labels=['Low', 'Medium', 'High'])

    return df