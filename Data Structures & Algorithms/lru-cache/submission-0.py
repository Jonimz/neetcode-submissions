class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Sentinels: left = LRU end, right = MRU end
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the list
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert a node at the MRU end (just left of self.right)
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move node to MRU
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node before replacing/moving
            self.remove(self.cache[key])

        # Insert new / updated node at MRU
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Evict LRU if over capacity
        if len(self.cache) > self.cap:
            lru = self.left.next  # least recently used
            self.remove(lru)
            del self.cache[lru.key]
