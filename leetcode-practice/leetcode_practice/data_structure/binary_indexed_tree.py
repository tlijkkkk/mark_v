from typing import List

# BIT is good to perform update in O(lg n) and query for prefix sum of i in O(lg n)
# BIT is static, we cannot dynamically insert new element to he tree
class BinaryIndexedTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)  # Renamed BIT to bit
        self.nums = nums[:]

        # Build BIT using update function
        for i in range(self.n):
            self.update(i, self.nums[i])

    def update(self, index: int, num: int) -> None:
        diff = num - self.nums[index]
        self.nums[index] = num

        # Update others accordingly
        i = index + 1  # BIT uses 1-based indexing because index 0 is a dummy root
        while i <= self.n:
            self.bit[i] += diff  # Renamed BIT to bit
            i += i & -i

    def query(self, index: int) -> int:
        prefix_sum = 0  # Renamed prefixSum to prefix_sum
        i = index + 1
        while i >= 1:
            prefix_sum += self.bit[i]  # Renamed BIT to bit
            i -= i & -i
        return prefix_sum


