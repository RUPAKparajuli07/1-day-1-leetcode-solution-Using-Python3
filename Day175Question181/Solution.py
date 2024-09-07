import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Merge employee data with itself to get manager info
    df = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('', '_manager'))
    
    # Filter rows where employee salary is greater than manager salary
    result = df[df['salary'] > df['salary_manager']]
    
    # Select only the 'name' column from the filtered result
    return result[['name']].rename(columns={'name': 'Employee'})

# Example usage:
employee_data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}

employee_df = pd.DataFrame(employee_data)

# Find employees who earn more than their managers
result_df = find_employees(employee_df)
print(result_df)
