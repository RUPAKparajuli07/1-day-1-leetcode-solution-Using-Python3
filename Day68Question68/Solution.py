from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []  # Resultant list of justified text lines
        cur_line = []  # Current line being processed
        num_of_letters = 0  # Number of letters in the current line
        
        for word in words:
            # Check if adding the next word would exceed the maxWidth
            if num_of_letters + len(word) + len(cur_line) > maxWidth:
                # Justify the current line
                for i in range(maxWidth - num_of_letters):
                    cur_line[i % (len(cur_line) - 1 or 1)] += ' '
                res.append(''.join(cur_line))
                cur_line, num_of_letters = [], 0
            
            cur_line.append(word)
            num_of_letters += len(word)
        
        # Handle the last line (left-justified)
        res.append(' '.join(cur_line).ljust(maxWidth))
        return res

# Example usage:
solution = Solution()
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
print(solution.fullJustify(words1, maxWidth1))

words2 = ["What","must","be","acknowledgment","shall","be"]
maxWidth2 = 16
print(solution.fullJustify(words2, maxWidth2))

words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth3 = 20
print(solution.fullJustify(words3, maxWidth3))
