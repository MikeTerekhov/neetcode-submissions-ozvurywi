class DynamicArray:
    
    def __init__(self, capacity: int):
        self.ar = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.ar[i]

    def set(self, i: int, n: int) -> None:
        self.ar[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() + 1 > self.capacity:
            self.resize()
        self.ar.append(n)

    def popback(self) -> int:
        num = self.ar.pop()
        return num

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.ar)
    
    def getCapacity(self) -> int:
        return self.capacity
