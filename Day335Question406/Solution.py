from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the people list
        people.sort(key=lambda x: (-x[0], x[1]))  # Sort by height descending, then k ascending
        
        queue = []  # Result queue
        
        # Step 2: Insert people at the correct index
        for person in people:
            queue.insert(person[1], person)  # Insert at index k
        
        return queue
