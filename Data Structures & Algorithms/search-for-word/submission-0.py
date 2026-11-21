class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r,c,k):
            if k == len(word):
                return True

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[k]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
            backtrack(r+1, c, k+1)
            or backtrack(r-1, c, k+1)
            or backtrack(r, c+1, k+1)
            or backtrack(r, c-1, k+1)
            )

            board[r][c] = temp
            return found
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                found = backtrack(row,col,0)
                if found:
                    return found
        return False
        
                

            
            
        