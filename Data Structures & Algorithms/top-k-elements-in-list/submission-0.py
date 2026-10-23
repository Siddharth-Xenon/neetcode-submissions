class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        top_k = [[key,value] for key,value in freq.items()] 
        top_k.sort(key = lambda x: x[1])
        top_elements = top_k[-k:]
        return [i[0] for i in top_elements]

