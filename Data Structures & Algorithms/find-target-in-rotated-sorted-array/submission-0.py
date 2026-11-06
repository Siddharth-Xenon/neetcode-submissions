class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        def find_pivot(nums):
            lo , hi = 0 , len(nums)-1
            
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < nums[0]:
                    hi = mid
                else:
                    lo = mid + 1
            # print(lo)
            return lo


        if target < nums[0]:
            lo, hi = find_pivot(nums), n-1
        elif nums[0] < nums[n-1]:
            lo, hi = 0, n-1
        else:
            lo, hi = 0 , find_pivot(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        if nums[lo] == target:
            return lo
        return -1
        