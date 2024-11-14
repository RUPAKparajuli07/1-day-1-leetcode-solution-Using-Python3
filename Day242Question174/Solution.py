from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Step 1: Sort the citations in descending order
        citations.sort(reverse=True)
        
        # Step 2: Find the h-index by iterating through the sorted list
        h_index = 0
        for i, citation in enumerate(citations):
            # Check if we have at least `i + 1` papers with `i + 1` citations
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index
