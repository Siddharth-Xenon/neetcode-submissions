class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        i, j = 0, 0
        window = set()
        while j < len(nums):
             
            if nums[j] in window:
                return True
            
            window.add(nums[j]) 

            if j-i >= k:                
                window.remove(nums[i])
                i+=1

            j+=1
            

        return False
            



        