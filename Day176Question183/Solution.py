import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Left join customers with orders on the customerId
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    
    # Filter customers who have never ordered anything (customerId is NaN)
    never_ordered = merged_df[merged_df['customerId'].isna()]

    # Select only the 'name' column and rename it to 'Customers'
    result = never_ordered[['name']].rename(columns={'name': 'Customers'})
    
    return result
