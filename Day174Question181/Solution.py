import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by email and count occurrences
    email_counts = person.groupby('email').size().reset_index(name='count')
    
    # Filter emails that appear more than once
    duplicates = email_counts[email_counts['count'] > 1]
    
    # Return only the 'email' column as 'Email'
    return duplicates[['email']].rename(columns={'email': 'Email'})

# Example usage
data = {'id': [1, 2, 3], 'email': ['a@b.com', 'c@d.com', 'a@b.com']}
person = pd.DataFrame(data)

# Call the function to get duplicate emails
result = duplicate_emails(person)
print(result)
