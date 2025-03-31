from typing import List


class Solution:
    def max_sum_of_two_non_overlapping_subarrays(self, nums: List[int], first_len: int, second_len: int) -> int:        
        def do_search(first_len: int, second_len: int):
            max_final = 0  # given 0 <= nums[i] <= 1000
            max_second = 0
            sum_first = 0
            sum_second = 0

            for i in range(len(nums)):
                sum_first += nums[i]
                if i >= first_len:
                    sum_first -= nums[i - first_len]
                    sum_second += nums[i - first_len]
                    if i - first_len >= second_len:
                        sum_second -= nums[i - first_len - second_len]
                    max_second = max(max_second, sum_second)
                    max_final = max(max_final, sum_first + max_second)

            return max_final
        
        return max(do_search(first_len=first_len, second_len=second_len), do_search(first_len=second_len, second_len=first_len))
