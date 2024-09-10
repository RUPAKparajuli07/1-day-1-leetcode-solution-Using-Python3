import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the Employee and Department data on departmentId
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id')
    
    # Sort by department and salary in descending order
    merged_df = merged_df.sort_values(by=['name_y', 'salary'], ascending=[True, False])
    
    # Rank salaries within each department and keep only top 3 unique salaries
    merged_df['rank'] = merged_df.groupby('name_y')['salary'].rank(method='dense', ascending=False)
    top_salaries_df = merged_df[merged_df['rank'] <= 3]
    
    # Select only the necessary columns and rename them
    result = top_salaries_df[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result
