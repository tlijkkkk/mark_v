from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        maxVal = 200 * (len(grid) + len(grid[0]))
        dp: List[int] = [maxVal] * (len(grid[0]) + 1) # grid[i][j] is 200 max so the max of possible sum is 200 * (row + column)

        for i in range(len(grid)):
            current: List[int] = [maxVal] + [0] *(len(grid[i]))
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    current[j + 1] = grid[i][j]
                else:
                    current[j + 1] = min(current[j] + grid[i][j], dp[j + 1] + grid[i][j])
            dp = current
        
        return dp[-1]
