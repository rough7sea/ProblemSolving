class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
        elif len(self.nums) > 0:
            self.nums.append(self.nums[-1] * num)
        else:
            self.nums.append(num)

    def getProduct(self, k: int) -> int:
        if k > len(self.nums):
            return 0

        if k == len(self.nums):
            return self.nums[-1]

        return self.nums[-1] / self.nums[-(k + 1)]
