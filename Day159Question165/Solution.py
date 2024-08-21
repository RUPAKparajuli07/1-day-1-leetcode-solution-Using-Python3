class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings into lists of revisions
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        
        # Determine the maximum length of the revision lists
        max_len = max(len(revisions1), len(revisions2))
        
        # Compare each revision pair
        for i in range(max_len):
            # Get the integer value of the current revision, or 0 if out of bounds
            rev1 = int(revisions1[i]) if i < len(revisions1) else 0
            rev2 = int(revisions2[i]) if i < len(revisions2) else 0
            
            # Compare the revisions
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        # If all revisions are equal, return 0
        return 0
