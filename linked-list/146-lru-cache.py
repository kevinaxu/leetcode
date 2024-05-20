'''
Conceptually: 

Cache key / values are going to be stored in a Hash Map 
- Instead of storing the key values in the Hash map, we're going to store references to the Linked List node

How do we store orderings?
- Linked List (Doubly) 
    - Dummy nodes to: 
        - Least recently used (head) 
        - Most recently used (tail) 
    - These are going to exist in the hash table as well 
'''

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.head = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}         # map key -> node

        # least = LRU, right = MRU 
        self.left, self.right = Node(0, 0), Node(0 ,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    # every time we get something, we need to update it to the most recent
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_list(node)
            self.insert_at_right(node)
            return node.val
        else:
            return -1 

    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_right(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev 
        node.next = self.right
        self.right.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:            # node already exists, update the value and move to 
            self.remove_from_list(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert_at_right(self.cache[key])

        if len(self.cache) > self.cap:              # need to do eviction
            lru = self.left.next 
            lru.next.prev = self.left               # update prev pointer
            self.left.next = lru.next               # update self.left.next 
            self.remove_from_list(lru)
            del self.cache[lru.key]


'''
# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
'''