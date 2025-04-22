class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1: Remove dashes and convert to uppercase
        s = s.replace('-', '').upper()

        # Step 2: Start grouping from the end
        result = []
        while len(s) > 0:
            # Take the last k characters and add to result
            result.append(s[-k:])
            # Remove the last k characters from s
            s = s[:-k]

        # Step 3: Since we added from the end, reverse the result and join with dashes
        return '-'.join(result[::-1])
