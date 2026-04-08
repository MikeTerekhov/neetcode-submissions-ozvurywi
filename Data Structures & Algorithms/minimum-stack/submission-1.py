class MinStack:

    def __init__(self):
        # stack
        self.vals = []
        # min stack
        self.m = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        
        # find the min between top of min stack and val
        # make sure min stack has something in it
        val = min(val, self.m[-1] if self.m else val)
        self.m.append(val)

    def pop(self) -> None:
        self.vals.pop()
        self.m.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.m[-1]

