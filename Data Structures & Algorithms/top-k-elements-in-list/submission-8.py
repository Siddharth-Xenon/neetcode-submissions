class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq_count = {}

        for i in range(len(nums)):
            unit = nums[i]
            if unit in freq_count.keys():
                freq_count[unit] += 1
            else:
                freq_count[unit] = 1
        
        heap = [(-value, key) for key,value in freq_count.items()]
        largest = heapq.nsmallest(10, heap)
        largest = [(key, -value) for value, key in largest]


        return [arr[0] for arr in largest[:k]]

