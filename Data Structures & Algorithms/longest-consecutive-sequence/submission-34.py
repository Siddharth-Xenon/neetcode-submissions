class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numbers = set(nums)
        # print(numbers)
        longest = 0
        length=1
        for num in numbers:
            if num-1 not in numbers:
                length  = 1
            
                while num + length in numbers:
                    print(num, length)
                    length += 1
            
            longest = max(longest, length)
        return longest

    