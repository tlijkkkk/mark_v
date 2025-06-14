from typing import List

class Solution:
    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr) - k

        while i < j:
            mid = i + (j - i) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                i = mid
            else:
                j = mid + 1
        
        return arr[mid : mid + k]