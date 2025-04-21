from typing import List


class Solution:
    def longest_increasing_sub_seq(self, nums: List[int]) -> int:
        dp: List[int] = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    
        # subseq = []
        # for num in nums:
        #     idx = bisect_left(subseq, num)
        #     if idx == len(subseq):
        #         subseq.append(num)
        #     else:
        #         subseq[idx] = num

        # return len(subseq)