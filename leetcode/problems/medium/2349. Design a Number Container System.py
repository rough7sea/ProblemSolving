from collections import defaultdict

from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.indexToNumber = dict()
        self.numberToIndex = defaultdict(SortedSet)


    def change(self, index: int, number: int) -> None:
        if index in self.indexToNumber:
            prevNumber = self.indexToNumber[index]
            self.numberToIndex[prevNumber].remove(index)
        self.indexToNumber[index] = number
        self.numberToIndex[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.numberToIndex or not self.numberToIndex[number]:
            return -1
        return min(self.numberToIndex[number])



# Your NumberContainers object will be instantiated and called as such:
nc = NumberContainers()
nc.change(1, 10)
print(nc.find(10))

nc.change(1, 20)
print(nc.find(10))
print(nc.find(20))
print(nc.find(30))

# obj.change(index,number)
# param_2 = obj.find(number)