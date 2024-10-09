import pandas as pd


def transform_sales_data(df):
    # Изчисляване на обща стойност на продажбите
    df['total_value'] = df['quantity'] * df['price']

    # Преобразуване на датата в datetime формат
    df['date'] = pd.to_datetime(df['date'])

    # Групиране по дата и изчисляване на дневни продажби
    daily_sales = df.groupby('date')['total_value'].sum().reset_index()
    daily_sales.columns = ['date', 'daily_total']

    return daily_sales


def transform_api_data(data):
    # Преобразуване на списъка от речници в DataFrame
    df = pd.DataFrame(data)

    # Избиране само на нужните колони
    df = df[['userId', 'id', 'title']]

    # Преименуване на колоните
    df.columns = ['user_id', 'post_id', 'post_title']

    return df


def transform_customer_data(df):
    # Категоризиране на клиентите въз основа на общо похарчената сума
    df['category'] = pd.cut(df['total_spent'],
                            bins=[0, 100, 200, float('inf')],
                            labels=['Low', 'Medium', 'High'])

    return df