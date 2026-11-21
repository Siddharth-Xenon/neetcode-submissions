class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        op = 0
        co = 0
        valid = 0
        path = []
        def is_valid(s):
            if len(s) % 2 !=0:
                return False
        
            stack = []
            mapping = {
                "]":"[",
                "}":"{",
                ")":"("
            }
            for i in range(len(s)):
                value = s[i]
                if value in mapping.keys():
                    if not stack:
                        return False
                    if stack.pop() != mapping.get(value):
                        return False
                    continue
                
                stack.append(value)
                # print(stack)
            
            return stack == []

        def backtrack(op, co):
            if co > op:
                return
            if op==n and op == co:
                results.append("".join(path)) 
                return
            

            if op < n:
                path.append("(")
                
                backtrack(op+1, co)
                path.pop()
            
            if co<op:
                path.append(")")
                backtrack(op, co+1)
                path.pop()

        backtrack(0,0)
        return results