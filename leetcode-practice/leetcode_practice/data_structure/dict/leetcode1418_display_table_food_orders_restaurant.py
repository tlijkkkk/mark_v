from typing import List, Dict, Set
from collections import defaultdict

class Solution:
    def display_table_food_orders_restaurant(self, orders: List[List[str]]) -> List[List[str]]:
        display_table: Dict[int, Dict[str, int]] = defaultdict(lambda : defaultdict(int))
        ordered_items: Set[str] = set()

        for order in orders:
            display_table[int(order[1])][order[2]] += 1
            ordered_items.add(order[2])

        sorted_order_items = sorted(list(ordered_items))
        sorted_tables = sorted(display_table.keys())

        result: List[List[str]] = [["Table"] + sorted_order_items] + [[[""] for _ in range(len(sorted_order_items) + 1)] for _ in range(len(sorted_tables))]

        for i in range(len(sorted_tables)):
            result[i + 1][0] = str(sorted_tables[i])
            for j in range(len(sorted_order_items)):
                result[i + 1][j + 1] = str(display_table[sorted_tables[i]][sorted_order_items[j]])

        return result