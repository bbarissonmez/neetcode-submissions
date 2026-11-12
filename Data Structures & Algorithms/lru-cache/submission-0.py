class DoubleNode:
    def __init__(self, left=None, right=None, val=(0, 0)):
        self.left = left
        self.right = right
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = {}

        self.start = DoubleNode() # Dummy start
        self.end = DoubleNode() # Dummy end

        self.start.right = self.end
        self.end.left = self.start

    def remove(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def append(self, node):
        last = self.end.left

        last.right = node
        node.left = last
        node.right = self.end
        self.end.left = node

    def get(self, key: int) -> int:
        if key not in self.hash_table:
            return -1

        curr = self.hash_table[key]

        self.remove(curr)
        self.append(curr)

        return curr.val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            node = self.hash_table[key]
            self.remove(node)
            node.val = (key, value)
        else:
            node = DoubleNode(val=(key, value))
            self.hash_table[key] = node

        self.append(node)

        if len(self.hash_table) > self.capacity:
            lru = self.start.right

            self.remove(lru)
            self.hash_table.pop(lru.val[0])