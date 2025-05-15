# You're having a grand old time clicking through the rabbit hole that is your favorite online encyclopedia.

# The encyclopedia consists of N different web pages, numbered from 1 to N. Each page i contains nothing but a single link to a different page L[i].

# A session spent on this website involves beginning on one of the N pages, and then navigating around using the links until you decide to stop. That is, while on page i, you may either move to page L[i], or stop your browsing session.

# Assuming you can choose which page you begin the session on, what's the maximum number of different pages you can visit in a single session? Note that a page only counts once even if visited multiple times during the session.

# Constraints:
# 2 <= N <= 500000
# 1 <= L[i] <= N
# L[i] != i

from typing import List

def get_max_visitable_webpages(N: int, L: List[int]) -> int:
    # This is actually to find the longest path from multiple SLL that contains one circle
    stack = []
    map = {}
    for i in range(N):
        j = i
        while j not in map:
            map[j] = 0
            stack.append(j)
            j = L[j] - 1

        if map[j] == 0:
            tmp = []
            count = 0
            while stack:
                tmp.append(stack.pop())
                count += 1
                if tmp[-1] == j:
                    break
            for t in tmp:
                map[t] = count
        
        while stack:
            t = stack.pop()
            map[t] = map[j] + 1
            j = t
    
    return max(map.values())

