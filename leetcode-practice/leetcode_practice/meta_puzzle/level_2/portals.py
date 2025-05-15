# You've found yourself in a grid of cells with R rows and C columns. The cell in the i-th row from the top and j-th column from the left contains one of the following (indicated by the character G[i][j]):

# If G[i][j] = ".", the cell is empty.  
# If G[i][j] = "S", the cell contains your starting position. There is exactly one such cell.  
# If G[i][j] = "E", the cell contains an exit. There is at least one such cell.  
# If G[i][j] = "#", the cell contains a wall.  
# Otherwise, if G[i][j] is a lowercase letter (between "a" and "z", inclusive), the cell contains a portal marked with that letter.

# Your objective is to reach any exit from your starting position as quickly as possible. Each second, you may take either of the following actions:

# Walk to a cell adjacent to your current one (directly above, below, to the left, or to the right), as long as you remain within the grid and that cell does not contain a wall.

# If your current cell contains a portal, teleport to any other cell in the grid containing a portal marked with the same letter as your current cell's portal.

# Determine the minimum number of seconds required to reach any exit, if it's possible to do so at all. If it's not possible, return -1 instead.

# Constraints:
# 1 <= R, C <= 50  
# G[i][j] ∈ {".", "S", "E", "#", "a"..."z"}

from typing import List
from collections import deque

def get_seconds_required(R: int, C: int, G: List[List[str]]) -> int:
    start_node = ()
    letter_nodes = {}
    for i in range(R):
        for j in range(C):
            if 'a' <= G[i][j] <= 'z':
                letter_nodes.setdefault(G[i][j], []).append((i, j))
            if G[i][j] == 'S':
                start_node = (i, j)

    queue = deque()
    visited = {start_node}
    queue.append((start_node[0], start_node[1], 0))

    while queue:
        i, j, dist = queue.popleft()

        if G[i][j] == 'E':
            return dist
        
        next_nodes = {(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)}

        if 'a' <= G[i][j] <= 'z':
            next_nodes.update(letter_nodes.get(G[i][j])) # this will includes self but it is ok we have mark self visited

        for next_i, next_j in next_nodes:
            if 0 <= next_i < R and 0 <= next_j < C and G[next_i][next_j] != '#' and (next_i, next_j) not in visited:
                queue.append((next_i, next_j, dist + 1))
                visited.add((next_i, next_j))
    
    return -1