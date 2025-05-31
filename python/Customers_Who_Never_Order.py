import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  return customers[~customers['id'].isin(orders['customerId'])].drop(columns=['id']).rename(columns={'name': 'Customers'})
