from typing import List


class Solution:
    def maxSumOfTwoNonOverlappingSubArrays(self, nums: List[int], firstLen: int, secondLen: int) -> int:        
        def doSearch(firstLen: int, secondLen: int):
            maxFinal = 0 # given 0 <= nums[i] <= 1000
            max2 = 0
            sum1 = 0
            sum2 = 0
            j = 0

            for i in range(len(nums)):
                sum1 += nums[i]
                if i >= firstLen:
                    sum1 -= nums[i - firstLen]
                    sum2 += nums[i - firstLen]
                    if i - firstLen >= secondLen:
                        sum2 -= nums[i - firstLen - secondLen]
                    max2 = max(max2, sum2)
                    maxFinal = max(maxFinal, sum1 + max2)

            return maxFinal
        
        return max(doSearch(firstLen=firstLen, secondLen=secondLen), doSearch(firstLen=secondLen, secondLen=firstLen))
