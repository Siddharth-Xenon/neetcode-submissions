class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, hi = 0, len(nums) - 1
        if nums[0] < nums[hi]:
            return nums[0]


        while low < hi:
            mid = low + (hi - low) // 2
            if nums[mid] < nums[0]:
                hi = mid
            else:
                low = mid + 1
        
        return nums[low]