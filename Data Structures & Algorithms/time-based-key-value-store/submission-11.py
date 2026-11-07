class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        prev = self.store.get(key, [])
        prev.append([timestamp,value])
        self.store.update({key:prev})

    def get_latest(self, key:str, target:int):
        values = self.store.get(key, None)
        
        if not values:
            return ""

        lo, hi = 0 , len(values)-1

        while lo < hi:
            mid = (hi + lo + 1 ) // 2
            if values[mid][0] <= target:
                lo = mid
            else:
                hi = mid - 1

        if target >= values[lo][0]:
            return values[lo][1]
        
        return ""


    def get(self, key: str, timestamp: int) -> str:
        return self.get_latest(key, timestamp)
       
        
