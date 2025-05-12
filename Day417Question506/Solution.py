from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Step 1: Pair each score with its original index
        indexed_scores = list(enumerate(score))
        
        # Step 2: Sort the scores in descending order based on score value
        indexed_scores.sort(key=lambda x: -x[1])
        
        # Step 3: Prepare a result list of the same length
        result = [""] * len(score)
        
        # Step 4: Assign ranks
        for rank, (idx, _) in enumerate(indexed_scores):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result
