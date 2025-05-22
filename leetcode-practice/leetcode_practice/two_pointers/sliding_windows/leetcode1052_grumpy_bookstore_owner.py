from typing import List


class Solution:
    def grumpy_bookstore_owner(self, customers: List[int], grumpy:  List[int], minutes: int) -> int:
        if len(customers) <= minutes:
            return sum(customers)
        
        satisfied_cust = sum(customers[i] for i in range(len(customers)) if i < minutes or not grumpy[i])
        max_satisfied_cust = satisfied_cust

        i = 0
        j = minutes # points to the first element outside of the window

        while j < len(customers):
            if grumpy[j]:
                satisfied_cust += customers[j]
            if grumpy[i]:
                satisfied_cust -= customers[i]
            max_satisfied_cust = max(max_satisfied_cust, satisfied_cust)

            j += 1
            i += 1

        return max_satisfied_cust

