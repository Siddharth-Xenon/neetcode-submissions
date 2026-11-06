class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        

        if target < matrix[0][0] or target > matrix[n-1][m-1]:
            return False

        
        def predicate(mid):
            if matrix[mid][0] <= target:
                return True
            return False
        
        # lo, hi = matrix[0][0] , matrix[n][0]
        lo, hi = 0 , n -1
        while lo < hi: 
            mid = (lo + hi + 1)//2
            if predicate(mid):
                lo = mid
            else:
                hi = mid -1
        
        row = lo

        lo, hi = 0 , m-1

        def predicate2(mid):
            if matrix[row][mid] <= target:
                return True
            return False
        
        while lo < hi: 
            mid = (lo + hi + 1)//2

            if predicate2(mid):
                lo = mid
            else:
                hi = mid - 1
        

        return matrix[row][lo] == target



        