from collections import List

class Solution:
    def product_array_except_self(self, nums: List[int]) -> List[int]:
        def accumulate_prod(nums: List) -> List[int]:
            tmp = 1
            result = []
            for num in nums:
                tmp *= num  
                result.append(tmp)
            return result
        
        prefix_prod = [1] + accumulate_prod(nums=nums)
        suffix_prod = list(reversed(accumulate_prod(nums=list(reversed(nums))))) + [1]
        ans = []

        for i in range(len(nums)):
            ans.append(prefix_prod[i] * suffix_prod[i + 1])

        return ans

