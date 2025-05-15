from typing import List


class Solution:
    # original title: Maximum length of repeated subarray 
    def max_len_of_common_subarray(self, nums1: List[int], nums2: List[int]) -> int:
        dp: List[int] = [0] * (len(nums2) + 1)
        max_len = 0

        for i in range(len(nums1)):
            tmp: List[int] = [0] * (len(nums2) + 1)
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    tmp[j + 1] = dp[j] + 1
                    max_len = max(max_len, tmp[j + 1])
            dp = tmp

        return max_len
