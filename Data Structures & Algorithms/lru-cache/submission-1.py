class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # KEY : this is 
            # key : number
            # val : pointer to a node item
        self.cache = {} # maps key -> node

        # create left node to point to LEAST recently used
        self.left = Node(0, 0)
        # create right node to point to MOST recently used
        self.right = Node(0, 0)

        # link them to each other
        self.left.nxt = self.right
        self.right.prev = self.left

    # remove from list
    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    #  insert node @ right
    def insert(self, node):
        # 1 b4 last
        prev = self.right.prev
        # last
        nxt = self.right

        nxt.prev = node
        node.nxt = nxt

        prev.nxt = node
        node.prev = prev



    def get(self, key: int) -> int:
        if key in self.cache:
            # must update most recently used
            # remove
            self.remove(self.cache[key])
            # insert
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if putting one that already exists, must replace it
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # over-filled
        if len(self.cache) > self.capacity:
            # remove the LRU
            LRU = self.left.nxt
            self.remove(LRU)
            # delete from cache
            del self.cache[LRU.key]
        
