class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for i in nums:
            if i in mapping:
                return True
            else:
                mapping[i]=1
        return False
        