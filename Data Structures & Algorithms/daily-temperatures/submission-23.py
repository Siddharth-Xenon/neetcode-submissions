class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            stack = []
            temp = temperatures
            output = [0] * len(temperatures)
            stack.append(0)

            for i in range(1,len(temp)):


                curr = temp[i]
                
                while stack and curr > temp[stack[-1]]:
                    res = i - stack[-1]
                    output[stack[-1]] = res
                    stack.pop()
                    
                # if  not stack or curr <= temp[stack[-1]]:
                stack.append(i)

            return output



