class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        total = 0
        left, right = 0, 0
        n = len(nums)
        while right < n and left <= right:
            print(nums[right], nums[left], total)
            total += nums[right]

            while total >= target:
                if count == 0:
                    count = right-left+1
                else:
                    count = min(count, right-left+1)
                total-=nums[left]
                left+=1
            
            right+=1
        
        return count
