class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        results = []
        nums.sort()
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

            while index < len(nums)-1 and nums[index] == nums[index+1]:
                index+=1

            backtrack(index+1, path)

        backtrack(0, [])
        return results
        