class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        i, j = 0, 0
        window = set()
        while j < len(nums):
            # check constraint
            if nums[j] in window:
                return True
            
            #grow window
            window.add(nums[j]) 
            
            #fix window valid
            if j-i >= k:                
                window.remove(nums[i])
                i+=1
            
            j+=1

        return False
            



        