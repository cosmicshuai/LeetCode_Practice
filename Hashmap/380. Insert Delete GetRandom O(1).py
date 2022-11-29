import random

class RandomizedSet:
    def __init__(self):
        self.has = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.has:
            return False
        l = len(self.array)
        self.array.append(val)
        self.has[val] = l
        return True

    def remove(self, val: int) -> bool:
        if not val in self.has:
            return False
        idx = self.has[val]
        v = self.array[-1]
        self.array[idx] = v
        self.has[v] = idx
        self.has.pop(val)
        self.array.pop()
        return True

    def getRandom(self) -> int:
        return self.array[random.randint(0, len(self.array) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()