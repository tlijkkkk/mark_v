from typing import List


class Solution:
    def houseRobberII(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        def doRob(wealths: List[int]):
            prePre = wealths[0]
            pre = prePre
            
            for i in range(2, len(wealths)):
                current = max(pre, prePre + wealths[i])
                prePre = pre
                pre = current

            return pre

        return max(doRob(nums[0: -1]), doRob(nums[1:]))