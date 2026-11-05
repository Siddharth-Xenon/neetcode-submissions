class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        tta = 0
        wall = 0
        fleet = 0
        for car in cars:
            
            tta = (target - car[0])/car[1]
            
            if tta > wall:
                wall = tta
                fleet +=1
            
            
        return fleet




        

        