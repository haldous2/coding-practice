"""
Design and build a "least recently used" cache, which evicts the least recently used item.
The cache should map from keys to values 
(allowing you to insert and retrieve a value associated with a particular key)
and be initialized with a max size. 
When it is full, it should evict the least recently used item. 
You can assume the keys are integers and the values are strings.

Need:
Initialize: with max size, empty data struture
Insert, Retrieve (Peek)
Delete will happen automatically via least used on insert when full
Build as class for reuse

Use a hash table for quick lookups, and a linked list to maintian order, and LRU status
"""
class LRUCache(object):

    def __init__(self, maxsize):
        self.head = None
        self.keys = {}              # track keys for fast key to node lookups
        self.last = None            # track last node for trimming
        self.cursize = 0            # current node count
        self.maxsize = maxsize

    class Node(object):
        def __init__(self, key, val):
            self.next = None
            self.prev = None
            self.key = key
            self.val = val

    def test_keys(self, key):
        if key in self.keys:
            print "test keys:", key, self.keys[key].val

    def insert_val(self, key, val):
        if key in self.keys:
            self.move_node_to_front(self.keys[key])
            self.keys[key].val = val
        else:
            # Create new node
            node = self.Node(key, val)
            # Track new key
            self.keys[key] = node
            # Insert node at front
            self.insert_head(node)
            # Remove any over max
            self.remove_tail()

    def insert_head(self, node):
        if self.head is None:
            # head not set - first node
            self.head = node
            self.last = node    # track last node for removal
        else:
            # head is set - need to shift stuff around
            temp = self.head
            temp.prev = node
            node.next = temp
            self.head = node
        self.cursize += 1

    def remove_tail(self):
        if self.cursize > self.maxsize:
            remove_node = self.last
            # print "remove_node:", id(remove_node), remove_node.key, remove_node.val
            del self.keys[remove_node.key]
            if self.last.prev is None:
                # previous is head
                self.head = None
            else:
                # previous is node
                self.last = self.last.prev
                self.last.next = None
            del(remove_node)
            self.cursize -= 1

    def move_node_to_front(self, node):
        # move if not already the first node
        #   head -> node(last)
        if node.prev is not None:
            if node.next is None:
                # reset last if this last node
                self.last = node.prev
                # connect node prev & next
                # head -> node -> node(move) -> None
                node.prev.next = None
            else:
                # connect node prev & next
                # head -> node -> node(move) -> node -> None
                node.prev.next = node.next
                node.next.prev = node.prev
            # insert node at the head of the list
            node.next = self.head
            self.head = node

    def retrieve(self, key):
        if key in self.keys:
            self.move_node_to_front(self.keys[key])
            return self.keys[key].val

    def print_cache(self):
        # print "keys:", self.keys  # prints objects
        curr = self.head
        while curr is not None:
            print curr.val,
            curr = curr.next
        print

lru = LRUCache(5)
lru.insert_val(1, "one")
lru.insert_val(2, "two")
lru.insert_val(3, "three")
lru.insert_val(4, "four")
lru.insert_val(5, "five")
lru.insert_val(6, "six")  ## should dump key 1 here
lru.insert_val(2, "two")
lru.insert_val(3, "three")
lru.insert_val(1, "one")
print "retrieve 5:", lru.retrieve(5)

lru.print_cache()
