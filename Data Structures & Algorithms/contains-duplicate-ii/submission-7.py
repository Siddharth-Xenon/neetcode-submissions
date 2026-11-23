class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for j in range(len(nums)):
            # check constraint
            if nums[j] in window:
                return True
            
            #grow window
            window.add(nums[j]) 
            
            #fix window valid
            if len(window) > k:                
                window.remove(nums[j-k])
        return False
            



        