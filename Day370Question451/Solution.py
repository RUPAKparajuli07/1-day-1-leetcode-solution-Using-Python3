from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        frequency = Counter(s)
        
        # Step 2: Sort characters based on frequency in descending order
        # The sorted function sorts by frequency (value), and we use reverse=True for descending order
        sorted_chars = sorted(frequency.items(), key=lambda x: -x[1])
        
        # Step 3: Construct the result string by repeating characters according to their frequency
        result = ''.join([char * count for char, count in sorted_chars])
        
        return result
