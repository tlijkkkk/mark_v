from typing import List


class Solution:
    def numOfIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited: List[List[int]] = [[0] * len(grid[0]) for _ in range(len(grid))]

        def doMark(i: int, j: int) -> None:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            
            if visited[i][j] == 1:
                return

            visited[i][j] = 1
            
            doMark(i, j + 1)
            doMark(i + 1, j)
            doMark(i, j - 1)
            doMark(i -1, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]) == "1" and visited[i][j] == 0:
                    numIslands += 1
                    doMark(i, j)

        return numIslands


