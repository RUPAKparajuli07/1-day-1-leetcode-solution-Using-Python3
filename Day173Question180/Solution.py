import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # Sort the DataFrame by 'id' column in ascending order
    logs = logs.sort_values(by=['id'], ascending=True)
    
    # Convert 'num' and 'id' columns to lists for easier iteration
    num_list = list(logs['num'])
    id_list = list(logs['id'])
    
    # Initialize an empty list to store numbers that appear consecutively
    consecutive_numbers_list = []
    
    # Iterate through the list of numbers, checking for consecutive occurrences
    for i in range(len(num_list) - 2):
        # Check if the current number is the same as the next two numbers
        # and if their ids are consecutive
        if num_list[i] == num_list[i+1] == num_list[i+2] and id_list[i] + 1 == id_list[i+1] and id_list[i] + 2 == id_list[i+2]:
            # If conditions are met, add the number to the list of consecutive numbers
            consecutive_numbers_list.append(num_list[i])
    
    # Convert the list of consecutive numbers to a DataFrame
    result_df = pd.DataFrame({"ConsecutiveNums": consecutive_numbers_list})
    
    # Remove duplicate entries from the DataFrame
    result_df = pd.DataFrame(result_df['ConsecutiveNums'].unique(), columns=['ConsecutiveNums'])
    
    # Return the final result DataFrame
    return result_df