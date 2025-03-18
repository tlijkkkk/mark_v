from typing import List


class BinaryIndexedTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.BIT = [0] * (self.n + 1)
        self.nums = nums[:]

        # Build BIT using update function
        for i in range(self.n):
            self.update(i, self.nums[i])

    def update(self, index: int, num: int) -> None:
        diff = num - self.nums[index]
        self.nums[index] = num

        # Update others accoridngly
        i = index + 1 # BIT uses 1-based indexing because index 0 is a dummy root
        while i <= self.n:
            self.BIT[i] += diff # Update i and all its siblings
            i += i & -i

    def query(self, index: int) -> int:
        prefixSum = 0 # Because index is 0 based, so i at least 1
        i = index + 1
        while i >= 1:
            prefixSum += self.BIT[i]
            i -= i & -i
        return prefixSum
    

