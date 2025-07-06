from typing import List, Set

class Solution:
    def contains_duplicate_ii(self, nums: List[int], k: int) -> bool:
        s: Set[int] = set()
        i = 0
        
        for j in range(len(nums)):      
            while j - i > k:
                s.remove(nums[i])
                i += 1
            
            if nums[j] in s:
                return True
            
            s.add(nums[j])
            
        return False