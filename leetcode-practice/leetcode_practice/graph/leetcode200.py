from typing import List


class Solution:
    def num_of_islands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited: List[List[int]] = [[0] * len(grid[0]) for _ in range(len(grid))]

        def do_mark(i: int, j: int) -> None:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            
            if visited[i][j] == 1:
                return

            visited[i][j] = 1
            
            do_mark(i, j + 1)
            do_mark(i + 1, j)
            do_mark(i, j - 1)
            do_mark(i - 1, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]) == "1" and visited[i][j] == 0:
                    num_islands += 1
                    do_mark(i, j)

        return num_islands


