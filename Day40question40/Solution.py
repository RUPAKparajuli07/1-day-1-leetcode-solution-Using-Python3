class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to handle duplicates properly
        candidates.sort()
        result = []
        
        def backtrack(start, target, path):
            if target == 0:
                # If the target is achieved, add the current combination to the result
                result.append(path)
                return
            if target < 0:
                # If the target becomes negative, backtrack
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    # Skip duplicates to avoid duplicate combinations
                    continue
                # Explore the next candidate
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        
        backtrack(0, target, [])
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
print(solution.combinationSum2([2,5,2,1,2], 5))      # Output: [[1, 2, 2], [5]]
