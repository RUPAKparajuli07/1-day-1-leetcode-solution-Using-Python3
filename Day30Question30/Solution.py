from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = len(words) * word_len
        words_count = Counter(words)
        result = []
        
        for i in range(len(s) - total_len + 1):
            seen = Counter()
            for j in range(i, i + total_len, word_len):
                word = s[j:j+word_len]
                if word in words_count:
                    seen[word] += 1
                    if seen[word] > words_count[word]:
                        break
                else:
                    break
            if seen == words_count:
                result.append(i)
        
        return result
