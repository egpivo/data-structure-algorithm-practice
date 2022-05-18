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

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)