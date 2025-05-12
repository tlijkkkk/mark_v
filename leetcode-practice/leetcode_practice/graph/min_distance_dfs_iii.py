# Find the shortest path between single source S and multiple destinations E in 2D matrix M, 
# if M[i][j] = '#' it means a block. If no such path, return -1

# Possible solutions can be
# 1. Use DFS
# 2. Improve DFS with branch prune
# 3. (Best) Use BFS


from typing import List, Tuple


class Solution:
    def min_distance_dfs_ii(self, M: List[List[str]], S: Tuple[int]) -> int:
        rows, cols = len(M), len(M[0])
        memo = [[-1] * cols for _ in range(rows)]
        min_dist = [float('inf')]

        def dfs(S: Tuple[int], dist: int):
            i, j = S[0], S[1]
            if not (0 <= i < rows and 0 <= j < cols) or M[i][j] == '#':
                return 
            
            if memo[i][j] != -1 and memo[i][j] <= dist:
                return
            
            memo[i][j] = dist

            if M[i][j] == 'E':
                min_dist[0] = min(min_dist[0], dist)
                return
            
            dfs((i + 1, j), dist + 1)
            dfs((i - 1, j), dist + 1)
            dfs((i, j + 1), dist + 1)
            dfs((i, j - 1), dist + 1)

        dfs(S=S, dist=0)
        return min_dist[0] if min_dist[0] != float('inf') else -1

