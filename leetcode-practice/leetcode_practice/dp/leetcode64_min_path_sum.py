from typing import List


class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:
        max_val = 200 * (len(grid) + len(grid[0]))
        dp: List[int] = [max_val] * (len(grid[0]) + 1)

        for i in range(len(grid)):
            current: List[int] = [max_val] + [0] * (len(grid[i]))
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    current[j + 1] = grid[i][j]
                else:
                    current[j + 1] = min(current[j] + grid[i][j], dp[j + 1] + grid[i][j])
            dp = current
        
        return dp[-1]
