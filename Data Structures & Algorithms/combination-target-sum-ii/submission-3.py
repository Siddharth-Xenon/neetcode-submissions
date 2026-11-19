class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, path):


            if sum(path) == target:
                print("passed")
                result.append(path[:])
                return

            if index == len(candidates) or sum(path)>target:
                return 
            
            
            path.append(candidates[index])
            backtrack(index+1, path)
            path.pop()

            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1

            backtrack(index+1, path)
        
        backtrack(0, [])
        return result

