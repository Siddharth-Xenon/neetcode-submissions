class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                value1=int(stack.pop())
                value2=int(stack.pop())
                if token =="+":
                    res = value2 + value1
                elif token =="-":
                    res = value2 - value1
                elif token =="*":
                    res = value2 * value1
                elif token =="/":
                    res = value2 / value1

                stack.append(res)
        return int(stack[-1])

        