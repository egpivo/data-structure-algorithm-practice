from random import choice


class RandomizedSet:
    """

    Complexity
    ----------
    - TC:
        - getRandom: O(1)
        - insert/remove: O(1) (average); O(n) (worst when the operation exceeds the capacity of currently allocated array/hashmap and invokes space reallocation)
    - SC: O(n)
    """

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx

            self.list.pop()
            del self.dict[val]

            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
