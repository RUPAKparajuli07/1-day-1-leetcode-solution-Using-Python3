from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Initialize sets for seen sequences and repeated sequences
        seen, repeated = set(), set()
        
        # Traverse the string and capture all 10-letter-long sequences
        for i in range(len(s) - 9):
            # Extract the current 10-letter-long substring
            sequence = s[i:i+10]
            
            # If the sequence has already been seen, add it to repeated
            if sequence in seen:
                repeated.add(sequence)
            else:
                # If not seen before, add it to seen set
                seen.add(sequence)
        
        # Return the list of repeated sequences
        return list(repeated)
