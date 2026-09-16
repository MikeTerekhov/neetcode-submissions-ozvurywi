class MyHashMap:

    def __init__(self):
        self.a = []

    def put(self, key: int, value: int) -> None:
        for entry in self.a:
            k = entry[0]
            v = entry[1]
            if k == key:
                self.a.remove(entry)

        self.a.append([key, value])

    def get(self, key: int) -> int:
        for entry in self.a:
            k = entry[0]
            v = entry[1]
            if k == key:
                return v

        return -1 

    def remove(self, key: int) -> None:
        for entry in self.a:
            k = entry[0]
            v = entry[1]
            if k == key:
                self.a.remove(entry)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)