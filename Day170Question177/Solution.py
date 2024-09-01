import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    d = set()  # Step to store unique salaries
    for i in employee["salary"]:
        d.add(i)
    c = list(d)
    c.sort()  # Sorting unique salaries
    
    if len(c) < N or len(c) == 0 or N <= 0:  # Edge cases check
        a = None
    else:
        a = c[-N]  # Access Nth highest salary
    
    r = "getNthHighestSalary(" + str(N) + ")"
    t = {r: [a]}
    o = pd.DataFrame(t)  # Prepare output DataFrame
    return o

# Example usage
employee_data = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
})

result = nth_highest_salary(employee_data, 2)
print(result)

# Testing for a non-existent Nth salary
result = nth_highest_salary(employee_data, 4)
print(result)
