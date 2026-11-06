class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        total = sum(piles)  
        lo = ceil(total/h)
        print(lo)
        hi = max(piles)

        def predicate(mid):
            time_taken = 0
            k = mid
            for i in piles:
                
                if i < k:
                    time_taken += 1
                else:
                    time_taken += ceil(i/k)

            return time_taken <= h
                


        while lo < hi:
            mid = lo + (hi -lo) // 2
            if predicate(mid):
                hi = mid
            else:
                lo = mid+1


        return lo
