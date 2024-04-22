from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path, result)
                path.pop()
        
        result = []
        backtrack(0, target, [], result)
        return result

# Test the solution
solution = Solution()
candidates1 = [2, 3, 6, 7]
target1 = 7
print(solution.combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(solution.combinationSum(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates3 = [2]
target3 = 1
print(solution.combinationSum(candidates3, target3))  # Output: []
