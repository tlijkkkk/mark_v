# Find the shortest path between single source S and multiple destinations E in 2D matrix M, 
# if M[i][j] = '#' it means a block. If no such path, return -1

# Possible solutions can be
# 1. Use DFS
# 2. Improve DFS with branch prune
# 3. (Best) Use BFS

from typing import List, Tuple


class Solution:
    # Use bottom up style
    def min_distance_dfs_i(self, M: List[List[str]], S: Tuple[int]) -> int:
        rows = len(M)
        cols = len(M[0])
        memo = [[-1] * cols for _ in range(rows)] 

        def dfs(S: Tuple[int]) -> int:
            i, j = S[0], S[1]
            
            if not (0 <= i < rows and 0 <= j < cols) or M[i][j] == '#':
                return float('inf')
            
            if M[i][j] == 'E':
                return 0
            
            if memo[i][j] == float('inf'):
                return float('inf')

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = float('inf') # this is the key that prevents from infinite recursion by marking it as same as blocked but allow later on the update with the actual value

            ret = min(dfs((i + 1, j)), dfs((i - 1, j)), dfs((i, j + 1)), dfs((i, j - 1))) + 1

            memo[i][j] = ret 

            return ret    
            # This is not so efficient even though we use memorization, because we attempt to invoke all adjacent cell 

        ret_val = dfs(S=S)

        return ret_val if ret_val != float('inf') else -1