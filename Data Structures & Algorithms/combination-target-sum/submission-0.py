class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        
        def backtrack(index, path):
            nonlocal result
            if sum(path) == target:
                result.append(path[:])
                return

            if sum(path) > target or index >= len(nums):
                return
            
            path.append(nums[index])
            backtrack(index, path)
            path.pop()

            backtrack(index+1, path)
        
        backtrack(0 , [])
        return result