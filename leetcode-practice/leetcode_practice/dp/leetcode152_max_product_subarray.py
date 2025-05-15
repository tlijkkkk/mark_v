from typing import List


class Solution:
    def max_product_subarray(self, nums: List[int]) -> int:
        max_prod_so_far = nums[0]
        min_prod_so_far = nums[0]
        max_prod = nums[0]

        for num in nums[1:]:
            tmp = max_prod_so_far
            max_prod_so_far = max(max_prod_so_far * num, min_prod_so_far * num, num)
            min_prod_so_far = min(min_prod_so_far * num, tmp * num, num)
            max_prod = max(max_prod, max_prod_so_far)
        
        return max_prod


