from typing import List


class Solution:
    def max_num_k_sum_pair(self, nums: List[int], k: int) -> int:
        ht = {}
        count = 0

        for num in nums:
            if k - num in ht:
                ht[k - num] -= 1
                if ht[k - num] == 0:
                    ht.pop(k - num)
                count += 1
            else:
                ht[num] = ht.get(num, 0) + 1
        
        return count
