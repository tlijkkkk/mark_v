from typing import List

class Solution:
    def subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0

        i, j = 0, 0
        prod = 1
        result = 0

        while j < len(nums):
            prod *= nums[j]

            while prod >= k:
                prod /= nums[i]
                i += 1

            result += j - i + 1
            j += 1
    
        return result