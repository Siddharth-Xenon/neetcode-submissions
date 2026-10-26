class MinStack:
    def __init__(self):
        self.stack = []          # entries are (value, min_at_this_point)

    def push(self, value: int) -> None:
        current_min = value if not self.stack else min(value, self.stack[-1][1])
        self.stack.append((value, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]