from typing import List


class Solution:
    def palindromePartitioning(self, s: str) -> List[List[str]]:
        dp: List[List[int]] = [[2 if i == j else 0 for i in range(len(s))] for j in range(len(s))]
        result: List[List[str]] = []

        def isPalindrome(i: int, j: int):
            ii = i
            jj = j
            isPal = True
            while ii < jj:
                if s[ii] != s[jj] or dp[i][j] == 1:
                    isPal = False
                    break
                if dp[i][j] == 2: # If a known palindrome 
                    break
                ii += 1
                jj -= 1
            
            # Update dp 
            while i <= ii and j >= jj:
                dp[i][j] = 2 if isPal else 1
                i += 1
                j -= 1
            
            return isPal

        for i in range(len(s)):
            for j in range(i,len(s)):
                if isPalindrome(i, j):
                    result.append([s[i: j + 1]])
        
        return result
