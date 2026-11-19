class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        results = []
        def backtrack(index, path):
            nonlocal results
            if index == len(nums):
                results.append(path[:])
                return
            

            if path in results:
                return
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()

            backtrack(index+1, path)

        backtrack(0, [])
        return results
        