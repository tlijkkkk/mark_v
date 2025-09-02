from typing import List, Set, Tuple
from collections import deque

class Solution:
    def num_of_islands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited: Set[Tuple[int]] = set()
        queue: deque[Tuple[int]] = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]) == '1' and (i, j) not in visited:
                    num_islands += 1
                    queue.append((i, j))
                    visited.add((i, j))
                    while queue:
                        x, y = queue.popleft()
                        for next_x, next_y in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[next_x]) and grid[next_x][next_y] == '1' and (next_x, next_y) not in visited:
                                visited.add((next_x, next_y))
                                queue.append((next_x, next_y))

        return num_islands


