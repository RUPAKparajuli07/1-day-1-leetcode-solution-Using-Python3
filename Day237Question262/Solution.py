import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Filter for only unbanned clients and drivers
    unbanned_clients = users[(users['banned'] == 'No') & (users['role'] == 'client')]
    unbanned_drivers = users[(users['banned'] == 'No') & (users['role'] == 'driver')]
    
    # Rename columns for joining
    unbanned_clients = unbanned_clients.rename(columns={'users_id': 'client_id'})
    unbanned_drivers = unbanned_drivers.rename(columns={'users_id': 'driver_id'})
    
    # Merge trips with unbanned clients and drivers to filter only unbanned trips
    unbanned_trips = trips.merge(unbanned_clients[['client_id']], on='client_id') \
                          .merge(unbanned_drivers[['driver_id']], on='driver_id')
    
    # Filter trips between "2013-10-01" and "2013-10-03"
    filtered_trips = unbanned_trips[(unbanned_trips['request_at'] >= '2013-10-01') &
                                    (unbanned_trips['request_at'] <= '2013-10-03')]
    
    # Group by day and calculate total and canceled requests
    daily_stats = filtered_trips.groupby('request_at').agg(
        total_requests=('id', 'count'),
        canceled_requests=('status', lambda x: (x.isin(['cancelled_by_driver', 'cancelled_by_client'])).sum())
    ).reset_index()
    
    # Calculate cancellation rate and round to 2 decimal points
    daily_stats['Cancellation Rate'] = (daily_stats['canceled_requests'] / daily_stats['total_requests']).round(2)
    
    # Rename columns to match the expected output format
    daily_stats = daily_stats.rename(columns={'request_at': 'Day'})
    
    # Select only necessary columns
    result = daily_stats[['Day', 'Cancellation Rate']]
    
    return result
