from typing import List


class Solution:
    def delete_and_earn(self, nums: List[int]) -> int:
        num_map = {}

        for num in nums:
            if num in num_map:
                num_map[num] = num_map[num] + num
            else:
                num_map[num] = num

        sorted_nums = sorted(num_map.keys())

        pre_pre = num_map[sorted_nums[0]]

        if len(sorted_nums) == 1:
            return pre_pre

        pre = max(pre_pre, num_map[sorted_nums[1]]) if sorted_nums[1] - sorted_nums[0] == 1 else pre_pre + num_map[sorted_nums[1]]

        if len(sorted_nums) == 2:
            return pre

        for i in range(2, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                cur = max(pre, pre_pre + num_map[sorted_nums[i]])
            else:
                cur = pre + num_map[sorted_nums[i]]
            pre_pre = pre
            pre = cur
            
        return cur







