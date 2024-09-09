import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Merge employee and department DataFrames
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # Step 2: Find the maximum salary for each department
    max_salaries = merged_df.groupby('departmentId')['salary'].transform(max)
    
    # Step 3: Filter employees who have the maximum salary in their department
    highest_salary_employees = merged_df[merged_df['salary'] == max_salaries]
    
    # Step 4: Select relevant columns: Department name, Employee name, and Salary
    result = highest_salary_employees[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']  # Renaming columns as per the output requirement
    
    return result

# Example usage with provided data
employee_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
})

department_data = pd.DataFrame({
    'id': [1, 2],
    'name': ['IT', 'Sales']
})

result = department_highest_salary(employee_data, department_data)
print(result)
