# You are sitting in front of a kaiten belt with N dishes passing by in a row. The i-th dish is of type D[i]. Some dishes may have the same type as others.

# You're very hungry, but also like to keep things interesting:
# - For each dish, you'll eat it if it isn't the same type as any of the last K dishes you've eaten.
# - You eat fast enough to consume a dish instantly before the next one arrives.
# - Any dish you don’t eat is taken by others and can’t be eaten later.

# Your goal is to determine how many dishes you'll eat.

# Constraints:
# - 1 ≤ N ≤ 500,000
# - 1 ≤ K ≤ N
# - 1 ≤ D[i] ≤ 1,000,000

from typing import List
from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  eaten_set_previous_k = set()
  eaten_previous_k = deque()
  eaten_count = 0
  
  for dish_type in D:
    if dish_type not in eaten_set_previous_k:
      eaten_set_previous_k.add(dish_type)
      eaten_count += 1
      if len(eaten_previous_k) == K:
        dish_type_drop = eaten_previous_k.popleft()
        eaten_set_previous_k.remove(dish_type_drop)
      eaten_previous_k.append(dish_type)
  
  return eaten_count