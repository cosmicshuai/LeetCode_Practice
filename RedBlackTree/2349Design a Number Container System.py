from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.mem = {}
        #use a hashmap to memorize the mapping of each index to number
        self.idxMem = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idxMem:
            self.mem[self.idxMem[index]].remove(index)

        if not number in self.mem:
            # use a SortedList to memorize indecies for each number
            self.mem[number] = SortedList()
            self.mem[number].add(index)
        else:
            self.mem[number].add(index)
        self.idxMem[index] = number

    def find(self, number: int) -> int:
        if not number in self.mem:
            return -1
        print(self.mem)
        if len(self.mem[number]) > 0:
            return self.mem[number][0]
        else:
            return -1


S = NumberContainers()
S.change(1, 10)
S.change(2, 10)
S.change(1, 20)
print(S.find(10))