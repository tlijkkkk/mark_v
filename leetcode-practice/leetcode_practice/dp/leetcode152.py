from typing import List


class Solution:
    def maxProductSubArray(self, nums: List[int]) -> int:
        maxProdSoFar = nums[0]
        minProdSoFar = nums[0]
        maxProd = nums[0]

        for num in nums[1:]:
            tmp = maxProdSoFar
            maxProdSoFar = max(maxProdSoFar * num, minProdSoFar * num, num)
            minProdSoFar = min(minProdSoFar * num, tmp * num, num)
            maxProd = max(maxProd, maxProdSoFar)
        
        return maxProd


