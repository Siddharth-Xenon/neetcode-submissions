class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        tta = []
        stack = []
        fleet = 0
        merge = 0
        stack.append( (target - cars[0][0])/cars[0][1])
        for car in cars[1:]:
            
            tta = (target - car[0])/car[1]
            
            if tta > stack[-1]:
                stack.append(tta)
                fleet +=1
            
            
        return fleet + 1 




        

        