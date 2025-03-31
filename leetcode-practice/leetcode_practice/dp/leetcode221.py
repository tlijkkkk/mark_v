from typing import List


class Solution:
    def maxSquare(self, matrix: List[List[str]]) -> int:
        dp: List[int] = [0] * (len(matrix[0]) + 1)
        maxSideLen = 0
        
        for i in range(len(matrix)):
            cur: List[int] = [0] * (len(matrix[0]) + 1)
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0":
                    cur[j + 1] = 0
                elif matrix[i][j] == "1":
                    cur[j + 1] = min(dp[j + 1], dp[j], cur[j]) + 1
                    maxSideLen = max(maxSideLen, cur[j + 1])
            dp = cur

        return maxSideLen ** 2





