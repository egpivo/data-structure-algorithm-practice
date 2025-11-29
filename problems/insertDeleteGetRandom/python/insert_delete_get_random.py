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


class RandomizedSetRefined:
    def __init__(self):
        # List to store the elements
        self.elements = []
        # Dictionary to map element to its index in the list
        self.element_index_map = {}

    def insert(self, val: int) -> bool:
        # Check if the value already exists
        if val in self.element_index_map:
            return False
        else:
            # Add the value to the list and update the index in the dictionary
            self.elements.append(val)
            self.element_index_map[val] = len(self.elements) - 1
            return True

    def remove(self, val: int) -> bool:
        # Check if the value exists
        if val in self.element_index_map:
            # Get the index of the element to remove
            index_to_remove = self.element_index_map[val]

            # Swap the element with the last one in the list
            last_element = self.elements.pop()
            if index_to_remove != len(self.elements):
                self.elements[index_to_remove] = last_element
                self.element_index_map[last_element] = index_to_remove

            # Remove the element from the dictionary
            del self.element_index_map[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        # Use random.choice to directly select a random element from the list
        return choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
