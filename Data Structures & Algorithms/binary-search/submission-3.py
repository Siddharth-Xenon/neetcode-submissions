class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums)
        low = 0
        while low < hi:
            mid = low + (hi - low) // 2
            if nums[mid] > target:
                hi = mid
            elif nums[mid] == target:
                return mid
            else:
                low = mid + 1 
        return -1
            



                



        