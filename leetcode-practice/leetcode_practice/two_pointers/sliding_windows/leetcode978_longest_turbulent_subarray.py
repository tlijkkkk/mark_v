from typing import List

class Solution:
    def longest_turbulent_subarray(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 1
        
        i = 0
        longest = 0
        last_comparison_sign = -1

        for j in range(1, len(arr)):
            if arr[j] > arr[j - 1]:
                comparison_sign = 0
            elif arr[j] < arr[j - 1]:
                comparison_sign = 1
            else:
                comparison_sign = -1
            
            if last_comparison_sign + comparison_sign != 1:
                    i = j - 1

            if comparison_sign == -1:
                 longest = max(longest, 1)
            else:
                longest = max(longest, j - i + 1)

            last_comparison_sign = comparison_sign
        
        return longest
        
