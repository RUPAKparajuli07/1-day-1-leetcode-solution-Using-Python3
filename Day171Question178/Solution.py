import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort the DataFrame by 'score' in descending order
    scores = scores.sort_values(by='score', ascending=False)
    
    # Rank the scores using 'dense' method for consecutive ranking without gaps
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # Select the required columns and return the result
    result = scores[['score', 'rank']]
    
    return result
