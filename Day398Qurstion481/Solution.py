class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2
        num = 1
        
        while len(s) < n:
            s.extend([num] * s[i])
            num = 3 - num
            i += 1

        return s[:n].count(1)
