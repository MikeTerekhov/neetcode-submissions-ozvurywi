class MyStack:

    def __init__(self):
        self.a = []

        # 1 2 3
        # a - 
        # b - 2, 1

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        for i in range(len(self.a) - 1):
            self.push(self.a.pop(0))
        return self.a.pop(0)

    def top(self) -> int:
        return self.a[-1]

    def empty(self) -> bool:
        return len(self.a) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()