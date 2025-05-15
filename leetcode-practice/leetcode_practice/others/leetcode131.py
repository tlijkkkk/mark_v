from typing import List


class Solution:
    def palindrome_partitioning(self, s: str) -> List[List[str]]:
        dp: List[List[int]] = [[2 if i == j else 0 for i in range(len(s))] for j in range(len(s))]
        result: List[List[str]] = []

        def is_palindrome(i: int, j: int):
            ii = i
            jj = j
            is_pal = True
            while ii < jj:
                if s[ii] != s[jj] or dp[i][j] == 1:
                    is_pal = False
                    break
                if dp[i][j] == 2:  # If a known palindrome
                    break
                ii += 1
                jj -= 1
            
            # Update dp 
            while i <= ii and j >= jj:
                dp[i][j] = 2 if is_pal else 1
                i += 1
                j -= 1
            
            return is_pal

        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    result.append([s[i: j + 1]])
        
        return result
