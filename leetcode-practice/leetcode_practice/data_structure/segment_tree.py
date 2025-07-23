# Segment tree is to support update in O(lg n) and range query in O(lg n). Unlike BIT supports only prefix sum, segment tree support both prefix sum and prefix min/max
# Segment tree is static, we cannot dynamically insert new element to he tree
class MinSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1  # smallest power of 2 ≥ n
        self.tree = [float('inf')] * (2 * self.size)

        # Fill the leaf nodes
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]

        # Build internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, value):
        # Set arr[i] = value
        i += self.size
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        # Return min in range [l, r)
        l += self.size
        r += self.size
        res = float('inf')
        while l < r:
            if l % 2:
                res = min(res, self.tree[l])
                l += 1
            if r % 2:
                r -= 1
                res = min(res, self.tree[r])
            l //= 2
            r //= 2
        return res