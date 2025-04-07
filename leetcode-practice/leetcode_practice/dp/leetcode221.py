from typing import List


class Solution:
    def max_square(self, matrix: List[List[str]]) -> int:
        dp: List[int] = [0] * (len(matrix[0]) + 1)
        max_side_len = 0
        
        for i in range(len(matrix)):
            cur: List[int] = [0] * (len(matrix[0]) + 1)
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0":
                    cur[j + 1] = 0
                elif matrix[i][j] == "1":
                    cur[j + 1] = min(dp[j + 1], dp[j], cur[j]) + 1
                    max_side_len = max(max_side_len, cur[j + 1])
            dp = cur

        return max_side_len ** 2





