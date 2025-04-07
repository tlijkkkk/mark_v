from typing import List


class Solution:
    def house_robber_ii(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        def do_rob(wealths: List[int]):
            pre_pre = wealths[0]
            pre = pre_pre
            
            for i in range(2, len(wealths)):
                current = max(pre, pre_pre + wealths[i])
                pre_pre = pre
                pre = current

            return pre

        return max(do_rob(nums[0: -1]), do_rob(nums[1:]))