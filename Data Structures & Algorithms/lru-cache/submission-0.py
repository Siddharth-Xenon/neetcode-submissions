class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def detach(self, node):
        front = node.prev
        front.next = node.next
        node.next.prev = front

    def attach(self, node):
        last = self.tail.prev
        last.next = node
        self.tail.prev = node
        node.prev = last
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.detach(node)
        self.attach(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        

        if key in self.cache: 
            node = self.cache[key]
            self.detach(node)
            node.val = value
            self.attach(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self.detach(lru)
                del self.cache[lru.key]
            node = Node(key,value)
            self.attach(node)
            self.cache[key] = node
            
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)