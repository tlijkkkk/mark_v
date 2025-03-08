from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = {}

        for num in nums:
            if num in m:
                m[num] = m[num] + num
            else:
                m[num] = num

        sortedNums = sorted(m.keys())

        prePre = m[sortedNums[0]]

        if len(sortedNums) == 1:
            return prePre

        pre = max(prePre, m[sortedNums[1]]) if sortedNums[1] - sortedNums[0] == 1 else prePre + m[sortedNums[1]]

        if len(sortedNums) == 2:
            return pre

        for i in range(2, len(sortedNums)):
            if sortedNums[i] - sortedNums[i - 1] == 1:
                cur = max(pre, prePre + m[sortedNums[i]])
            else:
                cur = pre + m[sortedNums[i]]
            prePre = pre
            pre = cur
            
        return cur


        




