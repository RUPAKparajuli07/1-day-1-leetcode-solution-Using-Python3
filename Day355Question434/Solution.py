class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())  # Splitting the string by spaces and counting non-empty segments
