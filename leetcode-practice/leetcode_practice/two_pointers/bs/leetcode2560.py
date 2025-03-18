from typing import List


class Solution:
    def houseRobberIV(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = max(nums)

        # Find the target between [low, high] that is the max of at least k houses

        def housesBelow(wealth: int) -> int:
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= wealth:
                    count += 1
                    i += 1
                i += 1
            return count
        
        minWealth = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            if housesBelow(mid) < k:
                low = mid + 1
            else:
                minWealth = mid
                high = mid - 1

        return minWealth
