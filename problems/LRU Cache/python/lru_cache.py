from collections import OrderedDict


class LRUCache:
    """

    Complexity
    ----------
    - TC: O(1)
    - SC: O(capacity)

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        self.cache.move_to_end(key, last=True)
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class ListNode:
    def __init__(self, key: int, value: int, next: "ListNode" = None, prev: "ListNode" = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache2:
    """
    Notes
    -----
    Double linked list (order)+ dictionary (node info)

    Complexity
    ----------
    - TC: O(1)
    - SC: O(capacity)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = {}

        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dictionary:
            node = self.dictionary[key]
            self.remove_from_list(node)
            self.insert_into_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            node = self.dictionary[key]
            self.remove_from_list(node)
            self.insert_into_head(node)
            node.value = value
        else:
            if len(self.dictionary) >= self.capacity:
                self.remove_from_tail()
            node = ListNode(key, value)
            self.insert_into_head(node)
            self.dictionary[key] = node

    def remove_from_list(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_into_head(self, node) -> None:
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def remove_from_tail(self) -> None:
        if len(self.dictionary) == 0:
            return

        tail_prev = self.tail.prev
        self.remove_from_list(tail_prev)
        del self.dictionary[tail_prev.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
