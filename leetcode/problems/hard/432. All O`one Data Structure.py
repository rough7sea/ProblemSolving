from heapq import heappush, heapify


class AllOne:

    def __init__(self):
        self.valToFreqMap = dict()
        self.freqToValMap = dict()
        self.minFreq = []
        self.maxFreq = []
        self.freqSet = set()

    def inc(self, key: str) -> None:
        if key in self.valToFreqMap:
            self.valToFreqMap[key] += 1
        else:
            self.valToFreqMap[key] = 1

        freq = self.valToFreqMap[key]
        if freq not in self.freqToValMap:
            self.freqToValMap[freq] = set()
        self.freqToValMap[freq].add(key)

        if freq not in self.freqSet:
            heappush(self.minFreq, freq)
            heappush(self.maxFreq, -freq)
            self.freqSet.add(freq)

        prevFreq = freq - 1
        if prevFreq > 0:
            self.freqToValMap[prevFreq].remove(key)
            if len(self.freqToValMap[prevFreq]) == 0:
                self.freqToValMap.pop(prevFreq)

                self.freqSet.remove(prevFreq)
                self.minFreq.remove(prevFreq)
                heapify(self.minFreq)
                self.maxFreq.remove(-prevFreq)
                heapify(self.maxFreq)




    def dec(self, key: str) -> None:
        # cur freq
        freq = self.valToFreqMap[key]
        self.valToFreqMap[key] -= 1

        self.freqToValMap[freq].remove(key)
        if len(self.freqToValMap[freq]) == 0:
            self.freqToValMap.pop(freq)

            if freq in self.freqSet:
                self.freqSet.remove(freq)

                self.minFreq.remove(freq)
                heapify(self.minFreq)
                self.maxFreq.remove(-freq)
                heapify(self.maxFreq)


        if self.valToFreqMap[key] == 0:
            self.valToFreqMap.pop(key)
            return


        nextFreq = self.valToFreqMap[key]
        if nextFreq not in self.freqSet:
            self.freqToValMap[nextFreq] = set()
            self.freqSet.add(nextFreq)
            heappush(self.minFreq, nextFreq)
            heappush(self.maxFreq, -nextFreq)
        self.freqToValMap[nextFreq].add(key)


    def getMaxKey(self) -> str:
        if len(self.freqSet) > 0:
            return list(self.freqToValMap[abs(self.maxFreq[0])])[0]
        return ""


    def getMinKey(self) -> str:
        if len(self.freqSet) > 0:
            return list(self.freqToValMap[self.minFreq[0]])[0]
        return ""



# Your AllOne object will be instantiated and called as such:
obj = AllOne()
# obj.inc("a")
# obj.inc("b")
# obj.inc("b")
# obj.inc("c")
# obj.inc("c")
# obj.inc("c")
#
# obj.dec("b")
# obj.dec("b")
#
# print(obj.getMinKey())
#
# obj.dec("a")
#
# print(obj.getMaxKey())
# print(obj.getMinKey())


obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("b")
obj.inc("b")

obj.dec("b")
obj.dec("b")

print(obj.getMaxKey())
print(obj.getMinKey())
