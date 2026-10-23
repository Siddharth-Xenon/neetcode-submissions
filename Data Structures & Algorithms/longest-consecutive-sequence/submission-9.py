class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        output = 1
        count = 1
        for i in range(1, len(nums)):
            print(sorted_nums[i])
            if sorted_nums[i]-sorted_nums[i-1]==1:
                count+=1
                output = max(count, output)
            elif sorted_nums[i]-sorted_nums[i-1]==0:
                continue
            else:
                count = 1
        return output
    