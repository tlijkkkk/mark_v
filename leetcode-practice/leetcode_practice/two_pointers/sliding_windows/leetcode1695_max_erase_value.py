from typing import Set, List

class Solution:
    def max_erase_value(self, nums: List[int]) -> int:
        s_unique: Set[int] = set()
        i = 0
        tmp_score = 0
        max_score = 0

        for j in range(len(nums)):
            tmp_score += nums[j]

            while nums[j] in s_unique:
                s_unique.remove(nums[i])
                tmp_score -= nums[i]
                i += 1
            
            s_unique.add(nums[j])
            max_score = max(max_score, tmp_score)

        return max_score