"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        early_free = []
        intervals.sort(key = lambda x: x.start)

        for meet in intervals:
            if not early_free:
                heapq.heappush(early_free, meet.end)
                continue
            earliest_free = early_free[0]
            if meet.start>=earliest_free:
                heapq.heappushpop(early_free, meet.end)
            else:
                heapq.heappush(early_free, meet.end)
        
        return len(early_free)


        