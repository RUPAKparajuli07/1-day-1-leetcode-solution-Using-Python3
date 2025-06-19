import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find each player's first login date
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login.columns = ['player_id', 'first_login']
    
    # Step 2: Merge this info back to original activity
    merged = activity.merge(first_login, on='player_id')
    
    # Step 3: Calculate the next day of first login
    merged['next_day'] = merged['first_login'] + pd.Timedelta(days=1)
    
    # Step 4: Check if player logged in on the next day
    next_day_logins = merged[merged['event_date'] == merged['next_day']]['player_id'].nunique()
    
    # Step 5: Total players
    total_players = activity['player_id'].nunique()
    
    # Step 6: Calculate fraction
    fraction = round(next_day_logins / total_players, 2)
    
    return pd.DataFrame({'fraction': [fraction]})
