from typing import List


class Solution:
    def house_robber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        pre_pre = nums[0]
        pre = max(nums[0], nums[1])
        current = 0

        for num in nums[2:]:
            current = max(pre, pre_pre + num)
            pre_pre = pre
            pre = current

        return current