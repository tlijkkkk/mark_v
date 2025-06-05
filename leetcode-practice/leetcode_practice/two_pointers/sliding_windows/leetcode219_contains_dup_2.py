from typing import List, Set

class Solution:
    def contains_duplicate_ii(self, nums: List[int], k: int) -> bool:
        s: Set[int] = set()
        i, j = 0, 0
        
        while j < len(nums):      
            if j - i > k:
                s.remove(nums[i])
            
            if nums[j] in s:
                return True
            
            s.add(nums[j])
            j += 1
        return False