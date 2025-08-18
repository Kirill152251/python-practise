# https://leetcode.com/problems/min-stack/description/
# Design, Stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            return
        if self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            cur_min = self.min_stack.pop()
            self.min_stack.append(val)
            self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == "__main__":
    ms = MinStack()
    ms.push(1000)
    ms.push(9900)
    ms.push(210)

    print(ms.min_stack)
    print(ms.getMin())
    print(ms.top())

    ms.pop()

    print(ms.getMin()) # -> 1000 
    print(ms.top()) # -> 9900
